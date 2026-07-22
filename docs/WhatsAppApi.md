# WhatsAppApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addWhatsAppGroupParticipants**](WhatsAppApi.md#addWhatsAppGroupParticipants) | **POST** /v1/whatsapp/wa-groups/{groupId}/participants | Add participants |
| [**addWhatsAppGroupParticipantsWithHttpInfo**](WhatsAppApi.md#addWhatsAppGroupParticipantsWithHttpInfo) | **POST** /v1/whatsapp/wa-groups/{groupId}/participants | Add participants |
| [**approveWhatsAppGroupJoinRequests**](WhatsAppApi.md#approveWhatsAppGroupJoinRequests) | **POST** /v1/whatsapp/wa-groups/{groupId}/join-requests | Approve join requests |
| [**approveWhatsAppGroupJoinRequestsWithHttpInfo**](WhatsAppApi.md#approveWhatsAppGroupJoinRequestsWithHttpInfo) | **POST** /v1/whatsapp/wa-groups/{groupId}/join-requests | Approve join requests |
| [**blockWhatsAppUsers**](WhatsAppApi.md#blockWhatsAppUsers) | **POST** /v1/whatsapp/block-users | Block users |
| [**blockWhatsAppUsersWithHttpInfo**](WhatsAppApi.md#blockWhatsAppUsersWithHttpInfo) | **POST** /v1/whatsapp/block-users | Block users |
| [**createWhatsAppDataset**](WhatsAppApi.md#createWhatsAppDataset) | **POST** /v1/whatsapp/dataset | Provision CTWA dataset |
| [**createWhatsAppDatasetWithHttpInfo**](WhatsAppApi.md#createWhatsAppDatasetWithHttpInfo) | **POST** /v1/whatsapp/dataset | Provision CTWA dataset |
| [**createWhatsAppGroupChat**](WhatsAppApi.md#createWhatsAppGroupChat) | **POST** /v1/whatsapp/wa-groups | Create group |
| [**createWhatsAppGroupChatWithHttpInfo**](WhatsAppApi.md#createWhatsAppGroupChatWithHttpInfo) | **POST** /v1/whatsapp/wa-groups | Create group |
| [**createWhatsAppGroupInviteLink**](WhatsAppApi.md#createWhatsAppGroupInviteLink) | **POST** /v1/whatsapp/wa-groups/{groupId}/invite-link | Create invite link |
| [**createWhatsAppGroupInviteLinkWithHttpInfo**](WhatsAppApi.md#createWhatsAppGroupInviteLinkWithHttpInfo) | **POST** /v1/whatsapp/wa-groups/{groupId}/invite-link | Create invite link |
| [**createWhatsAppTemplate**](WhatsAppApi.md#createWhatsAppTemplate) | **POST** /v1/whatsapp/templates | Create template |
| [**createWhatsAppTemplateWithHttpInfo**](WhatsAppApi.md#createWhatsAppTemplateWithHttpInfo) | **POST** /v1/whatsapp/templates | Create template |
| [**deleteWhatsAppGroupChat**](WhatsAppApi.md#deleteWhatsAppGroupChat) | **DELETE** /v1/whatsapp/wa-groups/{groupId} | Delete group |
| [**deleteWhatsAppGroupChatWithHttpInfo**](WhatsAppApi.md#deleteWhatsAppGroupChatWithHttpInfo) | **DELETE** /v1/whatsapp/wa-groups/{groupId} | Delete group |
| [**deleteWhatsAppTemplate**](WhatsAppApi.md#deleteWhatsAppTemplate) | **DELETE** /v1/whatsapp/templates/{templateName} | Delete template |
| [**deleteWhatsAppTemplateWithHttpInfo**](WhatsAppApi.md#deleteWhatsAppTemplateWithHttpInfo) | **DELETE** /v1/whatsapp/templates/{templateName} | Delete template |
| [**deleteWhatsappBusinessUsername**](WhatsAppApi.md#deleteWhatsappBusinessUsername) | **DELETE** /v1/whatsapp/business-profile/username | Delete business username |
| [**deleteWhatsappBusinessUsernameWithHttpInfo**](WhatsAppApi.md#deleteWhatsappBusinessUsernameWithHttpInfo) | **DELETE** /v1/whatsapp/business-profile/username | Delete business username |
| [**getWhatsAppBlockStatus**](WhatsAppApi.md#getWhatsAppBlockStatus) | **GET** /v1/whatsapp/block-users/status | Check if a user is blocked |
| [**getWhatsAppBlockStatusWithHttpInfo**](WhatsAppApi.md#getWhatsAppBlockStatusWithHttpInfo) | **GET** /v1/whatsapp/block-users/status | Check if a user is blocked |
| [**getWhatsAppBlockedUsers**](WhatsAppApi.md#getWhatsAppBlockedUsers) | **GET** /v1/whatsapp/block-users | List blocked users |
| [**getWhatsAppBlockedUsersWithHttpInfo**](WhatsAppApi.md#getWhatsAppBlockedUsersWithHttpInfo) | **GET** /v1/whatsapp/block-users | List blocked users |
| [**getWhatsAppBusinessProfile**](WhatsAppApi.md#getWhatsAppBusinessProfile) | **GET** /v1/whatsapp/business-profile | Get business profile |
| [**getWhatsAppBusinessProfileWithHttpInfo**](WhatsAppApi.md#getWhatsAppBusinessProfileWithHttpInfo) | **GET** /v1/whatsapp/business-profile | Get business profile |
| [**getWhatsAppDataset**](WhatsAppApi.md#getWhatsAppDataset) | **GET** /v1/whatsapp/dataset | Get CTWA conversions dataset |
| [**getWhatsAppDatasetWithHttpInfo**](WhatsAppApi.md#getWhatsAppDatasetWithHttpInfo) | **GET** /v1/whatsapp/dataset | Get CTWA conversions dataset |
| [**getWhatsAppDisplayName**](WhatsAppApi.md#getWhatsAppDisplayName) | **GET** /v1/whatsapp/business-profile/display-name | Get display name status |
| [**getWhatsAppDisplayNameWithHttpInfo**](WhatsAppApi.md#getWhatsAppDisplayNameWithHttpInfo) | **GET** /v1/whatsapp/business-profile/display-name | Get display name status |
| [**getWhatsAppGroupChat**](WhatsAppApi.md#getWhatsAppGroupChat) | **GET** /v1/whatsapp/wa-groups/{groupId} | Get group info |
| [**getWhatsAppGroupChatWithHttpInfo**](WhatsAppApi.md#getWhatsAppGroupChatWithHttpInfo) | **GET** /v1/whatsapp/wa-groups/{groupId} | Get group info |
| [**getWhatsAppMedia**](WhatsAppApi.md#getWhatsAppMedia) | **GET** /v1/whatsapp/media/{mediaId} | Download WhatsApp media |
| [**getWhatsAppMediaWithHttpInfo**](WhatsAppApi.md#getWhatsAppMediaWithHttpInfo) | **GET** /v1/whatsapp/media/{mediaId} | Download WhatsApp media |
| [**getWhatsAppTemplate**](WhatsAppApi.md#getWhatsAppTemplate) | **GET** /v1/whatsapp/templates/{templateName} | Get template |
| [**getWhatsAppTemplateWithHttpInfo**](WhatsAppApi.md#getWhatsAppTemplateWithHttpInfo) | **GET** /v1/whatsapp/templates/{templateName} | Get template |
| [**getWhatsAppTemplates**](WhatsAppApi.md#getWhatsAppTemplates) | **GET** /v1/whatsapp/templates | List templates |
| [**getWhatsAppTemplatesWithHttpInfo**](WhatsAppApi.md#getWhatsAppTemplatesWithHttpInfo) | **GET** /v1/whatsapp/templates | List templates |
| [**getWhatsappBusinessUsername**](WhatsAppApi.md#getWhatsappBusinessUsername) | **GET** /v1/whatsapp/business-profile/username | Get business username |
| [**getWhatsappBusinessUsernameWithHttpInfo**](WhatsAppApi.md#getWhatsappBusinessUsernameWithHttpInfo) | **GET** /v1/whatsapp/business-profile/username | Get business username |
| [**getWhatsappBusinessUsernameSuggestions**](WhatsAppApi.md#getWhatsappBusinessUsernameSuggestions) | **GET** /v1/whatsapp/business-profile/username/suggestions | Get username suggestions |
| [**getWhatsappBusinessUsernameSuggestionsWithHttpInfo**](WhatsAppApi.md#getWhatsappBusinessUsernameSuggestionsWithHttpInfo) | **GET** /v1/whatsapp/business-profile/username/suggestions | Get username suggestions |
| [**listWhatsAppConversions**](WhatsAppApi.md#listWhatsAppConversions) | **GET** /v1/whatsapp/conversions | List conversion events |
| [**listWhatsAppConversionsWithHttpInfo**](WhatsAppApi.md#listWhatsAppConversionsWithHttpInfo) | **GET** /v1/whatsapp/conversions | List conversion events |
| [**listWhatsAppGroupChats**](WhatsAppApi.md#listWhatsAppGroupChats) | **GET** /v1/whatsapp/wa-groups | List active groups |
| [**listWhatsAppGroupChatsWithHttpInfo**](WhatsAppApi.md#listWhatsAppGroupChatsWithHttpInfo) | **GET** /v1/whatsapp/wa-groups | List active groups |
| [**listWhatsAppGroupJoinRequests**](WhatsAppApi.md#listWhatsAppGroupJoinRequests) | **GET** /v1/whatsapp/wa-groups/{groupId}/join-requests | List join requests |
| [**listWhatsAppGroupJoinRequestsWithHttpInfo**](WhatsAppApi.md#listWhatsAppGroupJoinRequestsWithHttpInfo) | **GET** /v1/whatsapp/wa-groups/{groupId}/join-requests | List join requests |
| [**rejectWhatsAppGroupJoinRequests**](WhatsAppApi.md#rejectWhatsAppGroupJoinRequests) | **DELETE** /v1/whatsapp/wa-groups/{groupId}/join-requests | Reject join requests |
| [**rejectWhatsAppGroupJoinRequestsWithHttpInfo**](WhatsAppApi.md#rejectWhatsAppGroupJoinRequestsWithHttpInfo) | **DELETE** /v1/whatsapp/wa-groups/{groupId}/join-requests | Reject join requests |
| [**removeWhatsAppGroupParticipants**](WhatsAppApi.md#removeWhatsAppGroupParticipants) | **DELETE** /v1/whatsapp/wa-groups/{groupId}/participants | Remove participants |
| [**removeWhatsAppGroupParticipantsWithHttpInfo**](WhatsAppApi.md#removeWhatsAppGroupParticipantsWithHttpInfo) | **DELETE** /v1/whatsapp/wa-groups/{groupId}/participants | Remove participants |
| [**sendWhatsAppConversion**](WhatsAppApi.md#sendWhatsAppConversion) | **POST** /v1/whatsapp/conversions | Send WhatsApp conversion event |
| [**sendWhatsAppConversionWithHttpInfo**](WhatsAppApi.md#sendWhatsAppConversionWithHttpInfo) | **POST** /v1/whatsapp/conversions | Send WhatsApp conversion event |
| [**setWhatsappBusinessUsername**](WhatsAppApi.md#setWhatsappBusinessUsername) | **POST** /v1/whatsapp/business-profile/username | Set business username |
| [**setWhatsappBusinessUsernameWithHttpInfo**](WhatsAppApi.md#setWhatsappBusinessUsernameWithHttpInfo) | **POST** /v1/whatsapp/business-profile/username | Set business username |
| [**unblockWhatsAppUsers**](WhatsAppApi.md#unblockWhatsAppUsers) | **DELETE** /v1/whatsapp/block-users | Unblock users |
| [**unblockWhatsAppUsersWithHttpInfo**](WhatsAppApi.md#unblockWhatsAppUsersWithHttpInfo) | **DELETE** /v1/whatsapp/block-users | Unblock users |
| [**updateWhatsAppBusinessProfile**](WhatsAppApi.md#updateWhatsAppBusinessProfile) | **POST** /v1/whatsapp/business-profile | Update business profile |
| [**updateWhatsAppBusinessProfileWithHttpInfo**](WhatsAppApi.md#updateWhatsAppBusinessProfileWithHttpInfo) | **POST** /v1/whatsapp/business-profile | Update business profile |
| [**updateWhatsAppDisplayName**](WhatsAppApi.md#updateWhatsAppDisplayName) | **POST** /v1/whatsapp/business-profile/display-name | Request display name change |
| [**updateWhatsAppDisplayNameWithHttpInfo**](WhatsAppApi.md#updateWhatsAppDisplayNameWithHttpInfo) | **POST** /v1/whatsapp/business-profile/display-name | Request display name change |
| [**updateWhatsAppGroupChat**](WhatsAppApi.md#updateWhatsAppGroupChat) | **POST** /v1/whatsapp/wa-groups/{groupId} | Update group settings |
| [**updateWhatsAppGroupChatWithHttpInfo**](WhatsAppApi.md#updateWhatsAppGroupChatWithHttpInfo) | **POST** /v1/whatsapp/wa-groups/{groupId} | Update group settings |
| [**updateWhatsAppTemplate**](WhatsAppApi.md#updateWhatsAppTemplate) | **PATCH** /v1/whatsapp/templates/{templateName} | Update template |
| [**updateWhatsAppTemplateWithHttpInfo**](WhatsAppApi.md#updateWhatsAppTemplateWithHttpInfo) | **PATCH** /v1/whatsapp/templates/{templateName} | Update template |
| [**uploadWhatsAppProfilePhoto**](WhatsAppApi.md#uploadWhatsAppProfilePhoto) | **POST** /v1/whatsapp/business-profile/photo | Upload profile picture |
| [**uploadWhatsAppProfilePhotoWithHttpInfo**](WhatsAppApi.md#uploadWhatsAppProfilePhotoWithHttpInfo) | **POST** /v1/whatsapp/business-profile/photo | Upload profile picture |



## addWhatsAppGroupParticipants

> UnpublishPost200Response addWhatsAppGroupParticipants(groupId, accountId, addWhatsAppGroupParticipantsRequest)

Add participants

Add participants to a WhatsApp group. Maximum 8 participants per request.  Not available on [Coexistence](/platforms/whatsapp/connection#whatsapp-business-app-coexistence) numbers. Requires a Cloud API-only number. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String groupId = "groupId_example"; // String | Group ID
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        AddWhatsAppGroupParticipantsRequest addWhatsAppGroupParticipantsRequest = new AddWhatsAppGroupParticipantsRequest(); // AddWhatsAppGroupParticipantsRequest | 
        try {
            UnpublishPost200Response result = apiInstance.addWhatsAppGroupParticipants(groupId, accountId, addWhatsAppGroupParticipantsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#addWhatsAppGroupParticipants");
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
| **groupId** | **String**| Group ID | |
| **accountId** | **String**| WhatsApp social account ID | |
| **addWhatsAppGroupParticipantsRequest** | [**AddWhatsAppGroupParticipantsRequest**](AddWhatsAppGroupParticipantsRequest.md)|  | |

### Return type

[**UnpublishPost200Response**](UnpublishPost200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Participants added |  -  |
| **401** | Unauthorized |  -  |

## addWhatsAppGroupParticipantsWithHttpInfo

> ApiResponse<UnpublishPost200Response> addWhatsAppGroupParticipants addWhatsAppGroupParticipantsWithHttpInfo(groupId, accountId, addWhatsAppGroupParticipantsRequest)

Add participants

Add participants to a WhatsApp group. Maximum 8 participants per request.  Not available on [Coexistence](/platforms/whatsapp/connection#whatsapp-business-app-coexistence) numbers. Requires a Cloud API-only number. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String groupId = "groupId_example"; // String | Group ID
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        AddWhatsAppGroupParticipantsRequest addWhatsAppGroupParticipantsRequest = new AddWhatsAppGroupParticipantsRequest(); // AddWhatsAppGroupParticipantsRequest | 
        try {
            ApiResponse<UnpublishPost200Response> response = apiInstance.addWhatsAppGroupParticipantsWithHttpInfo(groupId, accountId, addWhatsAppGroupParticipantsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#addWhatsAppGroupParticipants");
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
| **groupId** | **String**| Group ID | |
| **accountId** | **String**| WhatsApp social account ID | |
| **addWhatsAppGroupParticipantsRequest** | [**AddWhatsAppGroupParticipantsRequest**](AddWhatsAppGroupParticipantsRequest.md)|  | |

### Return type

ApiResponse<[**UnpublishPost200Response**](UnpublishPost200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Participants added |  -  |
| **401** | Unauthorized |  -  |


## approveWhatsAppGroupJoinRequests

> UnpublishPost200Response approveWhatsAppGroupJoinRequests(groupId, accountId, approveWhatsAppGroupJoinRequestsRequest)

Approve join requests

Approve pending join requests for a WhatsApp group.  Not available on [Coexistence](/platforms/whatsapp/connection#whatsapp-business-app-coexistence) numbers. Requires a Cloud API-only number. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String groupId = "groupId_example"; // String | Group ID
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        ApproveWhatsAppGroupJoinRequestsRequest approveWhatsAppGroupJoinRequestsRequest = new ApproveWhatsAppGroupJoinRequestsRequest(); // ApproveWhatsAppGroupJoinRequestsRequest | 
        try {
            UnpublishPost200Response result = apiInstance.approveWhatsAppGroupJoinRequests(groupId, accountId, approveWhatsAppGroupJoinRequestsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#approveWhatsAppGroupJoinRequests");
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
| **groupId** | **String**| Group ID | |
| **accountId** | **String**| WhatsApp social account ID | |
| **approveWhatsAppGroupJoinRequestsRequest** | [**ApproveWhatsAppGroupJoinRequestsRequest**](ApproveWhatsAppGroupJoinRequestsRequest.md)|  | |

### Return type

[**UnpublishPost200Response**](UnpublishPost200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Requests approved |  -  |
| **401** | Unauthorized |  -  |

## approveWhatsAppGroupJoinRequestsWithHttpInfo

> ApiResponse<UnpublishPost200Response> approveWhatsAppGroupJoinRequests approveWhatsAppGroupJoinRequestsWithHttpInfo(groupId, accountId, approveWhatsAppGroupJoinRequestsRequest)

Approve join requests

Approve pending join requests for a WhatsApp group.  Not available on [Coexistence](/platforms/whatsapp/connection#whatsapp-business-app-coexistence) numbers. Requires a Cloud API-only number. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String groupId = "groupId_example"; // String | Group ID
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        ApproveWhatsAppGroupJoinRequestsRequest approveWhatsAppGroupJoinRequestsRequest = new ApproveWhatsAppGroupJoinRequestsRequest(); // ApproveWhatsAppGroupJoinRequestsRequest | 
        try {
            ApiResponse<UnpublishPost200Response> response = apiInstance.approveWhatsAppGroupJoinRequestsWithHttpInfo(groupId, accountId, approveWhatsAppGroupJoinRequestsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#approveWhatsAppGroupJoinRequests");
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
| **groupId** | **String**| Group ID | |
| **accountId** | **String**| WhatsApp social account ID | |
| **approveWhatsAppGroupJoinRequestsRequest** | [**ApproveWhatsAppGroupJoinRequestsRequest**](ApproveWhatsAppGroupJoinRequestsRequest.md)|  | |

### Return type

ApiResponse<[**UnpublishPost200Response**](UnpublishPost200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Requests approved |  -  |
| **401** | Unauthorized |  -  |


## blockWhatsAppUsers

> BlockWhatsAppUsers200Response blockWhatsAppUsers(blockWhatsAppUsersRequest)

Block users

Block one or more WhatsApp users on this number. Blocked users cannot message your number or see that you are online, and your sends to them return an error.  Meta constraints, surfaced per-user in &#x60;failed&#x60; (the request itself still succeeds for the rest of the batch): - Only users who messaged your business within the last 24 hours can be   blocked (failures outside the window report \&quot;Re-engagement required\&quot;). - Up to 1,000 users per request; the blocklist caps at 64,000. - Other WhatsApp Business accounts cannot be blocked. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        BlockWhatsAppUsersRequest blockWhatsAppUsersRequest = new BlockWhatsAppUsersRequest(); // BlockWhatsAppUsersRequest | 
        try {
            BlockWhatsAppUsers200Response result = apiInstance.blockWhatsAppUsers(blockWhatsAppUsersRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#blockWhatsAppUsers");
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
| **blockWhatsAppUsersRequest** | [**BlockWhatsAppUsersRequest**](BlockWhatsAppUsersRequest.md)|  | |

### Return type

[**BlockWhatsAppUsers200Response**](BlockWhatsAppUsers200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-user results |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

## blockWhatsAppUsersWithHttpInfo

> ApiResponse<BlockWhatsAppUsers200Response> blockWhatsAppUsers blockWhatsAppUsersWithHttpInfo(blockWhatsAppUsersRequest)

Block users

Block one or more WhatsApp users on this number. Blocked users cannot message your number or see that you are online, and your sends to them return an error.  Meta constraints, surfaced per-user in &#x60;failed&#x60; (the request itself still succeeds for the rest of the batch): - Only users who messaged your business within the last 24 hours can be   blocked (failures outside the window report \&quot;Re-engagement required\&quot;). - Up to 1,000 users per request; the blocklist caps at 64,000. - Other WhatsApp Business accounts cannot be blocked. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        BlockWhatsAppUsersRequest blockWhatsAppUsersRequest = new BlockWhatsAppUsersRequest(); // BlockWhatsAppUsersRequest | 
        try {
            ApiResponse<BlockWhatsAppUsers200Response> response = apiInstance.blockWhatsAppUsersWithHttpInfo(blockWhatsAppUsersRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#blockWhatsAppUsers");
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
| **blockWhatsAppUsersRequest** | [**BlockWhatsAppUsersRequest**](BlockWhatsAppUsersRequest.md)|  | |

### Return type

ApiResponse<[**BlockWhatsAppUsers200Response**](BlockWhatsAppUsers200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-user results |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |


## createWhatsAppDataset

> CreateWhatsAppDataset200Response createWhatsAppDataset(deleteWhatsappBusinessUsernameRequest)

Provision CTWA dataset

Creates (or fetches, if one already exists) the Meta dataset that Click-to-WhatsApp ad events are reported against via the Conversions API, and persists its ID on the account as &#x60;metadata.metaCapiDatasetId&#x60;.  The call is GET-first idempotent — a WABA can only own one CTWA dataset, so a second call after a successful provision is a safe no-op that returns the same ID with &#x60;created: false&#x60;.  Requires the connected WhatsApp account&#39;s token to carry the &#x60;whatsapp_business_manage_events&#x60; permission. If the permission is missing the endpoint returns 422 with a message asking the user to reconnect the account. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        DeleteWhatsappBusinessUsernameRequest deleteWhatsappBusinessUsernameRequest = new DeleteWhatsappBusinessUsernameRequest(); // DeleteWhatsappBusinessUsernameRequest | 
        try {
            CreateWhatsAppDataset200Response result = apiInstance.createWhatsAppDataset(deleteWhatsappBusinessUsernameRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#createWhatsAppDataset");
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
| **deleteWhatsappBusinessUsernameRequest** | [**DeleteWhatsappBusinessUsernameRequest**](DeleteWhatsappBusinessUsernameRequest.md)|  | |

### Return type

[**CreateWhatsAppDataset200Response**](CreateWhatsAppDataset200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Dataset provisioned (or already present) |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |
| **422** | Account is missing &#x60;whatsapp_business_manage_events&#x60; — reconnect required |  -  |
| **502** | Upstream Meta failure during provisioning |  -  |

## createWhatsAppDatasetWithHttpInfo

> ApiResponse<CreateWhatsAppDataset200Response> createWhatsAppDataset createWhatsAppDatasetWithHttpInfo(deleteWhatsappBusinessUsernameRequest)

Provision CTWA dataset

Creates (or fetches, if one already exists) the Meta dataset that Click-to-WhatsApp ad events are reported against via the Conversions API, and persists its ID on the account as &#x60;metadata.metaCapiDatasetId&#x60;.  The call is GET-first idempotent — a WABA can only own one CTWA dataset, so a second call after a successful provision is a safe no-op that returns the same ID with &#x60;created: false&#x60;.  Requires the connected WhatsApp account&#39;s token to carry the &#x60;whatsapp_business_manage_events&#x60; permission. If the permission is missing the endpoint returns 422 with a message asking the user to reconnect the account. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        DeleteWhatsappBusinessUsernameRequest deleteWhatsappBusinessUsernameRequest = new DeleteWhatsappBusinessUsernameRequest(); // DeleteWhatsappBusinessUsernameRequest | 
        try {
            ApiResponse<CreateWhatsAppDataset200Response> response = apiInstance.createWhatsAppDatasetWithHttpInfo(deleteWhatsappBusinessUsernameRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#createWhatsAppDataset");
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
| **deleteWhatsappBusinessUsernameRequest** | [**DeleteWhatsappBusinessUsernameRequest**](DeleteWhatsappBusinessUsernameRequest.md)|  | |

### Return type

ApiResponse<[**CreateWhatsAppDataset200Response**](CreateWhatsAppDataset200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Dataset provisioned (or already present) |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |
| **422** | Account is missing &#x60;whatsapp_business_manage_events&#x60; — reconnect required |  -  |
| **502** | Upstream Meta failure during provisioning |  -  |


## createWhatsAppGroupChat

> CreateWhatsAppGroupChat201Response createWhatsAppGroupChat(createWhatsAppGroupChatRequest)

Create group

Create a new WhatsApp group chat. Returns the group ID and optionally an invite link.  Not available on [Coexistence](/platforms/whatsapp/connection#whatsapp-business-app-coexistence) numbers. Requires a Cloud API-only number. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        CreateWhatsAppGroupChatRequest createWhatsAppGroupChatRequest = new CreateWhatsAppGroupChatRequest(); // CreateWhatsAppGroupChatRequest | 
        try {
            CreateWhatsAppGroupChat201Response result = apiInstance.createWhatsAppGroupChat(createWhatsAppGroupChatRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#createWhatsAppGroupChat");
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
| **createWhatsAppGroupChatRequest** | [**CreateWhatsAppGroupChatRequest**](CreateWhatsAppGroupChatRequest.md)|  | |

### Return type

[**CreateWhatsAppGroupChat201Response**](CreateWhatsAppGroupChat201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Group created |  -  |
| **401** | Unauthorized |  -  |

## createWhatsAppGroupChatWithHttpInfo

> ApiResponse<CreateWhatsAppGroupChat201Response> createWhatsAppGroupChat createWhatsAppGroupChatWithHttpInfo(createWhatsAppGroupChatRequest)

Create group

Create a new WhatsApp group chat. Returns the group ID and optionally an invite link.  Not available on [Coexistence](/platforms/whatsapp/connection#whatsapp-business-app-coexistence) numbers. Requires a Cloud API-only number. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        CreateWhatsAppGroupChatRequest createWhatsAppGroupChatRequest = new CreateWhatsAppGroupChatRequest(); // CreateWhatsAppGroupChatRequest | 
        try {
            ApiResponse<CreateWhatsAppGroupChat201Response> response = apiInstance.createWhatsAppGroupChatWithHttpInfo(createWhatsAppGroupChatRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#createWhatsAppGroupChat");
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
| **createWhatsAppGroupChatRequest** | [**CreateWhatsAppGroupChatRequest**](CreateWhatsAppGroupChatRequest.md)|  | |

### Return type

ApiResponse<[**CreateWhatsAppGroupChat201Response**](CreateWhatsAppGroupChat201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Group created |  -  |
| **401** | Unauthorized |  -  |


## createWhatsAppGroupInviteLink

> CreateWhatsAppGroupInviteLink200Response createWhatsAppGroupInviteLink(groupId, accountId)

Create invite link

Create a new invite link for a WhatsApp group. The previous link is revoked.  Not available on [Coexistence](/platforms/whatsapp/connection#whatsapp-business-app-coexistence) numbers. Requires a Cloud API-only number. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String groupId = "groupId_example"; // String | Group ID
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            CreateWhatsAppGroupInviteLink200Response result = apiInstance.createWhatsAppGroupInviteLink(groupId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#createWhatsAppGroupInviteLink");
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
| **groupId** | **String**| Group ID | |
| **accountId** | **String**| WhatsApp social account ID | |

### Return type

[**CreateWhatsAppGroupInviteLink200Response**](CreateWhatsAppGroupInviteLink200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Invite link created |  -  |
| **401** | Unauthorized |  -  |

## createWhatsAppGroupInviteLinkWithHttpInfo

> ApiResponse<CreateWhatsAppGroupInviteLink200Response> createWhatsAppGroupInviteLink createWhatsAppGroupInviteLinkWithHttpInfo(groupId, accountId)

Create invite link

Create a new invite link for a WhatsApp group. The previous link is revoked.  Not available on [Coexistence](/platforms/whatsapp/connection#whatsapp-business-app-coexistence) numbers. Requires a Cloud API-only number. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String groupId = "groupId_example"; // String | Group ID
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            ApiResponse<CreateWhatsAppGroupInviteLink200Response> response = apiInstance.createWhatsAppGroupInviteLinkWithHttpInfo(groupId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#createWhatsAppGroupInviteLink");
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
| **groupId** | **String**| Group ID | |
| **accountId** | **String**| WhatsApp social account ID | |

### Return type

ApiResponse<[**CreateWhatsAppGroupInviteLink200Response**](CreateWhatsAppGroupInviteLink200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Invite link created |  -  |
| **401** | Unauthorized |  -  |


## createWhatsAppTemplate

> CreateWhatsAppTemplate200Response createWhatsAppTemplate(createWhatsAppTemplateRequest)

Create template

Create a new message template. Supports two modes:  Custom template: Provide components with your own content. Submitted to Meta for review (can take up to 24h).  Library template: Provide library_template_name instead of components to use a pre-built template from Meta&#39;s template library. Library templates are pre-approved (no review wait). You can optionally customize parameters and buttons via library_template_body_inputs and library_template_button_inputs.  Browse available library templates at: https://business.facebook.com/wa/manage/message-templates/ 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        CreateWhatsAppTemplateRequest createWhatsAppTemplateRequest = new CreateWhatsAppTemplateRequest(); // CreateWhatsAppTemplateRequest | 
        try {
            CreateWhatsAppTemplate200Response result = apiInstance.createWhatsAppTemplate(createWhatsAppTemplateRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#createWhatsAppTemplate");
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
| **createWhatsAppTemplateRequest** | [**CreateWhatsAppTemplateRequest**](CreateWhatsAppTemplateRequest.md)|  | |

### Return type

[**CreateWhatsAppTemplate200Response**](CreateWhatsAppTemplate200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Template created (pre-approved for library templates, pending review for custom) |  -  |
| **400** | Validation error (invalid name format, missing fields, invalid category) |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

## createWhatsAppTemplateWithHttpInfo

> ApiResponse<CreateWhatsAppTemplate200Response> createWhatsAppTemplate createWhatsAppTemplateWithHttpInfo(createWhatsAppTemplateRequest)

Create template

Create a new message template. Supports two modes:  Custom template: Provide components with your own content. Submitted to Meta for review (can take up to 24h).  Library template: Provide library_template_name instead of components to use a pre-built template from Meta&#39;s template library. Library templates are pre-approved (no review wait). You can optionally customize parameters and buttons via library_template_body_inputs and library_template_button_inputs.  Browse available library templates at: https://business.facebook.com/wa/manage/message-templates/ 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        CreateWhatsAppTemplateRequest createWhatsAppTemplateRequest = new CreateWhatsAppTemplateRequest(); // CreateWhatsAppTemplateRequest | 
        try {
            ApiResponse<CreateWhatsAppTemplate200Response> response = apiInstance.createWhatsAppTemplateWithHttpInfo(createWhatsAppTemplateRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#createWhatsAppTemplate");
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
| **createWhatsAppTemplateRequest** | [**CreateWhatsAppTemplateRequest**](CreateWhatsAppTemplateRequest.md)|  | |

### Return type

ApiResponse<[**CreateWhatsAppTemplate200Response**](CreateWhatsAppTemplate200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Template created (pre-approved for library templates, pending review for custom) |  -  |
| **400** | Validation error (invalid name format, missing fields, invalid category) |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |


## deleteWhatsAppGroupChat

> UnpublishPost200Response deleteWhatsAppGroupChat(groupId, accountId)

Delete group

Delete a WhatsApp group and remove all participants.  Not available on [Coexistence](/platforms/whatsapp/connection#whatsapp-business-app-coexistence) numbers. Requires a Cloud API-only number. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String groupId = "groupId_example"; // String | Group ID
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            UnpublishPost200Response result = apiInstance.deleteWhatsAppGroupChat(groupId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#deleteWhatsAppGroupChat");
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
| **groupId** | **String**| Group ID | |
| **accountId** | **String**| WhatsApp social account ID | |

### Return type

[**UnpublishPost200Response**](UnpublishPost200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Group deleted |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## deleteWhatsAppGroupChatWithHttpInfo

> ApiResponse<UnpublishPost200Response> deleteWhatsAppGroupChat deleteWhatsAppGroupChatWithHttpInfo(groupId, accountId)

Delete group

Delete a WhatsApp group and remove all participants.  Not available on [Coexistence](/platforms/whatsapp/connection#whatsapp-business-app-coexistence) numbers. Requires a Cloud API-only number. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String groupId = "groupId_example"; // String | Group ID
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            ApiResponse<UnpublishPost200Response> response = apiInstance.deleteWhatsAppGroupChatWithHttpInfo(groupId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#deleteWhatsAppGroupChat");
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
| **groupId** | **String**| Group ID | |
| **accountId** | **String**| WhatsApp social account ID | |

### Return type

ApiResponse<[**UnpublishPost200Response**](UnpublishPost200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Group deleted |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## deleteWhatsAppTemplate

> UnpublishPost200Response deleteWhatsAppTemplate(templateName, accountId)

Delete template

Permanently delete a message template by name. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String templateName = "templateName_example"; // String | Template name
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            UnpublishPost200Response result = apiInstance.deleteWhatsAppTemplate(templateName, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#deleteWhatsAppTemplate");
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
| **templateName** | **String**| Template name | |
| **accountId** | **String**| WhatsApp social account ID | |

### Return type

[**UnpublishPost200Response**](UnpublishPost200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Template deleted successfully |  -  |
| **400** | accountId or template name is required |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## deleteWhatsAppTemplateWithHttpInfo

> ApiResponse<UnpublishPost200Response> deleteWhatsAppTemplate deleteWhatsAppTemplateWithHttpInfo(templateName, accountId)

Delete template

Permanently delete a message template by name. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String templateName = "templateName_example"; // String | Template name
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            ApiResponse<UnpublishPost200Response> response = apiInstance.deleteWhatsAppTemplateWithHttpInfo(templateName, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#deleteWhatsAppTemplate");
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
| **templateName** | **String**| Template name | |
| **accountId** | **String**| WhatsApp social account ID | |

### Return type

ApiResponse<[**UnpublishPost200Response**](UnpublishPost200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Template deleted successfully |  -  |
| **400** | accountId or template name is required |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## deleteWhatsappBusinessUsername

> UpdateYoutubeDefaultPlaylist200Response deleteWhatsappBusinessUsername(deleteWhatsappBusinessUsernameRequest)

Delete business username

Release the currently claimed WhatsApp Business username from the account. After deletion the username becomes available for other accounts to claim. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        DeleteWhatsappBusinessUsernameRequest deleteWhatsappBusinessUsernameRequest = new DeleteWhatsappBusinessUsernameRequest(); // DeleteWhatsappBusinessUsernameRequest | 
        try {
            UpdateYoutubeDefaultPlaylist200Response result = apiInstance.deleteWhatsappBusinessUsername(deleteWhatsappBusinessUsernameRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#deleteWhatsappBusinessUsername");
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
| **deleteWhatsappBusinessUsernameRequest** | [**DeleteWhatsappBusinessUsernameRequest**](DeleteWhatsappBusinessUsernameRequest.md)|  | |

### Return type

[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Username deleted successfully |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

## deleteWhatsappBusinessUsernameWithHttpInfo

> ApiResponse<UpdateYoutubeDefaultPlaylist200Response> deleteWhatsappBusinessUsername deleteWhatsappBusinessUsernameWithHttpInfo(deleteWhatsappBusinessUsernameRequest)

Delete business username

Release the currently claimed WhatsApp Business username from the account. After deletion the username becomes available for other accounts to claim. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        DeleteWhatsappBusinessUsernameRequest deleteWhatsappBusinessUsernameRequest = new DeleteWhatsappBusinessUsernameRequest(); // DeleteWhatsappBusinessUsernameRequest | 
        try {
            ApiResponse<UpdateYoutubeDefaultPlaylist200Response> response = apiInstance.deleteWhatsappBusinessUsernameWithHttpInfo(deleteWhatsappBusinessUsernameRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#deleteWhatsappBusinessUsername");
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
| **deleteWhatsappBusinessUsernameRequest** | [**DeleteWhatsappBusinessUsernameRequest**](DeleteWhatsappBusinessUsernameRequest.md)|  | |

### Return type

ApiResponse<[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Username deleted successfully |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |


## getWhatsAppBlockStatus

> GetWhatsAppBlockStatus200Response getWhatsAppBlockStatus(accountId, user)

Check if a user is blocked

Definitive blocked-state lookup for a single contact. Meta exposes no membership endpoint, so this reads Zernio&#39;s blocklist mirror (kept in sync by the block/unblock endpoints; the first call per account backfills the mirror from Meta&#39;s full list). Constant-time regardless of blocklist size. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String user = "user_example"; // String | Consumer wa_id or E.164 phone (leading + optional)
        try {
            GetWhatsAppBlockStatus200Response result = apiInstance.getWhatsAppBlockStatus(accountId, user);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#getWhatsAppBlockStatus");
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
| **accountId** | **String**|  | |
| **user** | **String**| Consumer wa_id or E.164 phone (leading + optional) | |

### Return type

[**GetWhatsAppBlockStatus200Response**](GetWhatsAppBlockStatus200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Blocked state |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

## getWhatsAppBlockStatusWithHttpInfo

> ApiResponse<GetWhatsAppBlockStatus200Response> getWhatsAppBlockStatus getWhatsAppBlockStatusWithHttpInfo(accountId, user)

Check if a user is blocked

Definitive blocked-state lookup for a single contact. Meta exposes no membership endpoint, so this reads Zernio&#39;s blocklist mirror (kept in sync by the block/unblock endpoints; the first call per account backfills the mirror from Meta&#39;s full list). Constant-time regardless of blocklist size. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String user = "user_example"; // String | Consumer wa_id or E.164 phone (leading + optional)
        try {
            ApiResponse<GetWhatsAppBlockStatus200Response> response = apiInstance.getWhatsAppBlockStatusWithHttpInfo(accountId, user);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#getWhatsAppBlockStatus");
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
| **accountId** | **String**|  | |
| **user** | **String**| Consumer wa_id or E.164 phone (leading + optional) | |

### Return type

ApiResponse<[**GetWhatsAppBlockStatus200Response**](GetWhatsAppBlockStatus200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Blocked state |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |


## getWhatsAppBlockedUsers

> GetWhatsAppBlockedUsers200Response getWhatsAppBlockedUsers(accountId, limit, after)

List blocked users

List the WhatsApp users blocked on this number. Cursor-paginated; pass &#x60;nextCursor&#x60; back as &#x60;after&#x60; to fetch the next page. The blocklist holds up to 64,000 users. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        Integer limit = 56; // Integer | Page size.
        String after = "after_example"; // String | Cursor from a previous response's `nextCursor`.
        try {
            GetWhatsAppBlockedUsers200Response result = apiInstance.getWhatsAppBlockedUsers(accountId, limit, after);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#getWhatsAppBlockedUsers");
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
| **limit** | **Integer**| Page size. | [optional] |
| **after** | **String**| Cursor from a previous response&#39;s &#x60;nextCursor&#x60;. | [optional] |

### Return type

[**GetWhatsAppBlockedUsers200Response**](GetWhatsAppBlockedUsers200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Blocked users |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

## getWhatsAppBlockedUsersWithHttpInfo

> ApiResponse<GetWhatsAppBlockedUsers200Response> getWhatsAppBlockedUsers getWhatsAppBlockedUsersWithHttpInfo(accountId, limit, after)

List blocked users

List the WhatsApp users blocked on this number. Cursor-paginated; pass &#x60;nextCursor&#x60; back as &#x60;after&#x60; to fetch the next page. The blocklist holds up to 64,000 users. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        Integer limit = 56; // Integer | Page size.
        String after = "after_example"; // String | Cursor from a previous response's `nextCursor`.
        try {
            ApiResponse<GetWhatsAppBlockedUsers200Response> response = apiInstance.getWhatsAppBlockedUsersWithHttpInfo(accountId, limit, after);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#getWhatsAppBlockedUsers");
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
| **limit** | **Integer**| Page size. | [optional] |
| **after** | **String**| Cursor from a previous response&#39;s &#x60;nextCursor&#x60;. | [optional] |

### Return type

ApiResponse<[**GetWhatsAppBlockedUsers200Response**](GetWhatsAppBlockedUsers200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Blocked users |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |


## getWhatsAppBusinessProfile

> GetWhatsAppBusinessProfile200Response getWhatsAppBusinessProfile(accountId)

Get business profile

Retrieve the WhatsApp Business profile for the account (about, address, description, email, websites, etc.). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            GetWhatsAppBusinessProfile200Response result = apiInstance.getWhatsAppBusinessProfile(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#getWhatsAppBusinessProfile");
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

[**GetWhatsAppBusinessProfile200Response**](GetWhatsAppBusinessProfile200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Business profile retrieved successfully |  -  |
| **400** | accountId is required or phone number ID not found |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

## getWhatsAppBusinessProfileWithHttpInfo

> ApiResponse<GetWhatsAppBusinessProfile200Response> getWhatsAppBusinessProfile getWhatsAppBusinessProfileWithHttpInfo(accountId)

Get business profile

Retrieve the WhatsApp Business profile for the account (about, address, description, email, websites, etc.). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            ApiResponse<GetWhatsAppBusinessProfile200Response> response = apiInstance.getWhatsAppBusinessProfileWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#getWhatsAppBusinessProfile");
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

ApiResponse<[**GetWhatsAppBusinessProfile200Response**](GetWhatsAppBusinessProfile200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Business profile retrieved successfully |  -  |
| **400** | accountId is required or phone number ID not found |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |


## getWhatsAppDataset

> GetWhatsAppDataset200Response getWhatsAppDataset(accountId)

Get CTWA conversions dataset

Returns the Meta Click-to-WhatsApp conversions dataset currently linked to the WhatsApp account, if one has been provisioned. Reads only from the stored &#x60;metadata.metaCapiDatasetId&#x60; — never hits Meta, never creates a dataset. Use this to detect whether &#x60;POST /v1/whatsapp/conversions&#x60; is configured for an account. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            GetWhatsAppDataset200Response result = apiInstance.getWhatsAppDataset(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#getWhatsAppDataset");
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

[**GetWhatsAppDataset200Response**](GetWhatsAppDataset200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Dataset lookup |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

## getWhatsAppDatasetWithHttpInfo

> ApiResponse<GetWhatsAppDataset200Response> getWhatsAppDataset getWhatsAppDatasetWithHttpInfo(accountId)

Get CTWA conversions dataset

Returns the Meta Click-to-WhatsApp conversions dataset currently linked to the WhatsApp account, if one has been provisioned. Reads only from the stored &#x60;metadata.metaCapiDatasetId&#x60; — never hits Meta, never creates a dataset. Use this to detect whether &#x60;POST /v1/whatsapp/conversions&#x60; is configured for an account. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            ApiResponse<GetWhatsAppDataset200Response> response = apiInstance.getWhatsAppDatasetWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#getWhatsAppDataset");
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

ApiResponse<[**GetWhatsAppDataset200Response**](GetWhatsAppDataset200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Dataset lookup |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |


## getWhatsAppDisplayName

> GetWhatsAppDisplayName200Response getWhatsAppDisplayName(accountId)

Get display name status

Fetch the current display name and its Meta review status for a WhatsApp Business account. Display name changes require Meta approval and can take 1-3 business days. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            GetWhatsAppDisplayName200Response result = apiInstance.getWhatsAppDisplayName(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#getWhatsAppDisplayName");
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

[**GetWhatsAppDisplayName200Response**](GetWhatsAppDisplayName200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Display name info retrieved |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

## getWhatsAppDisplayNameWithHttpInfo

> ApiResponse<GetWhatsAppDisplayName200Response> getWhatsAppDisplayName getWhatsAppDisplayNameWithHttpInfo(accountId)

Get display name status

Fetch the current display name and its Meta review status for a WhatsApp Business account. Display name changes require Meta approval and can take 1-3 business days. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            ApiResponse<GetWhatsAppDisplayName200Response> response = apiInstance.getWhatsAppDisplayNameWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#getWhatsAppDisplayName");
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

ApiResponse<[**GetWhatsAppDisplayName200Response**](GetWhatsAppDisplayName200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Display name info retrieved |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |


## getWhatsAppGroupChat

> GetWhatsAppGroupChat200Response getWhatsAppGroupChat(groupId, accountId)

Get group info

Retrieve metadata about a WhatsApp group including subject, description, participants, and settings.  Not available on [Coexistence](/platforms/whatsapp/connection#whatsapp-business-app-coexistence) numbers. Requires a Cloud API-only number. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String groupId = "groupId_example"; // String | Group ID
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            GetWhatsAppGroupChat200Response result = apiInstance.getWhatsAppGroupChat(groupId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#getWhatsAppGroupChat");
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
| **groupId** | **String**| Group ID | |
| **accountId** | **String**| WhatsApp social account ID | |

### Return type

[**GetWhatsAppGroupChat200Response**](GetWhatsAppGroupChat200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Group info |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## getWhatsAppGroupChatWithHttpInfo

> ApiResponse<GetWhatsAppGroupChat200Response> getWhatsAppGroupChat getWhatsAppGroupChatWithHttpInfo(groupId, accountId)

Get group info

Retrieve metadata about a WhatsApp group including subject, description, participants, and settings.  Not available on [Coexistence](/platforms/whatsapp/connection#whatsapp-business-app-coexistence) numbers. Requires a Cloud API-only number. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String groupId = "groupId_example"; // String | Group ID
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            ApiResponse<GetWhatsAppGroupChat200Response> response = apiInstance.getWhatsAppGroupChatWithHttpInfo(groupId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#getWhatsAppGroupChat");
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
| **groupId** | **String**| Group ID | |
| **accountId** | **String**| WhatsApp social account ID | |

### Return type

ApiResponse<[**GetWhatsAppGroupChat200Response**](GetWhatsAppGroupChat200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Group info |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


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
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String mediaId = "mediaId_example"; // String | The media id from `attachments[].payload.id`.
        String accountId = "accountId_example"; // String | The WhatsApp account that received the media.
        try {
            File result = apiInstance.getWhatsAppMedia(mediaId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#getWhatsAppMedia");
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
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String mediaId = "mediaId_example"; // String | The media id from `attachments[].payload.id`.
        String accountId = "accountId_example"; // String | The WhatsApp account that received the media.
        try {
            ApiResponse<File> response = apiInstance.getWhatsAppMediaWithHttpInfo(mediaId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#getWhatsAppMedia");
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


## getWhatsAppTemplate

> GetWhatsAppTemplate200Response getWhatsAppTemplate(templateName, accountId)

Get template

Retrieve a single message template by name. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String templateName = "templateName_example"; // String | Template name
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            GetWhatsAppTemplate200Response result = apiInstance.getWhatsAppTemplate(templateName, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#getWhatsAppTemplate");
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
| **templateName** | **String**| Template name | |
| **accountId** | **String**| WhatsApp social account ID | |

### Return type

[**GetWhatsAppTemplate200Response**](GetWhatsAppTemplate200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Template retrieved successfully |  -  |
| **400** | accountId is required |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## getWhatsAppTemplateWithHttpInfo

> ApiResponse<GetWhatsAppTemplate200Response> getWhatsAppTemplate getWhatsAppTemplateWithHttpInfo(templateName, accountId)

Get template

Retrieve a single message template by name. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String templateName = "templateName_example"; // String | Template name
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            ApiResponse<GetWhatsAppTemplate200Response> response = apiInstance.getWhatsAppTemplateWithHttpInfo(templateName, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#getWhatsAppTemplate");
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
| **templateName** | **String**| Template name | |
| **accountId** | **String**| WhatsApp social account ID | |

### Return type

ApiResponse<[**GetWhatsAppTemplate200Response**](GetWhatsAppTemplate200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Template retrieved successfully |  -  |
| **400** | accountId is required |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## getWhatsAppTemplates

> GetWhatsAppTemplates200Response getWhatsAppTemplates(accountId)

List templates

List all message templates for the WhatsApp Business Account (WABA) associated with the given account. Templates are fetched directly from the WhatsApp Cloud API. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            GetWhatsAppTemplates200Response result = apiInstance.getWhatsAppTemplates(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#getWhatsAppTemplates");
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

[**GetWhatsAppTemplates200Response**](GetWhatsAppTemplates200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Templates retrieved successfully |  -  |
| **400** | accountId is required or WABA ID not found |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

## getWhatsAppTemplatesWithHttpInfo

> ApiResponse<GetWhatsAppTemplates200Response> getWhatsAppTemplates getWhatsAppTemplatesWithHttpInfo(accountId)

List templates

List all message templates for the WhatsApp Business Account (WABA) associated with the given account. Templates are fetched directly from the WhatsApp Cloud API. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            ApiResponse<GetWhatsAppTemplates200Response> response = apiInstance.getWhatsAppTemplatesWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#getWhatsAppTemplates");
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

ApiResponse<[**GetWhatsAppTemplates200Response**](GetWhatsAppTemplates200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Templates retrieved successfully |  -  |
| **400** | accountId is required or WABA ID not found |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |


## getWhatsappBusinessUsername

> GetWhatsappBusinessUsername200Response getWhatsappBusinessUsername(accountId)

Get business username

Fetch the current WhatsApp Business username and its approval status. Username status can be &#x60;approved&#x60; (active), &#x60;reserved&#x60; (pending activation), or &#x60;none&#x60; (no username set). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            GetWhatsappBusinessUsername200Response result = apiInstance.getWhatsappBusinessUsername(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#getWhatsappBusinessUsername");
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

[**GetWhatsappBusinessUsername200Response**](GetWhatsappBusinessUsername200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Business username retrieved successfully |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

## getWhatsappBusinessUsernameWithHttpInfo

> ApiResponse<GetWhatsappBusinessUsername200Response> getWhatsappBusinessUsername getWhatsappBusinessUsernameWithHttpInfo(accountId)

Get business username

Fetch the current WhatsApp Business username and its approval status. Username status can be &#x60;approved&#x60; (active), &#x60;reserved&#x60; (pending activation), or &#x60;none&#x60; (no username set). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            ApiResponse<GetWhatsappBusinessUsername200Response> response = apiInstance.getWhatsappBusinessUsernameWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#getWhatsappBusinessUsername");
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

ApiResponse<[**GetWhatsappBusinessUsername200Response**](GetWhatsappBusinessUsername200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Business username retrieved successfully |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |


## getWhatsappBusinessUsernameSuggestions

> GetWhatsappBusinessUsernameSuggestions200Response getWhatsappBusinessUsernameSuggestions(accountId)

Get username suggestions

Retrieve a list of available WhatsApp Business username suggestions based on the account&#39;s business profile name. Use these to help users discover valid, unclaimed usernames. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            GetWhatsappBusinessUsernameSuggestions200Response result = apiInstance.getWhatsappBusinessUsernameSuggestions(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#getWhatsappBusinessUsernameSuggestions");
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

[**GetWhatsappBusinessUsernameSuggestions200Response**](GetWhatsappBusinessUsernameSuggestions200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Username suggestions retrieved successfully |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

## getWhatsappBusinessUsernameSuggestionsWithHttpInfo

> ApiResponse<GetWhatsappBusinessUsernameSuggestions200Response> getWhatsappBusinessUsernameSuggestions getWhatsappBusinessUsernameSuggestionsWithHttpInfo(accountId)

Get username suggestions

Retrieve a list of available WhatsApp Business username suggestions based on the account&#39;s business profile name. Use these to help users discover valid, unclaimed usernames. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            ApiResponse<GetWhatsappBusinessUsernameSuggestions200Response> response = apiInstance.getWhatsappBusinessUsernameSuggestionsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#getWhatsappBusinessUsernameSuggestions");
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

ApiResponse<[**GetWhatsappBusinessUsernameSuggestions200Response**](GetWhatsappBusinessUsernameSuggestions200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Username suggestions retrieved successfully |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |


## listWhatsAppConversions

> ListWhatsAppConversions200Response listWhatsAppConversions(accountId, limit)

List conversion events

Returns the most recent conversion events sent through &#x60;POST /v1/whatsapp/conversions&#x60; for the given WhatsApp account. Sourced from delivery logs (Axiom &#x60;late&#x60; dataset), so the visible window is bounded by log retention (about 30 days). Useful for rendering a \&quot;recent activity\&quot; panel on the conversions setup tab without standing up a parallel persistence layer.  Per-event payload mirrors the structured log we write on every successful send: &#x60;eventName&#x60;, &#x60;conversationId&#x60;, &#x60;eventsReceived&#x60;, &#x60;eventsFailed&#x60;, &#x60;traceId&#x60;, &#x60;durationMs&#x60;, and the wall-clock &#x60;timestamp&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        Integer limit = 50; // Integer | Max events to return (1-200, default 50).
        try {
            ListWhatsAppConversions200Response result = apiInstance.listWhatsAppConversions(accountId, limit);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#listWhatsAppConversions");
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
| **limit** | **Integer**| Max events to return (1-200, default 50). | [optional] [default to 50] |

### Return type

[**ListWhatsAppConversions200Response**](ListWhatsAppConversions200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Recent conversion events |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

## listWhatsAppConversionsWithHttpInfo

> ApiResponse<ListWhatsAppConversions200Response> listWhatsAppConversions listWhatsAppConversionsWithHttpInfo(accountId, limit)

List conversion events

Returns the most recent conversion events sent through &#x60;POST /v1/whatsapp/conversions&#x60; for the given WhatsApp account. Sourced from delivery logs (Axiom &#x60;late&#x60; dataset), so the visible window is bounded by log retention (about 30 days). Useful for rendering a \&quot;recent activity\&quot; panel on the conversions setup tab without standing up a parallel persistence layer.  Per-event payload mirrors the structured log we write on every successful send: &#x60;eventName&#x60;, &#x60;conversationId&#x60;, &#x60;eventsReceived&#x60;, &#x60;eventsFailed&#x60;, &#x60;traceId&#x60;, &#x60;durationMs&#x60;, and the wall-clock &#x60;timestamp&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        Integer limit = 50; // Integer | Max events to return (1-200, default 50).
        try {
            ApiResponse<ListWhatsAppConversions200Response> response = apiInstance.listWhatsAppConversionsWithHttpInfo(accountId, limit);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#listWhatsAppConversions");
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
| **limit** | **Integer**| Max events to return (1-200, default 50). | [optional] [default to 50] |

### Return type

ApiResponse<[**ListWhatsAppConversions200Response**](ListWhatsAppConversions200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Recent conversion events |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |


## listWhatsAppGroupChats

> ListWhatsAppGroupChats200Response listWhatsAppGroupChats(accountId, limit, after)

List active groups

List active WhatsApp group chats for a business phone number. These are actual WhatsApp group conversations on the platform.  Not available on [Coexistence](/platforms/whatsapp/connection#whatsapp-business-app-coexistence) numbers. Requires a Cloud API-only number. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        Integer limit = 25; // Integer | Max groups to return
        String after = "after_example"; // String | Pagination cursor
        try {
            ListWhatsAppGroupChats200Response result = apiInstance.listWhatsAppGroupChats(accountId, limit, after);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#listWhatsAppGroupChats");
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
| **limit** | **Integer**| Max groups to return | [optional] [default to 25] |
| **after** | **String**| Pagination cursor | [optional] |

### Return type

[**ListWhatsAppGroupChats200Response**](ListWhatsAppGroupChats200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of active groups |  -  |
| **401** | Unauthorized |  -  |

## listWhatsAppGroupChatsWithHttpInfo

> ApiResponse<ListWhatsAppGroupChats200Response> listWhatsAppGroupChats listWhatsAppGroupChatsWithHttpInfo(accountId, limit, after)

List active groups

List active WhatsApp group chats for a business phone number. These are actual WhatsApp group conversations on the platform.  Not available on [Coexistence](/platforms/whatsapp/connection#whatsapp-business-app-coexistence) numbers. Requires a Cloud API-only number. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        Integer limit = 25; // Integer | Max groups to return
        String after = "after_example"; // String | Pagination cursor
        try {
            ApiResponse<ListWhatsAppGroupChats200Response> response = apiInstance.listWhatsAppGroupChatsWithHttpInfo(accountId, limit, after);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#listWhatsAppGroupChats");
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
| **limit** | **Integer**| Max groups to return | [optional] [default to 25] |
| **after** | **String**| Pagination cursor | [optional] |

### Return type

ApiResponse<[**ListWhatsAppGroupChats200Response**](ListWhatsAppGroupChats200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of active groups |  -  |
| **401** | Unauthorized |  -  |


## listWhatsAppGroupJoinRequests

> ListWhatsAppGroupJoinRequests200Response listWhatsAppGroupJoinRequests(groupId, accountId)

List join requests

List pending join requests for a WhatsApp group (only for groups with approval_required mode).  Not available on [Coexistence](/platforms/whatsapp/connection#whatsapp-business-app-coexistence) numbers. Requires a Cloud API-only number. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String groupId = "groupId_example"; // String | Group ID
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            ListWhatsAppGroupJoinRequests200Response result = apiInstance.listWhatsAppGroupJoinRequests(groupId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#listWhatsAppGroupJoinRequests");
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
| **groupId** | **String**| Group ID | |
| **accountId** | **String**| WhatsApp social account ID | |

### Return type

[**ListWhatsAppGroupJoinRequests200Response**](ListWhatsAppGroupJoinRequests200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Join requests |  -  |
| **401** | Unauthorized |  -  |

## listWhatsAppGroupJoinRequestsWithHttpInfo

> ApiResponse<ListWhatsAppGroupJoinRequests200Response> listWhatsAppGroupJoinRequests listWhatsAppGroupJoinRequestsWithHttpInfo(groupId, accountId)

List join requests

List pending join requests for a WhatsApp group (only for groups with approval_required mode).  Not available on [Coexistence](/platforms/whatsapp/connection#whatsapp-business-app-coexistence) numbers. Requires a Cloud API-only number. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String groupId = "groupId_example"; // String | Group ID
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        try {
            ApiResponse<ListWhatsAppGroupJoinRequests200Response> response = apiInstance.listWhatsAppGroupJoinRequestsWithHttpInfo(groupId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#listWhatsAppGroupJoinRequests");
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
| **groupId** | **String**| Group ID | |
| **accountId** | **String**| WhatsApp social account ID | |

### Return type

ApiResponse<[**ListWhatsAppGroupJoinRequests200Response**](ListWhatsAppGroupJoinRequests200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Join requests |  -  |
| **401** | Unauthorized |  -  |


## rejectWhatsAppGroupJoinRequests

> UnpublishPost200Response rejectWhatsAppGroupJoinRequests(groupId, accountId, rejectWhatsAppGroupJoinRequestsRequest)

Reject join requests

Reject pending join requests for a WhatsApp group.  Not available on [Coexistence](/platforms/whatsapp/connection#whatsapp-business-app-coexistence) numbers. Requires a Cloud API-only number. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String groupId = "groupId_example"; // String | Group ID
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        RejectWhatsAppGroupJoinRequestsRequest rejectWhatsAppGroupJoinRequestsRequest = new RejectWhatsAppGroupJoinRequestsRequest(); // RejectWhatsAppGroupJoinRequestsRequest | 
        try {
            UnpublishPost200Response result = apiInstance.rejectWhatsAppGroupJoinRequests(groupId, accountId, rejectWhatsAppGroupJoinRequestsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#rejectWhatsAppGroupJoinRequests");
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
| **groupId** | **String**| Group ID | |
| **accountId** | **String**| WhatsApp social account ID | |
| **rejectWhatsAppGroupJoinRequestsRequest** | [**RejectWhatsAppGroupJoinRequestsRequest**](RejectWhatsAppGroupJoinRequestsRequest.md)|  | |

### Return type

[**UnpublishPost200Response**](UnpublishPost200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Requests rejected |  -  |
| **401** | Unauthorized |  -  |

## rejectWhatsAppGroupJoinRequestsWithHttpInfo

> ApiResponse<UnpublishPost200Response> rejectWhatsAppGroupJoinRequests rejectWhatsAppGroupJoinRequestsWithHttpInfo(groupId, accountId, rejectWhatsAppGroupJoinRequestsRequest)

Reject join requests

Reject pending join requests for a WhatsApp group.  Not available on [Coexistence](/platforms/whatsapp/connection#whatsapp-business-app-coexistence) numbers. Requires a Cloud API-only number. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String groupId = "groupId_example"; // String | Group ID
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        RejectWhatsAppGroupJoinRequestsRequest rejectWhatsAppGroupJoinRequestsRequest = new RejectWhatsAppGroupJoinRequestsRequest(); // RejectWhatsAppGroupJoinRequestsRequest | 
        try {
            ApiResponse<UnpublishPost200Response> response = apiInstance.rejectWhatsAppGroupJoinRequestsWithHttpInfo(groupId, accountId, rejectWhatsAppGroupJoinRequestsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#rejectWhatsAppGroupJoinRequests");
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
| **groupId** | **String**| Group ID | |
| **accountId** | **String**| WhatsApp social account ID | |
| **rejectWhatsAppGroupJoinRequestsRequest** | [**RejectWhatsAppGroupJoinRequestsRequest**](RejectWhatsAppGroupJoinRequestsRequest.md)|  | |

### Return type

ApiResponse<[**UnpublishPost200Response**](UnpublishPost200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Requests rejected |  -  |
| **401** | Unauthorized |  -  |


## removeWhatsAppGroupParticipants

> UnpublishPost200Response removeWhatsAppGroupParticipants(groupId, accountId, removeWhatsAppGroupParticipantsRequest)

Remove participants

Remove participants from a WhatsApp group.  Not available on [Coexistence](/platforms/whatsapp/connection#whatsapp-business-app-coexistence) numbers. Requires a Cloud API-only number. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String groupId = "groupId_example"; // String | Group ID
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        RemoveWhatsAppGroupParticipantsRequest removeWhatsAppGroupParticipantsRequest = new RemoveWhatsAppGroupParticipantsRequest(); // RemoveWhatsAppGroupParticipantsRequest | 
        try {
            UnpublishPost200Response result = apiInstance.removeWhatsAppGroupParticipants(groupId, accountId, removeWhatsAppGroupParticipantsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#removeWhatsAppGroupParticipants");
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
| **groupId** | **String**| Group ID | |
| **accountId** | **String**| WhatsApp social account ID | |
| **removeWhatsAppGroupParticipantsRequest** | [**RemoveWhatsAppGroupParticipantsRequest**](RemoveWhatsAppGroupParticipantsRequest.md)|  | |

### Return type

[**UnpublishPost200Response**](UnpublishPost200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Participants removed |  -  |
| **401** | Unauthorized |  -  |

## removeWhatsAppGroupParticipantsWithHttpInfo

> ApiResponse<UnpublishPost200Response> removeWhatsAppGroupParticipants removeWhatsAppGroupParticipantsWithHttpInfo(groupId, accountId, removeWhatsAppGroupParticipantsRequest)

Remove participants

Remove participants from a WhatsApp group.  Not available on [Coexistence](/platforms/whatsapp/connection#whatsapp-business-app-coexistence) numbers. Requires a Cloud API-only number. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String groupId = "groupId_example"; // String | Group ID
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        RemoveWhatsAppGroupParticipantsRequest removeWhatsAppGroupParticipantsRequest = new RemoveWhatsAppGroupParticipantsRequest(); // RemoveWhatsAppGroupParticipantsRequest | 
        try {
            ApiResponse<UnpublishPost200Response> response = apiInstance.removeWhatsAppGroupParticipantsWithHttpInfo(groupId, accountId, removeWhatsAppGroupParticipantsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#removeWhatsAppGroupParticipants");
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
| **groupId** | **String**| Group ID | |
| **accountId** | **String**| WhatsApp social account ID | |
| **removeWhatsAppGroupParticipantsRequest** | [**RemoveWhatsAppGroupParticipantsRequest**](RemoveWhatsAppGroupParticipantsRequest.md)|  | |

### Return type

ApiResponse<[**UnpublishPost200Response**](UnpublishPost200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Participants removed |  -  |
| **401** | Unauthorized |  -  |


## sendWhatsAppConversion

> SendWhatsAppConversion200Response sendWhatsAppConversion(sendWhatsAppConversionRequest)

Send WhatsApp conversion event

Forward a WhatsApp Business Messaging conversion event (&#x60;LeadSubmitted&#x60;, &#x60;Purchase&#x60;, &#x60;AddToCart&#x60;, &#x60;InitiateCheckout&#x60;, &#x60;ViewContent&#x60;) to Meta&#39;s Conversions API with &#x60;action_source &#x3D; business_messaging&#x60; and &#x60;messaging_channel &#x3D; whatsapp&#x60;. The endpoint looks up the originating CTWA click ID (&#x60;ctwa_clid&#x60;) captured on the first inbound message of the conversation and replays it on every event so Meta can attribute the conversion back to the Click-to-WhatsApp ad that drove the chat.  Configuration prerequisite on the WhatsApp account metadata:   - &#x60;metaCapiDatasetId&#x60;: the Meta dataset ID linked to the WABA.     Provision one with &#x60;POST /v1/whatsapp/dataset&#x60;.  The WABA ID (already set automatically at connect time) is forwarded as &#x60;user_data.whatsapp_business_account_id&#x60;, which is the per-channel attribution identifier Meta requires for WhatsApp events. No Facebook Page ID is needed (that field is the Messenger-branch identifier).  Identify the conversation by either &#x60;conversationId&#x60; (preferred) or &#x60;phoneE164&#x60; (digits only, no &#x60;+&#x60;). At least one is required. If the conversation has no captured &#x60;ctwa_clid&#x60;, the request returns 422 because there is nothing to attribute.  Token and dataset coupling: the WhatsApp account&#39;s accessToken must have access to the configured &#x60;metaCapiDatasetId&#x60;. By default a WABA&#39;s system-user token is scoped to the WABA&#39;s own Business Manager and cannot post to a pixel owned by a different Business; Meta returns code 100 in that case. Either share the dataset with the WhatsApp app&#39;s Business in BM, or use a dataset already in the same Business as the WABA. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        SendWhatsAppConversionRequest sendWhatsAppConversionRequest = new SendWhatsAppConversionRequest(); // SendWhatsAppConversionRequest | 
        try {
            SendWhatsAppConversion200Response result = apiInstance.sendWhatsAppConversion(sendWhatsAppConversionRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#sendWhatsAppConversion");
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
| **sendWhatsAppConversionRequest** | [**SendWhatsAppConversionRequest**](SendWhatsAppConversionRequest.md)|  | |

### Return type

[**SendWhatsAppConversion200Response**](SendWhatsAppConversion200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event submitted to Meta. Inspect &#x60;eventsFailed&#x60; and &#x60;failures[]&#x60; to detect partial failures. A 200 does not mean Meta accepted the event; the status reflects \&quot;request reached Meta\&quot; only.  |  -  |
| **400** | Invalid body. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Conversation not found. |  -  |
| **422** | Configuration missing (no &#x60;metaCapiDatasetId&#x60; on the account, set it via POST /v1/whatsapp/dataset) OR the resolved conversation has no captured &#x60;ctwa_clid&#x60;.  |  -  |

## sendWhatsAppConversionWithHttpInfo

> ApiResponse<SendWhatsAppConversion200Response> sendWhatsAppConversion sendWhatsAppConversionWithHttpInfo(sendWhatsAppConversionRequest)

Send WhatsApp conversion event

Forward a WhatsApp Business Messaging conversion event (&#x60;LeadSubmitted&#x60;, &#x60;Purchase&#x60;, &#x60;AddToCart&#x60;, &#x60;InitiateCheckout&#x60;, &#x60;ViewContent&#x60;) to Meta&#39;s Conversions API with &#x60;action_source &#x3D; business_messaging&#x60; and &#x60;messaging_channel &#x3D; whatsapp&#x60;. The endpoint looks up the originating CTWA click ID (&#x60;ctwa_clid&#x60;) captured on the first inbound message of the conversation and replays it on every event so Meta can attribute the conversion back to the Click-to-WhatsApp ad that drove the chat.  Configuration prerequisite on the WhatsApp account metadata:   - &#x60;metaCapiDatasetId&#x60;: the Meta dataset ID linked to the WABA.     Provision one with &#x60;POST /v1/whatsapp/dataset&#x60;.  The WABA ID (already set automatically at connect time) is forwarded as &#x60;user_data.whatsapp_business_account_id&#x60;, which is the per-channel attribution identifier Meta requires for WhatsApp events. No Facebook Page ID is needed (that field is the Messenger-branch identifier).  Identify the conversation by either &#x60;conversationId&#x60; (preferred) or &#x60;phoneE164&#x60; (digits only, no &#x60;+&#x60;). At least one is required. If the conversation has no captured &#x60;ctwa_clid&#x60;, the request returns 422 because there is nothing to attribute.  Token and dataset coupling: the WhatsApp account&#39;s accessToken must have access to the configured &#x60;metaCapiDatasetId&#x60;. By default a WABA&#39;s system-user token is scoped to the WABA&#39;s own Business Manager and cannot post to a pixel owned by a different Business; Meta returns code 100 in that case. Either share the dataset with the WhatsApp app&#39;s Business in BM, or use a dataset already in the same Business as the WABA. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        SendWhatsAppConversionRequest sendWhatsAppConversionRequest = new SendWhatsAppConversionRequest(); // SendWhatsAppConversionRequest | 
        try {
            ApiResponse<SendWhatsAppConversion200Response> response = apiInstance.sendWhatsAppConversionWithHttpInfo(sendWhatsAppConversionRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#sendWhatsAppConversion");
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
| **sendWhatsAppConversionRequest** | [**SendWhatsAppConversionRequest**](SendWhatsAppConversionRequest.md)|  | |

### Return type

ApiResponse<[**SendWhatsAppConversion200Response**](SendWhatsAppConversion200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event submitted to Meta. Inspect &#x60;eventsFailed&#x60; and &#x60;failures[]&#x60; to detect partial failures. A 200 does not mean Meta accepted the event; the status reflects \&quot;request reached Meta\&quot; only.  |  -  |
| **400** | Invalid body. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Conversation not found. |  -  |
| **422** | Configuration missing (no &#x60;metaCapiDatasetId&#x60; on the account, set it via POST /v1/whatsapp/dataset) OR the resolved conversation has no captured &#x60;ctwa_clid&#x60;.  |  -  |


## setWhatsappBusinessUsername

> SetWhatsappBusinessUsername200Response setWhatsappBusinessUsername(setWhatsappBusinessUsernameRequest)

Set business username

Claim or transfer a WhatsApp Business username for the account.  Username rules: 3-35 characters, letters/digits/period/underscore only, must contain at least one letter, no leading or trailing periods, no consecutive periods, no &#x60;www&#x60; prefix, no domain TLD suffix (e.g. &#x60;.com&#x60;).  If the desired username is currently held by another account, pass &#x60;transferAction: \&quot;force_transfer\&quot;&#x60; to request a transfer. On failure the API returns a standard error envelope with one of these codes: &#x60;whatsapp_username_unavailable&#x60; (already taken and transfer not requested), &#x60;whatsapp_username_ineligible&#x60; (account not eligible to claim a username), or &#x60;whatsapp_username_transfer_required&#x60; (username is held elsewhere; retry with &#x60;force_transfer&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        SetWhatsappBusinessUsernameRequest setWhatsappBusinessUsernameRequest = new SetWhatsappBusinessUsernameRequest(); // SetWhatsappBusinessUsernameRequest | 
        try {
            SetWhatsappBusinessUsername200Response result = apiInstance.setWhatsappBusinessUsername(setWhatsappBusinessUsernameRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#setWhatsappBusinessUsername");
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
| **setWhatsappBusinessUsernameRequest** | [**SetWhatsappBusinessUsernameRequest**](SetWhatsappBusinessUsernameRequest.md)|  | |

### Return type

[**SetWhatsappBusinessUsername200Response**](SetWhatsappBusinessUsername200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Username claimed successfully |  -  |
| **400** | Validation error or username unavailable (see error code in response) |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

## setWhatsappBusinessUsernameWithHttpInfo

> ApiResponse<SetWhatsappBusinessUsername200Response> setWhatsappBusinessUsername setWhatsappBusinessUsernameWithHttpInfo(setWhatsappBusinessUsernameRequest)

Set business username

Claim or transfer a WhatsApp Business username for the account.  Username rules: 3-35 characters, letters/digits/period/underscore only, must contain at least one letter, no leading or trailing periods, no consecutive periods, no &#x60;www&#x60; prefix, no domain TLD suffix (e.g. &#x60;.com&#x60;).  If the desired username is currently held by another account, pass &#x60;transferAction: \&quot;force_transfer\&quot;&#x60; to request a transfer. On failure the API returns a standard error envelope with one of these codes: &#x60;whatsapp_username_unavailable&#x60; (already taken and transfer not requested), &#x60;whatsapp_username_ineligible&#x60; (account not eligible to claim a username), or &#x60;whatsapp_username_transfer_required&#x60; (username is held elsewhere; retry with &#x60;force_transfer&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        SetWhatsappBusinessUsernameRequest setWhatsappBusinessUsernameRequest = new SetWhatsappBusinessUsernameRequest(); // SetWhatsappBusinessUsernameRequest | 
        try {
            ApiResponse<SetWhatsappBusinessUsername200Response> response = apiInstance.setWhatsappBusinessUsernameWithHttpInfo(setWhatsappBusinessUsernameRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#setWhatsappBusinessUsername");
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
| **setWhatsappBusinessUsernameRequest** | [**SetWhatsappBusinessUsernameRequest**](SetWhatsappBusinessUsernameRequest.md)|  | |

### Return type

ApiResponse<[**SetWhatsappBusinessUsername200Response**](SetWhatsappBusinessUsername200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Username claimed successfully |  -  |
| **400** | Validation error or username unavailable (see error code in response) |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |


## unblockWhatsAppUsers

> UnblockWhatsAppUsers200Response unblockWhatsAppUsers(unblockWhatsAppUsersRequest)

Unblock users

Unblock one or more previously blocked WhatsApp users on this number. Up to 1,000 users per request; per-user failures are reported in &#x60;failed&#x60; without failing the rest of the batch. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        UnblockWhatsAppUsersRequest unblockWhatsAppUsersRequest = new UnblockWhatsAppUsersRequest(); // UnblockWhatsAppUsersRequest | 
        try {
            UnblockWhatsAppUsers200Response result = apiInstance.unblockWhatsAppUsers(unblockWhatsAppUsersRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#unblockWhatsAppUsers");
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
| **unblockWhatsAppUsersRequest** | [**UnblockWhatsAppUsersRequest**](UnblockWhatsAppUsersRequest.md)|  | |

### Return type

[**UnblockWhatsAppUsers200Response**](UnblockWhatsAppUsers200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-user results |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

## unblockWhatsAppUsersWithHttpInfo

> ApiResponse<UnblockWhatsAppUsers200Response> unblockWhatsAppUsers unblockWhatsAppUsersWithHttpInfo(unblockWhatsAppUsersRequest)

Unblock users

Unblock one or more previously blocked WhatsApp users on this number. Up to 1,000 users per request; per-user failures are reported in &#x60;failed&#x60; without failing the rest of the batch. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        UnblockWhatsAppUsersRequest unblockWhatsAppUsersRequest = new UnblockWhatsAppUsersRequest(); // UnblockWhatsAppUsersRequest | 
        try {
            ApiResponse<UnblockWhatsAppUsers200Response> response = apiInstance.unblockWhatsAppUsersWithHttpInfo(unblockWhatsAppUsersRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#unblockWhatsAppUsers");
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
| **unblockWhatsAppUsersRequest** | [**UnblockWhatsAppUsersRequest**](UnblockWhatsAppUsersRequest.md)|  | |

### Return type

ApiResponse<[**UnblockWhatsAppUsers200Response**](UnblockWhatsAppUsers200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-user results |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |


## updateWhatsAppBusinessProfile

> UnpublishPost200Response updateWhatsAppBusinessProfile(updateWhatsAppBusinessProfileRequest)

Update business profile

Update the WhatsApp Business profile. All fields are optional; only provided fields will be updated. Constraints: about max 139 chars, description max 512 chars, max 2 websites. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        UpdateWhatsAppBusinessProfileRequest updateWhatsAppBusinessProfileRequest = new UpdateWhatsAppBusinessProfileRequest(); // UpdateWhatsAppBusinessProfileRequest | 
        try {
            UnpublishPost200Response result = apiInstance.updateWhatsAppBusinessProfile(updateWhatsAppBusinessProfileRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#updateWhatsAppBusinessProfile");
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
| **updateWhatsAppBusinessProfileRequest** | [**UpdateWhatsAppBusinessProfileRequest**](UpdateWhatsAppBusinessProfileRequest.md)|  | |

### Return type

[**UnpublishPost200Response**](UnpublishPost200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Business profile updated successfully |  -  |
| **400** | Validation error (field too long, too many websites, etc.) |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

## updateWhatsAppBusinessProfileWithHttpInfo

> ApiResponse<UnpublishPost200Response> updateWhatsAppBusinessProfile updateWhatsAppBusinessProfileWithHttpInfo(updateWhatsAppBusinessProfileRequest)

Update business profile

Update the WhatsApp Business profile. All fields are optional; only provided fields will be updated. Constraints: about max 139 chars, description max 512 chars, max 2 websites. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        UpdateWhatsAppBusinessProfileRequest updateWhatsAppBusinessProfileRequest = new UpdateWhatsAppBusinessProfileRequest(); // UpdateWhatsAppBusinessProfileRequest | 
        try {
            ApiResponse<UnpublishPost200Response> response = apiInstance.updateWhatsAppBusinessProfileWithHttpInfo(updateWhatsAppBusinessProfileRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#updateWhatsAppBusinessProfile");
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
| **updateWhatsAppBusinessProfileRequest** | [**UpdateWhatsAppBusinessProfileRequest**](UpdateWhatsAppBusinessProfileRequest.md)|  | |

### Return type

ApiResponse<[**UnpublishPost200Response**](UnpublishPost200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Business profile updated successfully |  -  |
| **400** | Validation error (field too long, too many websites, etc.) |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |


## updateWhatsAppDisplayName

> UpdateWhatsAppDisplayName200Response updateWhatsAppDisplayName(updateWhatsAppDisplayNameRequest)

Request display name change

Submit a display name change request for the WhatsApp Business account. The new name must follow WhatsApp naming guidelines (3-512 characters, must represent your business). Changes require Meta review and approval, which typically takes 1-3 business days. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        UpdateWhatsAppDisplayNameRequest updateWhatsAppDisplayNameRequest = new UpdateWhatsAppDisplayNameRequest(); // UpdateWhatsAppDisplayNameRequest | 
        try {
            UpdateWhatsAppDisplayName200Response result = apiInstance.updateWhatsAppDisplayName(updateWhatsAppDisplayNameRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#updateWhatsAppDisplayName");
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
| **updateWhatsAppDisplayNameRequest** | [**UpdateWhatsAppDisplayNameRequest**](UpdateWhatsAppDisplayNameRequest.md)|  | |

### Return type

[**UpdateWhatsAppDisplayName200Response**](UpdateWhatsAppDisplayName200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Display name change submitted for review |  -  |
| **400** | Invalid display name (too short, too long, or missing) |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

## updateWhatsAppDisplayNameWithHttpInfo

> ApiResponse<UpdateWhatsAppDisplayName200Response> updateWhatsAppDisplayName updateWhatsAppDisplayNameWithHttpInfo(updateWhatsAppDisplayNameRequest)

Request display name change

Submit a display name change request for the WhatsApp Business account. The new name must follow WhatsApp naming guidelines (3-512 characters, must represent your business). Changes require Meta review and approval, which typically takes 1-3 business days. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        UpdateWhatsAppDisplayNameRequest updateWhatsAppDisplayNameRequest = new UpdateWhatsAppDisplayNameRequest(); // UpdateWhatsAppDisplayNameRequest | 
        try {
            ApiResponse<UpdateWhatsAppDisplayName200Response> response = apiInstance.updateWhatsAppDisplayNameWithHttpInfo(updateWhatsAppDisplayNameRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#updateWhatsAppDisplayName");
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
| **updateWhatsAppDisplayNameRequest** | [**UpdateWhatsAppDisplayNameRequest**](UpdateWhatsAppDisplayNameRequest.md)|  | |

### Return type

ApiResponse<[**UpdateWhatsAppDisplayName200Response**](UpdateWhatsAppDisplayName200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Display name change submitted for review |  -  |
| **400** | Invalid display name (too short, too long, or missing) |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |


## updateWhatsAppGroupChat

> UnpublishPost200Response updateWhatsAppGroupChat(groupId, accountId, updateWhatsAppGroupChatRequest)

Update group settings

Update the subject, description, or join approval mode of a WhatsApp group.  Not available on [Coexistence](/platforms/whatsapp/connection#whatsapp-business-app-coexistence) numbers. Requires a Cloud API-only number. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String groupId = "groupId_example"; // String | Group ID
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        UpdateWhatsAppGroupChatRequest updateWhatsAppGroupChatRequest = new UpdateWhatsAppGroupChatRequest(); // UpdateWhatsAppGroupChatRequest | 
        try {
            UnpublishPost200Response result = apiInstance.updateWhatsAppGroupChat(groupId, accountId, updateWhatsAppGroupChatRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#updateWhatsAppGroupChat");
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
| **groupId** | **String**| Group ID | |
| **accountId** | **String**| WhatsApp social account ID | |
| **updateWhatsAppGroupChatRequest** | [**UpdateWhatsAppGroupChatRequest**](UpdateWhatsAppGroupChatRequest.md)|  | |

### Return type

[**UnpublishPost200Response**](UnpublishPost200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Group updated |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## updateWhatsAppGroupChatWithHttpInfo

> ApiResponse<UnpublishPost200Response> updateWhatsAppGroupChat updateWhatsAppGroupChatWithHttpInfo(groupId, accountId, updateWhatsAppGroupChatRequest)

Update group settings

Update the subject, description, or join approval mode of a WhatsApp group.  Not available on [Coexistence](/platforms/whatsapp/connection#whatsapp-business-app-coexistence) numbers. Requires a Cloud API-only number. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String groupId = "groupId_example"; // String | Group ID
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        UpdateWhatsAppGroupChatRequest updateWhatsAppGroupChatRequest = new UpdateWhatsAppGroupChatRequest(); // UpdateWhatsAppGroupChatRequest | 
        try {
            ApiResponse<UnpublishPost200Response> response = apiInstance.updateWhatsAppGroupChatWithHttpInfo(groupId, accountId, updateWhatsAppGroupChatRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#updateWhatsAppGroupChat");
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
| **groupId** | **String**| Group ID | |
| **accountId** | **String**| WhatsApp social account ID | |
| **updateWhatsAppGroupChatRequest** | [**UpdateWhatsAppGroupChatRequest**](UpdateWhatsAppGroupChatRequest.md)|  | |

### Return type

ApiResponse<[**UnpublishPost200Response**](UnpublishPost200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Group updated |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## updateWhatsAppTemplate

> UpdateWhatsAppTemplate200Response updateWhatsAppTemplate(templateName, updateWhatsAppTemplateRequest)

Update template

Update a message template&#39;s components. Only certain fields can be updated depending on the template&#39;s current approval state. Approved templates can only have components updated. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String templateName = "templateName_example"; // String | Template name
        UpdateWhatsAppTemplateRequest updateWhatsAppTemplateRequest = new UpdateWhatsAppTemplateRequest(); // UpdateWhatsAppTemplateRequest | 
        try {
            UpdateWhatsAppTemplate200Response result = apiInstance.updateWhatsAppTemplate(templateName, updateWhatsAppTemplateRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#updateWhatsAppTemplate");
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
| **templateName** | **String**| Template name | |
| **updateWhatsAppTemplateRequest** | [**UpdateWhatsAppTemplateRequest**](UpdateWhatsAppTemplateRequest.md)|  | |

### Return type

[**UpdateWhatsAppTemplate200Response**](UpdateWhatsAppTemplate200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Template updated successfully |  -  |
| **400** | Validation error (missing fields) |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## updateWhatsAppTemplateWithHttpInfo

> ApiResponse<UpdateWhatsAppTemplate200Response> updateWhatsAppTemplate updateWhatsAppTemplateWithHttpInfo(templateName, updateWhatsAppTemplateRequest)

Update template

Update a message template&#39;s components. Only certain fields can be updated depending on the template&#39;s current approval state. Approved templates can only have components updated. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String templateName = "templateName_example"; // String | Template name
        UpdateWhatsAppTemplateRequest updateWhatsAppTemplateRequest = new UpdateWhatsAppTemplateRequest(); // UpdateWhatsAppTemplateRequest | 
        try {
            ApiResponse<UpdateWhatsAppTemplate200Response> response = apiInstance.updateWhatsAppTemplateWithHttpInfo(templateName, updateWhatsAppTemplateRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#updateWhatsAppTemplate");
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
| **templateName** | **String**| Template name | |
| **updateWhatsAppTemplateRequest** | [**UpdateWhatsAppTemplateRequest**](UpdateWhatsAppTemplateRequest.md)|  | |

### Return type

ApiResponse<[**UpdateWhatsAppTemplate200Response**](UpdateWhatsAppTemplate200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Template updated successfully |  -  |
| **400** | Validation error (missing fields) |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## uploadWhatsAppProfilePhoto

> UnpublishPost200Response uploadWhatsAppProfilePhoto(accountId, _file)

Upload profile picture

Upload a new profile picture for the WhatsApp Business Profile. Uses Meta&#39;s resumable upload API under the hood: creates an upload session, uploads the image bytes, then updates the business profile with the resulting handle.  Provide the image either as a binary upload (&#x60;multipart/form-data&#x60; with &#x60;file&#x60;) or as a download URL (&#x60;application/json&#x60; with &#x60;url&#x60;) — with a URL we fetch the image server-side and upload the bytes for you. Meta&#39;s profile-photo API is bytes-only, so there is no direct URL passthrough. JPEG/PNG, max 5MB either way. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        File _file = new File("/path/to/file"); // File | Image file (JPEG or PNG, max 5MB, recommended 640x640)
        try {
            UnpublishPost200Response result = apiInstance.uploadWhatsAppProfilePhoto(accountId, _file);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#uploadWhatsAppProfilePhoto");
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
| **_file** | **File**| Image file (JPEG or PNG, max 5MB, recommended 640x640) | |

### Return type

[**UnpublishPost200Response**](UnpublishPost200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data, application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Profile picture updated successfully |  -  |
| **400** | Invalid file type/URL, file too large, or missing parameters |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |
| **422** | Profile photo is locked for WhatsApp coexistence numbers (manage it in the WhatsApp Business app) |  -  |

## uploadWhatsAppProfilePhotoWithHttpInfo

> ApiResponse<UnpublishPost200Response> uploadWhatsAppProfilePhoto uploadWhatsAppProfilePhotoWithHttpInfo(accountId, _file)

Upload profile picture

Upload a new profile picture for the WhatsApp Business Profile. Uses Meta&#39;s resumable upload API under the hood: creates an upload session, uploads the image bytes, then updates the business profile with the resulting handle.  Provide the image either as a binary upload (&#x60;multipart/form-data&#x60; with &#x60;file&#x60;) or as a download URL (&#x60;application/json&#x60; with &#x60;url&#x60;) — with a URL we fetch the image server-side and upload the bytes for you. Meta&#39;s profile-photo API is bytes-only, so there is no direct URL passthrough. JPEG/PNG, max 5MB either way. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WhatsAppApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WhatsAppApi apiInstance = new WhatsAppApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        File _file = new File("/path/to/file"); // File | Image file (JPEG or PNG, max 5MB, recommended 640x640)
        try {
            ApiResponse<UnpublishPost200Response> response = apiInstance.uploadWhatsAppProfilePhotoWithHttpInfo(accountId, _file);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WhatsAppApi#uploadWhatsAppProfilePhoto");
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
| **_file** | **File**| Image file (JPEG or PNG, max 5MB, recommended 640x640) | |

### Return type

ApiResponse<[**UnpublishPost200Response**](UnpublishPost200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data, application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Profile picture updated successfully |  -  |
| **400** | Invalid file type/URL, file too large, or missing parameters |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |
| **422** | Profile photo is locked for WhatsApp coexistence numbers (manage it in the WhatsApp Business app) |  -  |

