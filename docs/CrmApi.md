# CrmApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCrmActivity**](CrmApi.md#createCrmActivity) | **POST** /v1/crm/{accountId}/contacts/{contactId}/activities | Log a CRM activity |
| [**createCrmActivityWithHttpInfo**](CrmApi.md#createCrmActivityWithHttpInfo) | **POST** /v1/crm/{accountId}/contacts/{contactId}/activities | Log a CRM activity |
| [**createCrmContact**](CrmApi.md#createCrmContact) | **POST** /v1/crm/{accountId}/contacts | Create a CRM contact |
| [**createCrmContactWithHttpInfo**](CrmApi.md#createCrmContactWithHttpInfo) | **POST** /v1/crm/{accountId}/contacts | Create a CRM contact |
| [**getCrmContact**](CrmApi.md#getCrmContact) | **GET** /v1/crm/{accountId}/contacts/{contactId} | Get a CRM contact |
| [**getCrmContactWithHttpInfo**](CrmApi.md#getCrmContactWithHttpInfo) | **GET** /v1/crm/{accountId}/contacts/{contactId} | Get a CRM contact |
| [**getCrmDeal**](CrmApi.md#getCrmDeal) | **GET** /v1/crm/{accountId}/deals/{dealId} | Get a CRM deal |
| [**getCrmDealWithHttpInfo**](CrmApi.md#getCrmDealWithHttpInfo) | **GET** /v1/crm/{accountId}/deals/{dealId} | Get a CRM deal |
| [**listCrmDeals**](CrmApi.md#listCrmDeals) | **GET** /v1/crm/{accountId}/deals | List CRM deals |
| [**listCrmDealsWithHttpInfo**](CrmApi.md#listCrmDealsWithHttpInfo) | **GET** /v1/crm/{accountId}/deals | List CRM deals |
| [**listCrmOwners**](CrmApi.md#listCrmOwners) | **GET** /v1/crm/{accountId}/owners | List CRM owners |
| [**listCrmOwnersWithHttpInfo**](CrmApi.md#listCrmOwnersWithHttpInfo) | **GET** /v1/crm/{accountId}/owners | List CRM owners |
| [**searchCrmContacts**](CrmApi.md#searchCrmContacts) | **GET** /v1/crm/{accountId}/contacts/search | Search CRM contacts |
| [**searchCrmContactsWithHttpInfo**](CrmApi.md#searchCrmContactsWithHttpInfo) | **GET** /v1/crm/{accountId}/contacts/search | Search CRM contacts |
| [**updateCrmContact**](CrmApi.md#updateCrmContact) | **PATCH** /v1/crm/{accountId}/contacts/{contactId} | Update a CRM contact |
| [**updateCrmContactWithHttpInfo**](CrmApi.md#updateCrmContactWithHttpInfo) | **PATCH** /v1/crm/{accountId}/contacts/{contactId} | Update a CRM contact |
| [**updateCrmDeal**](CrmApi.md#updateCrmDeal) | **PATCH** /v1/crm/{accountId}/deals/{dealId} | Update a CRM deal |
| [**updateCrmDealWithHttpInfo**](CrmApi.md#updateCrmDealWithHttpInfo) | **PATCH** /v1/crm/{accountId}/deals/{dealId} | Update a CRM deal |



## createCrmActivity

> CreateCrmActivity201Response createCrmActivity(accountId, contactId, createCrmActivityRequest)

Log a CRM activity

Log something that happened with a person on their CRM record.  - HubSpot: a Communication on the contact&#39;s timeline for &#x60;channel&#x60; &#x60;whatsapp&#x60; or &#x60;sms&#x60;, otherwise a Note. The subject and direction lead the text. - Salesforce: a completed Task on the Contact or Lead (&#x60;WhoId&#x60;), dated &#x60;occurredAt&#x60;, with &#x60;body&#x60; as its comments. &#x60;channel: call&#x60; logs a call. - HighLevel: a plain-text note on the contact. HighLevel dates a note when it is logged, so the subject (or channel), direction and &#x60;occurredAt&#x60; lead its text.  To log inbox conversations automatically instead, turn on &#x60;logMessages&#x60; in the CRM settings.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CrmApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CrmApi apiInstance = new CrmApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected HubSpot, Salesforce or HighLevel account (`GET /v1/accounts?platform=hubspot`, `salesforce` or `gohighlevel`).
        String contactId = "contactId_example"; // String | The CRM's own id. HubSpot contact id, Salesforce Contact (`003...`) or Lead (`00Q...`) id, or HighLevel contact id.
        CreateCrmActivityRequest createCrmActivityRequest = new CreateCrmActivityRequest(); // CreateCrmActivityRequest | 
        try {
            CreateCrmActivity201Response result = apiInstance.createCrmActivity(accountId, contactId, createCrmActivityRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CrmApi#createCrmActivity");
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
| **accountId** | **String**| The connected HubSpot, Salesforce or HighLevel account (&#x60;GET /v1/accounts?platform&#x3D;hubspot&#x60;, &#x60;salesforce&#x60; or &#x60;gohighlevel&#x60;). | |
| **contactId** | **String**| The CRM&#39;s own id. HubSpot contact id, Salesforce Contact (&#x60;003...&#x60;) or Lead (&#x60;00Q...&#x60;) id, or HighLevel contact id. | |
| **createCrmActivityRequest** | [**CreateCrmActivityRequest**](CreateCrmActivityRequest.md)|  | |

### Return type

[**CreateCrmActivity201Response**](CreateCrmActivity201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The logged activity. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;crm_scope_missing&#x60;: the connection did not grant a scope this call needs (&#x60;details.scope&#x60;), typically a HubSpot optional scope added after the portal connected, or a HighLevel scope (such as &#x60;users.readonly&#x60;) added after the location installed the app. Reconnect the CRM and approve it; the account id stays the same.  &#x60;crm_access_denied&#x60;: the CRM refused the connected user (Salesforce field-level security or sharing, a HubSpot permission). &#x60;details.errors&#x60; holds the CRM&#39;s own errors. |  -  |
| **404** | &#x60;account_not_found&#x60;: the accountId is not a CRM account you can access. &#x60;crm_record_not_found&#x60;: the CRM has no record with this id (deleted, merged, or another object type). |  -  |
| **409** | The account exists but is disconnected (deactivated, or flagged as needing reconnection). Code &#x60;account_disconnected&#x60;.  &#x60;details&#x60; names the account (&#x60;accountId&#x60;, &#x60;platform&#x60;, &#x60;username&#x60;) with its &#x60;disconnectReason&#x60;, &#x60;disconnectionType&#x60;, &#x60;unhealthySince&#x60; and &#x60;action: reconnect&#x60;.  Reconnect the account (its accountId stays the same), then retry. The disconnect is also sent as the &#x60;account.disconnected&#x60; webhook. |  -  |
| **422** | The CRM refused the values: a validation rule, a required field, a bad picklist value or an unknown field. Code &#x60;crm_validation_failed&#x60;; &#x60;details.errors&#x60; lists the CRM&#39;s own errors, each with &#x60;code&#x60;, &#x60;message&#x60; and the &#x60;fields&#x60; at fault when the CRM names them. |  -  |
| **429** | Zernio paces every connection inside its CRM limits (HubSpot per portal, Salesforce per org, HighLevel per location, shared with the conversation sync). Code &#x60;rate_limited&#x60;; wait for &#x60;Retry-After&#x60; seconds. |  * Retry-After - Seconds to wait before retrying. <br>  |
| **502** | The platform returned a server error. |  -  |

## createCrmActivityWithHttpInfo

> ApiResponse<CreateCrmActivity201Response> createCrmActivity createCrmActivityWithHttpInfo(accountId, contactId, createCrmActivityRequest)

Log a CRM activity

Log something that happened with a person on their CRM record.  - HubSpot: a Communication on the contact&#39;s timeline for &#x60;channel&#x60; &#x60;whatsapp&#x60; or &#x60;sms&#x60;, otherwise a Note. The subject and direction lead the text. - Salesforce: a completed Task on the Contact or Lead (&#x60;WhoId&#x60;), dated &#x60;occurredAt&#x60;, with &#x60;body&#x60; as its comments. &#x60;channel: call&#x60; logs a call. - HighLevel: a plain-text note on the contact. HighLevel dates a note when it is logged, so the subject (or channel), direction and &#x60;occurredAt&#x60; lead its text.  To log inbox conversations automatically instead, turn on &#x60;logMessages&#x60; in the CRM settings.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CrmApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CrmApi apiInstance = new CrmApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected HubSpot, Salesforce or HighLevel account (`GET /v1/accounts?platform=hubspot`, `salesforce` or `gohighlevel`).
        String contactId = "contactId_example"; // String | The CRM's own id. HubSpot contact id, Salesforce Contact (`003...`) or Lead (`00Q...`) id, or HighLevel contact id.
        CreateCrmActivityRequest createCrmActivityRequest = new CreateCrmActivityRequest(); // CreateCrmActivityRequest | 
        try {
            ApiResponse<CreateCrmActivity201Response> response = apiInstance.createCrmActivityWithHttpInfo(accountId, contactId, createCrmActivityRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CrmApi#createCrmActivity");
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
| **accountId** | **String**| The connected HubSpot, Salesforce or HighLevel account (&#x60;GET /v1/accounts?platform&#x3D;hubspot&#x60;, &#x60;salesforce&#x60; or &#x60;gohighlevel&#x60;). | |
| **contactId** | **String**| The CRM&#39;s own id. HubSpot contact id, Salesforce Contact (&#x60;003...&#x60;) or Lead (&#x60;00Q...&#x60;) id, or HighLevel contact id. | |
| **createCrmActivityRequest** | [**CreateCrmActivityRequest**](CreateCrmActivityRequest.md)|  | |

### Return type

ApiResponse<[**CreateCrmActivity201Response**](CreateCrmActivity201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The logged activity. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;crm_scope_missing&#x60;: the connection did not grant a scope this call needs (&#x60;details.scope&#x60;), typically a HubSpot optional scope added after the portal connected, or a HighLevel scope (such as &#x60;users.readonly&#x60;) added after the location installed the app. Reconnect the CRM and approve it; the account id stays the same.  &#x60;crm_access_denied&#x60;: the CRM refused the connected user (Salesforce field-level security or sharing, a HubSpot permission). &#x60;details.errors&#x60; holds the CRM&#39;s own errors. |  -  |
| **404** | &#x60;account_not_found&#x60;: the accountId is not a CRM account you can access. &#x60;crm_record_not_found&#x60;: the CRM has no record with this id (deleted, merged, or another object type). |  -  |
| **409** | The account exists but is disconnected (deactivated, or flagged as needing reconnection). Code &#x60;account_disconnected&#x60;.  &#x60;details&#x60; names the account (&#x60;accountId&#x60;, &#x60;platform&#x60;, &#x60;username&#x60;) with its &#x60;disconnectReason&#x60;, &#x60;disconnectionType&#x60;, &#x60;unhealthySince&#x60; and &#x60;action: reconnect&#x60;.  Reconnect the account (its accountId stays the same), then retry. The disconnect is also sent as the &#x60;account.disconnected&#x60; webhook. |  -  |
| **422** | The CRM refused the values: a validation rule, a required field, a bad picklist value or an unknown field. Code &#x60;crm_validation_failed&#x60;; &#x60;details.errors&#x60; lists the CRM&#39;s own errors, each with &#x60;code&#x60;, &#x60;message&#x60; and the &#x60;fields&#x60; at fault when the CRM names them. |  -  |
| **429** | Zernio paces every connection inside its CRM limits (HubSpot per portal, Salesforce per org, HighLevel per location, shared with the conversation sync). Code &#x60;rate_limited&#x60;; wait for &#x60;Retry-After&#x60; seconds. |  * Retry-After - Seconds to wait before retrying. <br>  |
| **502** | The platform returned a server error. |  -  |


## createCrmContact

> CreateCrmContact201Response createCrmContact(accountId, createCrmContactRequest)

Create a CRM contact

Create a person in the connected CRM. HubSpot creates a contact. Salesforce creates a Lead or a Contact: &#x60;createAs&#x60;, else the connection&#39;s &#x60;createAs&#x60; setting (default &#x60;lead&#x60;).  Salesforce requires &#x60;lastName&#x60; on both, and &#x60;company&#x60; on a Lead (&#x60;[not provided]&#x60; when you send none). A Contact takes its company from its Account: set &#x60;properties.AccountId&#x60; instead.  HighLevel creates a contact in the connected location. A location that does not allow duplicates answers 409 with the existing contact.  Anything the CRM refuses (a required field, a validation rule, a duplicate rule) comes back as 422 or 409 with the CRM&#39;s own errors in &#x60;details.errors&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CrmApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CrmApi apiInstance = new CrmApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected HubSpot, Salesforce or HighLevel account (`GET /v1/accounts?platform=hubspot`, `salesforce` or `gohighlevel`).
        CreateCrmContactRequest createCrmContactRequest = new CreateCrmContactRequest(); // CreateCrmContactRequest | 
        try {
            CreateCrmContact201Response result = apiInstance.createCrmContact(accountId, createCrmContactRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CrmApi#createCrmContact");
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
| **accountId** | **String**| The connected HubSpot, Salesforce or HighLevel account (&#x60;GET /v1/accounts?platform&#x3D;hubspot&#x60;, &#x60;salesforce&#x60; or &#x60;gohighlevel&#x60;). | |
| **createCrmContactRequest** | [**CreateCrmContactRequest**](CreateCrmContactRequest.md)|  | |

### Return type

[**CreateCrmContact201Response**](CreateCrmContact201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The created contact, read back from the CRM. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;crm_scope_missing&#x60;: the connection did not grant a scope this call needs (&#x60;details.scope&#x60;), typically a HubSpot optional scope added after the portal connected, or a HighLevel scope (such as &#x60;users.readonly&#x60;) added after the location installed the app. Reconnect the CRM and approve it; the account id stays the same.  &#x60;crm_access_denied&#x60;: the CRM refused the connected user (Salesforce field-level security or sharing, a HubSpot permission). &#x60;details.errors&#x60; holds the CRM&#39;s own errors. |  -  |
| **404** | &#x60;account_not_found&#x60;: the accountId is not a CRM account you can access. &#x60;crm_record_not_found&#x60;: the CRM has no record with this id (deleted, merged, or another object type). |  -  |
| **409** | &#x60;crm_duplicate_record&#x60;: the CRM refused a duplicate (HubSpot: the email belongs to another contact; Salesforce: a duplicate rule; HighLevel: a location that does not allow duplicate contacts). &#x60;details.existingId&#x60; is the existing record when the CRM names it.  &#x60;account_disconnected&#x60;: the CRM account needs reconnecting; see AccountDisconnected. |  -  |
| **422** | The CRM refused the values: a validation rule, a required field, a bad picklist value or an unknown field. Code &#x60;crm_validation_failed&#x60;; &#x60;details.errors&#x60; lists the CRM&#39;s own errors, each with &#x60;code&#x60;, &#x60;message&#x60; and the &#x60;fields&#x60; at fault when the CRM names them. |  -  |
| **429** | Zernio paces every connection inside its CRM limits (HubSpot per portal, Salesforce per org, HighLevel per location, shared with the conversation sync). Code &#x60;rate_limited&#x60;; wait for &#x60;Retry-After&#x60; seconds. |  * Retry-After - Seconds to wait before retrying. <br>  |
| **502** | The platform returned a server error. |  -  |

## createCrmContactWithHttpInfo

> ApiResponse<CreateCrmContact201Response> createCrmContact createCrmContactWithHttpInfo(accountId, createCrmContactRequest)

Create a CRM contact

Create a person in the connected CRM. HubSpot creates a contact. Salesforce creates a Lead or a Contact: &#x60;createAs&#x60;, else the connection&#39;s &#x60;createAs&#x60; setting (default &#x60;lead&#x60;).  Salesforce requires &#x60;lastName&#x60; on both, and &#x60;company&#x60; on a Lead (&#x60;[not provided]&#x60; when you send none). A Contact takes its company from its Account: set &#x60;properties.AccountId&#x60; instead.  HighLevel creates a contact in the connected location. A location that does not allow duplicates answers 409 with the existing contact.  Anything the CRM refuses (a required field, a validation rule, a duplicate rule) comes back as 422 or 409 with the CRM&#39;s own errors in &#x60;details.errors&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CrmApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CrmApi apiInstance = new CrmApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected HubSpot, Salesforce or HighLevel account (`GET /v1/accounts?platform=hubspot`, `salesforce` or `gohighlevel`).
        CreateCrmContactRequest createCrmContactRequest = new CreateCrmContactRequest(); // CreateCrmContactRequest | 
        try {
            ApiResponse<CreateCrmContact201Response> response = apiInstance.createCrmContactWithHttpInfo(accountId, createCrmContactRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CrmApi#createCrmContact");
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
| **accountId** | **String**| The connected HubSpot, Salesforce or HighLevel account (&#x60;GET /v1/accounts?platform&#x3D;hubspot&#x60;, &#x60;salesforce&#x60; or &#x60;gohighlevel&#x60;). | |
| **createCrmContactRequest** | [**CreateCrmContactRequest**](CreateCrmContactRequest.md)|  | |

### Return type

ApiResponse<[**CreateCrmContact201Response**](CreateCrmContact201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The created contact, read back from the CRM. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;crm_scope_missing&#x60;: the connection did not grant a scope this call needs (&#x60;details.scope&#x60;), typically a HubSpot optional scope added after the portal connected, or a HighLevel scope (such as &#x60;users.readonly&#x60;) added after the location installed the app. Reconnect the CRM and approve it; the account id stays the same.  &#x60;crm_access_denied&#x60;: the CRM refused the connected user (Salesforce field-level security or sharing, a HubSpot permission). &#x60;details.errors&#x60; holds the CRM&#39;s own errors. |  -  |
| **404** | &#x60;account_not_found&#x60;: the accountId is not a CRM account you can access. &#x60;crm_record_not_found&#x60;: the CRM has no record with this id (deleted, merged, or another object type). |  -  |
| **409** | &#x60;crm_duplicate_record&#x60;: the CRM refused a duplicate (HubSpot: the email belongs to another contact; Salesforce: a duplicate rule; HighLevel: a location that does not allow duplicate contacts). &#x60;details.existingId&#x60; is the existing record when the CRM names it.  &#x60;account_disconnected&#x60;: the CRM account needs reconnecting; see AccountDisconnected. |  -  |
| **422** | The CRM refused the values: a validation rule, a required field, a bad picklist value or an unknown field. Code &#x60;crm_validation_failed&#x60;; &#x60;details.errors&#x60; lists the CRM&#39;s own errors, each with &#x60;code&#x60;, &#x60;message&#x60; and the &#x60;fields&#x60; at fault when the CRM names them. |  -  |
| **429** | Zernio paces every connection inside its CRM limits (HubSpot per portal, Salesforce per org, HighLevel per location, shared with the conversation sync). Code &#x60;rate_limited&#x60;; wait for &#x60;Retry-After&#x60; seconds. |  * Retry-After - Seconds to wait before retrying. <br>  |
| **502** | The platform returned a server error. |  -  |


## getCrmContact

> CreateCrmContact201Response getCrmContact(accountId, contactId, properties, includeRaw)

Get a CRM contact

Read one person from the connected CRM. On Salesforce the id can be a Contact (&#x60;003...&#x60;) or a Lead (&#x60;00Q...&#x60;).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CrmApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CrmApi apiInstance = new CrmApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected HubSpot, Salesforce or HighLevel account (`GET /v1/accounts?platform=hubspot`, `salesforce` or `gohighlevel`).
        String contactId = "contactId_example"; // String | The CRM's own id. HubSpot contact id, Salesforce Contact (`003...`) or Lead (`00Q...`) id, or HighLevel contact id.
        String properties = "properties_example"; // String | Comma-separated native field names to return in `properties` (at most 50), for example `lifecyclestage,hs_lead_status` or `LeadSource,Industry__c`. On HighLevel, a field of the record (`source`, `status`), or a custom field by id or key.
        Boolean includeRaw = false; // Boolean | Also return the CRM's own record as `raw`.
        try {
            CreateCrmContact201Response result = apiInstance.getCrmContact(accountId, contactId, properties, includeRaw);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CrmApi#getCrmContact");
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
| **accountId** | **String**| The connected HubSpot, Salesforce or HighLevel account (&#x60;GET /v1/accounts?platform&#x3D;hubspot&#x60;, &#x60;salesforce&#x60; or &#x60;gohighlevel&#x60;). | |
| **contactId** | **String**| The CRM&#39;s own id. HubSpot contact id, Salesforce Contact (&#x60;003...&#x60;) or Lead (&#x60;00Q...&#x60;) id, or HighLevel contact id. | |
| **properties** | **String**| Comma-separated native field names to return in &#x60;properties&#x60; (at most 50), for example &#x60;lifecyclestage,hs_lead_status&#x60; or &#x60;LeadSource,Industry__c&#x60;. On HighLevel, a field of the record (&#x60;source&#x60;, &#x60;status&#x60;), or a custom field by id or key. | [optional] |
| **includeRaw** | **Boolean**| Also return the CRM&#39;s own record as &#x60;raw&#x60;. | [optional] [default to false] |

### Return type

[**CreateCrmContact201Response**](CreateCrmContact201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The contact. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;crm_scope_missing&#x60;: the connection did not grant a scope this call needs (&#x60;details.scope&#x60;), typically a HubSpot optional scope added after the portal connected, or a HighLevel scope (such as &#x60;users.readonly&#x60;) added after the location installed the app. Reconnect the CRM and approve it; the account id stays the same.  &#x60;crm_access_denied&#x60;: the CRM refused the connected user (Salesforce field-level security or sharing, a HubSpot permission). &#x60;details.errors&#x60; holds the CRM&#39;s own errors. |  -  |
| **404** | &#x60;account_not_found&#x60;: the accountId is not a CRM account you can access. &#x60;crm_record_not_found&#x60;: the CRM has no record with this id (deleted, merged, or another object type). |  -  |
| **409** | The account exists but is disconnected (deactivated, or flagged as needing reconnection). Code &#x60;account_disconnected&#x60;.  &#x60;details&#x60; names the account (&#x60;accountId&#x60;, &#x60;platform&#x60;, &#x60;username&#x60;) with its &#x60;disconnectReason&#x60;, &#x60;disconnectionType&#x60;, &#x60;unhealthySince&#x60; and &#x60;action: reconnect&#x60;.  Reconnect the account (its accountId stays the same), then retry. The disconnect is also sent as the &#x60;account.disconnected&#x60; webhook. |  -  |
| **429** | Zernio paces every connection inside its CRM limits (HubSpot per portal, Salesforce per org, HighLevel per location, shared with the conversation sync). Code &#x60;rate_limited&#x60;; wait for &#x60;Retry-After&#x60; seconds. |  * Retry-After - Seconds to wait before retrying. <br>  |
| **502** | The platform returned a server error. |  -  |

## getCrmContactWithHttpInfo

> ApiResponse<CreateCrmContact201Response> getCrmContact getCrmContactWithHttpInfo(accountId, contactId, properties, includeRaw)

Get a CRM contact

Read one person from the connected CRM. On Salesforce the id can be a Contact (&#x60;003...&#x60;) or a Lead (&#x60;00Q...&#x60;).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CrmApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CrmApi apiInstance = new CrmApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected HubSpot, Salesforce or HighLevel account (`GET /v1/accounts?platform=hubspot`, `salesforce` or `gohighlevel`).
        String contactId = "contactId_example"; // String | The CRM's own id. HubSpot contact id, Salesforce Contact (`003...`) or Lead (`00Q...`) id, or HighLevel contact id.
        String properties = "properties_example"; // String | Comma-separated native field names to return in `properties` (at most 50), for example `lifecyclestage,hs_lead_status` or `LeadSource,Industry__c`. On HighLevel, a field of the record (`source`, `status`), or a custom field by id or key.
        Boolean includeRaw = false; // Boolean | Also return the CRM's own record as `raw`.
        try {
            ApiResponse<CreateCrmContact201Response> response = apiInstance.getCrmContactWithHttpInfo(accountId, contactId, properties, includeRaw);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CrmApi#getCrmContact");
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
| **accountId** | **String**| The connected HubSpot, Salesforce or HighLevel account (&#x60;GET /v1/accounts?platform&#x3D;hubspot&#x60;, &#x60;salesforce&#x60; or &#x60;gohighlevel&#x60;). | |
| **contactId** | **String**| The CRM&#39;s own id. HubSpot contact id, Salesforce Contact (&#x60;003...&#x60;) or Lead (&#x60;00Q...&#x60;) id, or HighLevel contact id. | |
| **properties** | **String**| Comma-separated native field names to return in &#x60;properties&#x60; (at most 50), for example &#x60;lifecyclestage,hs_lead_status&#x60; or &#x60;LeadSource,Industry__c&#x60;. On HighLevel, a field of the record (&#x60;source&#x60;, &#x60;status&#x60;), or a custom field by id or key. | [optional] |
| **includeRaw** | **Boolean**| Also return the CRM&#39;s own record as &#x60;raw&#x60;. | [optional] [default to false] |

### Return type

ApiResponse<[**CreateCrmContact201Response**](CreateCrmContact201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The contact. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;crm_scope_missing&#x60;: the connection did not grant a scope this call needs (&#x60;details.scope&#x60;), typically a HubSpot optional scope added after the portal connected, or a HighLevel scope (such as &#x60;users.readonly&#x60;) added after the location installed the app. Reconnect the CRM and approve it; the account id stays the same.  &#x60;crm_access_denied&#x60;: the CRM refused the connected user (Salesforce field-level security or sharing, a HubSpot permission). &#x60;details.errors&#x60; holds the CRM&#39;s own errors. |  -  |
| **404** | &#x60;account_not_found&#x60;: the accountId is not a CRM account you can access. &#x60;crm_record_not_found&#x60;: the CRM has no record with this id (deleted, merged, or another object type). |  -  |
| **409** | The account exists but is disconnected (deactivated, or flagged as needing reconnection). Code &#x60;account_disconnected&#x60;.  &#x60;details&#x60; names the account (&#x60;accountId&#x60;, &#x60;platform&#x60;, &#x60;username&#x60;) with its &#x60;disconnectReason&#x60;, &#x60;disconnectionType&#x60;, &#x60;unhealthySince&#x60; and &#x60;action: reconnect&#x60;.  Reconnect the account (its accountId stays the same), then retry. The disconnect is also sent as the &#x60;account.disconnected&#x60; webhook. |  -  |
| **429** | Zernio paces every connection inside its CRM limits (HubSpot per portal, Salesforce per org, HighLevel per location, shared with the conversation sync). Code &#x60;rate_limited&#x60;; wait for &#x60;Retry-After&#x60; seconds. |  * Retry-After - Seconds to wait before retrying. <br>  |
| **502** | The platform returned a server error. |  -  |


## getCrmDeal

> GetCrmDeal200Response getCrmDeal(accountId, dealId, properties, includeRaw)

Get a CRM deal

Read one deal (HubSpot), Opportunity (Salesforce) or opportunity (HighLevel) with its contacts.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CrmApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CrmApi apiInstance = new CrmApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected HubSpot, Salesforce or HighLevel account (`GET /v1/accounts?platform=hubspot`, `salesforce` or `gohighlevel`).
        String dealId = "dealId_example"; // String | HubSpot deal id, Salesforce Opportunity id (`006...`) or HighLevel opportunity id.
        String properties = "properties_example"; // String | Comma-separated native field names to return in `properties` (at most 50), for example `lifecyclestage,hs_lead_status` or `LeadSource,Industry__c`. On HighLevel, a field of the record (`source`, `status`), or a custom field by id or key.
        Boolean includeRaw = false; // Boolean | Also return the CRM's own record as `raw`.
        try {
            GetCrmDeal200Response result = apiInstance.getCrmDeal(accountId, dealId, properties, includeRaw);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CrmApi#getCrmDeal");
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
| **accountId** | **String**| The connected HubSpot, Salesforce or HighLevel account (&#x60;GET /v1/accounts?platform&#x3D;hubspot&#x60;, &#x60;salesforce&#x60; or &#x60;gohighlevel&#x60;). | |
| **dealId** | **String**| HubSpot deal id, Salesforce Opportunity id (&#x60;006...&#x60;) or HighLevel opportunity id. | |
| **properties** | **String**| Comma-separated native field names to return in &#x60;properties&#x60; (at most 50), for example &#x60;lifecyclestage,hs_lead_status&#x60; or &#x60;LeadSource,Industry__c&#x60;. On HighLevel, a field of the record (&#x60;source&#x60;, &#x60;status&#x60;), or a custom field by id or key. | [optional] |
| **includeRaw** | **Boolean**| Also return the CRM&#39;s own record as &#x60;raw&#x60;. | [optional] [default to false] |

### Return type

[**GetCrmDeal200Response**](GetCrmDeal200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deal. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;crm_scope_missing&#x60;: the connection did not grant a scope this call needs (&#x60;details.scope&#x60;), typically a HubSpot optional scope added after the portal connected, or a HighLevel scope (such as &#x60;users.readonly&#x60;) added after the location installed the app. Reconnect the CRM and approve it; the account id stays the same.  &#x60;crm_access_denied&#x60;: the CRM refused the connected user (Salesforce field-level security or sharing, a HubSpot permission). &#x60;details.errors&#x60; holds the CRM&#39;s own errors. |  -  |
| **404** | &#x60;account_not_found&#x60;: the accountId is not a CRM account you can access. &#x60;crm_record_not_found&#x60;: the CRM has no record with this id (deleted, merged, or another object type). |  -  |
| **409** | The account exists but is disconnected (deactivated, or flagged as needing reconnection). Code &#x60;account_disconnected&#x60;.  &#x60;details&#x60; names the account (&#x60;accountId&#x60;, &#x60;platform&#x60;, &#x60;username&#x60;) with its &#x60;disconnectReason&#x60;, &#x60;disconnectionType&#x60;, &#x60;unhealthySince&#x60; and &#x60;action: reconnect&#x60;.  Reconnect the account (its accountId stays the same), then retry. The disconnect is also sent as the &#x60;account.disconnected&#x60; webhook. |  -  |
| **429** | Zernio paces every connection inside its CRM limits (HubSpot per portal, Salesforce per org, HighLevel per location, shared with the conversation sync). Code &#x60;rate_limited&#x60;; wait for &#x60;Retry-After&#x60; seconds. |  * Retry-After - Seconds to wait before retrying. <br>  |
| **502** | The platform returned a server error. |  -  |

## getCrmDealWithHttpInfo

> ApiResponse<GetCrmDeal200Response> getCrmDeal getCrmDealWithHttpInfo(accountId, dealId, properties, includeRaw)

Get a CRM deal

Read one deal (HubSpot), Opportunity (Salesforce) or opportunity (HighLevel) with its contacts.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CrmApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CrmApi apiInstance = new CrmApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected HubSpot, Salesforce or HighLevel account (`GET /v1/accounts?platform=hubspot`, `salesforce` or `gohighlevel`).
        String dealId = "dealId_example"; // String | HubSpot deal id, Salesforce Opportunity id (`006...`) or HighLevel opportunity id.
        String properties = "properties_example"; // String | Comma-separated native field names to return in `properties` (at most 50), for example `lifecyclestage,hs_lead_status` or `LeadSource,Industry__c`. On HighLevel, a field of the record (`source`, `status`), or a custom field by id or key.
        Boolean includeRaw = false; // Boolean | Also return the CRM's own record as `raw`.
        try {
            ApiResponse<GetCrmDeal200Response> response = apiInstance.getCrmDealWithHttpInfo(accountId, dealId, properties, includeRaw);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CrmApi#getCrmDeal");
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
| **accountId** | **String**| The connected HubSpot, Salesforce or HighLevel account (&#x60;GET /v1/accounts?platform&#x3D;hubspot&#x60;, &#x60;salesforce&#x60; or &#x60;gohighlevel&#x60;). | |
| **dealId** | **String**| HubSpot deal id, Salesforce Opportunity id (&#x60;006...&#x60;) or HighLevel opportunity id. | |
| **properties** | **String**| Comma-separated native field names to return in &#x60;properties&#x60; (at most 50), for example &#x60;lifecyclestage,hs_lead_status&#x60; or &#x60;LeadSource,Industry__c&#x60;. On HighLevel, a field of the record (&#x60;source&#x60;, &#x60;status&#x60;), or a custom field by id or key. | [optional] |
| **includeRaw** | **Boolean**| Also return the CRM&#39;s own record as &#x60;raw&#x60;. | [optional] [default to false] |

### Return type

ApiResponse<[**GetCrmDeal200Response**](GetCrmDeal200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The deal. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;crm_scope_missing&#x60;: the connection did not grant a scope this call needs (&#x60;details.scope&#x60;), typically a HubSpot optional scope added after the portal connected, or a HighLevel scope (such as &#x60;users.readonly&#x60;) added after the location installed the app. Reconnect the CRM and approve it; the account id stays the same.  &#x60;crm_access_denied&#x60;: the CRM refused the connected user (Salesforce field-level security or sharing, a HubSpot permission). &#x60;details.errors&#x60; holds the CRM&#39;s own errors. |  -  |
| **404** | &#x60;account_not_found&#x60;: the accountId is not a CRM account you can access. &#x60;crm_record_not_found&#x60;: the CRM has no record with this id (deleted, merged, or another object type). |  -  |
| **409** | The account exists but is disconnected (deactivated, or flagged as needing reconnection). Code &#x60;account_disconnected&#x60;.  &#x60;details&#x60; names the account (&#x60;accountId&#x60;, &#x60;platform&#x60;, &#x60;username&#x60;) with its &#x60;disconnectReason&#x60;, &#x60;disconnectionType&#x60;, &#x60;unhealthySince&#x60; and &#x60;action: reconnect&#x60;.  Reconnect the account (its accountId stays the same), then retry. The disconnect is also sent as the &#x60;account.disconnected&#x60; webhook. |  -  |
| **429** | Zernio paces every connection inside its CRM limits (HubSpot per portal, Salesforce per org, HighLevel per location, shared with the conversation sync). Code &#x60;rate_limited&#x60;; wait for &#x60;Retry-After&#x60; seconds. |  * Retry-After - Seconds to wait before retrying. <br>  |
| **502** | The platform returned a server error. |  -  |


## listCrmDeals

> ListCrmDeals200Response listCrmDeals(accountId, stage, updatedSince, properties, includeRaw, limit, cursor)

List CRM deals

List deals (HubSpot) or Opportunities (Salesforce), most recently changed first, or a HighLevel location&#39;s opportunities in HighLevel&#39;s own order.  HubSpot needs the portal to have granted &#x60;crm.objects.deals.read&#x60;; otherwise 403 &#x60;crm_scope_missing&#x60;. HighLevel cannot filter by update time: &#x60;updatedSince&#x60; answers 400 there.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CrmApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CrmApi apiInstance = new CrmApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected HubSpot, Salesforce or HighLevel account (`GET /v1/accounts?platform=hubspot`, `salesforce` or `gohighlevel`).
        String stage = "stage_example"; // String | Only deals in this stage. HubSpot takes the stage's internal id (`closedwon`, `appointmentscheduled`); Salesforce the `StageName` (`Closed Won`); HighLevel the pipeline stage id.
        OffsetDateTime updatedSince = OffsetDateTime.now(); // OffsetDateTime | Only deals changed at or after this time. HubSpot and Salesforce only.
        String properties = "properties_example"; // String | Comma-separated native field names to return in `properties` (at most 50), for example `lifecyclestage,hs_lead_status` or `LeadSource,Industry__c`. On HighLevel, a field of the record (`source`, `status`), or a custom field by id or key.
        Boolean includeRaw = false; // Boolean | Also return the CRM's own record as `raw`.
        Integer limit = 25; // Integer | 
        String cursor = "cursor_example"; // String | The `nextCursor` of the previous page, unchanged.
        try {
            ListCrmDeals200Response result = apiInstance.listCrmDeals(accountId, stage, updatedSince, properties, includeRaw, limit, cursor);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CrmApi#listCrmDeals");
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
| **accountId** | **String**| The connected HubSpot, Salesforce or HighLevel account (&#x60;GET /v1/accounts?platform&#x3D;hubspot&#x60;, &#x60;salesforce&#x60; or &#x60;gohighlevel&#x60;). | |
| **stage** | **String**| Only deals in this stage. HubSpot takes the stage&#39;s internal id (&#x60;closedwon&#x60;, &#x60;appointmentscheduled&#x60;); Salesforce the &#x60;StageName&#x60; (&#x60;Closed Won&#x60;); HighLevel the pipeline stage id. | [optional] |
| **updatedSince** | **OffsetDateTime**| Only deals changed at or after this time. HubSpot and Salesforce only. | [optional] |
| **properties** | **String**| Comma-separated native field names to return in &#x60;properties&#x60; (at most 50), for example &#x60;lifecyclestage,hs_lead_status&#x60; or &#x60;LeadSource,Industry__c&#x60;. On HighLevel, a field of the record (&#x60;source&#x60;, &#x60;status&#x60;), or a custom field by id or key. | [optional] |
| **includeRaw** | **Boolean**| Also return the CRM&#39;s own record as &#x60;raw&#x60;. | [optional] [default to false] |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **cursor** | **String**| The &#x60;nextCursor&#x60; of the previous page, unchanged. | [optional] |

### Return type

[**ListCrmDeals200Response**](ListCrmDeals200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One page of deals. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;crm_scope_missing&#x60;: the connection did not grant a scope this call needs (&#x60;details.scope&#x60;), typically a HubSpot optional scope added after the portal connected, or a HighLevel scope (such as &#x60;users.readonly&#x60;) added after the location installed the app. Reconnect the CRM and approve it; the account id stays the same.  &#x60;crm_access_denied&#x60;: the CRM refused the connected user (Salesforce field-level security or sharing, a HubSpot permission). &#x60;details.errors&#x60; holds the CRM&#39;s own errors. |  -  |
| **404** | &#x60;account_not_found&#x60;: the accountId is not a CRM account you can access. &#x60;crm_record_not_found&#x60;: the CRM has no record with this id (deleted, merged, or another object type). |  -  |
| **409** | The account exists but is disconnected (deactivated, or flagged as needing reconnection). Code &#x60;account_disconnected&#x60;.  &#x60;details&#x60; names the account (&#x60;accountId&#x60;, &#x60;platform&#x60;, &#x60;username&#x60;) with its &#x60;disconnectReason&#x60;, &#x60;disconnectionType&#x60;, &#x60;unhealthySince&#x60; and &#x60;action: reconnect&#x60;.  Reconnect the account (its accountId stays the same), then retry. The disconnect is also sent as the &#x60;account.disconnected&#x60; webhook. |  -  |
| **429** | Zernio paces every connection inside its CRM limits (HubSpot per portal, Salesforce per org, HighLevel per location, shared with the conversation sync). Code &#x60;rate_limited&#x60;; wait for &#x60;Retry-After&#x60; seconds. |  * Retry-After - Seconds to wait before retrying. <br>  |
| **502** | The platform returned a server error. |  -  |

## listCrmDealsWithHttpInfo

> ApiResponse<ListCrmDeals200Response> listCrmDeals listCrmDealsWithHttpInfo(accountId, stage, updatedSince, properties, includeRaw, limit, cursor)

List CRM deals

List deals (HubSpot) or Opportunities (Salesforce), most recently changed first, or a HighLevel location&#39;s opportunities in HighLevel&#39;s own order.  HubSpot needs the portal to have granted &#x60;crm.objects.deals.read&#x60;; otherwise 403 &#x60;crm_scope_missing&#x60;. HighLevel cannot filter by update time: &#x60;updatedSince&#x60; answers 400 there.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CrmApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CrmApi apiInstance = new CrmApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected HubSpot, Salesforce or HighLevel account (`GET /v1/accounts?platform=hubspot`, `salesforce` or `gohighlevel`).
        String stage = "stage_example"; // String | Only deals in this stage. HubSpot takes the stage's internal id (`closedwon`, `appointmentscheduled`); Salesforce the `StageName` (`Closed Won`); HighLevel the pipeline stage id.
        OffsetDateTime updatedSince = OffsetDateTime.now(); // OffsetDateTime | Only deals changed at or after this time. HubSpot and Salesforce only.
        String properties = "properties_example"; // String | Comma-separated native field names to return in `properties` (at most 50), for example `lifecyclestage,hs_lead_status` or `LeadSource,Industry__c`. On HighLevel, a field of the record (`source`, `status`), or a custom field by id or key.
        Boolean includeRaw = false; // Boolean | Also return the CRM's own record as `raw`.
        Integer limit = 25; // Integer | 
        String cursor = "cursor_example"; // String | The `nextCursor` of the previous page, unchanged.
        try {
            ApiResponse<ListCrmDeals200Response> response = apiInstance.listCrmDealsWithHttpInfo(accountId, stage, updatedSince, properties, includeRaw, limit, cursor);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CrmApi#listCrmDeals");
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
| **accountId** | **String**| The connected HubSpot, Salesforce or HighLevel account (&#x60;GET /v1/accounts?platform&#x3D;hubspot&#x60;, &#x60;salesforce&#x60; or &#x60;gohighlevel&#x60;). | |
| **stage** | **String**| Only deals in this stage. HubSpot takes the stage&#39;s internal id (&#x60;closedwon&#x60;, &#x60;appointmentscheduled&#x60;); Salesforce the &#x60;StageName&#x60; (&#x60;Closed Won&#x60;); HighLevel the pipeline stage id. | [optional] |
| **updatedSince** | **OffsetDateTime**| Only deals changed at or after this time. HubSpot and Salesforce only. | [optional] |
| **properties** | **String**| Comma-separated native field names to return in &#x60;properties&#x60; (at most 50), for example &#x60;lifecyclestage,hs_lead_status&#x60; or &#x60;LeadSource,Industry__c&#x60;. On HighLevel, a field of the record (&#x60;source&#x60;, &#x60;status&#x60;), or a custom field by id or key. | [optional] |
| **includeRaw** | **Boolean**| Also return the CRM&#39;s own record as &#x60;raw&#x60;. | [optional] [default to false] |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **cursor** | **String**| The &#x60;nextCursor&#x60; of the previous page, unchanged. | [optional] |

### Return type

ApiResponse<[**ListCrmDeals200Response**](ListCrmDeals200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One page of deals. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;crm_scope_missing&#x60;: the connection did not grant a scope this call needs (&#x60;details.scope&#x60;), typically a HubSpot optional scope added after the portal connected, or a HighLevel scope (such as &#x60;users.readonly&#x60;) added after the location installed the app. Reconnect the CRM and approve it; the account id stays the same.  &#x60;crm_access_denied&#x60;: the CRM refused the connected user (Salesforce field-level security or sharing, a HubSpot permission). &#x60;details.errors&#x60; holds the CRM&#39;s own errors. |  -  |
| **404** | &#x60;account_not_found&#x60;: the accountId is not a CRM account you can access. &#x60;crm_record_not_found&#x60;: the CRM has no record with this id (deleted, merged, or another object type). |  -  |
| **409** | The account exists but is disconnected (deactivated, or flagged as needing reconnection). Code &#x60;account_disconnected&#x60;.  &#x60;details&#x60; names the account (&#x60;accountId&#x60;, &#x60;platform&#x60;, &#x60;username&#x60;) with its &#x60;disconnectReason&#x60;, &#x60;disconnectionType&#x60;, &#x60;unhealthySince&#x60; and &#x60;action: reconnect&#x60;.  Reconnect the account (its accountId stays the same), then retry. The disconnect is also sent as the &#x60;account.disconnected&#x60; webhook. |  -  |
| **429** | Zernio paces every connection inside its CRM limits (HubSpot per portal, Salesforce per org, HighLevel per location, shared with the conversation sync). Code &#x60;rate_limited&#x60;; wait for &#x60;Retry-After&#x60; seconds. |  * Retry-After - Seconds to wait before retrying. <br>  |
| **502** | The platform returned a server error. |  -  |


## listCrmOwners

> ListCrmOwners200Response listCrmOwners(accountId, includeRaw, limit, cursor)

List CRM owners

List the users records can be assigned to: HubSpot owners, active standard Salesforce users, or the HighLevel location&#39;s users. Use an &#x60;id&#x60; as &#x60;ownerId&#x60; on contacts and deals.  HubSpot needs &#x60;crm.objects.owners.read&#x60;, an optional scope portals approve when they connect; without it, 403 &#x60;crm_scope_missing&#x60; asks to reconnect HubSpot. HighLevel needs &#x60;users.readonly&#x60;: a location installed before Zernio asked for it answers 403 &#x60;crm_scope_missing&#x60; until it reconnects.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CrmApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CrmApi apiInstance = new CrmApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected HubSpot, Salesforce or HighLevel account (`GET /v1/accounts?platform=hubspot`, `salesforce` or `gohighlevel`).
        Boolean includeRaw = false; // Boolean | Also return the CRM's own record as `raw`.
        Integer limit = 25; // Integer | 
        String cursor = "cursor_example"; // String | The `nextCursor` of the previous page, unchanged.
        try {
            ListCrmOwners200Response result = apiInstance.listCrmOwners(accountId, includeRaw, limit, cursor);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CrmApi#listCrmOwners");
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
| **accountId** | **String**| The connected HubSpot, Salesforce or HighLevel account (&#x60;GET /v1/accounts?platform&#x3D;hubspot&#x60;, &#x60;salesforce&#x60; or &#x60;gohighlevel&#x60;). | |
| **includeRaw** | **Boolean**| Also return the CRM&#39;s own record as &#x60;raw&#x60;. | [optional] [default to false] |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **cursor** | **String**| The &#x60;nextCursor&#x60; of the previous page, unchanged. | [optional] |

### Return type

[**ListCrmOwners200Response**](ListCrmOwners200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One page of owners. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;crm_scope_missing&#x60;: the connection did not grant a scope this call needs (&#x60;details.scope&#x60;), typically a HubSpot optional scope added after the portal connected, or a HighLevel scope (such as &#x60;users.readonly&#x60;) added after the location installed the app. Reconnect the CRM and approve it; the account id stays the same.  &#x60;crm_access_denied&#x60;: the CRM refused the connected user (Salesforce field-level security or sharing, a HubSpot permission). &#x60;details.errors&#x60; holds the CRM&#39;s own errors. |  -  |
| **404** | &#x60;account_not_found&#x60;: the accountId is not a CRM account you can access. &#x60;crm_record_not_found&#x60;: the CRM has no record with this id (deleted, merged, or another object type). |  -  |
| **409** | The account exists but is disconnected (deactivated, or flagged as needing reconnection). Code &#x60;account_disconnected&#x60;.  &#x60;details&#x60; names the account (&#x60;accountId&#x60;, &#x60;platform&#x60;, &#x60;username&#x60;) with its &#x60;disconnectReason&#x60;, &#x60;disconnectionType&#x60;, &#x60;unhealthySince&#x60; and &#x60;action: reconnect&#x60;.  Reconnect the account (its accountId stays the same), then retry. The disconnect is also sent as the &#x60;account.disconnected&#x60; webhook. |  -  |
| **429** | Zernio paces every connection inside its CRM limits (HubSpot per portal, Salesforce per org, HighLevel per location, shared with the conversation sync). Code &#x60;rate_limited&#x60;; wait for &#x60;Retry-After&#x60; seconds. |  * Retry-After - Seconds to wait before retrying. <br>  |
| **502** | The platform returned a server error. |  -  |

## listCrmOwnersWithHttpInfo

> ApiResponse<ListCrmOwners200Response> listCrmOwners listCrmOwnersWithHttpInfo(accountId, includeRaw, limit, cursor)

List CRM owners

List the users records can be assigned to: HubSpot owners, active standard Salesforce users, or the HighLevel location&#39;s users. Use an &#x60;id&#x60; as &#x60;ownerId&#x60; on contacts and deals.  HubSpot needs &#x60;crm.objects.owners.read&#x60;, an optional scope portals approve when they connect; without it, 403 &#x60;crm_scope_missing&#x60; asks to reconnect HubSpot. HighLevel needs &#x60;users.readonly&#x60;: a location installed before Zernio asked for it answers 403 &#x60;crm_scope_missing&#x60; until it reconnects.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CrmApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CrmApi apiInstance = new CrmApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected HubSpot, Salesforce or HighLevel account (`GET /v1/accounts?platform=hubspot`, `salesforce` or `gohighlevel`).
        Boolean includeRaw = false; // Boolean | Also return the CRM's own record as `raw`.
        Integer limit = 25; // Integer | 
        String cursor = "cursor_example"; // String | The `nextCursor` of the previous page, unchanged.
        try {
            ApiResponse<ListCrmOwners200Response> response = apiInstance.listCrmOwnersWithHttpInfo(accountId, includeRaw, limit, cursor);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CrmApi#listCrmOwners");
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
| **accountId** | **String**| The connected HubSpot, Salesforce or HighLevel account (&#x60;GET /v1/accounts?platform&#x3D;hubspot&#x60;, &#x60;salesforce&#x60; or &#x60;gohighlevel&#x60;). | |
| **includeRaw** | **Boolean**| Also return the CRM&#39;s own record as &#x60;raw&#x60;. | [optional] [default to false] |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **cursor** | **String**| The &#x60;nextCursor&#x60; of the previous page, unchanged. | [optional] |

### Return type

ApiResponse<[**ListCrmOwners200Response**](ListCrmOwners200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | One page of owners. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;crm_scope_missing&#x60;: the connection did not grant a scope this call needs (&#x60;details.scope&#x60;), typically a HubSpot optional scope added after the portal connected, or a HighLevel scope (such as &#x60;users.readonly&#x60;) added after the location installed the app. Reconnect the CRM and approve it; the account id stays the same.  &#x60;crm_access_denied&#x60;: the CRM refused the connected user (Salesforce field-level security or sharing, a HubSpot permission). &#x60;details.errors&#x60; holds the CRM&#39;s own errors. |  -  |
| **404** | &#x60;account_not_found&#x60;: the accountId is not a CRM account you can access. &#x60;crm_record_not_found&#x60;: the CRM has no record with this id (deleted, merged, or another object type). |  -  |
| **409** | The account exists but is disconnected (deactivated, or flagged as needing reconnection). Code &#x60;account_disconnected&#x60;.  &#x60;details&#x60; names the account (&#x60;accountId&#x60;, &#x60;platform&#x60;, &#x60;username&#x60;) with its &#x60;disconnectReason&#x60;, &#x60;disconnectionType&#x60;, &#x60;unhealthySince&#x60; and &#x60;action: reconnect&#x60;.  Reconnect the account (its accountId stays the same), then retry. The disconnect is also sent as the &#x60;account.disconnected&#x60; webhook. |  -  |
| **429** | Zernio paces every connection inside its CRM limits (HubSpot per portal, Salesforce per org, HighLevel per location, shared with the conversation sync). Code &#x60;rate_limited&#x60;; wait for &#x60;Retry-After&#x60; seconds. |  * Retry-After - Seconds to wait before retrying. <br>  |
| **502** | The platform returned a server error. |  -  |


## searchCrmContacts

> SearchCrmContacts200Response searchCrmContacts(accountId, q, email, phone, properties, includeRaw, limit, cursor)

Search CRM contacts

Find people in the connected CRM by free text, email or phone. Send exactly one of &#x60;q&#x60;, &#x60;email&#x60; or &#x60;phone&#x60;.  HubSpot searches contacts. Salesforce searches Contacts and Leads that are not converted (&#x60;objectType&#x60; tells which), newest change first. HighLevel searches the location&#39;s contacts.  - &#x60;email&#x60; is an exact match. - &#x60;phone&#x60; takes an international number and matches it however the CRM stored it (\&quot;+44 7911 123456\&quot;, \&quot;07911 123456\&quot;). - &#x60;q&#x60; searches names, emails, phones and company. On Salesforce, &#x60;q&#x60; and &#x60;phone&#x60; use the search index, so a record saved in the last few minutes may not show yet; &#x60;email&#x60; never lags. - On HighLevel, &#x60;email&#x60; and &#x60;phone&#x60; use the location&#39;s duplicate check: at most one contact, with no next page.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CrmApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CrmApi apiInstance = new CrmApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected HubSpot, Salesforce or HighLevel account (`GET /v1/accounts?platform=hubspot`, `salesforce` or `gohighlevel`).
        String q = "q_example"; // String | Free text, at least 2 characters.
        String email = "email_example"; // String | 
        String phone = "phone_example"; // String | International number with its country code, for example `+14155550100`.
        String properties = "properties_example"; // String | Comma-separated native field names to return in `properties` (at most 50), for example `lifecyclestage,hs_lead_status` or `LeadSource,Industry__c`. On HighLevel, a field of the record (`source`, `status`), or a custom field by id or key.
        Boolean includeRaw = false; // Boolean | Also return the CRM's own record as `raw`.
        Integer limit = 25; // Integer | 
        String cursor = "cursor_example"; // String | The `nextCursor` of the previous page, unchanged.
        try {
            SearchCrmContacts200Response result = apiInstance.searchCrmContacts(accountId, q, email, phone, properties, includeRaw, limit, cursor);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CrmApi#searchCrmContacts");
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
| **accountId** | **String**| The connected HubSpot, Salesforce or HighLevel account (&#x60;GET /v1/accounts?platform&#x3D;hubspot&#x60;, &#x60;salesforce&#x60; or &#x60;gohighlevel&#x60;). | |
| **q** | **String**| Free text, at least 2 characters. | [optional] |
| **email** | **String**|  | [optional] |
| **phone** | **String**| International number with its country code, for example &#x60;+14155550100&#x60;. | [optional] |
| **properties** | **String**| Comma-separated native field names to return in &#x60;properties&#x60; (at most 50), for example &#x60;lifecyclestage,hs_lead_status&#x60; or &#x60;LeadSource,Industry__c&#x60;. On HighLevel, a field of the record (&#x60;source&#x60;, &#x60;status&#x60;), or a custom field by id or key. | [optional] |
| **includeRaw** | **Boolean**| Also return the CRM&#39;s own record as &#x60;raw&#x60;. | [optional] [default to false] |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **cursor** | **String**| The &#x60;nextCursor&#x60; of the previous page, unchanged. | [optional] |

### Return type

[**SearchCrmContacts200Response**](SearchCrmContacts200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Matching contacts, one page. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;crm_scope_missing&#x60;: the connection did not grant a scope this call needs (&#x60;details.scope&#x60;), typically a HubSpot optional scope added after the portal connected, or a HighLevel scope (such as &#x60;users.readonly&#x60;) added after the location installed the app. Reconnect the CRM and approve it; the account id stays the same.  &#x60;crm_access_denied&#x60;: the CRM refused the connected user (Salesforce field-level security or sharing, a HubSpot permission). &#x60;details.errors&#x60; holds the CRM&#39;s own errors. |  -  |
| **404** | &#x60;account_not_found&#x60;: the accountId is not a CRM account you can access. &#x60;crm_record_not_found&#x60;: the CRM has no record with this id (deleted, merged, or another object type). |  -  |
| **409** | The account exists but is disconnected (deactivated, or flagged as needing reconnection). Code &#x60;account_disconnected&#x60;.  &#x60;details&#x60; names the account (&#x60;accountId&#x60;, &#x60;platform&#x60;, &#x60;username&#x60;) with its &#x60;disconnectReason&#x60;, &#x60;disconnectionType&#x60;, &#x60;unhealthySince&#x60; and &#x60;action: reconnect&#x60;.  Reconnect the account (its accountId stays the same), then retry. The disconnect is also sent as the &#x60;account.disconnected&#x60; webhook. |  -  |
| **429** | Zernio paces every connection inside its CRM limits (HubSpot per portal, Salesforce per org, HighLevel per location, shared with the conversation sync). Code &#x60;rate_limited&#x60;; wait for &#x60;Retry-After&#x60; seconds. |  * Retry-After - Seconds to wait before retrying. <br>  |
| **502** | The platform returned a server error. |  -  |

## searchCrmContactsWithHttpInfo

> ApiResponse<SearchCrmContacts200Response> searchCrmContacts searchCrmContactsWithHttpInfo(accountId, q, email, phone, properties, includeRaw, limit, cursor)

Search CRM contacts

Find people in the connected CRM by free text, email or phone. Send exactly one of &#x60;q&#x60;, &#x60;email&#x60; or &#x60;phone&#x60;.  HubSpot searches contacts. Salesforce searches Contacts and Leads that are not converted (&#x60;objectType&#x60; tells which), newest change first. HighLevel searches the location&#39;s contacts.  - &#x60;email&#x60; is an exact match. - &#x60;phone&#x60; takes an international number and matches it however the CRM stored it (\&quot;+44 7911 123456\&quot;, \&quot;07911 123456\&quot;). - &#x60;q&#x60; searches names, emails, phones and company. On Salesforce, &#x60;q&#x60; and &#x60;phone&#x60; use the search index, so a record saved in the last few minutes may not show yet; &#x60;email&#x60; never lags. - On HighLevel, &#x60;email&#x60; and &#x60;phone&#x60; use the location&#39;s duplicate check: at most one contact, with no next page.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CrmApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CrmApi apiInstance = new CrmApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected HubSpot, Salesforce or HighLevel account (`GET /v1/accounts?platform=hubspot`, `salesforce` or `gohighlevel`).
        String q = "q_example"; // String | Free text, at least 2 characters.
        String email = "email_example"; // String | 
        String phone = "phone_example"; // String | International number with its country code, for example `+14155550100`.
        String properties = "properties_example"; // String | Comma-separated native field names to return in `properties` (at most 50), for example `lifecyclestage,hs_lead_status` or `LeadSource,Industry__c`. On HighLevel, a field of the record (`source`, `status`), or a custom field by id or key.
        Boolean includeRaw = false; // Boolean | Also return the CRM's own record as `raw`.
        Integer limit = 25; // Integer | 
        String cursor = "cursor_example"; // String | The `nextCursor` of the previous page, unchanged.
        try {
            ApiResponse<SearchCrmContacts200Response> response = apiInstance.searchCrmContactsWithHttpInfo(accountId, q, email, phone, properties, includeRaw, limit, cursor);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CrmApi#searchCrmContacts");
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
| **accountId** | **String**| The connected HubSpot, Salesforce or HighLevel account (&#x60;GET /v1/accounts?platform&#x3D;hubspot&#x60;, &#x60;salesforce&#x60; or &#x60;gohighlevel&#x60;). | |
| **q** | **String**| Free text, at least 2 characters. | [optional] |
| **email** | **String**|  | [optional] |
| **phone** | **String**| International number with its country code, for example &#x60;+14155550100&#x60;. | [optional] |
| **properties** | **String**| Comma-separated native field names to return in &#x60;properties&#x60; (at most 50), for example &#x60;lifecyclestage,hs_lead_status&#x60; or &#x60;LeadSource,Industry__c&#x60;. On HighLevel, a field of the record (&#x60;source&#x60;, &#x60;status&#x60;), or a custom field by id or key. | [optional] |
| **includeRaw** | **Boolean**| Also return the CRM&#39;s own record as &#x60;raw&#x60;. | [optional] [default to false] |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **cursor** | **String**| The &#x60;nextCursor&#x60; of the previous page, unchanged. | [optional] |

### Return type

ApiResponse<[**SearchCrmContacts200Response**](SearchCrmContacts200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Matching contacts, one page. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;crm_scope_missing&#x60;: the connection did not grant a scope this call needs (&#x60;details.scope&#x60;), typically a HubSpot optional scope added after the portal connected, or a HighLevel scope (such as &#x60;users.readonly&#x60;) added after the location installed the app. Reconnect the CRM and approve it; the account id stays the same.  &#x60;crm_access_denied&#x60;: the CRM refused the connected user (Salesforce field-level security or sharing, a HubSpot permission). &#x60;details.errors&#x60; holds the CRM&#39;s own errors. |  -  |
| **404** | &#x60;account_not_found&#x60;: the accountId is not a CRM account you can access. &#x60;crm_record_not_found&#x60;: the CRM has no record with this id (deleted, merged, or another object type). |  -  |
| **409** | The account exists but is disconnected (deactivated, or flagged as needing reconnection). Code &#x60;account_disconnected&#x60;.  &#x60;details&#x60; names the account (&#x60;accountId&#x60;, &#x60;platform&#x60;, &#x60;username&#x60;) with its &#x60;disconnectReason&#x60;, &#x60;disconnectionType&#x60;, &#x60;unhealthySince&#x60; and &#x60;action: reconnect&#x60;.  Reconnect the account (its accountId stays the same), then retry. The disconnect is also sent as the &#x60;account.disconnected&#x60; webhook. |  -  |
| **429** | Zernio paces every connection inside its CRM limits (HubSpot per portal, Salesforce per org, HighLevel per location, shared with the conversation sync). Code &#x60;rate_limited&#x60;; wait for &#x60;Retry-After&#x60; seconds. |  * Retry-After - Seconds to wait before retrying. <br>  |
| **502** | The platform returned a server error. |  -  |


## updateCrmContact

> CreateCrmContact201Response updateCrmContact(accountId, contactId, crmContactInput)

Update a CRM contact

Change fields on a person in the connected CRM. Send only what changes; &#x60;null&#x60; clears a field. Native fields go in &#x60;properties&#x60;.  On Salesforce, &#x60;company&#x60; applies to Leads only (400 on a Contact).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CrmApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CrmApi apiInstance = new CrmApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected HubSpot, Salesforce or HighLevel account (`GET /v1/accounts?platform=hubspot`, `salesforce` or `gohighlevel`).
        String contactId = "contactId_example"; // String | The CRM's own id. HubSpot contact id, Salesforce Contact (`003...`) or Lead (`00Q...`) id, or HighLevel contact id.
        CrmContactInput crmContactInput = new CrmContactInput(); // CrmContactInput | 
        try {
            CreateCrmContact201Response result = apiInstance.updateCrmContact(accountId, contactId, crmContactInput);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CrmApi#updateCrmContact");
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
| **accountId** | **String**| The connected HubSpot, Salesforce or HighLevel account (&#x60;GET /v1/accounts?platform&#x3D;hubspot&#x60;, &#x60;salesforce&#x60; or &#x60;gohighlevel&#x60;). | |
| **contactId** | **String**| The CRM&#39;s own id. HubSpot contact id, Salesforce Contact (&#x60;003...&#x60;) or Lead (&#x60;00Q...&#x60;) id, or HighLevel contact id. | |
| **crmContactInput** | [**CrmContactInput**](CrmContactInput.md)|  | |

### Return type

[**CreateCrmContact201Response**](CreateCrmContact201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated contact, read back from the CRM. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;crm_scope_missing&#x60;: the connection did not grant a scope this call needs (&#x60;details.scope&#x60;), typically a HubSpot optional scope added after the portal connected, or a HighLevel scope (such as &#x60;users.readonly&#x60;) added after the location installed the app. Reconnect the CRM and approve it; the account id stays the same.  &#x60;crm_access_denied&#x60;: the CRM refused the connected user (Salesforce field-level security or sharing, a HubSpot permission). &#x60;details.errors&#x60; holds the CRM&#39;s own errors. |  -  |
| **404** | &#x60;account_not_found&#x60;: the accountId is not a CRM account you can access. &#x60;crm_record_not_found&#x60;: the CRM has no record with this id (deleted, merged, or another object type). |  -  |
| **409** | &#x60;crm_duplicate_record&#x60;: the CRM refused a duplicate (HubSpot: the email belongs to another contact; Salesforce: a duplicate rule; HighLevel: a location that does not allow duplicate contacts). &#x60;details.existingId&#x60; is the existing record when the CRM names it.  &#x60;account_disconnected&#x60;: the CRM account needs reconnecting; see AccountDisconnected. |  -  |
| **422** | The CRM refused the values: a validation rule, a required field, a bad picklist value or an unknown field. Code &#x60;crm_validation_failed&#x60;; &#x60;details.errors&#x60; lists the CRM&#39;s own errors, each with &#x60;code&#x60;, &#x60;message&#x60; and the &#x60;fields&#x60; at fault when the CRM names them. |  -  |
| **429** | Zernio paces every connection inside its CRM limits (HubSpot per portal, Salesforce per org, HighLevel per location, shared with the conversation sync). Code &#x60;rate_limited&#x60;; wait for &#x60;Retry-After&#x60; seconds. |  * Retry-After - Seconds to wait before retrying. <br>  |
| **502** | The platform returned a server error. |  -  |

## updateCrmContactWithHttpInfo

> ApiResponse<CreateCrmContact201Response> updateCrmContact updateCrmContactWithHttpInfo(accountId, contactId, crmContactInput)

Update a CRM contact

Change fields on a person in the connected CRM. Send only what changes; &#x60;null&#x60; clears a field. Native fields go in &#x60;properties&#x60;.  On Salesforce, &#x60;company&#x60; applies to Leads only (400 on a Contact).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CrmApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CrmApi apiInstance = new CrmApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected HubSpot, Salesforce or HighLevel account (`GET /v1/accounts?platform=hubspot`, `salesforce` or `gohighlevel`).
        String contactId = "contactId_example"; // String | The CRM's own id. HubSpot contact id, Salesforce Contact (`003...`) or Lead (`00Q...`) id, or HighLevel contact id.
        CrmContactInput crmContactInput = new CrmContactInput(); // CrmContactInput | 
        try {
            ApiResponse<CreateCrmContact201Response> response = apiInstance.updateCrmContactWithHttpInfo(accountId, contactId, crmContactInput);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CrmApi#updateCrmContact");
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
| **accountId** | **String**| The connected HubSpot, Salesforce or HighLevel account (&#x60;GET /v1/accounts?platform&#x3D;hubspot&#x60;, &#x60;salesforce&#x60; or &#x60;gohighlevel&#x60;). | |
| **contactId** | **String**| The CRM&#39;s own id. HubSpot contact id, Salesforce Contact (&#x60;003...&#x60;) or Lead (&#x60;00Q...&#x60;) id, or HighLevel contact id. | |
| **crmContactInput** | [**CrmContactInput**](CrmContactInput.md)|  | |

### Return type

ApiResponse<[**CreateCrmContact201Response**](CreateCrmContact201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated contact, read back from the CRM. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;crm_scope_missing&#x60;: the connection did not grant a scope this call needs (&#x60;details.scope&#x60;), typically a HubSpot optional scope added after the portal connected, or a HighLevel scope (such as &#x60;users.readonly&#x60;) added after the location installed the app. Reconnect the CRM and approve it; the account id stays the same.  &#x60;crm_access_denied&#x60;: the CRM refused the connected user (Salesforce field-level security or sharing, a HubSpot permission). &#x60;details.errors&#x60; holds the CRM&#39;s own errors. |  -  |
| **404** | &#x60;account_not_found&#x60;: the accountId is not a CRM account you can access. &#x60;crm_record_not_found&#x60;: the CRM has no record with this id (deleted, merged, or another object type). |  -  |
| **409** | &#x60;crm_duplicate_record&#x60;: the CRM refused a duplicate (HubSpot: the email belongs to another contact; Salesforce: a duplicate rule; HighLevel: a location that does not allow duplicate contacts). &#x60;details.existingId&#x60; is the existing record when the CRM names it.  &#x60;account_disconnected&#x60;: the CRM account needs reconnecting; see AccountDisconnected. |  -  |
| **422** | The CRM refused the values: a validation rule, a required field, a bad picklist value or an unknown field. Code &#x60;crm_validation_failed&#x60;; &#x60;details.errors&#x60; lists the CRM&#39;s own errors, each with &#x60;code&#x60;, &#x60;message&#x60; and the &#x60;fields&#x60; at fault when the CRM names them. |  -  |
| **429** | Zernio paces every connection inside its CRM limits (HubSpot per portal, Salesforce per org, HighLevel per location, shared with the conversation sync). Code &#x60;rate_limited&#x60;; wait for &#x60;Retry-After&#x60; seconds. |  * Retry-After - Seconds to wait before retrying. <br>  |
| **502** | The platform returned a server error. |  -  |


## updateCrmDeal

> GetCrmDeal200Response updateCrmDeal(accountId, dealId, updateCrmDealRequest)

Update a CRM deal

Move a deal to another stage, or change its amount, close date, owner or native fields. Send only what changes.  HubSpot needs &#x60;crm.objects.deals.write&#x60;, an optional scope portals approve when they connect; without it, 403 &#x60;crm_scope_missing&#x60; asks to reconnect HubSpot. &#x60;currency&#x60; only works on multi-currency HubSpot portals and Salesforce orgs.  HighLevel: &#x60;stage&#x60; is the pipeline stage id, &#x60;amount&#x60; the opportunity value, and &#x60;properties.status&#x60; (&#x60;open&#x60;, &#x60;won&#x60;, &#x60;lost&#x60;, &#x60;abandoned&#x60;) marks it won or lost. Its opportunities have no close date or currency of their own: &#x60;closeDate&#x60; and &#x60;currency&#x60; answer 400.  Updating needs &#x60;opportunities.write&#x60;, which the Zernio HighLevel app does not request yet, so this call answers 403 &#x60;crm_scope_missing&#x60; on HighLevel for now.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CrmApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CrmApi apiInstance = new CrmApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected HubSpot, Salesforce or HighLevel account (`GET /v1/accounts?platform=hubspot`, `salesforce` or `gohighlevel`).
        String dealId = "dealId_example"; // String | HubSpot deal id, Salesforce Opportunity id (`006...`) or HighLevel opportunity id.
        UpdateCrmDealRequest updateCrmDealRequest = new UpdateCrmDealRequest(); // UpdateCrmDealRequest | 
        try {
            GetCrmDeal200Response result = apiInstance.updateCrmDeal(accountId, dealId, updateCrmDealRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling CrmApi#updateCrmDeal");
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
| **accountId** | **String**| The connected HubSpot, Salesforce or HighLevel account (&#x60;GET /v1/accounts?platform&#x3D;hubspot&#x60;, &#x60;salesforce&#x60; or &#x60;gohighlevel&#x60;). | |
| **dealId** | **String**| HubSpot deal id, Salesforce Opportunity id (&#x60;006...&#x60;) or HighLevel opportunity id. | |
| **updateCrmDealRequest** | [**UpdateCrmDealRequest**](UpdateCrmDealRequest.md)|  | |

### Return type

[**GetCrmDeal200Response**](GetCrmDeal200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated deal, read back from the CRM. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;crm_scope_missing&#x60;: the connection did not grant a scope this call needs (&#x60;details.scope&#x60;), typically a HubSpot optional scope added after the portal connected, or a HighLevel scope (such as &#x60;users.readonly&#x60;) added after the location installed the app. Reconnect the CRM and approve it; the account id stays the same.  &#x60;crm_access_denied&#x60;: the CRM refused the connected user (Salesforce field-level security or sharing, a HubSpot permission). &#x60;details.errors&#x60; holds the CRM&#39;s own errors. |  -  |
| **404** | &#x60;account_not_found&#x60;: the accountId is not a CRM account you can access. &#x60;crm_record_not_found&#x60;: the CRM has no record with this id (deleted, merged, or another object type). |  -  |
| **409** | The account exists but is disconnected (deactivated, or flagged as needing reconnection). Code &#x60;account_disconnected&#x60;.  &#x60;details&#x60; names the account (&#x60;accountId&#x60;, &#x60;platform&#x60;, &#x60;username&#x60;) with its &#x60;disconnectReason&#x60;, &#x60;disconnectionType&#x60;, &#x60;unhealthySince&#x60; and &#x60;action: reconnect&#x60;.  Reconnect the account (its accountId stays the same), then retry. The disconnect is also sent as the &#x60;account.disconnected&#x60; webhook. |  -  |
| **422** | The CRM refused the values: a validation rule, a required field, a bad picklist value or an unknown field. Code &#x60;crm_validation_failed&#x60;; &#x60;details.errors&#x60; lists the CRM&#39;s own errors, each with &#x60;code&#x60;, &#x60;message&#x60; and the &#x60;fields&#x60; at fault when the CRM names them. |  -  |
| **429** | Zernio paces every connection inside its CRM limits (HubSpot per portal, Salesforce per org, HighLevel per location, shared with the conversation sync). Code &#x60;rate_limited&#x60;; wait for &#x60;Retry-After&#x60; seconds. |  * Retry-After - Seconds to wait before retrying. <br>  |
| **502** | The platform returned a server error. |  -  |

## updateCrmDealWithHttpInfo

> ApiResponse<GetCrmDeal200Response> updateCrmDeal updateCrmDealWithHttpInfo(accountId, dealId, updateCrmDealRequest)

Update a CRM deal

Move a deal to another stage, or change its amount, close date, owner or native fields. Send only what changes.  HubSpot needs &#x60;crm.objects.deals.write&#x60;, an optional scope portals approve when they connect; without it, 403 &#x60;crm_scope_missing&#x60; asks to reconnect HubSpot. &#x60;currency&#x60; only works on multi-currency HubSpot portals and Salesforce orgs.  HighLevel: &#x60;stage&#x60; is the pipeline stage id, &#x60;amount&#x60; the opportunity value, and &#x60;properties.status&#x60; (&#x60;open&#x60;, &#x60;won&#x60;, &#x60;lost&#x60;, &#x60;abandoned&#x60;) marks it won or lost. Its opportunities have no close date or currency of their own: &#x60;closeDate&#x60; and &#x60;currency&#x60; answer 400.  Updating needs &#x60;opportunities.write&#x60;, which the Zernio HighLevel app does not request yet, so this call answers 403 &#x60;crm_scope_missing&#x60; on HighLevel for now.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.CrmApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        CrmApi apiInstance = new CrmApi(defaultClient);
        String accountId = "accountId_example"; // String | The connected HubSpot, Salesforce or HighLevel account (`GET /v1/accounts?platform=hubspot`, `salesforce` or `gohighlevel`).
        String dealId = "dealId_example"; // String | HubSpot deal id, Salesforce Opportunity id (`006...`) or HighLevel opportunity id.
        UpdateCrmDealRequest updateCrmDealRequest = new UpdateCrmDealRequest(); // UpdateCrmDealRequest | 
        try {
            ApiResponse<GetCrmDeal200Response> response = apiInstance.updateCrmDealWithHttpInfo(accountId, dealId, updateCrmDealRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling CrmApi#updateCrmDeal");
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
| **accountId** | **String**| The connected HubSpot, Salesforce or HighLevel account (&#x60;GET /v1/accounts?platform&#x3D;hubspot&#x60;, &#x60;salesforce&#x60; or &#x60;gohighlevel&#x60;). | |
| **dealId** | **String**| HubSpot deal id, Salesforce Opportunity id (&#x60;006...&#x60;) or HighLevel opportunity id. | |
| **updateCrmDealRequest** | [**UpdateCrmDealRequest**](UpdateCrmDealRequest.md)|  | |

### Return type

ApiResponse<[**GetCrmDeal200Response**](GetCrmDeal200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated deal, read back from the CRM. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | &#x60;crm_scope_missing&#x60;: the connection did not grant a scope this call needs (&#x60;details.scope&#x60;), typically a HubSpot optional scope added after the portal connected, or a HighLevel scope (such as &#x60;users.readonly&#x60;) added after the location installed the app. Reconnect the CRM and approve it; the account id stays the same.  &#x60;crm_access_denied&#x60;: the CRM refused the connected user (Salesforce field-level security or sharing, a HubSpot permission). &#x60;details.errors&#x60; holds the CRM&#39;s own errors. |  -  |
| **404** | &#x60;account_not_found&#x60;: the accountId is not a CRM account you can access. &#x60;crm_record_not_found&#x60;: the CRM has no record with this id (deleted, merged, or another object type). |  -  |
| **409** | The account exists but is disconnected (deactivated, or flagged as needing reconnection). Code &#x60;account_disconnected&#x60;.  &#x60;details&#x60; names the account (&#x60;accountId&#x60;, &#x60;platform&#x60;, &#x60;username&#x60;) with its &#x60;disconnectReason&#x60;, &#x60;disconnectionType&#x60;, &#x60;unhealthySince&#x60; and &#x60;action: reconnect&#x60;.  Reconnect the account (its accountId stays the same), then retry. The disconnect is also sent as the &#x60;account.disconnected&#x60; webhook. |  -  |
| **422** | The CRM refused the values: a validation rule, a required field, a bad picklist value or an unknown field. Code &#x60;crm_validation_failed&#x60;; &#x60;details.errors&#x60; lists the CRM&#39;s own errors, each with &#x60;code&#x60;, &#x60;message&#x60; and the &#x60;fields&#x60; at fault when the CRM names them. |  -  |
| **429** | Zernio paces every connection inside its CRM limits (HubSpot per portal, Salesforce per org, HighLevel per location, shared with the conversation sync). Code &#x60;rate_limited&#x60;; wait for &#x60;Retry-After&#x60; seconds. |  * Retry-After - Seconds to wait before retrying. <br>  |
| **502** | The platform returned a server error. |  -  |

