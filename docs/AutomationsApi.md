# AutomationsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activateAutomation**](AutomationsApi.md#activateAutomation) | **POST** /v1/automations/{automationId}/activate | Turn an automation on |
| [**activateAutomationWithHttpInfo**](AutomationsApi.md#activateAutomationWithHttpInfo) | **POST** /v1/automations/{automationId}/activate | Turn an automation on |
| [**approveAutomationApproval**](AutomationsApi.md#approveAutomationApproval) | **POST** /v1/automations/{automationId}/approvals/{approvalId}/approve | Approve an approval request |
| [**approveAutomationApprovalWithHttpInfo**](AutomationsApi.md#approveAutomationApprovalWithHttpInfo) | **POST** /v1/automations/{automationId}/approvals/{approvalId}/approve | Approve an approval request |
| [**backtestAutomation**](AutomationsApi.md#backtestAutomation) | **POST** /v1/automations/{automationId}/backtest | Backtest a saved automation |
| [**backtestAutomationWithHttpInfo**](AutomationsApi.md#backtestAutomationWithHttpInfo) | **POST** /v1/automations/{automationId}/backtest | Backtest a saved automation |
| [**backtestAutomationDraft**](AutomationsApi.md#backtestAutomationDraft) | **POST** /v1/automations/backtest | Backtest an unsaved automation |
| [**backtestAutomationDraftWithHttpInfo**](AutomationsApi.md#backtestAutomationDraftWithHttpInfo) | **POST** /v1/automations/backtest | Backtest an unsaved automation |
| [**createAutomation**](AutomationsApi.md#createAutomation) | **POST** /v1/automations | Create an automation |
| [**createAutomationWithHttpInfo**](AutomationsApi.md#createAutomationWithHttpInfo) | **POST** /v1/automations | Create an automation |
| [**createAutomationTemplate**](AutomationsApi.md#createAutomationTemplate) | **POST** /v1/automations/templates | Create an automation template |
| [**createAutomationTemplateWithHttpInfo**](AutomationsApi.md#createAutomationTemplateWithHttpInfo) | **POST** /v1/automations/templates | Create an automation template |
| [**deleteAutomation**](AutomationsApi.md#deleteAutomation) | **DELETE** /v1/automations/{automationId} | Delete an automation |
| [**deleteAutomationWithHttpInfo**](AutomationsApi.md#deleteAutomationWithHttpInfo) | **DELETE** /v1/automations/{automationId} | Delete an automation |
| [**deleteAutomationTemplate**](AutomationsApi.md#deleteAutomationTemplate) | **DELETE** /v1/automations/templates/{templateId} | Delete an automation template |
| [**deleteAutomationTemplateWithHttpInfo**](AutomationsApi.md#deleteAutomationTemplateWithHttpInfo) | **DELETE** /v1/automations/templates/{templateId} | Delete an automation template |
| [**getAutomation**](AutomationsApi.md#getAutomation) | **GET** /v1/automations/{automationId} | Get an automation |
| [**getAutomationWithHttpInfo**](AutomationsApi.md#getAutomationWithHttpInfo) | **GET** /v1/automations/{automationId} | Get an automation |
| [**getAutomationApproval**](AutomationsApi.md#getAutomationApproval) | **GET** /v1/automations/{automationId}/approvals/{approvalId} | Get an approval request |
| [**getAutomationApprovalWithHttpInfo**](AutomationsApi.md#getAutomationApprovalWithHttpInfo) | **GET** /v1/automations/{automationId}/approvals/{approvalId} | Get an approval request |
| [**getAutomationCatalog**](AutomationsApi.md#getAutomationCatalog) | **GET** /v1/automations/catalog | Get the automations catalog |
| [**getAutomationCatalogWithHttpInfo**](AutomationsApi.md#getAutomationCatalogWithHttpInfo) | **GET** /v1/automations/catalog | Get the automations catalog |
| [**getAutomationControls**](AutomationsApi.md#getAutomationControls) | **GET** /v1/automations/controls | Get automation controls |
| [**getAutomationControlsWithHttpInfo**](AutomationsApi.md#getAutomationControlsWithHttpInfo) | **GET** /v1/automations/controls | Get automation controls |
| [**getAutomationTemplate**](AutomationsApi.md#getAutomationTemplate) | **GET** /v1/automations/templates/{templateId} | Get an automation template |
| [**getAutomationTemplateWithHttpInfo**](AutomationsApi.md#getAutomationTemplateWithHttpInfo) | **GET** /v1/automations/templates/{templateId} | Get an automation template |
| [**getSharedAutomationTemplate**](AutomationsApi.md#getSharedAutomationTemplate) | **GET** /v1/automations/templates/shared/{shareToken} | Get a shared automation template |
| [**getSharedAutomationTemplateWithHttpInfo**](AutomationsApi.md#getSharedAutomationTemplateWithHttpInfo) | **GET** /v1/automations/templates/shared/{shareToken} | Get a shared automation template |
| [**getZernioAutomationTemplate**](AutomationsApi.md#getZernioAutomationTemplate) | **GET** /v1/automations/templates/zernio/{templateId} | Get a Zernio automation template |
| [**getZernioAutomationTemplateWithHttpInfo**](AutomationsApi.md#getZernioAutomationTemplateWithHttpInfo) | **GET** /v1/automations/templates/zernio/{templateId} | Get a Zernio automation template |
| [**installAutomationTemplate**](AutomationsApi.md#installAutomationTemplate) | **POST** /v1/automations/templates/{templateId}/install | Install an automation template |
| [**installAutomationTemplateWithHttpInfo**](AutomationsApi.md#installAutomationTemplateWithHttpInfo) | **POST** /v1/automations/templates/{templateId}/install | Install an automation template |
| [**installSharedAutomationTemplate**](AutomationsApi.md#installSharedAutomationTemplate) | **POST** /v1/automations/templates/shared/{shareToken}/install | Install a shared automation template |
| [**installSharedAutomationTemplateWithHttpInfo**](AutomationsApi.md#installSharedAutomationTemplateWithHttpInfo) | **POST** /v1/automations/templates/shared/{shareToken}/install | Install a shared automation template |
| [**installZernioAutomationTemplate**](AutomationsApi.md#installZernioAutomationTemplate) | **POST** /v1/automations/templates/zernio/{templateId}/install | Install a Zernio automation template |
| [**installZernioAutomationTemplateWithHttpInfo**](AutomationsApi.md#installZernioAutomationTemplateWithHttpInfo) | **POST** /v1/automations/templates/zernio/{templateId}/install | Install a Zernio automation template |
| [**listAutomationActions**](AutomationsApi.md#listAutomationActions) | **GET** /v1/automations/actions | List automation actions |
| [**listAutomationActionsWithHttpInfo**](AutomationsApi.md#listAutomationActionsWithHttpInfo) | **GET** /v1/automations/actions | List automation actions |
| [**listAutomationApprovals**](AutomationsApi.md#listAutomationApprovals) | **GET** /v1/automations/{automationId}/approvals | List an automation&#39;s approval requests |
| [**listAutomationApprovalsWithHttpInfo**](AutomationsApi.md#listAutomationApprovalsWithHttpInfo) | **GET** /v1/automations/{automationId}/approvals | List an automation&#39;s approval requests |
| [**listAutomationChecks**](AutomationsApi.md#listAutomationChecks) | **GET** /v1/automations/{automationId}/checks | List an automation&#39;s checks |
| [**listAutomationChecksWithHttpInfo**](AutomationsApi.md#listAutomationChecksWithHttpInfo) | **GET** /v1/automations/{automationId}/checks | List an automation&#39;s checks |
| [**listAutomationTemplates**](AutomationsApi.md#listAutomationTemplates) | **GET** /v1/automations/templates | List automation templates |
| [**listAutomationTemplatesWithHttpInfo**](AutomationsApi.md#listAutomationTemplatesWithHttpInfo) | **GET** /v1/automations/templates | List automation templates |
| [**listAutomations**](AutomationsApi.md#listAutomations) | **GET** /v1/automations | List automations |
| [**listAutomationsWithHttpInfo**](AutomationsApi.md#listAutomationsWithHttpInfo) | **GET** /v1/automations | List automations |
| [**pauseAutomation**](AutomationsApi.md#pauseAutomation) | **POST** /v1/automations/{automationId}/pause | Turn an automation off |
| [**pauseAutomationWithHttpInfo**](AutomationsApi.md#pauseAutomationWithHttpInfo) | **POST** /v1/automations/{automationId}/pause | Turn an automation off |
| [**previewAutomation**](AutomationsApi.md#previewAutomation) | **POST** /v1/automations/{automationId}/preview | Preview a saved automation |
| [**previewAutomationWithHttpInfo**](AutomationsApi.md#previewAutomationWithHttpInfo) | **POST** /v1/automations/{automationId}/preview | Preview a saved automation |
| [**previewAutomationDraft**](AutomationsApi.md#previewAutomationDraft) | **POST** /v1/automations/preview | Preview an unsaved automation |
| [**previewAutomationDraftWithHttpInfo**](AutomationsApi.md#previewAutomationDraftWithHttpInfo) | **POST** /v1/automations/preview | Preview an unsaved automation |
| [**rejectAutomationApproval**](AutomationsApi.md#rejectAutomationApproval) | **POST** /v1/automations/{automationId}/approvals/{approvalId}/reject | Reject an approval request |
| [**rejectAutomationApprovalWithHttpInfo**](AutomationsApi.md#rejectAutomationApprovalWithHttpInfo) | **POST** /v1/automations/{automationId}/approvals/{approvalId}/reject | Reject an approval request |
| [**updateAutomation**](AutomationsApi.md#updateAutomation) | **PATCH** /v1/automations/{automationId} | Edit an automation |
| [**updateAutomationWithHttpInfo**](AutomationsApi.md#updateAutomationWithHttpInfo) | **PATCH** /v1/automations/{automationId} | Edit an automation |
| [**updateAutomationAdAccountControls**](AutomationsApi.md#updateAutomationAdAccountControls) | **PATCH** /v1/automations/controls/ad-accounts | Update one ad account&#39;s controls |
| [**updateAutomationAdAccountControlsWithHttpInfo**](AutomationsApi.md#updateAutomationAdAccountControlsWithHttpInfo) | **PATCH** /v1/automations/controls/ad-accounts | Update one ad account&#39;s controls |
| [**updateAutomationControls**](AutomationsApi.md#updateAutomationControls) | **PATCH** /v1/automations/controls | Turn every ad automation off or on |
| [**updateAutomationControlsWithHttpInfo**](AutomationsApi.md#updateAutomationControlsWithHttpInfo) | **PATCH** /v1/automations/controls | Turn every ad automation off or on |
| [**updateAutomationTemplate**](AutomationsApi.md#updateAutomationTemplate) | **PATCH** /v1/automations/templates/{templateId} | Update an automation template |
| [**updateAutomationTemplateWithHttpInfo**](AutomationsApi.md#updateAutomationTemplateWithHttpInfo) | **PATCH** /v1/automations/templates/{templateId} | Update an automation template |



## activateAutomation

> CreateAutomation201Response activateAutomation(automationId)

Turn an automation on

An ad rule&#39;s first check runs right away.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        try {
            CreateAutomation201Response result = apiInstance.activateAutomation(automationId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#activateAutomation");
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
| **automationId** | **String**|  | |

### Return type

[**CreateAutomation201Response**](CreateAutomation201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Automation on |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ad rules only: your account has no ads access (code &#x60;ads_addon_required&#x60;). Ads are included on usage-based plans. Event and scheduled automations never get this 403: a boost step without ads access is refused with a 400 at its path. |  -  |
| **404** | Resource not found |  -  |

## activateAutomationWithHttpInfo

> ApiResponse<CreateAutomation201Response> activateAutomation activateAutomationWithHttpInfo(automationId)

Turn an automation on

An ad rule&#39;s first check runs right away.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        try {
            ApiResponse<CreateAutomation201Response> response = apiInstance.activateAutomationWithHttpInfo(automationId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#activateAutomation");
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
| **automationId** | **String**|  | |

### Return type

ApiResponse<[**CreateAutomation201Response**](CreateAutomation201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Automation on |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ad rules only: your account has no ads access (code &#x60;ads_addon_required&#x60;). Ads are included on usage-based plans. Event and scheduled automations never get this 403: a boost step without ads access is refused with a 400 at its path. |  -  |
| **404** | Resource not found |  -  |


## approveAutomationApproval

> GetAutomationApproval200Response approveAutomationApproval(automationId, approvalId, automationApprovalDecision)

Approve an approval request

Approves a pending request, so the automation acts on each change it holds. Each change is checked again first, and one that no longer applies is skipped.  Only the approvers the automation names now can decide, matched by the email of the user behind the API key. A request already decided, expired or cancelled is refused with nothing changed.  Each applied or failed change fires &#x60;automation.action.applied&#x60; or &#x60;automation.action.failed&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        String approvalId = "approvalId_example"; // String | 
        AutomationApprovalDecision automationApprovalDecision = new AutomationApprovalDecision(); // AutomationApprovalDecision | 
        try {
            GetAutomationApproval200Response result = apiInstance.approveAutomationApproval(automationId, approvalId, automationApprovalDecision);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#approveAutomationApproval");
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
| **automationId** | **String**|  | |
| **approvalId** | **String**|  | |
| **automationApprovalDecision** | [**AutomationApprovalDecision**](AutomationApprovalDecision.md)|  | [optional] |

### Return type

[**GetAutomationApproval200Response**](GetAutomationApproval200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request after the decision |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;insufficient_permissions&#x60; when you are not one of the approvers or &#x60;token&#x60; was sent to someone else, or &#x60;ads_addon_required&#x60; when the account has no ads access. |  -  |
| **404** | Resource not found |  -  |
| **409** | Code &#x60;invalid_resource_state&#x60;. Nothing was changed. The request was already approved or rejected, it expired, or it was cancelled when the automation stopped asking for approval.  Also returned when the automation no longer asks for approval or never does, and when it is acting on the ad account right now (try again in a minute).  |  -  |

## approveAutomationApprovalWithHttpInfo

> ApiResponse<GetAutomationApproval200Response> approveAutomationApproval approveAutomationApprovalWithHttpInfo(automationId, approvalId, automationApprovalDecision)

Approve an approval request

Approves a pending request, so the automation acts on each change it holds. Each change is checked again first, and one that no longer applies is skipped.  Only the approvers the automation names now can decide, matched by the email of the user behind the API key. A request already decided, expired or cancelled is refused with nothing changed.  Each applied or failed change fires &#x60;automation.action.applied&#x60; or &#x60;automation.action.failed&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        String approvalId = "approvalId_example"; // String | 
        AutomationApprovalDecision automationApprovalDecision = new AutomationApprovalDecision(); // AutomationApprovalDecision | 
        try {
            ApiResponse<GetAutomationApproval200Response> response = apiInstance.approveAutomationApprovalWithHttpInfo(automationId, approvalId, automationApprovalDecision);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#approveAutomationApproval");
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
| **automationId** | **String**|  | |
| **approvalId** | **String**|  | |
| **automationApprovalDecision** | [**AutomationApprovalDecision**](AutomationApprovalDecision.md)|  | [optional] |

### Return type

ApiResponse<[**GetAutomationApproval200Response**](GetAutomationApproval200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request after the decision |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;insufficient_permissions&#x60; when you are not one of the approvers or &#x60;token&#x60; was sent to someone else, or &#x60;ads_addon_required&#x60; when the account has no ads access. |  -  |
| **404** | Resource not found |  -  |
| **409** | Code &#x60;invalid_resource_state&#x60;. Nothing was changed. The request was already approved or rejected, it expired, or it was cancelled when the automation stopped asking for approval.  Also returned when the automation no longer asks for approval or never does, and when it is acting on the ad account right now (try again in a minute).  |  -  |


## backtestAutomation

> AutomationBacktest backtestAutomation(automationId, days)

Backtest a saved automation

What a saved automation would have done over the last &#x60;days&#x60; days, replayed on stored daily metrics. Nothing is changed.  Each day lists what it would have done. Its own changes carry into later days, but the metrics stay what really happened. &#x60;notes&#x60; says what the replay could not know.  Only ad automations can be backtested, on at most 5,000 ads. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        Integer days = 30; // Integer | How many whole days before today to replay. Today is not replayed.
        try {
            AutomationBacktest result = apiInstance.backtestAutomation(automationId, days);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#backtestAutomation");
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
| **automationId** | **String**|  | |
| **days** | **Integer**| How many whole days before today to replay. Today is not replayed. | [optional] [default to 30] |

### Return type

[**AutomationBacktest**](AutomationBacktest.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Backtest |  -  |
| **400** | The automation is invalid, or holds something its kind cannot: &#x60;details.problems&#x60; lists each problem with its JSON path. A few ad rule checks (an unsupported platform, step or metric, a cooldown shorter than the schedule, approvers not on the team) answer with &#x60;param&#x60; instead. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ad rules only: your account has no ads access (code &#x60;ads_addon_required&#x60;). Ads are included on usage-based plans. Event and scheduled automations never get this 403: a boost step without ads access is refused with a 400 at its path. |  -  |
| **404** | Resource not found |  -  |

## backtestAutomationWithHttpInfo

> ApiResponse<AutomationBacktest> backtestAutomation backtestAutomationWithHttpInfo(automationId, days)

Backtest a saved automation

What a saved automation would have done over the last &#x60;days&#x60; days, replayed on stored daily metrics. Nothing is changed.  Each day lists what it would have done. Its own changes carry into later days, but the metrics stay what really happened. &#x60;notes&#x60; says what the replay could not know.  Only ad automations can be backtested, on at most 5,000 ads. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        Integer days = 30; // Integer | How many whole days before today to replay. Today is not replayed.
        try {
            ApiResponse<AutomationBacktest> response = apiInstance.backtestAutomationWithHttpInfo(automationId, days);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#backtestAutomation");
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
| **automationId** | **String**|  | |
| **days** | **Integer**| How many whole days before today to replay. Today is not replayed. | [optional] [default to 30] |

### Return type

ApiResponse<[**AutomationBacktest**](AutomationBacktest.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Backtest |  -  |
| **400** | The automation is invalid, or holds something its kind cannot: &#x60;details.problems&#x60; lists each problem with its JSON path. A few ad rule checks (an unsupported platform, step or metric, a cooldown shorter than the schedule, approvers not on the team) answer with &#x60;param&#x60; instead. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ad rules only: your account has no ads access (code &#x60;ads_addon_required&#x60;). Ads are included on usage-based plans. Event and scheduled automations never get this 403: a boost step without ads access is refused with a 400 at its path. |  -  |
| **404** | Resource not found |  -  |


## backtestAutomationDraft

> AutomationBacktest backtestAutomationDraft(automationDefinition, days)

Backtest an unsaved automation

Replays an automation over past days on stored daily metrics, without saving it or changing anything. It refuses what saving would refuse.  Each day lists what it would have done. Its own changes carry into later days, but the metrics stay what really happened. &#x60;notes&#x60; says what the replay could not know.  Only ad automations can be backtested, on at most 5,000 ads. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        AutomationDefinition automationDefinition = new AutomationDefinition(); // AutomationDefinition | 
        Integer days = 30; // Integer | How many whole days before today to replay. Today is not replayed.
        try {
            AutomationBacktest result = apiInstance.backtestAutomationDraft(automationDefinition, days);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#backtestAutomationDraft");
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
| **automationDefinition** | [**AutomationDefinition**](AutomationDefinition.md)|  | |
| **days** | **Integer**| How many whole days before today to replay. Today is not replayed. | [optional] [default to 30] |

### Return type

[**AutomationBacktest**](AutomationBacktest.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Backtest |  -  |
| **400** | The automation is invalid, or holds something its kind cannot: &#x60;details.problems&#x60; lists each problem with its JSON path. A few ad rule checks (an unsupported platform, step or metric, a cooldown shorter than the schedule, approvers not on the team) answer with &#x60;param&#x60; instead. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ad rules only: your account has no ads access (code &#x60;ads_addon_required&#x60;). Ads are included on usage-based plans. Event and scheduled automations never get this 403: a boost step without ads access is refused with a 400 at its path. |  -  |

## backtestAutomationDraftWithHttpInfo

> ApiResponse<AutomationBacktest> backtestAutomationDraft backtestAutomationDraftWithHttpInfo(automationDefinition, days)

Backtest an unsaved automation

Replays an automation over past days on stored daily metrics, without saving it or changing anything. It refuses what saving would refuse.  Each day lists what it would have done. Its own changes carry into later days, but the metrics stay what really happened. &#x60;notes&#x60; says what the replay could not know.  Only ad automations can be backtested, on at most 5,000 ads. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        AutomationDefinition automationDefinition = new AutomationDefinition(); // AutomationDefinition | 
        Integer days = 30; // Integer | How many whole days before today to replay. Today is not replayed.
        try {
            ApiResponse<AutomationBacktest> response = apiInstance.backtestAutomationDraftWithHttpInfo(automationDefinition, days);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#backtestAutomationDraft");
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
| **automationDefinition** | [**AutomationDefinition**](AutomationDefinition.md)|  | |
| **days** | **Integer**| How many whole days before today to replay. Today is not replayed. | [optional] [default to 30] |

### Return type

ApiResponse<[**AutomationBacktest**](AutomationBacktest.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Backtest |  -  |
| **400** | The automation is invalid, or holds something its kind cannot: &#x60;details.problems&#x60; lists each problem with its JSON path. A few ad rule checks (an unsupported platform, step or metric, a cooldown shorter than the schedule, approvers not on the team) answer with &#x60;param&#x60; instead. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ad rules only: your account has no ads access (code &#x60;ads_addon_required&#x60;). Ads are included on usage-based plans. Event and scheduled automations never get this 403: a boost step without ads access is refused with a 400 at its path. |  -  |


## createAutomation

> CreateAutomation201Response createAutomation(automationDefinition, idempotencyKey)

Create an automation

Creates an automation. Its shape picks the kind:  - **Ad rule**: a &#x60;schedule&#x60; over campaigns, ad sets or ads, with metric &#x60;conditions&#x60; and ad &#x60;steps&#x60;. It stays paused unless &#x60;status&#x60; is &#x60;active&#x60;; preview it first with &#x60;POST /v1/automations/preview&#x60;. - **Event**: a Zernio event in &#x60;trigger.type&#x60;, such as &#x60;post.failed&#x60;, with notify steps. It is on unless &#x60;status&#x60; is &#x60;paused&#x60;. - **Scheduled**: a &#x60;schedule&#x60; over a profile&#39;s posts, with notify steps and an optional boost. It is on unless &#x60;status&#x60; is &#x60;paused&#x60;.  Everything an automation cannot hold is refused at once: the 400 lists every problem with its JSON path in &#x60;details.problems&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        AutomationDefinition automationDefinition = new AutomationDefinition(); // AutomationDefinition | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago. 
        try {
            CreateAutomation201Response result = apiInstance.createAutomation(automationDefinition, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#createAutomation");
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
| **automationDefinition** | [**AutomationDefinition**](AutomationDefinition.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago.  | [optional] |

### Return type

[**CreateAutomation201Response**](CreateAutomation201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Automation created |  -  |
| **400** | The automation is invalid, or holds something its kind cannot: &#x60;details.problems&#x60; lists each problem with its JSON path. A few ad rule checks (an unsupported platform, step or metric, a cooldown shorter than the schedule, approvers not on the team) answer with &#x60;param&#x60; instead. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ad rules only: no ads access (&#x60;ads_addon_required&#x60;), the ad account is not one the connection selected (&#x60;ad_account_not_selected&#x60;), or turning it on would raise live spend past the free ads allowance (&#x60;ads_allowance_exceeded&#x60;). |  -  |
| **409** | Same Idempotency-Key still processing; retry after a short backoff |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |

## createAutomationWithHttpInfo

> ApiResponse<CreateAutomation201Response> createAutomation createAutomationWithHttpInfo(automationDefinition, idempotencyKey)

Create an automation

Creates an automation. Its shape picks the kind:  - **Ad rule**: a &#x60;schedule&#x60; over campaigns, ad sets or ads, with metric &#x60;conditions&#x60; and ad &#x60;steps&#x60;. It stays paused unless &#x60;status&#x60; is &#x60;active&#x60;; preview it first with &#x60;POST /v1/automations/preview&#x60;. - **Event**: a Zernio event in &#x60;trigger.type&#x60;, such as &#x60;post.failed&#x60;, with notify steps. It is on unless &#x60;status&#x60; is &#x60;paused&#x60;. - **Scheduled**: a &#x60;schedule&#x60; over a profile&#39;s posts, with notify steps and an optional boost. It is on unless &#x60;status&#x60; is &#x60;paused&#x60;.  Everything an automation cannot hold is refused at once: the 400 lists every problem with its JSON path in &#x60;details.problems&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        AutomationDefinition automationDefinition = new AutomationDefinition(); // AutomationDefinition | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago. 
        try {
            ApiResponse<CreateAutomation201Response> response = apiInstance.createAutomationWithHttpInfo(automationDefinition, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#createAutomation");
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
| **automationDefinition** | [**AutomationDefinition**](AutomationDefinition.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago.  | [optional] |

### Return type

ApiResponse<[**CreateAutomation201Response**](CreateAutomation201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Automation created |  -  |
| **400** | The automation is invalid, or holds something its kind cannot: &#x60;details.problems&#x60; lists each problem with its JSON path. A few ad rule checks (an unsupported platform, step or metric, a cooldown shorter than the schedule, approvers not on the team) answer with &#x60;param&#x60; instead. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ad rules only: no ads access (&#x60;ads_addon_required&#x60;), the ad account is not one the connection selected (&#x60;ad_account_not_selected&#x60;), or turning it on would raise live spend past the free ads allowance (&#x60;ads_allowance_exceeded&#x60;). |  -  |
| **409** | Same Idempotency-Key still processing; retry after a short backoff |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |


## createAutomationTemplate

> CreateAutomationTemplate201Response createAutomationTemplate(createAutomationTemplateRequest, idempotencyKey)

Create an automation template

Saves a reusable setup of one or more automations (up to 20) that your team, or anyone you share it with, can install. Start from your own automations, one of Zernio&#39;s templates, a shared template, or definitions sent as they are.  Nothing tied to one account is kept. Ad accounts, a trigger&#39;s profile and accounts, and alert destinations become &#x60;inputs&#x60; that each install fills. Campaign ids, id filters, dates and approval steps are dropped.  From one of Zernio&#39;s templates, each threshold and budget or bid amount also becomes an input, with the template&#39;s own value as its default.  A template that would not install is refused: the 400 lists every problem in &#x60;details.problems&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        CreateAutomationTemplateRequest createAutomationTemplateRequest = new CreateAutomationTemplateRequest(); // CreateAutomationTemplateRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago. 
        try {
            CreateAutomationTemplate201Response result = apiInstance.createAutomationTemplate(createAutomationTemplateRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#createAutomationTemplate");
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
| **createAutomationTemplateRequest** | [**CreateAutomationTemplateRequest**](CreateAutomationTemplateRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago.  | [optional] |

### Return type

[**CreateAutomationTemplate201Response**](CreateAutomationTemplate201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Template created |  -  |
| **400** | The automation is invalid, or holds something its kind cannot: &#x60;details.problems&#x60; lists each problem with its JSON path. A few ad rule checks (an unsupported platform, step or metric, a cooldown shorter than the schedule, approvers not on the team) answer with &#x60;param&#x60; instead. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | An automation in &#x60;from.automationIds&#x60;, the Zernio template or the shared template was not found. |  -  |
| **409** | Your team already keeps 200 templates (code &#x60;automation_template_limit&#x60;); delete one to save another. Also returned when the same Idempotency-Key is still processing. |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |

## createAutomationTemplateWithHttpInfo

> ApiResponse<CreateAutomationTemplate201Response> createAutomationTemplate createAutomationTemplateWithHttpInfo(createAutomationTemplateRequest, idempotencyKey)

Create an automation template

Saves a reusable setup of one or more automations (up to 20) that your team, or anyone you share it with, can install. Start from your own automations, one of Zernio&#39;s templates, a shared template, or definitions sent as they are.  Nothing tied to one account is kept. Ad accounts, a trigger&#39;s profile and accounts, and alert destinations become &#x60;inputs&#x60; that each install fills. Campaign ids, id filters, dates and approval steps are dropped.  From one of Zernio&#39;s templates, each threshold and budget or bid amount also becomes an input, with the template&#39;s own value as its default.  A template that would not install is refused: the 400 lists every problem in &#x60;details.problems&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        CreateAutomationTemplateRequest createAutomationTemplateRequest = new CreateAutomationTemplateRequest(); // CreateAutomationTemplateRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago. 
        try {
            ApiResponse<CreateAutomationTemplate201Response> response = apiInstance.createAutomationTemplateWithHttpInfo(createAutomationTemplateRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#createAutomationTemplate");
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
| **createAutomationTemplateRequest** | [**CreateAutomationTemplateRequest**](CreateAutomationTemplateRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago.  | [optional] |

### Return type

ApiResponse<[**CreateAutomationTemplate201Response**](CreateAutomationTemplate201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Template created |  -  |
| **400** | The automation is invalid, or holds something its kind cannot: &#x60;details.problems&#x60; lists each problem with its JSON path. A few ad rule checks (an unsupported platform, step or metric, a cooldown shorter than the schedule, approvers not on the team) answer with &#x60;param&#x60; instead. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | An automation in &#x60;from.automationIds&#x60;, the Zernio template or the shared template was not found. |  -  |
| **409** | Your team already keeps 200 templates (code &#x60;automation_template_limit&#x60;); delete one to save another. Also returned when the same Idempotency-Key is still processing. |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |


## deleteAutomation

> UpdateYoutubeDefaultPlaylist200Response deleteAutomation(automationId)

Delete an automation

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        try {
            UpdateYoutubeDefaultPlaylist200Response result = apiInstance.deleteAutomation(automationId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#deleteAutomation");
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
| **automationId** | **String**|  | |

### Return type

[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Automation deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |

## deleteAutomationWithHttpInfo

> ApiResponse<UpdateYoutubeDefaultPlaylist200Response> deleteAutomation deleteAutomationWithHttpInfo(automationId)

Delete an automation

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        try {
            ApiResponse<UpdateYoutubeDefaultPlaylist200Response> response = apiInstance.deleteAutomationWithHttpInfo(automationId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#deleteAutomation");
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
| **automationId** | **String**|  | |

### Return type

ApiResponse<[**UpdateYoutubeDefaultPlaylist200Response**](UpdateYoutubeDefaultPlaylist200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Automation deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |


## deleteAutomationTemplate

> DeleteAutomationTemplate200Response deleteAutomationTemplate(templateId)

Delete an automation template

Deletes one of your team&#39;s templates and its share link. Automations already installed from it stay. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String templateId = "templateId_example"; // String | The template's id.
        try {
            DeleteAutomationTemplate200Response result = apiInstance.deleteAutomationTemplate(templateId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#deleteAutomationTemplate");
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
| **templateId** | **String**| The template&#39;s id. | |

### Return type

[**DeleteAutomationTemplate200Response**](DeleteAutomationTemplate200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Template deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | No template with this id in your team. |  -  |

## deleteAutomationTemplateWithHttpInfo

> ApiResponse<DeleteAutomationTemplate200Response> deleteAutomationTemplate deleteAutomationTemplateWithHttpInfo(templateId)

Delete an automation template

Deletes one of your team&#39;s templates and its share link. Automations already installed from it stay. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String templateId = "templateId_example"; // String | The template's id.
        try {
            ApiResponse<DeleteAutomationTemplate200Response> response = apiInstance.deleteAutomationTemplateWithHttpInfo(templateId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#deleteAutomationTemplate");
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
| **templateId** | **String**| The template&#39;s id. | |

### Return type

ApiResponse<[**DeleteAutomationTemplate200Response**](DeleteAutomationTemplate200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Template deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | No template with this id in your team. |  -  |


## getAutomation

> CreateAutomation201Response getAutomation(automationId)

Get an automation

An automation installed from a template also carries &#x60;template&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        try {
            CreateAutomation201Response result = apiInstance.getAutomation(automationId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#getAutomation");
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
| **automationId** | **String**|  | |

### Return type

[**CreateAutomation201Response**](CreateAutomation201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Automation |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |

## getAutomationWithHttpInfo

> ApiResponse<CreateAutomation201Response> getAutomation getAutomationWithHttpInfo(automationId)

Get an automation

An automation installed from a template also carries &#x60;template&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        try {
            ApiResponse<CreateAutomation201Response> response = apiInstance.getAutomationWithHttpInfo(automationId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#getAutomation");
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
| **automationId** | **String**|  | |

### Return type

ApiResponse<[**CreateAutomation201Response**](CreateAutomation201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Automation |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |


## getAutomationApproval

> GetAutomationApproval200Response getAutomationApproval(automationId, approvalId)

Get an approval request

One approval request with the changes it holds, who may decide it and whether you can.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        String approvalId = "approvalId_example"; // String | 
        try {
            GetAutomationApproval200Response result = apiInstance.getAutomationApproval(automationId, approvalId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#getAutomationApproval");
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
| **automationId** | **String**|  | |
| **approvalId** | **String**|  | |

### Return type

[**GetAutomationApproval200Response**](GetAutomationApproval200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Approval request |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **409** | Code &#x60;invalid_resource_state&#x60;: this automation never waits for approval. |  -  |

## getAutomationApprovalWithHttpInfo

> ApiResponse<GetAutomationApproval200Response> getAutomationApproval getAutomationApprovalWithHttpInfo(automationId, approvalId)

Get an approval request

One approval request with the changes it holds, who may decide it and whether you can.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        String approvalId = "approvalId_example"; // String | 
        try {
            ApiResponse<GetAutomationApproval200Response> response = apiInstance.getAutomationApprovalWithHttpInfo(automationId, approvalId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#getAutomationApproval");
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
| **automationId** | **String**|  | |
| **approvalId** | **String**|  | |

### Return type

ApiResponse<[**GetAutomationApproval200Response**](GetAutomationApproval200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Approval request |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **409** | Code &#x60;invalid_resource_state&#x60;: this automation never waits for approval. |  -  |


## getAutomationCatalog

> GetAutomationCatalog200Response getAutomationCatalog()

Get the automations catalog

What an automation can contain and where each part works, built from the same checks that validate a save, so it never offers what saving refuses.  - &#x60;schema&#x60;: the JSON Schema of the body of &#x60;POST /v1/automations&#x60;. - &#x60;triggers&#x60;: every trigger, tagged with its &#x60;kind&#x60;. Ad rule and scheduled triggers list their intervals; event triggers list each event with its facts. - The other sections describe ad rules: per subject (campaign, ad set, ad) its metrics and steps with the platforms that accept them, plus filters, groups, alerts, conditions, limits and approval. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        try {
            GetAutomationCatalog200Response result = apiInstance.getAutomationCatalog();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#getAutomationCatalog");
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

[**GetAutomationCatalog200Response**](GetAutomationCatalog200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Catalog |  * Cache-Control -  <br>  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |

## getAutomationCatalogWithHttpInfo

> ApiResponse<GetAutomationCatalog200Response> getAutomationCatalog getAutomationCatalogWithHttpInfo()

Get the automations catalog

What an automation can contain and where each part works, built from the same checks that validate a save, so it never offers what saving refuses.  - &#x60;schema&#x60;: the JSON Schema of the body of &#x60;POST /v1/automations&#x60;. - &#x60;triggers&#x60;: every trigger, tagged with its &#x60;kind&#x60;. Ad rule and scheduled triggers list their intervals; event triggers list each event with its facts. - The other sections describe ad rules: per subject (campaign, ad set, ad) its metrics and steps with the platforms that accept them, plus filters, groups, alerts, conditions, limits and approval. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        try {
            ApiResponse<GetAutomationCatalog200Response> response = apiInstance.getAutomationCatalogWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#getAutomationCatalog");
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

ApiResponse<[**GetAutomationCatalog200Response**](GetAutomationCatalog200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Catalog |  * Cache-Control -  <br>  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |


## getAutomationControls

> GetAutomationControls200Response getAutomationControls()

Get automation controls

The team&#39;s switch for every ad rule, and each ad account&#39;s own switch and daily raise limit. Boosting automations do not read them.  Every team member sees the same controls. &#x60;adAccounts&#x60; lists each ad account your automations use, plus any ad account that has controls set. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        try {
            GetAutomationControls200Response result = apiInstance.getAutomationControls();
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#getAutomationControls");
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

[**GetAutomationControls200Response**](GetAutomationControls200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Controls |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ad rules only: your account has no ads access (code &#x60;ads_addon_required&#x60;). Ads are included on usage-based plans. Event and scheduled automations never get this 403: a boost step without ads access is refused with a 400 at its path. |  -  |

## getAutomationControlsWithHttpInfo

> ApiResponse<GetAutomationControls200Response> getAutomationControls getAutomationControlsWithHttpInfo()

Get automation controls

The team&#39;s switch for every ad rule, and each ad account&#39;s own switch and daily raise limit. Boosting automations do not read them.  Every team member sees the same controls. &#x60;adAccounts&#x60; lists each ad account your automations use, plus any ad account that has controls set. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        try {
            ApiResponse<GetAutomationControls200Response> response = apiInstance.getAutomationControlsWithHttpInfo();
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#getAutomationControls");
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

ApiResponse<[**GetAutomationControls200Response**](GetAutomationControls200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Controls |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ad rules only: your account has no ads access (code &#x60;ads_addon_required&#x60;). Ads are included on usage-based plans. Event and scheduled automations never get this 403: a boost step without ads access is refused with a 400 at its path. |  -  |


## getAutomationTemplate

> CreateAutomationTemplate201Response getAutomationTemplate(templateId)

Get an automation template

Returns one of your team&#39;s templates, with its inputs and automations. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String templateId = "templateId_example"; // String | The template's id.
        try {
            CreateAutomationTemplate201Response result = apiInstance.getAutomationTemplate(templateId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#getAutomationTemplate");
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
| **templateId** | **String**| The template&#39;s id. | |

### Return type

[**CreateAutomationTemplate201Response**](CreateAutomationTemplate201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Template |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | No template with this id in your team. |  -  |

## getAutomationTemplateWithHttpInfo

> ApiResponse<CreateAutomationTemplate201Response> getAutomationTemplate getAutomationTemplateWithHttpInfo(templateId)

Get an automation template

Returns one of your team&#39;s templates, with its inputs and automations. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String templateId = "templateId_example"; // String | The template's id.
        try {
            ApiResponse<CreateAutomationTemplate201Response> response = apiInstance.getAutomationTemplateWithHttpInfo(templateId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#getAutomationTemplate");
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
| **templateId** | **String**| The template&#39;s id. | |

### Return type

ApiResponse<[**CreateAutomationTemplate201Response**](CreateAutomationTemplate201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Template |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | No template with this id in your team. |  -  |


## getSharedAutomationTemplate

> CreateAutomationTemplate201Response getSharedAutomationTemplate(shareToken)

Get a shared automation template

Returns a template shared by link, from any team. Who made it and its install counts in that team are left out, and &#x60;share&#x60; is null. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String shareToken = "shareToken_example"; // String | The token from the template's `share.token`.
        try {
            CreateAutomationTemplate201Response result = apiInstance.getSharedAutomationTemplate(shareToken);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#getSharedAutomationTemplate");
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
| **shareToken** | **String**| The token from the template&#39;s &#x60;share.token&#x60;. | |

### Return type

[**CreateAutomationTemplate201Response**](CreateAutomationTemplate201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Template |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | No template is shared with this token, or its link was turned off. |  -  |

## getSharedAutomationTemplateWithHttpInfo

> ApiResponse<CreateAutomationTemplate201Response> getSharedAutomationTemplate getSharedAutomationTemplateWithHttpInfo(shareToken)

Get a shared automation template

Returns a template shared by link, from any team. Who made it and its install counts in that team are left out, and &#x60;share&#x60; is null. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String shareToken = "shareToken_example"; // String | The token from the template's `share.token`.
        try {
            ApiResponse<CreateAutomationTemplate201Response> response = apiInstance.getSharedAutomationTemplateWithHttpInfo(shareToken);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#getSharedAutomationTemplate");
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
| **shareToken** | **String**| The token from the template&#39;s &#x60;share.token&#x60;. | |

### Return type

ApiResponse<[**CreateAutomationTemplate201Response**](CreateAutomationTemplate201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Template |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | No template is shared with this token, or its link was turned off. |  -  |


## getZernioAutomationTemplate

> CreateAutomationTemplate201Response getZernioAutomationTemplate(templateId)

Get a Zernio automation template

Returns one of Zernio&#39;s ready-made ad rule templates in the same shape as your own. Each threshold and budget or bid amount is an input with the template&#39;s own value as its default, so an install can change it or leave it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String templateId = "stop_losers"; // String | The id of one of Zernio's templates, for example `stop_losers`.
        try {
            CreateAutomationTemplate201Response result = apiInstance.getZernioAutomationTemplate(templateId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#getZernioAutomationTemplate");
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
| **templateId** | **String**| The id of one of Zernio&#39;s templates, for example &#x60;stop_losers&#x60;. | |

### Return type

[**CreateAutomationTemplate201Response**](CreateAutomationTemplate201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Template |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | No Zernio template with this id. |  -  |

## getZernioAutomationTemplateWithHttpInfo

> ApiResponse<CreateAutomationTemplate201Response> getZernioAutomationTemplate getZernioAutomationTemplateWithHttpInfo(templateId)

Get a Zernio automation template

Returns one of Zernio&#39;s ready-made ad rule templates in the same shape as your own. Each threshold and budget or bid amount is an input with the template&#39;s own value as its default, so an install can change it or leave it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String templateId = "stop_losers"; // String | The id of one of Zernio's templates, for example `stop_losers`.
        try {
            ApiResponse<CreateAutomationTemplate201Response> response = apiInstance.getZernioAutomationTemplateWithHttpInfo(templateId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#getZernioAutomationTemplate");
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
| **templateId** | **String**| The id of one of Zernio&#39;s templates, for example &#x60;stop_losers&#x60;. | |

### Return type

ApiResponse<[**CreateAutomationTemplate201Response**](CreateAutomationTemplate201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Template |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | No Zernio template with this id. |  -  |


## installAutomationTemplate

> AutomationTemplateInstallResponse installAutomationTemplate(templateId, automationTemplateInstallRequest, idempotencyKey)

Install an automation template

Creates every automation in the template, with your values in place of its inputs. All or nothing: if one automation fails, the ones already created are removed. New automations stay paused unless &#x60;status&#x60; is &#x60;active&#x60;.  To install on many ad accounts at once, send &#x60;targets&#x60; (up to 50). Each target is its own install with its own &#x60;inputs&#x60;, which win over the shared &#x60;inputs&#x60;. A failed target leaves the others in place, and the response is 207. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String templateId = "templateId_example"; // String | The template's id.
        AutomationTemplateInstallRequest automationTemplateInstallRequest = new AutomationTemplateInstallRequest(); // AutomationTemplateInstallRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago. 
        try {
            AutomationTemplateInstallResponse result = apiInstance.installAutomationTemplate(templateId, automationTemplateInstallRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#installAutomationTemplate");
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
| **templateId** | **String**| The template&#39;s id. | |
| **automationTemplateInstallRequest** | [**AutomationTemplateInstallRequest**](AutomationTemplateInstallRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago.  | [optional] |

### Return type

[**AutomationTemplateInstallResponse**](AutomationTemplateInstallResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Installed. &#x60;installation&#x60; for one install, &#x60;installations&#x60; when &#x60;targets&#x60; was sent and every target installed. |  -  |
| **207** | Some targets installed and some failed: check each &#x60;installations[].status&#x60;. |  -  |
| **400** | The request is invalid, or an input is missing, unknown or of the wrong type: &#x60;details.problems&#x60; lists each one at its path, such as &#x60;inputs.adAccount&#x60;.  When no target installed, the first target&#39;s error is returned with every target&#39;s result in &#x60;details.installations&#x60;. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ad rules only: your account has no ads access (code &#x60;ads_addon_required&#x60;). Ads are included on usage-based plans. Event and scheduled automations never get this 403: a boost step without ads access is refused with a 400 at its path. |  -  |
| **404** | No template with this id in your team. |  -  |
| **409** | Same Idempotency-Key still processing; retry after a short backoff |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |

## installAutomationTemplateWithHttpInfo

> ApiResponse<AutomationTemplateInstallResponse> installAutomationTemplate installAutomationTemplateWithHttpInfo(templateId, automationTemplateInstallRequest, idempotencyKey)

Install an automation template

Creates every automation in the template, with your values in place of its inputs. All or nothing: if one automation fails, the ones already created are removed. New automations stay paused unless &#x60;status&#x60; is &#x60;active&#x60;.  To install on many ad accounts at once, send &#x60;targets&#x60; (up to 50). Each target is its own install with its own &#x60;inputs&#x60;, which win over the shared &#x60;inputs&#x60;. A failed target leaves the others in place, and the response is 207. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String templateId = "templateId_example"; // String | The template's id.
        AutomationTemplateInstallRequest automationTemplateInstallRequest = new AutomationTemplateInstallRequest(); // AutomationTemplateInstallRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago. 
        try {
            ApiResponse<AutomationTemplateInstallResponse> response = apiInstance.installAutomationTemplateWithHttpInfo(templateId, automationTemplateInstallRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#installAutomationTemplate");
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
| **templateId** | **String**| The template&#39;s id. | |
| **automationTemplateInstallRequest** | [**AutomationTemplateInstallRequest**](AutomationTemplateInstallRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago.  | [optional] |

### Return type

ApiResponse<[**AutomationTemplateInstallResponse**](AutomationTemplateInstallResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Installed. &#x60;installation&#x60; for one install, &#x60;installations&#x60; when &#x60;targets&#x60; was sent and every target installed. |  -  |
| **207** | Some targets installed and some failed: check each &#x60;installations[].status&#x60;. |  -  |
| **400** | The request is invalid, or an input is missing, unknown or of the wrong type: &#x60;details.problems&#x60; lists each one at its path, such as &#x60;inputs.adAccount&#x60;.  When no target installed, the first target&#39;s error is returned with every target&#39;s result in &#x60;details.installations&#x60;. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ad rules only: your account has no ads access (code &#x60;ads_addon_required&#x60;). Ads are included on usage-based plans. Event and scheduled automations never get this 403: a boost step without ads access is refused with a 400 at its path. |  -  |
| **404** | No template with this id in your team. |  -  |
| **409** | Same Idempotency-Key still processing; retry after a short backoff |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |


## installSharedAutomationTemplate

> AutomationTemplateInstallResponse installSharedAutomationTemplate(shareToken, automationTemplateInstallRequest, idempotencyKey)

Install a shared automation template

Installs a template shared by link into your account, the same way as your own templates.  To install on many ad accounts at once, send &#x60;targets&#x60; (up to 50). Each target is its own install with its own &#x60;inputs&#x60;, which win over the shared &#x60;inputs&#x60;. A failed target leaves the others in place, and the response is 207. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String shareToken = "shareToken_example"; // String | The token from the template's `share.token`.
        AutomationTemplateInstallRequest automationTemplateInstallRequest = new AutomationTemplateInstallRequest(); // AutomationTemplateInstallRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago. 
        try {
            AutomationTemplateInstallResponse result = apiInstance.installSharedAutomationTemplate(shareToken, automationTemplateInstallRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#installSharedAutomationTemplate");
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
| **shareToken** | **String**| The token from the template&#39;s &#x60;share.token&#x60;. | |
| **automationTemplateInstallRequest** | [**AutomationTemplateInstallRequest**](AutomationTemplateInstallRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago.  | [optional] |

### Return type

[**AutomationTemplateInstallResponse**](AutomationTemplateInstallResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Installed. &#x60;installation&#x60; for one install, &#x60;installations&#x60; when &#x60;targets&#x60; was sent and every target installed. |  -  |
| **207** | Some targets installed and some failed: check each &#x60;installations[].status&#x60;. |  -  |
| **400** | The request is invalid, or an input is missing, unknown or of the wrong type: &#x60;details.problems&#x60; lists each one at its path, such as &#x60;inputs.adAccount&#x60;.  When no target installed, the first target&#39;s error is returned with every target&#39;s result in &#x60;details.installations&#x60;. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ad rules only: your account has no ads access (code &#x60;ads_addon_required&#x60;). Ads are included on usage-based plans. Event and scheduled automations never get this 403: a boost step without ads access is refused with a 400 at its path. |  -  |
| **404** | No template is shared with this token, or its link was turned off. |  -  |
| **409** | Same Idempotency-Key still processing; retry after a short backoff |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |

## installSharedAutomationTemplateWithHttpInfo

> ApiResponse<AutomationTemplateInstallResponse> installSharedAutomationTemplate installSharedAutomationTemplateWithHttpInfo(shareToken, automationTemplateInstallRequest, idempotencyKey)

Install a shared automation template

Installs a template shared by link into your account, the same way as your own templates.  To install on many ad accounts at once, send &#x60;targets&#x60; (up to 50). Each target is its own install with its own &#x60;inputs&#x60;, which win over the shared &#x60;inputs&#x60;. A failed target leaves the others in place, and the response is 207. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String shareToken = "shareToken_example"; // String | The token from the template's `share.token`.
        AutomationTemplateInstallRequest automationTemplateInstallRequest = new AutomationTemplateInstallRequest(); // AutomationTemplateInstallRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago. 
        try {
            ApiResponse<AutomationTemplateInstallResponse> response = apiInstance.installSharedAutomationTemplateWithHttpInfo(shareToken, automationTemplateInstallRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#installSharedAutomationTemplate");
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
| **shareToken** | **String**| The token from the template&#39;s &#x60;share.token&#x60;. | |
| **automationTemplateInstallRequest** | [**AutomationTemplateInstallRequest**](AutomationTemplateInstallRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago.  | [optional] |

### Return type

ApiResponse<[**AutomationTemplateInstallResponse**](AutomationTemplateInstallResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Installed. &#x60;installation&#x60; for one install, &#x60;installations&#x60; when &#x60;targets&#x60; was sent and every target installed. |  -  |
| **207** | Some targets installed and some failed: check each &#x60;installations[].status&#x60;. |  -  |
| **400** | The request is invalid, or an input is missing, unknown or of the wrong type: &#x60;details.problems&#x60; lists each one at its path, such as &#x60;inputs.adAccount&#x60;.  When no target installed, the first target&#39;s error is returned with every target&#39;s result in &#x60;details.installations&#x60;. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ad rules only: your account has no ads access (code &#x60;ads_addon_required&#x60;). Ads are included on usage-based plans. Event and scheduled automations never get this 403: a boost step without ads access is refused with a 400 at its path. |  -  |
| **404** | No template is shared with this token, or its link was turned off. |  -  |
| **409** | Same Idempotency-Key still processing; retry after a short backoff |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |


## installZernioAutomationTemplate

> AutomationTemplateInstallResponse installZernioAutomationTemplate(templateId, automationTemplateInstallRequest, idempotencyKey)

Install a Zernio automation template

Installs one of Zernio&#39;s ready-made templates. Leave a value input out to keep the template&#39;s default.  To install on many ad accounts at once, send &#x60;targets&#x60; (up to 50). Each target is its own install with its own &#x60;inputs&#x60;, which win over the shared &#x60;inputs&#x60;. A failed target leaves the others in place, and the response is 207. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String templateId = "stop_losers"; // String | The id of one of Zernio's templates, for example `stop_losers`.
        AutomationTemplateInstallRequest automationTemplateInstallRequest = new AutomationTemplateInstallRequest(); // AutomationTemplateInstallRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago. 
        try {
            AutomationTemplateInstallResponse result = apiInstance.installZernioAutomationTemplate(templateId, automationTemplateInstallRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#installZernioAutomationTemplate");
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
| **templateId** | **String**| The id of one of Zernio&#39;s templates, for example &#x60;stop_losers&#x60;. | |
| **automationTemplateInstallRequest** | [**AutomationTemplateInstallRequest**](AutomationTemplateInstallRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago.  | [optional] |

### Return type

[**AutomationTemplateInstallResponse**](AutomationTemplateInstallResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Installed. &#x60;installation&#x60; for one install, &#x60;installations&#x60; when &#x60;targets&#x60; was sent and every target installed. |  -  |
| **207** | Some targets installed and some failed: check each &#x60;installations[].status&#x60;. |  -  |
| **400** | The request is invalid, or an input is missing, unknown or of the wrong type: &#x60;details.problems&#x60; lists each one at its path, such as &#x60;inputs.adAccount&#x60;.  When no target installed, the first target&#39;s error is returned with every target&#39;s result in &#x60;details.installations&#x60;. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ad rules only: your account has no ads access (code &#x60;ads_addon_required&#x60;). Ads are included on usage-based plans. Event and scheduled automations never get this 403: a boost step without ads access is refused with a 400 at its path. |  -  |
| **404** | No Zernio template with this id. |  -  |
| **409** | Same Idempotency-Key still processing; retry after a short backoff |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |

## installZernioAutomationTemplateWithHttpInfo

> ApiResponse<AutomationTemplateInstallResponse> installZernioAutomationTemplate installZernioAutomationTemplateWithHttpInfo(templateId, automationTemplateInstallRequest, idempotencyKey)

Install a Zernio automation template

Installs one of Zernio&#39;s ready-made templates. Leave a value input out to keep the template&#39;s default.  To install on many ad accounts at once, send &#x60;targets&#x60; (up to 50). Each target is its own install with its own &#x60;inputs&#x60;, which win over the shared &#x60;inputs&#x60;. A failed target leaves the others in place, and the response is 207. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String templateId = "stop_losers"; // String | The id of one of Zernio's templates, for example `stop_losers`.
        AutomationTemplateInstallRequest automationTemplateInstallRequest = new AutomationTemplateInstallRequest(); // AutomationTemplateInstallRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago. 
        try {
            ApiResponse<AutomationTemplateInstallResponse> response = apiInstance.installZernioAutomationTemplateWithHttpInfo(templateId, automationTemplateInstallRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#installZernioAutomationTemplate");
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
| **templateId** | **String**| The id of one of Zernio&#39;s templates, for example &#x60;stop_losers&#x60;. | |
| **automationTemplateInstallRequest** | [**AutomationTemplateInstallRequest**](AutomationTemplateInstallRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  On the Ads create, boost and duplicate endpoints, a same-body retry runs again once the cut-off request started more than 15 minutes ago.  | [optional] |

### Return type

ApiResponse<[**AutomationTemplateInstallResponse**](AutomationTemplateInstallResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Installed. &#x60;installation&#x60; for one install, &#x60;installations&#x60; when &#x60;targets&#x60; was sent and every target installed. |  -  |
| **207** | Some targets installed and some failed: check each &#x60;installations[].status&#x60;. |  -  |
| **400** | The request is invalid, or an input is missing, unknown or of the wrong type: &#x60;details.problems&#x60; lists each one at its path, such as &#x60;inputs.adAccount&#x60;.  When no target installed, the first target&#39;s error is returned with every target&#39;s result in &#x60;details.installations&#x60;. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ad rules only: your account has no ads access (code &#x60;ads_addon_required&#x60;). Ads are included on usage-based plans. Event and scheduled automations never get this 403: a boost step without ads access is refused with a 400 at its path. |  -  |
| **404** | No Zernio template with this id. |  -  |
| **409** | Same Idempotency-Key still processing; retry after a short backoff |  -  |
| **422** | Idempotency-Key reused with a different request |  -  |


## listAutomationActions

> ListAutomationActions200Response listAutomationActions(automationId, accountId, type, from, to, limit, cursor)

List automation actions

Every change your ad rules made, newest first: what changed, the value before and after, and whether it was applied, skipped or failed. What event and scheduled automations did is in each one&#39;s checks. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        String accountId = "accountId_example"; // String | Only actions on this ads connection.
        String type = "ads.pause"; // String | A change reads as the value it set, so budget changes filter as `ads.set_budget`.
        OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | 
        OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | 
        Integer limit = 50; // Integer | 
        String cursor = "cursor_example"; // String | `nextCursor` from the previous page.
        try {
            ListAutomationActions200Response result = apiInstance.listAutomationActions(automationId, accountId, type, from, to, limit, cursor);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#listAutomationActions");
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
| **automationId** | **String**|  | [optional] |
| **accountId** | **String**| Only actions on this ads connection. | [optional] |
| **type** | **String**| A change reads as the value it set, so budget changes filter as &#x60;ads.set_budget&#x60;. | [optional] [enum: ads.pause, ads.activate, ads.set_budget, ads.duplicate, ads.edit_name, ads.set_bid, ads.set_target, ads.reallocate_budget] |
| **from** | **OffsetDateTime**|  | [optional] |
| **to** | **OffsetDateTime**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **cursor** | **String**| &#x60;nextCursor&#x60; from the previous page. | [optional] |

### Return type

[**ListAutomationActions200Response**](ListAutomationActions200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Actions |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |

## listAutomationActionsWithHttpInfo

> ApiResponse<ListAutomationActions200Response> listAutomationActions listAutomationActionsWithHttpInfo(automationId, accountId, type, from, to, limit, cursor)

List automation actions

Every change your ad rules made, newest first: what changed, the value before and after, and whether it was applied, skipped or failed. What event and scheduled automations did is in each one&#39;s checks. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        String accountId = "accountId_example"; // String | Only actions on this ads connection.
        String type = "ads.pause"; // String | A change reads as the value it set, so budget changes filter as `ads.set_budget`.
        OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | 
        OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | 
        Integer limit = 50; // Integer | 
        String cursor = "cursor_example"; // String | `nextCursor` from the previous page.
        try {
            ApiResponse<ListAutomationActions200Response> response = apiInstance.listAutomationActionsWithHttpInfo(automationId, accountId, type, from, to, limit, cursor);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#listAutomationActions");
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
| **automationId** | **String**|  | [optional] |
| **accountId** | **String**| Only actions on this ads connection. | [optional] |
| **type** | **String**| A change reads as the value it set, so budget changes filter as &#x60;ads.set_budget&#x60;. | [optional] [enum: ads.pause, ads.activate, ads.set_budget, ads.duplicate, ads.edit_name, ads.set_bid, ads.set_target, ads.reallocate_budget] |
| **from** | **OffsetDateTime**|  | [optional] |
| **to** | **OffsetDateTime**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **cursor** | **String**| &#x60;nextCursor&#x60; from the previous page. | [optional] |

### Return type

ApiResponse<[**ListAutomationActions200Response**](ListAutomationActions200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Actions |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |


## listAutomationApprovals

> ListAutomationApprovals200Response listAutomationApprovals(automationId, status, limit)

List an automation&#39;s approval requests

The requests an automation sent for a person&#39;s approval before acting, newest first. Each lists the changes it holds, who may decide it and until when.  Only automations that ask for approval have requests. Others return 409. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        String status = "pending"; // String | Only requests in this status.
        Integer limit = 20; // Integer | How many requests to return. There is no cursor; the newest come first.
        try {
            ListAutomationApprovals200Response result = apiInstance.listAutomationApprovals(automationId, status, limit);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#listAutomationApprovals");
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
| **automationId** | **String**|  | |
| **status** | **String**| Only requests in this status. | [optional] [enum: pending, approved, rejected, expired, cancelled] |
| **limit** | **Integer**| How many requests to return. There is no cursor; the newest come first. | [optional] [default to 20] |

### Return type

[**ListAutomationApprovals200Response**](ListAutomationApprovals200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Approval requests |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **409** | Code &#x60;invalid_resource_state&#x60;: this automation never waits for approval. |  -  |

## listAutomationApprovalsWithHttpInfo

> ApiResponse<ListAutomationApprovals200Response> listAutomationApprovals listAutomationApprovalsWithHttpInfo(automationId, status, limit)

List an automation&#39;s approval requests

The requests an automation sent for a person&#39;s approval before acting, newest first. Each lists the changes it holds, who may decide it and until when.  Only automations that ask for approval have requests. Others return 409. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        String status = "pending"; // String | Only requests in this status.
        Integer limit = 20; // Integer | How many requests to return. There is no cursor; the newest come first.
        try {
            ApiResponse<ListAutomationApprovals200Response> response = apiInstance.listAutomationApprovalsWithHttpInfo(automationId, status, limit);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#listAutomationApprovals");
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
| **automationId** | **String**|  | |
| **status** | **String**| Only requests in this status. | [optional] [enum: pending, approved, rejected, expired, cancelled] |
| **limit** | **Integer**| How many requests to return. There is no cursor; the newest come first. | [optional] [default to 20] |

### Return type

ApiResponse<[**ListAutomationApprovals200Response**](ListAutomationApprovals200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Approval requests |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **409** | Code &#x60;invalid_resource_state&#x60;: this automation never waits for approval. |  -  |


## listAutomationChecks

> ListAutomationChecks200Response listAutomationChecks(automationId, limit, cursor)

List an automation&#39;s checks

Each time the automation ran, newest first, with what matched and what it did. For an event automation, each check is one event that reached it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        Integer limit = 20; // Integer | 
        String cursor = "cursor_example"; // String | `nextCursor` from the previous page.
        try {
            ListAutomationChecks200Response result = apiInstance.listAutomationChecks(automationId, limit, cursor);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#listAutomationChecks");
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
| **automationId** | **String**|  | |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **cursor** | **String**| &#x60;nextCursor&#x60; from the previous page. | [optional] |

### Return type

[**ListAutomationChecks200Response**](ListAutomationChecks200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Checks |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |

## listAutomationChecksWithHttpInfo

> ApiResponse<ListAutomationChecks200Response> listAutomationChecks listAutomationChecksWithHttpInfo(automationId, limit, cursor)

List an automation&#39;s checks

Each time the automation ran, newest first, with what matched and what it did. For an event automation, each check is one event that reached it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        Integer limit = 20; // Integer | 
        String cursor = "cursor_example"; // String | `nextCursor` from the previous page.
        try {
            ApiResponse<ListAutomationChecks200Response> response = apiInstance.listAutomationChecksWithHttpInfo(automationId, limit, cursor);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#listAutomationChecks");
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
| **automationId** | **String**|  | |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **cursor** | **String**| &#x60;nextCursor&#x60; from the previous page. | [optional] |

### Return type

ApiResponse<[**ListAutomationChecks200Response**](ListAutomationChecks200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Checks |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |


## listAutomationTemplates

> ListAutomationTemplates200Response listAutomationTemplates(scope)

List automation templates

Lists your team&#39;s templates, newest first. Every team member sees the templates any member saved. A team keeps up to 200. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String scope = "team"; // String | Which templates to list. Only `team` today.
        try {
            ListAutomationTemplates200Response result = apiInstance.listAutomationTemplates(scope);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#listAutomationTemplates");
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
| **scope** | **String**| Which templates to list. Only &#x60;team&#x60; today. | [optional] [default to team] [enum: team] |

### Return type

[**ListAutomationTemplates200Response**](ListAutomationTemplates200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Templates |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |

## listAutomationTemplatesWithHttpInfo

> ApiResponse<ListAutomationTemplates200Response> listAutomationTemplates listAutomationTemplatesWithHttpInfo(scope)

List automation templates

Lists your team&#39;s templates, newest first. Every team member sees the templates any member saved. A team keeps up to 200. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String scope = "team"; // String | Which templates to list. Only `team` today.
        try {
            ApiResponse<ListAutomationTemplates200Response> response = apiInstance.listAutomationTemplatesWithHttpInfo(scope);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#listAutomationTemplates");
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
| **scope** | **String**| Which templates to list. Only &#x60;team&#x60; today. | [optional] [default to team] [enum: team] |

### Return type

ApiResponse<[**ListAutomationTemplates200Response**](ListAutomationTemplates200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Templates |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |


## listAutomations

> ListAutomations200Response listAutomations(accountId, adAccountId, limit, cursor)

List automations

Lists the automations on the profiles your key can reach, newest first, across every kind: ad rules, event automations and scheduled automations. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String accountId = "accountId_example"; // String | Only automations on this account: the ads connection of an ad rule, or one of the `accountIds` of an event or scheduled automation.
        String adAccountId = "adAccountId_example"; // String | Only ad rules checking this platform ad account.
        Integer limit = 50; // Integer | 
        String cursor = "cursor_example"; // String | `nextCursor` from the previous page.
        try {
            ListAutomations200Response result = apiInstance.listAutomations(accountId, adAccountId, limit, cursor);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#listAutomations");
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
| **accountId** | **String**| Only automations on this account: the ads connection of an ad rule, or one of the &#x60;accountIds&#x60; of an event or scheduled automation. | [optional] |
| **adAccountId** | **String**| Only ad rules checking this platform ad account. | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **cursor** | **String**| &#x60;nextCursor&#x60; from the previous page. | [optional] |

### Return type

[**ListAutomations200Response**](ListAutomations200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Automations |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |

## listAutomationsWithHttpInfo

> ApiResponse<ListAutomations200Response> listAutomations listAutomationsWithHttpInfo(accountId, adAccountId, limit, cursor)

List automations

Lists the automations on the profiles your key can reach, newest first, across every kind: ad rules, event automations and scheduled automations. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String accountId = "accountId_example"; // String | Only automations on this account: the ads connection of an ad rule, or one of the `accountIds` of an event or scheduled automation.
        String adAccountId = "adAccountId_example"; // String | Only ad rules checking this platform ad account.
        Integer limit = 50; // Integer | 
        String cursor = "cursor_example"; // String | `nextCursor` from the previous page.
        try {
            ApiResponse<ListAutomations200Response> response = apiInstance.listAutomationsWithHttpInfo(accountId, adAccountId, limit, cursor);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#listAutomations");
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
| **accountId** | **String**| Only automations on this account: the ads connection of an ad rule, or one of the &#x60;accountIds&#x60; of an event or scheduled automation. | [optional] |
| **adAccountId** | **String**| Only ad rules checking this platform ad account. | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **cursor** | **String**| &#x60;nextCursor&#x60; from the previous page. | [optional] |

### Return type

ApiResponse<[**ListAutomations200Response**](ListAutomations200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Automations |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |


## pauseAutomation

> CreateAutomation201Response pauseAutomation(automationId)

Turn an automation off

Pausing never needs ads access.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        try {
            CreateAutomation201Response result = apiInstance.pauseAutomation(automationId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#pauseAutomation");
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
| **automationId** | **String**|  | |

### Return type

[**CreateAutomation201Response**](CreateAutomation201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Automation off |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |

## pauseAutomationWithHttpInfo

> ApiResponse<CreateAutomation201Response> pauseAutomation pauseAutomationWithHttpInfo(automationId)

Turn an automation off

Pausing never needs ads access.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        try {
            ApiResponse<CreateAutomation201Response> response = apiInstance.pauseAutomationWithHttpInfo(automationId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#pauseAutomation");
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
| **automationId** | **String**|  | |

### Return type

ApiResponse<[**CreateAutomation201Response**](CreateAutomation201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Automation off |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |


## previewAutomation

> AutomationPreview previewAutomation(automationId, limit)

Preview a saved automation

Shows what an ad rule would do if it ran now. Nothing is changed. Event and scheduled automations cannot be previewed yet (400, &#x60;not_supported&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        Integer limit = 100; // Integer | How many subjects to list, matches first. `evaluated` and `matched` always count them all.
        try {
            AutomationPreview result = apiInstance.previewAutomation(automationId, limit);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#previewAutomation");
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
| **automationId** | **String**|  | |
| **limit** | **Integer**| How many subjects to list, matches first. &#x60;evaluated&#x60; and &#x60;matched&#x60; always count them all. | [optional] [default to 100] |

### Return type

[**AutomationPreview**](AutomationPreview.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Preview |  -  |
| **400** | The automation is invalid, or holds something its kind cannot: &#x60;details.problems&#x60; lists each problem with its JSON path. A few ad rule checks (an unsupported platform, step or metric, a cooldown shorter than the schedule, approvers not on the team) answer with &#x60;param&#x60; instead. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ad rules only: your account has no ads access (code &#x60;ads_addon_required&#x60;). Ads are included on usage-based plans. Event and scheduled automations never get this 403: a boost step without ads access is refused with a 400 at its path. |  -  |
| **404** | Resource not found |  -  |

## previewAutomationWithHttpInfo

> ApiResponse<AutomationPreview> previewAutomation previewAutomationWithHttpInfo(automationId, limit)

Preview a saved automation

Shows what an ad rule would do if it ran now. Nothing is changed. Event and scheduled automations cannot be previewed yet (400, &#x60;not_supported&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        Integer limit = 100; // Integer | How many subjects to list, matches first. `evaluated` and `matched` always count them all.
        try {
            ApiResponse<AutomationPreview> response = apiInstance.previewAutomationWithHttpInfo(automationId, limit);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#previewAutomation");
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
| **automationId** | **String**|  | |
| **limit** | **Integer**| How many subjects to list, matches first. &#x60;evaluated&#x60; and &#x60;matched&#x60; always count them all. | [optional] [default to 100] |

### Return type

ApiResponse<[**AutomationPreview**](AutomationPreview.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Preview |  -  |
| **400** | The automation is invalid, or holds something its kind cannot: &#x60;details.problems&#x60; lists each problem with its JSON path. A few ad rule checks (an unsupported platform, step or metric, a cooldown shorter than the schedule, approvers not on the team) answer with &#x60;param&#x60; instead. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ad rules only: your account has no ads access (code &#x60;ads_addon_required&#x60;). Ads are included on usage-based plans. Event and scheduled automations never get this 403: a boost step without ads access is refused with a 400 at its path. |  -  |
| **404** | Resource not found |  -  |


## previewAutomationDraft

> AutomationPreview previewAutomationDraft(automationDefinition, limit)

Preview an unsaved automation

Shows what an ad rule would do if it ran now, without saving it or changing anything: every object it checks, each condition with its actual value, and the steps a match would run. It refuses what saving would refuse.  Event and scheduled automations cannot be previewed yet (400, &#x60;not_supported&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        AutomationDefinition automationDefinition = new AutomationDefinition(); // AutomationDefinition | 
        Integer limit = 100; // Integer | How many subjects to list, matches first. `evaluated` and `matched` always count them all.
        try {
            AutomationPreview result = apiInstance.previewAutomationDraft(automationDefinition, limit);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#previewAutomationDraft");
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
| **automationDefinition** | [**AutomationDefinition**](AutomationDefinition.md)|  | |
| **limit** | **Integer**| How many subjects to list, matches first. &#x60;evaluated&#x60; and &#x60;matched&#x60; always count them all. | [optional] [default to 100] |

### Return type

[**AutomationPreview**](AutomationPreview.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Preview |  -  |
| **400** | The automation is invalid, or holds something its kind cannot: &#x60;details.problems&#x60; lists each problem with its JSON path. A few ad rule checks (an unsupported platform, step or metric, a cooldown shorter than the schedule, approvers not on the team) answer with &#x60;param&#x60; instead. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ad rules only: your account has no ads access (code &#x60;ads_addon_required&#x60;). Ads are included on usage-based plans. Event and scheduled automations never get this 403: a boost step without ads access is refused with a 400 at its path. |  -  |

## previewAutomationDraftWithHttpInfo

> ApiResponse<AutomationPreview> previewAutomationDraft previewAutomationDraftWithHttpInfo(automationDefinition, limit)

Preview an unsaved automation

Shows what an ad rule would do if it ran now, without saving it or changing anything: every object it checks, each condition with its actual value, and the steps a match would run. It refuses what saving would refuse.  Event and scheduled automations cannot be previewed yet (400, &#x60;not_supported&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        AutomationDefinition automationDefinition = new AutomationDefinition(); // AutomationDefinition | 
        Integer limit = 100; // Integer | How many subjects to list, matches first. `evaluated` and `matched` always count them all.
        try {
            ApiResponse<AutomationPreview> response = apiInstance.previewAutomationDraftWithHttpInfo(automationDefinition, limit);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#previewAutomationDraft");
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
| **automationDefinition** | [**AutomationDefinition**](AutomationDefinition.md)|  | |
| **limit** | **Integer**| How many subjects to list, matches first. &#x60;evaluated&#x60; and &#x60;matched&#x60; always count them all. | [optional] [default to 100] |

### Return type

ApiResponse<[**AutomationPreview**](AutomationPreview.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Preview |  -  |
| **400** | The automation is invalid, or holds something its kind cannot: &#x60;details.problems&#x60; lists each problem with its JSON path. A few ad rule checks (an unsupported platform, step or metric, a cooldown shorter than the schedule, approvers not on the team) answer with &#x60;param&#x60; instead. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ad rules only: your account has no ads access (code &#x60;ads_addon_required&#x60;). Ads are included on usage-based plans. Event and scheduled automations never get this 403: a boost step without ads access is refused with a 400 at its path. |  -  |


## rejectAutomationApproval

> GetAutomationApproval200Response rejectAutomationApproval(automationId, approvalId, automationApprovalDecision)

Reject an approval request

Rejects a pending request: every change it holds is skipped and nothing is changed on the ad account.  Only the approvers the automation names now can decide, matched by the email of the user behind the API key. Rejecting needs no ads access, like pausing. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        String approvalId = "approvalId_example"; // String | 
        AutomationApprovalDecision automationApprovalDecision = new AutomationApprovalDecision(); // AutomationApprovalDecision | 
        try {
            GetAutomationApproval200Response result = apiInstance.rejectAutomationApproval(automationId, approvalId, automationApprovalDecision);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#rejectAutomationApproval");
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
| **automationId** | **String**|  | |
| **approvalId** | **String**|  | |
| **automationApprovalDecision** | [**AutomationApprovalDecision**](AutomationApprovalDecision.md)|  | [optional] |

### Return type

[**GetAutomationApproval200Response**](GetAutomationApproval200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request after the decision |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;insufficient_permissions&#x60;: you are not one of the approvers, or &#x60;token&#x60; was sent to someone else. |  -  |
| **404** | Resource not found |  -  |
| **409** | Code &#x60;invalid_resource_state&#x60;. Nothing was changed. The request was already approved or rejected, it expired, or it was cancelled when the automation stopped asking for approval.  Also returned when the automation no longer asks for approval or never does, and when it is acting on the ad account right now (try again in a minute).  |  -  |

## rejectAutomationApprovalWithHttpInfo

> ApiResponse<GetAutomationApproval200Response> rejectAutomationApproval rejectAutomationApprovalWithHttpInfo(automationId, approvalId, automationApprovalDecision)

Reject an approval request

Rejects a pending request: every change it holds is skipped and nothing is changed on the ad account.  Only the approvers the automation names now can decide, matched by the email of the user behind the API key. Rejecting needs no ads access, like pausing. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        String approvalId = "approvalId_example"; // String | 
        AutomationApprovalDecision automationApprovalDecision = new AutomationApprovalDecision(); // AutomationApprovalDecision | 
        try {
            ApiResponse<GetAutomationApproval200Response> response = apiInstance.rejectAutomationApprovalWithHttpInfo(automationId, approvalId, automationApprovalDecision);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#rejectAutomationApproval");
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
| **automationId** | **String**|  | |
| **approvalId** | **String**|  | |
| **automationApprovalDecision** | [**AutomationApprovalDecision**](AutomationApprovalDecision.md)|  | [optional] |

### Return type

ApiResponse<[**GetAutomationApproval200Response**](GetAutomationApproval200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request after the decision |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;insufficient_permissions&#x60;: you are not one of the approvers, or &#x60;token&#x60; was sent to someone else. |  -  |
| **404** | Resource not found |  -  |
| **409** | Code &#x60;invalid_resource_state&#x60;. Nothing was changed. The request was already approved or rejected, it expired, or it was cancelled when the automation stopped asking for approval.  Also returned when the automation no longer asks for approval or never does, and when it is acting on the ad account right now (try again in a minute).  |  -  |


## updateAutomation

> CreateAutomation201Response updateAutomation(automationId, updateAutomationRequest, ifMatch)

Edit an automation

Replaces the top-level fields you send and keeps the rest: to change one step, send all of &#x60;steps&#x60;. The result is checked as a whole automation, so problems carry the same paths as on create.  An automation keeps its kind, and an ad rule stays on its ad account. Send &#x60;alert: null&#x60; to remove an ad rule&#39;s alert.  Send the &#x60;version&#x60; you read as &#x60;If-Match&#x60;: if the automation was saved since, the edit is refused with a 409 (&#x60;automation_stale&#x60;). An edit is also refused with a 409 when another save lands while it is being applied. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        UpdateAutomationRequest updateAutomationRequest = new UpdateAutomationRequest(); // UpdateAutomationRequest | 
        String ifMatch = "ifMatch_example"; // String | The automation's `version` when you read it.
        try {
            CreateAutomation201Response result = apiInstance.updateAutomation(automationId, updateAutomationRequest, ifMatch);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#updateAutomation");
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
| **automationId** | **String**|  | |
| **updateAutomationRequest** | [**UpdateAutomationRequest**](UpdateAutomationRequest.md)|  | |
| **ifMatch** | **String**| The automation&#39;s &#x60;version&#x60; when you read it. | [optional] |

### Return type

[**CreateAutomation201Response**](CreateAutomation201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Automation updated |  -  |
| **400** | The automation is invalid, or holds something its kind cannot: &#x60;details.problems&#x60; lists each problem with its JSON path. A few ad rule checks (an unsupported platform, step or metric, a cooldown shorter than the schedule, approvers not on the team) answer with &#x60;param&#x60; instead. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ad rules only: your account has no ads access (code &#x60;ads_addon_required&#x60;). Ads are included on usage-based plans. Event and scheduled automations never get this 403: a boost step without ads access is refused with a 400 at its path. |  -  |
| **404** | Resource not found |  -  |
| **409** | The automation was saved after the &#x60;version&#x60; in &#x60;If-Match&#x60; (code &#x60;automation_stale&#x60;). &#x60;details.version&#x60; is the current one: read it again and resend your edit. |  -  |

## updateAutomationWithHttpInfo

> ApiResponse<CreateAutomation201Response> updateAutomation updateAutomationWithHttpInfo(automationId, updateAutomationRequest, ifMatch)

Edit an automation

Replaces the top-level fields you send and keeps the rest: to change one step, send all of &#x60;steps&#x60;. The result is checked as a whole automation, so problems carry the same paths as on create.  An automation keeps its kind, and an ad rule stays on its ad account. Send &#x60;alert: null&#x60; to remove an ad rule&#39;s alert.  Send the &#x60;version&#x60; you read as &#x60;If-Match&#x60;: if the automation was saved since, the edit is refused with a 409 (&#x60;automation_stale&#x60;). An edit is also refused with a 409 when another save lands while it is being applied. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String automationId = "automationId_example"; // String | 
        UpdateAutomationRequest updateAutomationRequest = new UpdateAutomationRequest(); // UpdateAutomationRequest | 
        String ifMatch = "ifMatch_example"; // String | The automation's `version` when you read it.
        try {
            ApiResponse<CreateAutomation201Response> response = apiInstance.updateAutomationWithHttpInfo(automationId, updateAutomationRequest, ifMatch);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#updateAutomation");
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
| **automationId** | **String**|  | |
| **updateAutomationRequest** | [**UpdateAutomationRequest**](UpdateAutomationRequest.md)|  | |
| **ifMatch** | **String**| The automation&#39;s &#x60;version&#x60; when you read it. | [optional] |

### Return type

ApiResponse<[**CreateAutomation201Response**](CreateAutomation201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Automation updated |  -  |
| **400** | The automation is invalid, or holds something its kind cannot: &#x60;details.problems&#x60; lists each problem with its JSON path. A few ad rule checks (an unsupported platform, step or metric, a cooldown shorter than the schedule, approvers not on the team) answer with &#x60;param&#x60; instead. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ad rules only: your account has no ads access (code &#x60;ads_addon_required&#x60;). Ads are included on usage-based plans. Event and scheduled automations never get this 403: a boost step without ads access is refused with a 400 at its path. |  -  |
| **404** | Resource not found |  -  |
| **409** | The automation was saved after the &#x60;version&#x60; in &#x60;If-Match&#x60; (code &#x60;automation_stale&#x60;). &#x60;details.version&#x60; is the current one: read it again and resend your edit. |  -  |


## updateAutomationAdAccountControls

> GetAutomationControls200Response updateAutomationAdAccountControls(updateAutomationAdAccountControlsRequest)

Update one ad account&#39;s controls

Turns ad rules off or on for one ad account, sets its daily raise limit, or both. Send at least one of &#x60;paused&#x60; and &#x60;dailyRaiseLimit&#x60;; fields you leave out keep their value.  The ad account must be one the connection in &#x60;accountId&#x60; reaches, as for an automation on it. Controls apply to every ad rule of the team on that ad account. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        UpdateAutomationAdAccountControlsRequest updateAutomationAdAccountControlsRequest = new UpdateAutomationAdAccountControlsRequest(); // UpdateAutomationAdAccountControlsRequest | 
        try {
            GetAutomationControls200Response result = apiInstance.updateAutomationAdAccountControls(updateAutomationAdAccountControlsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#updateAutomationAdAccountControls");
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
| **updateAutomationAdAccountControlsRequest** | [**UpdateAutomationAdAccountControlsRequest**](UpdateAutomationAdAccountControlsRequest.md)|  | |

### Return type

[**GetAutomationControls200Response**](GetAutomationControls200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The controls after the change |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ads_addon_required&#x60; when the account has no ads access, or &#x60;ad_account_not_selected&#x60; when the ad account is not among the connection&#39;s selected ad accounts. |  -  |
| **404** | Resource not found |  -  |
| **409** | Code &#x60;ads_connection_required&#x60;: the connection needs reconnecting. |  -  |

## updateAutomationAdAccountControlsWithHttpInfo

> ApiResponse<GetAutomationControls200Response> updateAutomationAdAccountControls updateAutomationAdAccountControlsWithHttpInfo(updateAutomationAdAccountControlsRequest)

Update one ad account&#39;s controls

Turns ad rules off or on for one ad account, sets its daily raise limit, or both. Send at least one of &#x60;paused&#x60; and &#x60;dailyRaiseLimit&#x60;; fields you leave out keep their value.  The ad account must be one the connection in &#x60;accountId&#x60; reaches, as for an automation on it. Controls apply to every ad rule of the team on that ad account. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        UpdateAutomationAdAccountControlsRequest updateAutomationAdAccountControlsRequest = new UpdateAutomationAdAccountControlsRequest(); // UpdateAutomationAdAccountControlsRequest | 
        try {
            ApiResponse<GetAutomationControls200Response> response = apiInstance.updateAutomationAdAccountControlsWithHttpInfo(updateAutomationAdAccountControlsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#updateAutomationAdAccountControls");
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
| **updateAutomationAdAccountControlsRequest** | [**UpdateAutomationAdAccountControlsRequest**](UpdateAutomationAdAccountControlsRequest.md)|  | |

### Return type

ApiResponse<[**GetAutomationControls200Response**](GetAutomationControls200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The controls after the change |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ads_addon_required&#x60; when the account has no ads access, or &#x60;ad_account_not_selected&#x60; when the ad account is not among the connection&#39;s selected ad accounts. |  -  |
| **404** | Resource not found |  -  |
| **409** | Code &#x60;ads_connection_required&#x60;: the connection needs reconnecting. |  -  |


## updateAutomationControls

> GetAutomationControls200Response updateAutomationControls(updateAutomationControlsRequest)

Turn every ad automation off or on

Turns every ad rule of the team off (&#x60;paused: true&#x60;) or back on. Each rule keeps its own status, so turning the switch back on resumes exactly the rules that were active.  Scheduled automations that boost posts are not stopped by it: pause them one by one.  It reaches every profile, so only the account owner or a full-access team member can use it. A key limited to some profiles gets 403.  Turning off a switch that is already off keeps its original &#x60;pausedAt&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        UpdateAutomationControlsRequest updateAutomationControlsRequest = new UpdateAutomationControlsRequest(); // UpdateAutomationControlsRequest | 
        try {
            GetAutomationControls200Response result = apiInstance.updateAutomationControls(updateAutomationControlsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#updateAutomationControls");
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
| **updateAutomationControlsRequest** | [**UpdateAutomationControlsRequest**](UpdateAutomationControlsRequest.md)|  | |

### Return type

[**GetAutomationControls200Response**](GetAutomationControls200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The controls after the change |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;insufficient_permissions&#x60; when the caller is not the account owner or a full-access team member, or &#x60;ads_addon_required&#x60; when the account has no ads access. |  -  |

## updateAutomationControlsWithHttpInfo

> ApiResponse<GetAutomationControls200Response> updateAutomationControls updateAutomationControlsWithHttpInfo(updateAutomationControlsRequest)

Turn every ad automation off or on

Turns every ad rule of the team off (&#x60;paused: true&#x60;) or back on. Each rule keeps its own status, so turning the switch back on resumes exactly the rules that were active.  Scheduled automations that boost posts are not stopped by it: pause them one by one.  It reaches every profile, so only the account owner or a full-access team member can use it. A key limited to some profiles gets 403.  Turning off a switch that is already off keeps its original &#x60;pausedAt&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        UpdateAutomationControlsRequest updateAutomationControlsRequest = new UpdateAutomationControlsRequest(); // UpdateAutomationControlsRequest | 
        try {
            ApiResponse<GetAutomationControls200Response> response = apiInstance.updateAutomationControlsWithHttpInfo(updateAutomationControlsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#updateAutomationControls");
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
| **updateAutomationControlsRequest** | [**UpdateAutomationControlsRequest**](UpdateAutomationControlsRequest.md)|  | |

### Return type

ApiResponse<[**GetAutomationControls200Response**](GetAutomationControls200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The controls after the change |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;insufficient_permissions&#x60; when the caller is not the account owner or a full-access team member, or &#x60;ads_addon_required&#x60; when the account has no ads access. |  -  |


## updateAutomationTemplate

> CreateAutomationTemplate201Response updateAutomationTemplate(templateId, updateAutomationTemplateRequest)

Update an automation template

Renames a template, turns its share link on or off, or replaces its automations. Send at least one field.  Renaming or sharing keeps the &#x60;version&#x60;. New content (&#x60;from&#x60; or &#x60;automations&#x60;) is a new version; automations already installed keep the version they came from.  &#x60;visibility: link&#x60; turns the share link on (the same link while it stays on) and &#x60;visibility: team&#x60; revokes it. To copy a shared template, use &#x60;POST /v1/automations/templates&#x60; instead. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String templateId = "templateId_example"; // String | The template's id.
        UpdateAutomationTemplateRequest updateAutomationTemplateRequest = new UpdateAutomationTemplateRequest(); // UpdateAutomationTemplateRequest | 
        try {
            CreateAutomationTemplate201Response result = apiInstance.updateAutomationTemplate(templateId, updateAutomationTemplateRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#updateAutomationTemplate");
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
| **templateId** | **String**| The template&#39;s id. | |
| **updateAutomationTemplateRequest** | [**UpdateAutomationTemplateRequest**](UpdateAutomationTemplateRequest.md)|  | |

### Return type

[**CreateAutomationTemplate201Response**](CreateAutomationTemplate201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Template updated |  -  |
| **400** | The automation is invalid, or holds something its kind cannot: &#x60;details.problems&#x60; lists each problem with its JSON path. A few ad rule checks (an unsupported platform, step or metric, a cooldown shorter than the schedule, approvers not on the team) answer with &#x60;param&#x60; instead. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | No template with this id in your team, or a source in &#x60;from&#x60; was not found. |  -  |

## updateAutomationTemplateWithHttpInfo

> ApiResponse<CreateAutomationTemplate201Response> updateAutomationTemplate updateAutomationTemplateWithHttpInfo(templateId, updateAutomationTemplateRequest)

Update an automation template

Renames a template, turns its share link on or off, or replaces its automations. Send at least one field.  Renaming or sharing keeps the &#x60;version&#x60;. New content (&#x60;from&#x60; or &#x60;automations&#x60;) is a new version; automations already installed keep the version they came from.  &#x60;visibility: link&#x60; turns the share link on (the same link while it stays on) and &#x60;visibility: team&#x60; revokes it. To copy a shared template, use &#x60;POST /v1/automations/templates&#x60; instead. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AutomationsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AutomationsApi apiInstance = new AutomationsApi(defaultClient);
        String templateId = "templateId_example"; // String | The template's id.
        UpdateAutomationTemplateRequest updateAutomationTemplateRequest = new UpdateAutomationTemplateRequest(); // UpdateAutomationTemplateRequest | 
        try {
            ApiResponse<CreateAutomationTemplate201Response> response = apiInstance.updateAutomationTemplateWithHttpInfo(templateId, updateAutomationTemplateRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AutomationsApi#updateAutomationTemplate");
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
| **templateId** | **String**| The template&#39;s id. | |
| **updateAutomationTemplateRequest** | [**UpdateAutomationTemplateRequest**](UpdateAutomationTemplateRequest.md)|  | |

### Return type

ApiResponse<[**CreateAutomationTemplate201Response**](CreateAutomationTemplate201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Template updated |  -  |
| **400** | The automation is invalid, or holds something its kind cannot: &#x60;details.problems&#x60; lists each problem with its JSON path. A few ad rule checks (an unsupported platform, step or metric, a cooldown shorter than the schedule, approvers not on the team) answer with &#x60;param&#x60; instead. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | No template with this id in your team, or a source in &#x60;from&#x60; was not found. |  -  |

