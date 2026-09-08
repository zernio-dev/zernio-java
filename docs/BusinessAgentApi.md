# BusinessAgentApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addBusinessAgentAllowlistEntry**](BusinessAgentApi.md#addBusinessAgentAllowlistEntry) | **POST** /v1/accounts/{accountId}/business-agent/allowlist | Allowlist a consumer |
| [**addBusinessAgentAllowlistEntryWithHttpInfo**](BusinessAgentApi.md#addBusinessAgentAllowlistEntryWithHttpInfo) | **POST** /v1/accounts/{accountId}/business-agent/allowlist | Allowlist a consumer |
| [**addBusinessAgentWebsite**](BusinessAgentApi.md#addBusinessAgentWebsite) | **POST** /v1/accounts/{accountId}/business-agent/websites | Add a website to crawl |
| [**addBusinessAgentWebsiteWithHttpInfo**](BusinessAgentApi.md#addBusinessAgentWebsiteWithHttpInfo) | **POST** /v1/accounts/{accountId}/business-agent/websites | Add a website to crawl |
| [**createBusinessAgentConnector**](BusinessAgentApi.md#createBusinessAgentConnector) | **POST** /v1/accounts/{accountId}/business-agent/connectors | Create a connector |
| [**createBusinessAgentConnectorWithHttpInfo**](BusinessAgentApi.md#createBusinessAgentConnectorWithHttpInfo) | **POST** /v1/accounts/{accountId}/business-agent/connectors | Create a connector |
| [**createBusinessAgentConnectorTool**](BusinessAgentApi.md#createBusinessAgentConnectorTool) | **POST** /v1/accounts/{accountId}/business-agent/connectors/{connectorId}/tools | Create a connector tool |
| [**createBusinessAgentConnectorToolWithHttpInfo**](BusinessAgentApi.md#createBusinessAgentConnectorToolWithHttpInfo) | **POST** /v1/accounts/{accountId}/business-agent/connectors/{connectorId}/tools | Create a connector tool |
| [**createBusinessAgentFaq**](BusinessAgentApi.md#createBusinessAgentFaq) | **POST** /v1/accounts/{accountId}/business-agent/faqs | Create a FAQ |
| [**createBusinessAgentFaqWithHttpInfo**](BusinessAgentApi.md#createBusinessAgentFaqWithHttpInfo) | **POST** /v1/accounts/{accountId}/business-agent/faqs | Create a FAQ |
| [**createBusinessAgentSkill**](BusinessAgentApi.md#createBusinessAgentSkill) | **POST** /v1/accounts/{accountId}/business-agent/skills | Create a skill |
| [**createBusinessAgentSkillWithHttpInfo**](BusinessAgentApi.md#createBusinessAgentSkillWithHttpInfo) | **POST** /v1/accounts/{accountId}/business-agent/skills | Create a skill |
| [**createBusinessAgentUiSkill**](BusinessAgentApi.md#createBusinessAgentUiSkill) | **POST** /v1/accounts/{accountId}/business-agent/ui-skills | Create a UI skill |
| [**createBusinessAgentUiSkillWithHttpInfo**](BusinessAgentApi.md#createBusinessAgentUiSkillWithHttpInfo) | **POST** /v1/accounts/{accountId}/business-agent/ui-skills | Create a UI skill |
| [**deleteBusinessAgentConnector**](BusinessAgentApi.md#deleteBusinessAgentConnector) | **DELETE** /v1/accounts/{accountId}/business-agent/connectors/{connectorId} | Delete a connector |
| [**deleteBusinessAgentConnectorWithHttpInfo**](BusinessAgentApi.md#deleteBusinessAgentConnectorWithHttpInfo) | **DELETE** /v1/accounts/{accountId}/business-agent/connectors/{connectorId} | Delete a connector |
| [**deleteBusinessAgentConnectorTool**](BusinessAgentApi.md#deleteBusinessAgentConnectorTool) | **DELETE** /v1/accounts/{accountId}/business-agent/connectors/{connectorId}/tools/{toolId} | Delete a connector tool |
| [**deleteBusinessAgentConnectorToolWithHttpInfo**](BusinessAgentApi.md#deleteBusinessAgentConnectorToolWithHttpInfo) | **DELETE** /v1/accounts/{accountId}/business-agent/connectors/{connectorId}/tools/{toolId} | Delete a connector tool |
| [**deleteBusinessAgentFaq**](BusinessAgentApi.md#deleteBusinessAgentFaq) | **DELETE** /v1/accounts/{accountId}/business-agent/faqs/{faqId} | Delete a FAQ |
| [**deleteBusinessAgentFaqWithHttpInfo**](BusinessAgentApi.md#deleteBusinessAgentFaqWithHttpInfo) | **DELETE** /v1/accounts/{accountId}/business-agent/faqs/{faqId} | Delete a FAQ |
| [**deleteBusinessAgentFile**](BusinessAgentApi.md#deleteBusinessAgentFile) | **DELETE** /v1/accounts/{accountId}/business-agent/files/{fileId} | Delete a knowledge file |
| [**deleteBusinessAgentFileWithHttpInfo**](BusinessAgentApi.md#deleteBusinessAgentFileWithHttpInfo) | **DELETE** /v1/accounts/{accountId}/business-agent/files/{fileId} | Delete a knowledge file |
| [**deleteBusinessAgentSkill**](BusinessAgentApi.md#deleteBusinessAgentSkill) | **DELETE** /v1/accounts/{accountId}/business-agent/skills/{skillId} | Delete a skill |
| [**deleteBusinessAgentSkillWithHttpInfo**](BusinessAgentApi.md#deleteBusinessAgentSkillWithHttpInfo) | **DELETE** /v1/accounts/{accountId}/business-agent/skills/{skillId} | Delete a skill |
| [**deleteBusinessAgentUiSkill**](BusinessAgentApi.md#deleteBusinessAgentUiSkill) | **DELETE** /v1/accounts/{accountId}/business-agent/ui-skills/{uiSkillId} | Delete a UI skill |
| [**deleteBusinessAgentUiSkillWithHttpInfo**](BusinessAgentApi.md#deleteBusinessAgentUiSkillWithHttpInfo) | **DELETE** /v1/accounts/{accountId}/business-agent/ui-skills/{uiSkillId} | Delete a UI skill |
| [**deleteBusinessAgentWebsite**](BusinessAgentApi.md#deleteBusinessAgentWebsite) | **DELETE** /v1/accounts/{accountId}/business-agent/websites/{websiteId} | Remove a crawled website |
| [**deleteBusinessAgentWebsiteWithHttpInfo**](BusinessAgentApi.md#deleteBusinessAgentWebsiteWithHttpInfo) | **DELETE** /v1/accounts/{accountId}/business-agent/websites/{websiteId} | Remove a crawled website |
| [**getBusinessAgentBudget**](BusinessAgentApi.md#getBusinessAgentBudget) | **GET** /v1/accounts/{accountId}/business-agent/budget | Get usage budgets |
| [**getBusinessAgentBudgetWithHttpInfo**](BusinessAgentApi.md#getBusinessAgentBudgetWithHttpInfo) | **GET** /v1/accounts/{accountId}/business-agent/budget | Get usage budgets |
| [**getBusinessAgentBusinessInformation**](BusinessAgentApi.md#getBusinessAgentBusinessInformation) | **GET** /v1/accounts/{accountId}/business-agent/business-information | Get business information |
| [**getBusinessAgentBusinessInformationWithHttpInfo**](BusinessAgentApi.md#getBusinessAgentBusinessInformationWithHttpInfo) | **GET** /v1/accounts/{accountId}/business-agent/business-information | Get business information |
| [**getBusinessAgentConnector**](BusinessAgentApi.md#getBusinessAgentConnector) | **GET** /v1/accounts/{accountId}/business-agent/connectors/{connectorId} | Get a connector |
| [**getBusinessAgentConnectorWithHttpInfo**](BusinessAgentApi.md#getBusinessAgentConnectorWithHttpInfo) | **GET** /v1/accounts/{accountId}/business-agent/connectors/{connectorId} | Get a connector |
| [**getBusinessAgentConnectorLogs**](BusinessAgentApi.md#getBusinessAgentConnectorLogs) | **GET** /v1/accounts/{accountId}/business-agent/connectors/{connectorId}/logs | Get connector failure logs |
| [**getBusinessAgentConnectorLogsWithHttpInfo**](BusinessAgentApi.md#getBusinessAgentConnectorLogsWithHttpInfo) | **GET** /v1/accounts/{accountId}/business-agent/connectors/{connectorId}/logs | Get connector failure logs |
| [**getBusinessAgentConnectorTool**](BusinessAgentApi.md#getBusinessAgentConnectorTool) | **GET** /v1/accounts/{accountId}/business-agent/connectors/{connectorId}/tools/{toolId} | Get a connector tool |
| [**getBusinessAgentConnectorToolWithHttpInfo**](BusinessAgentApi.md#getBusinessAgentConnectorToolWithHttpInfo) | **GET** /v1/accounts/{accountId}/business-agent/connectors/{connectorId}/tools/{toolId} | Get a connector tool |
| [**getBusinessAgentEvent**](BusinessAgentApi.md#getBusinessAgentEvent) | **GET** /v1/accounts/{accountId}/business-agent/events/{eventId} | Get a business event status |
| [**getBusinessAgentEventWithHttpInfo**](BusinessAgentApi.md#getBusinessAgentEventWithHttpInfo) | **GET** /v1/accounts/{accountId}/business-agent/events/{eventId} | Get a business event status |
| [**getBusinessAgentFaq**](BusinessAgentApi.md#getBusinessAgentFaq) | **GET** /v1/accounts/{accountId}/business-agent/faqs/{faqId} | Get a FAQ |
| [**getBusinessAgentFaqWithHttpInfo**](BusinessAgentApi.md#getBusinessAgentFaqWithHttpInfo) | **GET** /v1/accounts/{accountId}/business-agent/faqs/{faqId} | Get a FAQ |
| [**getBusinessAgentFile**](BusinessAgentApi.md#getBusinessAgentFile) | **GET** /v1/accounts/{accountId}/business-agent/files/{fileId} | Get a knowledge file |
| [**getBusinessAgentFileWithHttpInfo**](BusinessAgentApi.md#getBusinessAgentFileWithHttpInfo) | **GET** /v1/accounts/{accountId}/business-agent/files/{fileId} | Get a knowledge file |
| [**getBusinessAgentSkill**](BusinessAgentApi.md#getBusinessAgentSkill) | **GET** /v1/accounts/{accountId}/business-agent/skills/{skillId} | Get a skill |
| [**getBusinessAgentSkillWithHttpInfo**](BusinessAgentApi.md#getBusinessAgentSkillWithHttpInfo) | **GET** /v1/accounts/{accountId}/business-agent/skills/{skillId} | Get a skill |
| [**getBusinessAgentStatus**](BusinessAgentApi.md#getBusinessAgentStatus) | **GET** /v1/accounts/{accountId}/business-agent | Get agent setup status |
| [**getBusinessAgentStatusWithHttpInfo**](BusinessAgentApi.md#getBusinessAgentStatusWithHttpInfo) | **GET** /v1/accounts/{accountId}/business-agent | Get agent setup status |
| [**getBusinessAgentUiSkill**](BusinessAgentApi.md#getBusinessAgentUiSkill) | **GET** /v1/accounts/{accountId}/business-agent/ui-skills/{uiSkillId} | Get a UI skill |
| [**getBusinessAgentUiSkillWithHttpInfo**](BusinessAgentApi.md#getBusinessAgentUiSkillWithHttpInfo) | **GET** /v1/accounts/{accountId}/business-agent/ui-skills/{uiSkillId} | Get a UI skill |
| [**getBusinessAgentWebsite**](BusinessAgentApi.md#getBusinessAgentWebsite) | **GET** /v1/accounts/{accountId}/business-agent/websites/{websiteId} | Get a crawled website |
| [**getBusinessAgentWebsiteWithHttpInfo**](BusinessAgentApi.md#getBusinessAgentWebsiteWithHttpInfo) | **GET** /v1/accounts/{accountId}/business-agent/websites/{websiteId} | Get a crawled website |
| [**listBusinessAgentAllowlist**](BusinessAgentApi.md#listBusinessAgentAllowlist) | **GET** /v1/accounts/{accountId}/business-agent/allowlist | List allowlisted consumers |
| [**listBusinessAgentAllowlistWithHttpInfo**](BusinessAgentApi.md#listBusinessAgentAllowlistWithHttpInfo) | **GET** /v1/accounts/{accountId}/business-agent/allowlist | List allowlisted consumers |
| [**listBusinessAgentConnectorTools**](BusinessAgentApi.md#listBusinessAgentConnectorTools) | **GET** /v1/accounts/{accountId}/business-agent/connectors/{connectorId}/tools | List connector tools |
| [**listBusinessAgentConnectorToolsWithHttpInfo**](BusinessAgentApi.md#listBusinessAgentConnectorToolsWithHttpInfo) | **GET** /v1/accounts/{accountId}/business-agent/connectors/{connectorId}/tools | List connector tools |
| [**listBusinessAgentConnectors**](BusinessAgentApi.md#listBusinessAgentConnectors) | **GET** /v1/accounts/{accountId}/business-agent/connectors | List connectors |
| [**listBusinessAgentConnectorsWithHttpInfo**](BusinessAgentApi.md#listBusinessAgentConnectorsWithHttpInfo) | **GET** /v1/accounts/{accountId}/business-agent/connectors | List connectors |
| [**listBusinessAgentFaqs**](BusinessAgentApi.md#listBusinessAgentFaqs) | **GET** /v1/accounts/{accountId}/business-agent/faqs | List FAQs |
| [**listBusinessAgentFaqsWithHttpInfo**](BusinessAgentApi.md#listBusinessAgentFaqsWithHttpInfo) | **GET** /v1/accounts/{accountId}/business-agent/faqs | List FAQs |
| [**listBusinessAgentFiles**](BusinessAgentApi.md#listBusinessAgentFiles) | **GET** /v1/accounts/{accountId}/business-agent/files | List knowledge files |
| [**listBusinessAgentFilesWithHttpInfo**](BusinessAgentApi.md#listBusinessAgentFilesWithHttpInfo) | **GET** /v1/accounts/{accountId}/business-agent/files | List knowledge files |
| [**listBusinessAgentSettings**](BusinessAgentApi.md#listBusinessAgentSettings) | **GET** /v1/accounts/{accountId}/business-agent/settings | List agent settings |
| [**listBusinessAgentSettingsWithHttpInfo**](BusinessAgentApi.md#listBusinessAgentSettingsWithHttpInfo) | **GET** /v1/accounts/{accountId}/business-agent/settings | List agent settings |
| [**listBusinessAgentSkills**](BusinessAgentApi.md#listBusinessAgentSkills) | **GET** /v1/accounts/{accountId}/business-agent/skills | List skills |
| [**listBusinessAgentSkillsWithHttpInfo**](BusinessAgentApi.md#listBusinessAgentSkillsWithHttpInfo) | **GET** /v1/accounts/{accountId}/business-agent/skills | List skills |
| [**listBusinessAgentUiSkills**](BusinessAgentApi.md#listBusinessAgentUiSkills) | **GET** /v1/accounts/{accountId}/business-agent/ui-skills | List UI skills |
| [**listBusinessAgentUiSkillsWithHttpInfo**](BusinessAgentApi.md#listBusinessAgentUiSkillsWithHttpInfo) | **GET** /v1/accounts/{accountId}/business-agent/ui-skills | List UI skills |
| [**listBusinessAgentWebsites**](BusinessAgentApi.md#listBusinessAgentWebsites) | **GET** /v1/accounts/{accountId}/business-agent/websites | List crawled websites |
| [**listBusinessAgentWebsitesWithHttpInfo**](BusinessAgentApi.md#listBusinessAgentWebsitesWithHttpInfo) | **GET** /v1/accounts/{accountId}/business-agent/websites | List crawled websites |
| [**onboardBusinessAgent**](BusinessAgentApi.md#onboardBusinessAgent) | **POST** /v1/accounts/{accountId}/business-agent/onboard | Create the agent |
| [**onboardBusinessAgentWithHttpInfo**](BusinessAgentApi.md#onboardBusinessAgentWithHttpInfo) | **POST** /v1/accounts/{accountId}/business-agent/onboard | Create the agent |
| [**readBusinessAgentEvals**](BusinessAgentApi.md#readBusinessAgentEvals) | **GET** /v1/accounts/{accountId}/business-agent/evals | Read evaluation data |
| [**readBusinessAgentEvalsWithHttpInfo**](BusinessAgentApi.md#readBusinessAgentEvalsWithHttpInfo) | **GET** /v1/accounts/{accountId}/business-agent/evals | Read evaluation data |
| [**refreshBusinessAgentConnectorTools**](BusinessAgentApi.md#refreshBusinessAgentConnectorTools) | **POST** /v1/accounts/{accountId}/business-agent/connectors/{connectorId}/refresh-tools | Refresh MCP connector tools |
| [**refreshBusinessAgentConnectorToolsWithHttpInfo**](BusinessAgentApi.md#refreshBusinessAgentConnectorToolsWithHttpInfo) | **POST** /v1/accounts/{accountId}/business-agent/connectors/{connectorId}/refresh-tools | Refresh MCP connector tools |
| [**removeBusinessAgentAllowlistEntry**](BusinessAgentApi.md#removeBusinessAgentAllowlistEntry) | **DELETE** /v1/accounts/{accountId}/business-agent/allowlist/{entryId} | Remove an allowlisted consumer |
| [**removeBusinessAgentAllowlistEntryWithHttpInfo**](BusinessAgentApi.md#removeBusinessAgentAllowlistEntryWithHttpInfo) | **DELETE** /v1/accounts/{accountId}/business-agent/allowlist/{entryId} | Remove an allowlisted consumer |
| [**replaceBusinessAgentBudget**](BusinessAgentApi.md#replaceBusinessAgentBudget) | **PUT** /v1/accounts/{accountId}/business-agent/budget | Replace usage budgets |
| [**replaceBusinessAgentBudgetWithHttpInfo**](BusinessAgentApi.md#replaceBusinessAgentBudgetWithHttpInfo) | **PUT** /v1/accounts/{accountId}/business-agent/budget | Replace usage budgets |
| [**replaceBusinessAgentBusinessInformation**](BusinessAgentApi.md#replaceBusinessAgentBusinessInformation) | **PUT** /v1/accounts/{accountId}/business-agent/business-information | Replace business information |
| [**replaceBusinessAgentBusinessInformationWithHttpInfo**](BusinessAgentApi.md#replaceBusinessAgentBusinessInformationWithHttpInfo) | **PUT** /v1/accounts/{accountId}/business-agent/business-information | Replace business information |
| [**resetBusinessAgentBusinessInformation**](BusinessAgentApi.md#resetBusinessAgentBusinessInformation) | **DELETE** /v1/accounts/{accountId}/business-agent/business-information | Reset business information |
| [**resetBusinessAgentBusinessInformationWithHttpInfo**](BusinessAgentApi.md#resetBusinessAgentBusinessInformationWithHttpInfo) | **DELETE** /v1/accounts/{accountId}/business-agent/business-information | Reset business information |
| [**runBusinessAgentConnectorTool**](BusinessAgentApi.md#runBusinessAgentConnectorTool) | **POST** /v1/accounts/{accountId}/business-agent/connectors/{connectorId}/tools/{toolId}/run | Run a connector tool once |
| [**runBusinessAgentConnectorToolWithHttpInfo**](BusinessAgentApi.md#runBusinessAgentConnectorToolWithHttpInfo) | **POST** /v1/accounts/{accountId}/business-agent/connectors/{connectorId}/tools/{toolId}/run | Run a connector tool once |
| [**sendBusinessAgentEvent**](BusinessAgentApi.md#sendBusinessAgentEvent) | **POST** /v1/accounts/{accountId}/business-agent/events | Send a business event |
| [**sendBusinessAgentEventWithHttpInfo**](BusinessAgentApi.md#sendBusinessAgentEventWithHttpInfo) | **POST** /v1/accounts/{accountId}/business-agent/events | Send a business event |
| [**sendBusinessAgentTestMessage**](BusinessAgentApi.md#sendBusinessAgentTestMessage) | **POST** /v1/accounts/{accountId}/business-agent/test-messages | Send a test message |
| [**sendBusinessAgentTestMessageWithHttpInfo**](BusinessAgentApi.md#sendBusinessAgentTestMessageWithHttpInfo) | **POST** /v1/accounts/{accountId}/business-agent/test-messages | Send a test message |
| [**setBusinessAgentConnectorCredentials**](BusinessAgentApi.md#setBusinessAgentConnectorCredentials) | **POST** /v1/accounts/{accountId}/business-agent/connectors/{connectorId}/credentials | Set connector credentials |
| [**setBusinessAgentConnectorCredentialsWithHttpInfo**](BusinessAgentApi.md#setBusinessAgentConnectorCredentialsWithHttpInfo) | **POST** /v1/accounts/{accountId}/business-agent/connectors/{connectorId}/credentials | Set connector credentials |
| [**startBusinessAgentEvalRun**](BusinessAgentApi.md#startBusinessAgentEvalRun) | **POST** /v1/accounts/{accountId}/business-agent/evals | Start an evaluation run |
| [**startBusinessAgentEvalRunWithHttpInfo**](BusinessAgentApi.md#startBusinessAgentEvalRunWithHttpInfo) | **POST** /v1/accounts/{accountId}/business-agent/evals | Start an evaluation run |
| [**updateBusinessAgentConnector**](BusinessAgentApi.md#updateBusinessAgentConnector) | **PUT** /v1/accounts/{accountId}/business-agent/connectors/{connectorId} | Update a connector |
| [**updateBusinessAgentConnectorWithHttpInfo**](BusinessAgentApi.md#updateBusinessAgentConnectorWithHttpInfo) | **PUT** /v1/accounts/{accountId}/business-agent/connectors/{connectorId} | Update a connector |
| [**updateBusinessAgentConnectorTool**](BusinessAgentApi.md#updateBusinessAgentConnectorTool) | **PUT** /v1/accounts/{accountId}/business-agent/connectors/{connectorId}/tools/{toolId} | Update a connector tool |
| [**updateBusinessAgentConnectorToolWithHttpInfo**](BusinessAgentApi.md#updateBusinessAgentConnectorToolWithHttpInfo) | **PUT** /v1/accounts/{accountId}/business-agent/connectors/{connectorId}/tools/{toolId} | Update a connector tool |
| [**updateBusinessAgentFaq**](BusinessAgentApi.md#updateBusinessAgentFaq) | **PUT** /v1/accounts/{accountId}/business-agent/faqs/{faqId} | Update a FAQ |
| [**updateBusinessAgentFaqWithHttpInfo**](BusinessAgentApi.md#updateBusinessAgentFaqWithHttpInfo) | **PUT** /v1/accounts/{accountId}/business-agent/faqs/{faqId} | Update a FAQ |
| [**updateBusinessAgentSettings**](BusinessAgentApi.md#updateBusinessAgentSettings) | **PATCH** /v1/accounts/{accountId}/business-agent/settings | Update agent settings |
| [**updateBusinessAgentSettingsWithHttpInfo**](BusinessAgentApi.md#updateBusinessAgentSettingsWithHttpInfo) | **PATCH** /v1/accounts/{accountId}/business-agent/settings | Update agent settings |
| [**updateBusinessAgentSkill**](BusinessAgentApi.md#updateBusinessAgentSkill) | **PUT** /v1/accounts/{accountId}/business-agent/skills/{skillId} | Update a skill |
| [**updateBusinessAgentSkillWithHttpInfo**](BusinessAgentApi.md#updateBusinessAgentSkillWithHttpInfo) | **PUT** /v1/accounts/{accountId}/business-agent/skills/{skillId} | Update a skill |
| [**updateBusinessAgentUiSkill**](BusinessAgentApi.md#updateBusinessAgentUiSkill) | **PUT** /v1/accounts/{accountId}/business-agent/ui-skills/{uiSkillId} | Update a UI skill |
| [**updateBusinessAgentUiSkillWithHttpInfo**](BusinessAgentApi.md#updateBusinessAgentUiSkillWithHttpInfo) | **PUT** /v1/accounts/{accountId}/business-agent/ui-skills/{uiSkillId} | Update a UI skill |
| [**updateBusinessAgentWebsite**](BusinessAgentApi.md#updateBusinessAgentWebsite) | **PUT** /v1/accounts/{accountId}/business-agent/websites/{websiteId} | Update a crawled website |
| [**updateBusinessAgentWebsiteWithHttpInfo**](BusinessAgentApi.md#updateBusinessAgentWebsiteWithHttpInfo) | **PUT** /v1/accounts/{accountId}/business-agent/websites/{websiteId} | Update a crawled website |
| [**uploadBusinessAgentFile**](BusinessAgentApi.md#uploadBusinessAgentFile) | **POST** /v1/accounts/{accountId}/business-agent/files | Upload a knowledge file |
| [**uploadBusinessAgentFileWithHttpInfo**](BusinessAgentApi.md#uploadBusinessAgentFileWithHttpInfo) | **POST** /v1/accounts/{accountId}/business-agent/files | Upload a knowledge file |



## addBusinessAgentAllowlistEntry

> BusinessAgentAllowlistEntry addBusinessAgentAllowlistEntry(accountId, addBusinessAgentAllowlistEntryRequest)

Allowlist a consumer

One E.164 number per call. Not idempotent.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        AddBusinessAgentAllowlistEntryRequest addBusinessAgentAllowlistEntryRequest = new AddBusinessAgentAllowlistEntryRequest(); // AddBusinessAgentAllowlistEntryRequest | 
        try {
            BusinessAgentAllowlistEntry result = apiInstance.addBusinessAgentAllowlistEntry(accountId, addBusinessAgentAllowlistEntryRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#addBusinessAgentAllowlistEntry");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **addBusinessAgentAllowlistEntryRequest** | [**AddBusinessAgentAllowlistEntryRequest**](AddBusinessAgentAllowlistEntryRequest.md)|  | |

### Return type

[**BusinessAgentAllowlistEntry**](BusinessAgentAllowlistEntry.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Entry added |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## addBusinessAgentAllowlistEntryWithHttpInfo

> ApiResponse<BusinessAgentAllowlistEntry> addBusinessAgentAllowlistEntry addBusinessAgentAllowlistEntryWithHttpInfo(accountId, addBusinessAgentAllowlistEntryRequest)

Allowlist a consumer

One E.164 number per call. Not idempotent.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        AddBusinessAgentAllowlistEntryRequest addBusinessAgentAllowlistEntryRequest = new AddBusinessAgentAllowlistEntryRequest(); // AddBusinessAgentAllowlistEntryRequest | 
        try {
            ApiResponse<BusinessAgentAllowlistEntry> response = apiInstance.addBusinessAgentAllowlistEntryWithHttpInfo(accountId, addBusinessAgentAllowlistEntryRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#addBusinessAgentAllowlistEntry");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **addBusinessAgentAllowlistEntryRequest** | [**AddBusinessAgentAllowlistEntryRequest**](AddBusinessAgentAllowlistEntryRequest.md)|  | |

### Return type

ApiResponse<[**BusinessAgentAllowlistEntry**](BusinessAgentAllowlistEntry.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Entry added |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## addBusinessAgentWebsite

> BusinessAgentWebsite addBusinessAgentWebsite(accountId, businessAgentWebsiteInput)

Add a website to crawl

Meta crawls the site into the agent knowledge and recrawls it periodically; check &#x60;crawl_status&#x60; and &#x60;crawl_error&#x60; on read. Not idempotent.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        BusinessAgentWebsiteInput businessAgentWebsiteInput = new BusinessAgentWebsiteInput(); // BusinessAgentWebsiteInput | 
        try {
            BusinessAgentWebsite result = apiInstance.addBusinessAgentWebsite(accountId, businessAgentWebsiteInput);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#addBusinessAgentWebsite");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **businessAgentWebsiteInput** | [**BusinessAgentWebsiteInput**](BusinessAgentWebsiteInput.md)|  | |

### Return type

[**BusinessAgentWebsite**](BusinessAgentWebsite.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Website added |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## addBusinessAgentWebsiteWithHttpInfo

> ApiResponse<BusinessAgentWebsite> addBusinessAgentWebsite addBusinessAgentWebsiteWithHttpInfo(accountId, businessAgentWebsiteInput)

Add a website to crawl

Meta crawls the site into the agent knowledge and recrawls it periodically; check &#x60;crawl_status&#x60; and &#x60;crawl_error&#x60; on read. Not idempotent.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        BusinessAgentWebsiteInput businessAgentWebsiteInput = new BusinessAgentWebsiteInput(); // BusinessAgentWebsiteInput | 
        try {
            ApiResponse<BusinessAgentWebsite> response = apiInstance.addBusinessAgentWebsiteWithHttpInfo(accountId, businessAgentWebsiteInput);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#addBusinessAgentWebsite");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **businessAgentWebsiteInput** | [**BusinessAgentWebsiteInput**](BusinessAgentWebsiteInput.md)|  | |

### Return type

ApiResponse<[**BusinessAgentWebsite**](BusinessAgentWebsite.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Website added |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## createBusinessAgentConnector

> BusinessAgentConnector createBusinessAgentConnector(accountId, businessAgentConnectorInput)

Create a connector

Base URL plus how to authenticate (OAuth client credentials, API key or none). Names are unique per number. Not idempotent.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        BusinessAgentConnectorInput businessAgentConnectorInput = new BusinessAgentConnectorInput(); // BusinessAgentConnectorInput | 
        try {
            BusinessAgentConnector result = apiInstance.createBusinessAgentConnector(accountId, businessAgentConnectorInput);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#createBusinessAgentConnector");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **businessAgentConnectorInput** | [**BusinessAgentConnectorInput**](BusinessAgentConnectorInput.md)|  | |

### Return type

[**BusinessAgentConnector**](BusinessAgentConnector.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Connector created |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |
| **409** | A connector with that name already exists (code business_agent_conflict). |  -  |

## createBusinessAgentConnectorWithHttpInfo

> ApiResponse<BusinessAgentConnector> createBusinessAgentConnector createBusinessAgentConnectorWithHttpInfo(accountId, businessAgentConnectorInput)

Create a connector

Base URL plus how to authenticate (OAuth client credentials, API key or none). Names are unique per number. Not idempotent.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        BusinessAgentConnectorInput businessAgentConnectorInput = new BusinessAgentConnectorInput(); // BusinessAgentConnectorInput | 
        try {
            ApiResponse<BusinessAgentConnector> response = apiInstance.createBusinessAgentConnectorWithHttpInfo(accountId, businessAgentConnectorInput);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#createBusinessAgentConnector");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **businessAgentConnectorInput** | [**BusinessAgentConnectorInput**](BusinessAgentConnectorInput.md)|  | |

### Return type

ApiResponse<[**BusinessAgentConnector**](BusinessAgentConnector.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Connector created |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |
| **409** | A connector with that name already exists (code business_agent_conflict). |  -  |


## createBusinessAgentConnectorTool

> BusinessAgentConnectorTool createBusinessAgentConnectorTool(accountId, connectorId, businessAgentConnectorToolInput)

Create a connector tool

One operation on the connector, with the request definition Meta uses to build the outbound call from the conversation. Type the body params explicitly. Not idempotent.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String connectorId = "connectorId_example"; // String | 
        BusinessAgentConnectorToolInput businessAgentConnectorToolInput = new BusinessAgentConnectorToolInput(); // BusinessAgentConnectorToolInput | 
        try {
            BusinessAgentConnectorTool result = apiInstance.createBusinessAgentConnectorTool(accountId, connectorId, businessAgentConnectorToolInput);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#createBusinessAgentConnectorTool");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **connectorId** | **String**|  | |
| **businessAgentConnectorToolInput** | [**BusinessAgentConnectorToolInput**](BusinessAgentConnectorToolInput.md)|  | |

### Return type

[**BusinessAgentConnectorTool**](BusinessAgentConnectorTool.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Tool created |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## createBusinessAgentConnectorToolWithHttpInfo

> ApiResponse<BusinessAgentConnectorTool> createBusinessAgentConnectorTool createBusinessAgentConnectorToolWithHttpInfo(accountId, connectorId, businessAgentConnectorToolInput)

Create a connector tool

One operation on the connector, with the request definition Meta uses to build the outbound call from the conversation. Type the body params explicitly. Not idempotent.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String connectorId = "connectorId_example"; // String | 
        BusinessAgentConnectorToolInput businessAgentConnectorToolInput = new BusinessAgentConnectorToolInput(); // BusinessAgentConnectorToolInput | 
        try {
            ApiResponse<BusinessAgentConnectorTool> response = apiInstance.createBusinessAgentConnectorToolWithHttpInfo(accountId, connectorId, businessAgentConnectorToolInput);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#createBusinessAgentConnectorTool");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **connectorId** | **String**|  | |
| **businessAgentConnectorToolInput** | [**BusinessAgentConnectorToolInput**](BusinessAgentConnectorToolInput.md)|  | |

### Return type

ApiResponse<[**BusinessAgentConnectorTool**](BusinessAgentConnectorTool.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Tool created |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## createBusinessAgentFaq

> BusinessAgentFaq createBusinessAgentFaq(accountId, businessAgentFaqInput)

Create a FAQ

One specific question per entry; beyond a few hundred entries retrieval quality drops. Not idempotent.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        BusinessAgentFaqInput businessAgentFaqInput = new BusinessAgentFaqInput(); // BusinessAgentFaqInput | 
        try {
            BusinessAgentFaq result = apiInstance.createBusinessAgentFaq(accountId, businessAgentFaqInput);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#createBusinessAgentFaq");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **businessAgentFaqInput** | [**BusinessAgentFaqInput**](BusinessAgentFaqInput.md)|  | |

### Return type

[**BusinessAgentFaq**](BusinessAgentFaq.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | FAQ created |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |
| **409** | Meta rejected the entry (code business_agent_conflict). |  -  |

## createBusinessAgentFaqWithHttpInfo

> ApiResponse<BusinessAgentFaq> createBusinessAgentFaq createBusinessAgentFaqWithHttpInfo(accountId, businessAgentFaqInput)

Create a FAQ

One specific question per entry; beyond a few hundred entries retrieval quality drops. Not idempotent.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        BusinessAgentFaqInput businessAgentFaqInput = new BusinessAgentFaqInput(); // BusinessAgentFaqInput | 
        try {
            ApiResponse<BusinessAgentFaq> response = apiInstance.createBusinessAgentFaqWithHttpInfo(accountId, businessAgentFaqInput);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#createBusinessAgentFaq");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **businessAgentFaqInput** | [**BusinessAgentFaqInput**](BusinessAgentFaqInput.md)|  | |

### Return type

ApiResponse<[**BusinessAgentFaq**](BusinessAgentFaq.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | FAQ created |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |
| **409** | Meta rejected the entry (code business_agent_conflict). |  -  |


## createBusinessAgentSkill

> BusinessAgentSkill createBusinessAgentSkill(accountId, businessAgentSkillInput)

Create a skill

Behavioral instructions in the brand voice. Reads back &#x60;pending_review&#x60; until Meta content review passes it. Not idempotent.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        BusinessAgentSkillInput businessAgentSkillInput = new BusinessAgentSkillInput(); // BusinessAgentSkillInput | 
        try {
            BusinessAgentSkill result = apiInstance.createBusinessAgentSkill(accountId, businessAgentSkillInput);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#createBusinessAgentSkill");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **businessAgentSkillInput** | [**BusinessAgentSkillInput**](BusinessAgentSkillInput.md)|  | |

### Return type

[**BusinessAgentSkill**](BusinessAgentSkill.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Skill created |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## createBusinessAgentSkillWithHttpInfo

> ApiResponse<BusinessAgentSkill> createBusinessAgentSkill createBusinessAgentSkillWithHttpInfo(accountId, businessAgentSkillInput)

Create a skill

Behavioral instructions in the brand voice. Reads back &#x60;pending_review&#x60; until Meta content review passes it. Not idempotent.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        BusinessAgentSkillInput businessAgentSkillInput = new BusinessAgentSkillInput(); // BusinessAgentSkillInput | 
        try {
            ApiResponse<BusinessAgentSkill> response = apiInstance.createBusinessAgentSkillWithHttpInfo(accountId, businessAgentSkillInput);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#createBusinessAgentSkill");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **businessAgentSkillInput** | [**BusinessAgentSkillInput**](BusinessAgentSkillInput.md)|  | |

### Return type

ApiResponse<[**BusinessAgentSkill**](BusinessAgentSkill.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Skill created |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## createBusinessAgentUiSkill

> BusinessAgentUiSkill createBusinessAgentUiSkill(accountId, businessAgentUiSkillInput)

Create a UI skill

Tells the agent when to send a rich component (CTA URL button, image, carousel, list, reply buttons, location, Flow) and what to put in it. Not idempotent.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        BusinessAgentUiSkillInput businessAgentUiSkillInput = new BusinessAgentUiSkillInput(); // BusinessAgentUiSkillInput | 
        try {
            BusinessAgentUiSkill result = apiInstance.createBusinessAgentUiSkill(accountId, businessAgentUiSkillInput);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#createBusinessAgentUiSkill");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **businessAgentUiSkillInput** | [**BusinessAgentUiSkillInput**](BusinessAgentUiSkillInput.md)|  | |

### Return type

[**BusinessAgentUiSkill**](BusinessAgentUiSkill.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | UI skill created |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## createBusinessAgentUiSkillWithHttpInfo

> ApiResponse<BusinessAgentUiSkill> createBusinessAgentUiSkill createBusinessAgentUiSkillWithHttpInfo(accountId, businessAgentUiSkillInput)

Create a UI skill

Tells the agent when to send a rich component (CTA URL button, image, carousel, list, reply buttons, location, Flow) and what to put in it. Not idempotent.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        BusinessAgentUiSkillInput businessAgentUiSkillInput = new BusinessAgentUiSkillInput(); // BusinessAgentUiSkillInput | 
        try {
            ApiResponse<BusinessAgentUiSkill> response = apiInstance.createBusinessAgentUiSkillWithHttpInfo(accountId, businessAgentUiSkillInput);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#createBusinessAgentUiSkill");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **businessAgentUiSkillInput** | [**BusinessAgentUiSkillInput**](BusinessAgentUiSkillInput.md)|  | |

### Return type

ApiResponse<[**BusinessAgentUiSkill**](BusinessAgentUiSkill.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | UI skill created |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## deleteBusinessAgentConnector

> InlineObject deleteBusinessAgentConnector(accountId, connectorId)

Delete a connector

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String connectorId = "connectorId_example"; // String | 
        try {
            InlineObject result = apiInstance.deleteBusinessAgentConnector(accountId, connectorId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#deleteBusinessAgentConnector");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **connectorId** | **String**|  | |

### Return type

[**InlineObject**](InlineObject.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## deleteBusinessAgentConnectorWithHttpInfo

> ApiResponse<InlineObject> deleteBusinessAgentConnector deleteBusinessAgentConnectorWithHttpInfo(accountId, connectorId)

Delete a connector

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String connectorId = "connectorId_example"; // String | 
        try {
            ApiResponse<InlineObject> response = apiInstance.deleteBusinessAgentConnectorWithHttpInfo(accountId, connectorId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#deleteBusinessAgentConnector");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **connectorId** | **String**|  | |

### Return type

ApiResponse<[**InlineObject**](InlineObject.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## deleteBusinessAgentConnectorTool

> InlineObject deleteBusinessAgentConnectorTool(accountId, connectorId, toolId)

Delete a connector tool

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String connectorId = "connectorId_example"; // String | 
        String toolId = "toolId_example"; // String | 
        try {
            InlineObject result = apiInstance.deleteBusinessAgentConnectorTool(accountId, connectorId, toolId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#deleteBusinessAgentConnectorTool");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **connectorId** | **String**|  | |
| **toolId** | **String**|  | |

### Return type

[**InlineObject**](InlineObject.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## deleteBusinessAgentConnectorToolWithHttpInfo

> ApiResponse<InlineObject> deleteBusinessAgentConnectorTool deleteBusinessAgentConnectorToolWithHttpInfo(accountId, connectorId, toolId)

Delete a connector tool

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String connectorId = "connectorId_example"; // String | 
        String toolId = "toolId_example"; // String | 
        try {
            ApiResponse<InlineObject> response = apiInstance.deleteBusinessAgentConnectorToolWithHttpInfo(accountId, connectorId, toolId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#deleteBusinessAgentConnectorTool");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **connectorId** | **String**|  | |
| **toolId** | **String**|  | |

### Return type

ApiResponse<[**InlineObject**](InlineObject.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## deleteBusinessAgentFaq

> InlineObject deleteBusinessAgentFaq(accountId, faqId)

Delete a FAQ

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String faqId = "faqId_example"; // String | 
        try {
            InlineObject result = apiInstance.deleteBusinessAgentFaq(accountId, faqId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#deleteBusinessAgentFaq");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **faqId** | **String**|  | |

### Return type

[**InlineObject**](InlineObject.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## deleteBusinessAgentFaqWithHttpInfo

> ApiResponse<InlineObject> deleteBusinessAgentFaq deleteBusinessAgentFaqWithHttpInfo(accountId, faqId)

Delete a FAQ

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String faqId = "faqId_example"; // String | 
        try {
            ApiResponse<InlineObject> response = apiInstance.deleteBusinessAgentFaqWithHttpInfo(accountId, faqId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#deleteBusinessAgentFaq");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **faqId** | **String**|  | |

### Return type

ApiResponse<[**InlineObject**](InlineObject.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## deleteBusinessAgentFile

> InlineObject deleteBusinessAgentFile(accountId, fileId)

Delete a knowledge file

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String fileId = "fileId_example"; // String | 
        try {
            InlineObject result = apiInstance.deleteBusinessAgentFile(accountId, fileId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#deleteBusinessAgentFile");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **fileId** | **String**|  | |

### Return type

[**InlineObject**](InlineObject.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## deleteBusinessAgentFileWithHttpInfo

> ApiResponse<InlineObject> deleteBusinessAgentFile deleteBusinessAgentFileWithHttpInfo(accountId, fileId)

Delete a knowledge file

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String fileId = "fileId_example"; // String | 
        try {
            ApiResponse<InlineObject> response = apiInstance.deleteBusinessAgentFileWithHttpInfo(accountId, fileId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#deleteBusinessAgentFile");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **fileId** | **String**|  | |

### Return type

ApiResponse<[**InlineObject**](InlineObject.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## deleteBusinessAgentSkill

> InlineObject deleteBusinessAgentSkill(accountId, skillId)

Delete a skill

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String skillId = "skillId_example"; // String | 
        try {
            InlineObject result = apiInstance.deleteBusinessAgentSkill(accountId, skillId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#deleteBusinessAgentSkill");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **skillId** | **String**|  | |

### Return type

[**InlineObject**](InlineObject.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## deleteBusinessAgentSkillWithHttpInfo

> ApiResponse<InlineObject> deleteBusinessAgentSkill deleteBusinessAgentSkillWithHttpInfo(accountId, skillId)

Delete a skill

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String skillId = "skillId_example"; // String | 
        try {
            ApiResponse<InlineObject> response = apiInstance.deleteBusinessAgentSkillWithHttpInfo(accountId, skillId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#deleteBusinessAgentSkill");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **skillId** | **String**|  | |

### Return type

ApiResponse<[**InlineObject**](InlineObject.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## deleteBusinessAgentUiSkill

> InlineObject deleteBusinessAgentUiSkill(accountId, uiSkillId)

Delete a UI skill

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String uiSkillId = "uiSkillId_example"; // String | 
        try {
            InlineObject result = apiInstance.deleteBusinessAgentUiSkill(accountId, uiSkillId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#deleteBusinessAgentUiSkill");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **uiSkillId** | **String**|  | |

### Return type

[**InlineObject**](InlineObject.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## deleteBusinessAgentUiSkillWithHttpInfo

> ApiResponse<InlineObject> deleteBusinessAgentUiSkill deleteBusinessAgentUiSkillWithHttpInfo(accountId, uiSkillId)

Delete a UI skill

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String uiSkillId = "uiSkillId_example"; // String | 
        try {
            ApiResponse<InlineObject> response = apiInstance.deleteBusinessAgentUiSkillWithHttpInfo(accountId, uiSkillId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#deleteBusinessAgentUiSkill");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **uiSkillId** | **String**|  | |

### Return type

ApiResponse<[**InlineObject**](InlineObject.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## deleteBusinessAgentWebsite

> InlineObject deleteBusinessAgentWebsite(accountId, websiteId)

Remove a crawled website

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String websiteId = "websiteId_example"; // String | 
        try {
            InlineObject result = apiInstance.deleteBusinessAgentWebsite(accountId, websiteId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#deleteBusinessAgentWebsite");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **websiteId** | **String**|  | |

### Return type

[**InlineObject**](InlineObject.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## deleteBusinessAgentWebsiteWithHttpInfo

> ApiResponse<InlineObject> deleteBusinessAgentWebsite deleteBusinessAgentWebsiteWithHttpInfo(accountId, websiteId)

Remove a crawled website

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String websiteId = "websiteId_example"; // String | 
        try {
            ApiResponse<InlineObject> response = apiInstance.deleteBusinessAgentWebsiteWithHttpInfo(accountId, websiteId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#deleteBusinessAgentWebsite");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **websiteId** | **String**|  | |

### Return type

ApiResponse<[**InlineObject**](InlineObject.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## getBusinessAgentBudget

> GetBusinessAgentBudget200Response getBusinessAgentBudget(accountId)

Get usage budgets

Caps over rolling windows for the Business Manager that owns the number. An empty list means unlimited.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        try {
            GetBusinessAgentBudget200Response result = apiInstance.getBusinessAgentBudget(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#getBusinessAgentBudget");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |

### Return type

[**GetBusinessAgentBudget200Response**](GetBusinessAgentBudget200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Budgets |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## getBusinessAgentBudgetWithHttpInfo

> ApiResponse<GetBusinessAgentBudget200Response> getBusinessAgentBudget getBusinessAgentBudgetWithHttpInfo(accountId)

Get usage budgets

Caps over rolling windows for the Business Manager that owns the number. An empty list means unlimited.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        try {
            ApiResponse<GetBusinessAgentBudget200Response> response = apiInstance.getBusinessAgentBudgetWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#getBusinessAgentBudget");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |

### Return type

ApiResponse<[**GetBusinessAgentBudget200Response**](GetBusinessAgentBudget200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Budgets |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## getBusinessAgentBusinessInformation

> BusinessAgentBusinessInformation getBusinessAgentBusinessInformation(accountId)

Get business information

Payment methods, return policy, how to buy, shipping, description and contact details the agent answers from. Empty values until configured.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        try {
            BusinessAgentBusinessInformation result = apiInstance.getBusinessAgentBusinessInformation(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#getBusinessAgentBusinessInformation");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |

### Return type

[**BusinessAgentBusinessInformation**](BusinessAgentBusinessInformation.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Business information |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## getBusinessAgentBusinessInformationWithHttpInfo

> ApiResponse<BusinessAgentBusinessInformation> getBusinessAgentBusinessInformation getBusinessAgentBusinessInformationWithHttpInfo(accountId)

Get business information

Payment methods, return policy, how to buy, shipping, description and contact details the agent answers from. Empty values until configured.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        try {
            ApiResponse<BusinessAgentBusinessInformation> response = apiInstance.getBusinessAgentBusinessInformationWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#getBusinessAgentBusinessInformation");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |

### Return type

ApiResponse<[**BusinessAgentBusinessInformation**](BusinessAgentBusinessInformation.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Business information |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## getBusinessAgentConnector

> BusinessAgentConnector getBusinessAgentConnector(accountId, connectorId)

Get a connector

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String connectorId = "connectorId_example"; // String | 
        try {
            BusinessAgentConnector result = apiInstance.getBusinessAgentConnector(accountId, connectorId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#getBusinessAgentConnector");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **connectorId** | **String**|  | |

### Return type

[**BusinessAgentConnector**](BusinessAgentConnector.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Connector |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## getBusinessAgentConnectorWithHttpInfo

> ApiResponse<BusinessAgentConnector> getBusinessAgentConnector getBusinessAgentConnectorWithHttpInfo(accountId, connectorId)

Get a connector

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String connectorId = "connectorId_example"; // String | 
        try {
            ApiResponse<BusinessAgentConnector> response = apiInstance.getBusinessAgentConnectorWithHttpInfo(accountId, connectorId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#getBusinessAgentConnector");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **connectorId** | **String**|  | |

### Return type

ApiResponse<[**BusinessAgentConnector**](BusinessAgentConnector.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Connector |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## getBusinessAgentConnectorLogs

> GetBusinessAgentConnectorLogs200Response getBusinessAgentConnectorLogs(accountId, connectorId, startTime, endTime, limit, toolId, includeStats, summaryOnly, topN)

Get connector failure logs

Third-party failures over the last 7 days (window at most 7 days, default the last 24 hours). Each entry carries &#x60;failure_code_name&#x60; and &#x60;error_message&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String connectorId = "connectorId_example"; // String | 
        Integer startTime = 56; // Integer | Unix seconds.
        Integer endTime = 56; // Integer | Unix seconds.
        Integer limit = 56; // Integer | 
        String toolId = "toolId_example"; // String | 
        Boolean includeStats = true; // Boolean | Add success rate and latency percentiles.
        Boolean summaryOnly = true; // Boolean | Aggregate failure patterns instead of entries.
        Integer topN = 56; // Integer | 
        try {
            GetBusinessAgentConnectorLogs200Response result = apiInstance.getBusinessAgentConnectorLogs(accountId, connectorId, startTime, endTime, limit, toolId, includeStats, summaryOnly, topN);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#getBusinessAgentConnectorLogs");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **connectorId** | **String**|  | |
| **startTime** | **Integer**| Unix seconds. | [optional] |
| **endTime** | **Integer**| Unix seconds. | [optional] |
| **limit** | **Integer**|  | [optional] |
| **toolId** | **String**|  | [optional] |
| **includeStats** | **Boolean**| Add success rate and latency percentiles. | [optional] |
| **summaryOnly** | **Boolean**| Aggregate failure patterns instead of entries. | [optional] |
| **topN** | **Integer**|  | [optional] |

### Return type

[**GetBusinessAgentConnectorLogs200Response**](GetBusinessAgentConnectorLogs200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Logs |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## getBusinessAgentConnectorLogsWithHttpInfo

> ApiResponse<GetBusinessAgentConnectorLogs200Response> getBusinessAgentConnectorLogs getBusinessAgentConnectorLogsWithHttpInfo(accountId, connectorId, startTime, endTime, limit, toolId, includeStats, summaryOnly, topN)

Get connector failure logs

Third-party failures over the last 7 days (window at most 7 days, default the last 24 hours). Each entry carries &#x60;failure_code_name&#x60; and &#x60;error_message&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String connectorId = "connectorId_example"; // String | 
        Integer startTime = 56; // Integer | Unix seconds.
        Integer endTime = 56; // Integer | Unix seconds.
        Integer limit = 56; // Integer | 
        String toolId = "toolId_example"; // String | 
        Boolean includeStats = true; // Boolean | Add success rate and latency percentiles.
        Boolean summaryOnly = true; // Boolean | Aggregate failure patterns instead of entries.
        Integer topN = 56; // Integer | 
        try {
            ApiResponse<GetBusinessAgentConnectorLogs200Response> response = apiInstance.getBusinessAgentConnectorLogsWithHttpInfo(accountId, connectorId, startTime, endTime, limit, toolId, includeStats, summaryOnly, topN);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#getBusinessAgentConnectorLogs");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **connectorId** | **String**|  | |
| **startTime** | **Integer**| Unix seconds. | [optional] |
| **endTime** | **Integer**| Unix seconds. | [optional] |
| **limit** | **Integer**|  | [optional] |
| **toolId** | **String**|  | [optional] |
| **includeStats** | **Boolean**| Add success rate and latency percentiles. | [optional] |
| **summaryOnly** | **Boolean**| Aggregate failure patterns instead of entries. | [optional] |
| **topN** | **Integer**|  | [optional] |

### Return type

ApiResponse<[**GetBusinessAgentConnectorLogs200Response**](GetBusinessAgentConnectorLogs200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Logs |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## getBusinessAgentConnectorTool

> BusinessAgentConnectorTool getBusinessAgentConnectorTool(accountId, connectorId, toolId)

Get a connector tool

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String connectorId = "connectorId_example"; // String | 
        String toolId = "toolId_example"; // String | 
        try {
            BusinessAgentConnectorTool result = apiInstance.getBusinessAgentConnectorTool(accountId, connectorId, toolId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#getBusinessAgentConnectorTool");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **connectorId** | **String**|  | |
| **toolId** | **String**|  | |

### Return type

[**BusinessAgentConnectorTool**](BusinessAgentConnectorTool.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tool |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## getBusinessAgentConnectorToolWithHttpInfo

> ApiResponse<BusinessAgentConnectorTool> getBusinessAgentConnectorTool getBusinessAgentConnectorToolWithHttpInfo(accountId, connectorId, toolId)

Get a connector tool

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String connectorId = "connectorId_example"; // String | 
        String toolId = "toolId_example"; // String | 
        try {
            ApiResponse<BusinessAgentConnectorTool> response = apiInstance.getBusinessAgentConnectorToolWithHttpInfo(accountId, connectorId, toolId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#getBusinessAgentConnectorTool");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **connectorId** | **String**|  | |
| **toolId** | **String**|  | |

### Return type

ApiResponse<[**BusinessAgentConnectorTool**](BusinessAgentConnectorTool.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tool |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## getBusinessAgentEvent

> BusinessAgentEventStatus getBusinessAgentEvent(accountId, eventId)

Get a business event status

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String eventId = "eventId_example"; // String | 
        try {
            BusinessAgentEventStatus result = apiInstance.getBusinessAgentEvent(accountId, eventId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#getBusinessAgentEvent");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **eventId** | **String**|  | |

### Return type

[**BusinessAgentEventStatus**](BusinessAgentEventStatus.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event status |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## getBusinessAgentEventWithHttpInfo

> ApiResponse<BusinessAgentEventStatus> getBusinessAgentEvent getBusinessAgentEventWithHttpInfo(accountId, eventId)

Get a business event status

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String eventId = "eventId_example"; // String | 
        try {
            ApiResponse<BusinessAgentEventStatus> response = apiInstance.getBusinessAgentEventWithHttpInfo(accountId, eventId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#getBusinessAgentEvent");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **eventId** | **String**|  | |

### Return type

ApiResponse<[**BusinessAgentEventStatus**](BusinessAgentEventStatus.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event status |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## getBusinessAgentFaq

> BusinessAgentFaq getBusinessAgentFaq(accountId, faqId)

Get a FAQ

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String faqId = "faqId_example"; // String | 
        try {
            BusinessAgentFaq result = apiInstance.getBusinessAgentFaq(accountId, faqId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#getBusinessAgentFaq");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **faqId** | **String**|  | |

### Return type

[**BusinessAgentFaq**](BusinessAgentFaq.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | FAQ |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## getBusinessAgentFaqWithHttpInfo

> ApiResponse<BusinessAgentFaq> getBusinessAgentFaq getBusinessAgentFaqWithHttpInfo(accountId, faqId)

Get a FAQ

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String faqId = "faqId_example"; // String | 
        try {
            ApiResponse<BusinessAgentFaq> response = apiInstance.getBusinessAgentFaqWithHttpInfo(accountId, faqId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#getBusinessAgentFaq");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **faqId** | **String**|  | |

### Return type

ApiResponse<[**BusinessAgentFaq**](BusinessAgentFaq.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | FAQ |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## getBusinessAgentFile

> BusinessAgentKnowledgeFile getBusinessAgentFile(accountId, fileId)

Get a knowledge file

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String fileId = "fileId_example"; // String | 
        try {
            BusinessAgentKnowledgeFile result = apiInstance.getBusinessAgentFile(accountId, fileId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#getBusinessAgentFile");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **fileId** | **String**|  | |

### Return type

[**BusinessAgentKnowledgeFile**](BusinessAgentKnowledgeFile.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | File |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## getBusinessAgentFileWithHttpInfo

> ApiResponse<BusinessAgentKnowledgeFile> getBusinessAgentFile getBusinessAgentFileWithHttpInfo(accountId, fileId)

Get a knowledge file

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String fileId = "fileId_example"; // String | 
        try {
            ApiResponse<BusinessAgentKnowledgeFile> response = apiInstance.getBusinessAgentFileWithHttpInfo(accountId, fileId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#getBusinessAgentFile");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **fileId** | **String**|  | |

### Return type

ApiResponse<[**BusinessAgentKnowledgeFile**](BusinessAgentKnowledgeFile.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | File |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## getBusinessAgentSkill

> BusinessAgentSkill getBusinessAgentSkill(accountId, skillId)

Get a skill

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String skillId = "skillId_example"; // String | 
        try {
            BusinessAgentSkill result = apiInstance.getBusinessAgentSkill(accountId, skillId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#getBusinessAgentSkill");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **skillId** | **String**|  | |

### Return type

[**BusinessAgentSkill**](BusinessAgentSkill.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Skill |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## getBusinessAgentSkillWithHttpInfo

> ApiResponse<BusinessAgentSkill> getBusinessAgentSkill getBusinessAgentSkillWithHttpInfo(accountId, skillId)

Get a skill

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String skillId = "skillId_example"; // String | 
        try {
            ApiResponse<BusinessAgentSkill> response = apiInstance.getBusinessAgentSkillWithHttpInfo(accountId, skillId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#getBusinessAgentSkill");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **skillId** | **String**|  | |

### Return type

ApiResponse<[**BusinessAgentSkill**](BusinessAgentSkill.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Skill |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## getBusinessAgentStatus

> BusinessAgentStatus getBusinessAgentStatus(accountId)

Get agent setup status

One read that says where the merchant is: whether the number is eligible, whether the Meta Business Agent terms are accepted, whether an agent exists, whether it is on, and its settings. &#x60;manualSteps&#x60; lists what Zernio can verify is still pending (accepting the terms in WhatsApp Manager); &#x60;unverifiedSteps&#x60; lists what Meta exposes no state for (the payment method in Billing Hub). Never fails for those pre-setup states; it reports them as flags. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        try {
            BusinessAgentStatus result = apiInstance.getBusinessAgentStatus(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#getBusinessAgentStatus");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |

### Return type

[**BusinessAgentStatus**](BusinessAgentStatus.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Setup status |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## getBusinessAgentStatusWithHttpInfo

> ApiResponse<BusinessAgentStatus> getBusinessAgentStatus getBusinessAgentStatusWithHttpInfo(accountId)

Get agent setup status

One read that says where the merchant is: whether the number is eligible, whether the Meta Business Agent terms are accepted, whether an agent exists, whether it is on, and its settings. &#x60;manualSteps&#x60; lists what Zernio can verify is still pending (accepting the terms in WhatsApp Manager); &#x60;unverifiedSteps&#x60; lists what Meta exposes no state for (the payment method in Billing Hub). Never fails for those pre-setup states; it reports them as flags. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        try {
            ApiResponse<BusinessAgentStatus> response = apiInstance.getBusinessAgentStatusWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#getBusinessAgentStatus");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |

### Return type

ApiResponse<[**BusinessAgentStatus**](BusinessAgentStatus.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Setup status |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## getBusinessAgentUiSkill

> BusinessAgentUiSkill getBusinessAgentUiSkill(accountId, uiSkillId)

Get a UI skill

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String uiSkillId = "uiSkillId_example"; // String | 
        try {
            BusinessAgentUiSkill result = apiInstance.getBusinessAgentUiSkill(accountId, uiSkillId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#getBusinessAgentUiSkill");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **uiSkillId** | **String**|  | |

### Return type

[**BusinessAgentUiSkill**](BusinessAgentUiSkill.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | UI skill |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## getBusinessAgentUiSkillWithHttpInfo

> ApiResponse<BusinessAgentUiSkill> getBusinessAgentUiSkill getBusinessAgentUiSkillWithHttpInfo(accountId, uiSkillId)

Get a UI skill

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String uiSkillId = "uiSkillId_example"; // String | 
        try {
            ApiResponse<BusinessAgentUiSkill> response = apiInstance.getBusinessAgentUiSkillWithHttpInfo(accountId, uiSkillId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#getBusinessAgentUiSkill");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **uiSkillId** | **String**|  | |

### Return type

ApiResponse<[**BusinessAgentUiSkill**](BusinessAgentUiSkill.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | UI skill |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## getBusinessAgentWebsite

> BusinessAgentWebsite getBusinessAgentWebsite(accountId, websiteId)

Get a crawled website

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String websiteId = "websiteId_example"; // String | 
        try {
            BusinessAgentWebsite result = apiInstance.getBusinessAgentWebsite(accountId, websiteId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#getBusinessAgentWebsite");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **websiteId** | **String**|  | |

### Return type

[**BusinessAgentWebsite**](BusinessAgentWebsite.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Website |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## getBusinessAgentWebsiteWithHttpInfo

> ApiResponse<BusinessAgentWebsite> getBusinessAgentWebsite getBusinessAgentWebsiteWithHttpInfo(accountId, websiteId)

Get a crawled website

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String websiteId = "websiteId_example"; // String | 
        try {
            ApiResponse<BusinessAgentWebsite> response = apiInstance.getBusinessAgentWebsiteWithHttpInfo(accountId, websiteId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#getBusinessAgentWebsite");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **websiteId** | **String**|  | |

### Return type

ApiResponse<[**BusinessAgentWebsite**](BusinessAgentWebsite.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Website |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## listBusinessAgentAllowlist

> ListBusinessAgentAllowlist200Response listBusinessAgentAllowlist(accountId)

List allowlisted consumers

Consumers the agent answers while &#x60;ai_audience&#x60; is ALLOWLISTED_ONLY.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        try {
            ListBusinessAgentAllowlist200Response result = apiInstance.listBusinessAgentAllowlist(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#listBusinessAgentAllowlist");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |

### Return type

[**ListBusinessAgentAllowlist200Response**](ListBusinessAgentAllowlist200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Allowlist |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## listBusinessAgentAllowlistWithHttpInfo

> ApiResponse<ListBusinessAgentAllowlist200Response> listBusinessAgentAllowlist listBusinessAgentAllowlistWithHttpInfo(accountId)

List allowlisted consumers

Consumers the agent answers while &#x60;ai_audience&#x60; is ALLOWLISTED_ONLY.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        try {
            ApiResponse<ListBusinessAgentAllowlist200Response> response = apiInstance.listBusinessAgentAllowlistWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#listBusinessAgentAllowlist");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |

### Return type

ApiResponse<[**ListBusinessAgentAllowlist200Response**](ListBusinessAgentAllowlist200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Allowlist |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## listBusinessAgentConnectorTools

> ListBusinessAgentConnectorTools200Response listBusinessAgentConnectorTools(accountId, connectorId)

List connector tools

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String connectorId = "connectorId_example"; // String | 
        try {
            ListBusinessAgentConnectorTools200Response result = apiInstance.listBusinessAgentConnectorTools(accountId, connectorId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#listBusinessAgentConnectorTools");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **connectorId** | **String**|  | |

### Return type

[**ListBusinessAgentConnectorTools200Response**](ListBusinessAgentConnectorTools200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tools |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## listBusinessAgentConnectorToolsWithHttpInfo

> ApiResponse<ListBusinessAgentConnectorTools200Response> listBusinessAgentConnectorTools listBusinessAgentConnectorToolsWithHttpInfo(accountId, connectorId)

List connector tools

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String connectorId = "connectorId_example"; // String | 
        try {
            ApiResponse<ListBusinessAgentConnectorTools200Response> response = apiInstance.listBusinessAgentConnectorToolsWithHttpInfo(accountId, connectorId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#listBusinessAgentConnectorTools");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **connectorId** | **String**|  | |

### Return type

ApiResponse<[**ListBusinessAgentConnectorTools200Response**](ListBusinessAgentConnectorTools200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tools |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## listBusinessAgentConnectors

> ListBusinessAgentConnectors200Response listBusinessAgentConnectors(accountId)

List connectors

External APIs the agent may call. &#x60;connection_status&#x60; says whether Meta can currently reach each one.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        try {
            ListBusinessAgentConnectors200Response result = apiInstance.listBusinessAgentConnectors(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#listBusinessAgentConnectors");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |

### Return type

[**ListBusinessAgentConnectors200Response**](ListBusinessAgentConnectors200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Connectors |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## listBusinessAgentConnectorsWithHttpInfo

> ApiResponse<ListBusinessAgentConnectors200Response> listBusinessAgentConnectors listBusinessAgentConnectorsWithHttpInfo(accountId)

List connectors

External APIs the agent may call. &#x60;connection_status&#x60; says whether Meta can currently reach each one.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        try {
            ApiResponse<ListBusinessAgentConnectors200Response> response = apiInstance.listBusinessAgentConnectorsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#listBusinessAgentConnectors");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |

### Return type

ApiResponse<[**ListBusinessAgentConnectors200Response**](ListBusinessAgentConnectors200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Connectors |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## listBusinessAgentFaqs

> ListBusinessAgentFaqs200Response listBusinessAgentFaqs(accountId)

List FAQs

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        try {
            ListBusinessAgentFaqs200Response result = apiInstance.listBusinessAgentFaqs(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#listBusinessAgentFaqs");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |

### Return type

[**ListBusinessAgentFaqs200Response**](ListBusinessAgentFaqs200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | FAQs |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## listBusinessAgentFaqsWithHttpInfo

> ApiResponse<ListBusinessAgentFaqs200Response> listBusinessAgentFaqs listBusinessAgentFaqsWithHttpInfo(accountId)

List FAQs

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        try {
            ApiResponse<ListBusinessAgentFaqs200Response> response = apiInstance.listBusinessAgentFaqsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#listBusinessAgentFaqs");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |

### Return type

ApiResponse<[**ListBusinessAgentFaqs200Response**](ListBusinessAgentFaqs200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | FAQs |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## listBusinessAgentFiles

> ListBusinessAgentFiles200Response listBusinessAgentFiles(accountId)

List knowledge files

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        try {
            ListBusinessAgentFiles200Response result = apiInstance.listBusinessAgentFiles(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#listBusinessAgentFiles");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |

### Return type

[**ListBusinessAgentFiles200Response**](ListBusinessAgentFiles200Response.md)


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
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## listBusinessAgentFilesWithHttpInfo

> ApiResponse<ListBusinessAgentFiles200Response> listBusinessAgentFiles listBusinessAgentFilesWithHttpInfo(accountId)

List knowledge files

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        try {
            ApiResponse<ListBusinessAgentFiles200Response> response = apiInstance.listBusinessAgentFilesWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#listBusinessAgentFiles");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |

### Return type

ApiResponse<[**ListBusinessAgentFiles200Response**](ListBusinessAgentFiles200Response.md)>


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
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## listBusinessAgentSettings

> ListBusinessAgentSettings200Response listBusinessAgentSettings(accountId, agentId)

List agent settings

Settings of every agent configured on the number (normally one). Pass &#x60;agentId&#x60; to read one.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String agentId = "agentId_example"; // String | 
        try {
            ListBusinessAgentSettings200Response result = apiInstance.listBusinessAgentSettings(accountId, agentId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#listBusinessAgentSettings");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **agentId** | **String**|  | [optional] |

### Return type

[**ListBusinessAgentSettings200Response**](ListBusinessAgentSettings200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Settings |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## listBusinessAgentSettingsWithHttpInfo

> ApiResponse<ListBusinessAgentSettings200Response> listBusinessAgentSettings listBusinessAgentSettingsWithHttpInfo(accountId, agentId)

List agent settings

Settings of every agent configured on the number (normally one). Pass &#x60;agentId&#x60; to read one.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String agentId = "agentId_example"; // String | 
        try {
            ApiResponse<ListBusinessAgentSettings200Response> response = apiInstance.listBusinessAgentSettingsWithHttpInfo(accountId, agentId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#listBusinessAgentSettings");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **agentId** | **String**|  | [optional] |

### Return type

ApiResponse<[**ListBusinessAgentSettings200Response**](ListBusinessAgentSettings200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Settings |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## listBusinessAgentSkills

> ListBusinessAgentSkills200Response listBusinessAgentSkills(accountId)

List skills

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        try {
            ListBusinessAgentSkills200Response result = apiInstance.listBusinessAgentSkills(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#listBusinessAgentSkills");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |

### Return type

[**ListBusinessAgentSkills200Response**](ListBusinessAgentSkills200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Skills |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## listBusinessAgentSkillsWithHttpInfo

> ApiResponse<ListBusinessAgentSkills200Response> listBusinessAgentSkills listBusinessAgentSkillsWithHttpInfo(accountId)

List skills

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        try {
            ApiResponse<ListBusinessAgentSkills200Response> response = apiInstance.listBusinessAgentSkillsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#listBusinessAgentSkills");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |

### Return type

ApiResponse<[**ListBusinessAgentSkills200Response**](ListBusinessAgentSkills200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Skills |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## listBusinessAgentUiSkills

> ListBusinessAgentUiSkills200Response listBusinessAgentUiSkills(accountId, before, after, limit)

List UI skills

Cursor paged; follow &#x60;paging.cursors.after&#x60; until &#x60;paging.next&#x60; is absent.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String before = "before_example"; // String | 
        String after = "after_example"; // String | 
        Integer limit = 56; // Integer | 
        try {
            ListBusinessAgentUiSkills200Response result = apiInstance.listBusinessAgentUiSkills(accountId, before, after, limit);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#listBusinessAgentUiSkills");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **before** | **String**|  | [optional] |
| **after** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |

### Return type

[**ListBusinessAgentUiSkills200Response**](ListBusinessAgentUiSkills200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | UI skills |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## listBusinessAgentUiSkillsWithHttpInfo

> ApiResponse<ListBusinessAgentUiSkills200Response> listBusinessAgentUiSkills listBusinessAgentUiSkillsWithHttpInfo(accountId, before, after, limit)

List UI skills

Cursor paged; follow &#x60;paging.cursors.after&#x60; until &#x60;paging.next&#x60; is absent.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String before = "before_example"; // String | 
        String after = "after_example"; // String | 
        Integer limit = 56; // Integer | 
        try {
            ApiResponse<ListBusinessAgentUiSkills200Response> response = apiInstance.listBusinessAgentUiSkillsWithHttpInfo(accountId, before, after, limit);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#listBusinessAgentUiSkills");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **before** | **String**|  | [optional] |
| **after** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] |

### Return type

ApiResponse<[**ListBusinessAgentUiSkills200Response**](ListBusinessAgentUiSkills200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | UI skills |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## listBusinessAgentWebsites

> ListBusinessAgentWebsites200Response listBusinessAgentWebsites(accountId)

List crawled websites

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        try {
            ListBusinessAgentWebsites200Response result = apiInstance.listBusinessAgentWebsites(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#listBusinessAgentWebsites");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |

### Return type

[**ListBusinessAgentWebsites200Response**](ListBusinessAgentWebsites200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Websites |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## listBusinessAgentWebsitesWithHttpInfo

> ApiResponse<ListBusinessAgentWebsites200Response> listBusinessAgentWebsites listBusinessAgentWebsitesWithHttpInfo(accountId)

List crawled websites

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        try {
            ApiResponse<ListBusinessAgentWebsites200Response> response = apiInstance.listBusinessAgentWebsitesWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#listBusinessAgentWebsites");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |

### Return type

ApiResponse<[**ListBusinessAgentWebsites200Response**](ListBusinessAgentWebsites200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Websites |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## onboardBusinessAgent

> OnboardBusinessAgent201Response onboardBusinessAgent(accountId)

Create the agent

Creates the Meta Business Agent on the number and schedules Meta&#39;s data preparation. Requires the terms to be accepted; eligibility is checked first and an ineligible number answers 403 &#x60;business_agent_not_eligible&#x60;. Not idempotent: call it once, then configure knowledge and skills, then enable it through the settings. Configuration calls made in the first minute can still answer &#x60;business_agent_not_found&#x60; while Meta prepares the workspace. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        try {
            OnboardBusinessAgent201Response result = apiInstance.onboardBusinessAgent(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#onboardBusinessAgent");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |

### Return type

[**OnboardBusinessAgent201Response**](OnboardBusinessAgent201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Agent created |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |
| **409** | Meta rejected the state change (code business_agent_conflict). |  -  |

## onboardBusinessAgentWithHttpInfo

> ApiResponse<OnboardBusinessAgent201Response> onboardBusinessAgent onboardBusinessAgentWithHttpInfo(accountId)

Create the agent

Creates the Meta Business Agent on the number and schedules Meta&#39;s data preparation. Requires the terms to be accepted; eligibility is checked first and an ineligible number answers 403 &#x60;business_agent_not_eligible&#x60;. Not idempotent: call it once, then configure knowledge and skills, then enable it through the settings. Configuration calls made in the first minute can still answer &#x60;business_agent_not_found&#x60; while Meta prepares the workspace. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        try {
            ApiResponse<OnboardBusinessAgent201Response> response = apiInstance.onboardBusinessAgentWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#onboardBusinessAgent");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |

### Return type

ApiResponse<[**OnboardBusinessAgent201Response**](OnboardBusinessAgent201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Agent created |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |
| **409** | Meta rejected the state change (code business_agent_conflict). |  -  |


## readBusinessAgentEvals

> Map<String, Object> readBusinessAgentEvals(accountId, jobId, summaryIds, evalIds)

Read evaluation data

Without query parameters, lists the evaluation scenarios (&#x60;eval_cases&#x60;). With &#x60;jobId&#x60;, polls a run started with POST. With &#x60;summaryIds&#x60;, returns the aggregated insight reports. With &#x60;evalIds&#x60;, returns per-conversation evaluation details. One of the three at a time. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String jobId = "jobId_example"; // String | 
        String summaryIds = "summaryIds_example"; // String | Comma-separated summary ids.
        String evalIds = "evalIds_example"; // String | Comma-separated evaluation ids.
        try {
            Map<String, Object> result = apiInstance.readBusinessAgentEvals(accountId, jobId, summaryIds, evalIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#readBusinessAgentEvals");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **jobId** | **String**|  | [optional] |
| **summaryIds** | **String**| Comma-separated summary ids. | [optional] |
| **evalIds** | **String**| Comma-separated evaluation ids. | [optional] |

### Return type

**Map&lt;String, Object&gt;**


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Evaluation data as Meta returns it for the selected read |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## readBusinessAgentEvalsWithHttpInfo

> ApiResponse<Map<String, Object>> readBusinessAgentEvals readBusinessAgentEvalsWithHttpInfo(accountId, jobId, summaryIds, evalIds)

Read evaluation data

Without query parameters, lists the evaluation scenarios (&#x60;eval_cases&#x60;). With &#x60;jobId&#x60;, polls a run started with POST. With &#x60;summaryIds&#x60;, returns the aggregated insight reports. With &#x60;evalIds&#x60;, returns per-conversation evaluation details. One of the three at a time. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String jobId = "jobId_example"; // String | 
        String summaryIds = "summaryIds_example"; // String | Comma-separated summary ids.
        String evalIds = "evalIds_example"; // String | Comma-separated evaluation ids.
        try {
            ApiResponse<Map<String, Object>> response = apiInstance.readBusinessAgentEvalsWithHttpInfo(accountId, jobId, summaryIds, evalIds);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#readBusinessAgentEvals");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **jobId** | **String**|  | [optional] |
| **summaryIds** | **String**| Comma-separated summary ids. | [optional] |
| **evalIds** | **String**| Comma-separated evaluation ids. | [optional] |

### Return type

ApiResponse<**Map&lt;String, Object&gt;**>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Evaluation data as Meta returns it for the selected read |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## refreshBusinessAgentConnectorTools

> BusinessAgentConnector refreshBusinessAgentConnectorTools(accountId, connectorId)

Refresh MCP connector tools

Re-discovers the tools of an MCP connector. A failed discovery keeps the previous tool set and reports an ERROR sync status inside a 200.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String connectorId = "connectorId_example"; // String | 
        try {
            BusinessAgentConnector result = apiInstance.refreshBusinessAgentConnectorTools(accountId, connectorId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#refreshBusinessAgentConnectorTools");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **connectorId** | **String**|  | |

### Return type

[**BusinessAgentConnector**](BusinessAgentConnector.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Connector with updated tool sync metadata |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## refreshBusinessAgentConnectorToolsWithHttpInfo

> ApiResponse<BusinessAgentConnector> refreshBusinessAgentConnectorTools refreshBusinessAgentConnectorToolsWithHttpInfo(accountId, connectorId)

Refresh MCP connector tools

Re-discovers the tools of an MCP connector. A failed discovery keeps the previous tool set and reports an ERROR sync status inside a 200.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String connectorId = "connectorId_example"; // String | 
        try {
            ApiResponse<BusinessAgentConnector> response = apiInstance.refreshBusinessAgentConnectorToolsWithHttpInfo(accountId, connectorId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#refreshBusinessAgentConnectorTools");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **connectorId** | **String**|  | |

### Return type

ApiResponse<[**BusinessAgentConnector**](BusinessAgentConnector.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Connector with updated tool sync metadata |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## removeBusinessAgentAllowlistEntry

> InlineObject removeBusinessAgentAllowlistEntry(accountId, entryId)

Remove an allowlisted consumer

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String entryId = "entryId_example"; // String | 
        try {
            InlineObject result = apiInstance.removeBusinessAgentAllowlistEntry(accountId, entryId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#removeBusinessAgentAllowlistEntry");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **entryId** | **String**|  | |

### Return type

[**InlineObject**](InlineObject.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## removeBusinessAgentAllowlistEntryWithHttpInfo

> ApiResponse<InlineObject> removeBusinessAgentAllowlistEntry removeBusinessAgentAllowlistEntryWithHttpInfo(accountId, entryId)

Remove an allowlisted consumer

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String entryId = "entryId_example"; // String | 
        try {
            ApiResponse<InlineObject> response = apiInstance.removeBusinessAgentAllowlistEntryWithHttpInfo(accountId, entryId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#removeBusinessAgentAllowlistEntry");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **entryId** | **String**|  | |

### Return type

ApiResponse<[**InlineObject**](InlineObject.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## replaceBusinessAgentBudget

> GetBusinessAgentBudget200Response replaceBusinessAgentBudget(accountId, getBusinessAgentBudget200Response)

Replace usage budgets

The full desired set: budgets left out are removed, an empty list returns to unlimited. Pass &#x60;budget_id&#x60; to edit one in place. When a cap is hit the agent finishes its turn, stops answering and hands the thread to a human until the window rolls over.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        GetBusinessAgentBudget200Response getBusinessAgentBudget200Response = new GetBusinessAgentBudget200Response(); // GetBusinessAgentBudget200Response | 
        try {
            GetBusinessAgentBudget200Response result = apiInstance.replaceBusinessAgentBudget(accountId, getBusinessAgentBudget200Response);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#replaceBusinessAgentBudget");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **getBusinessAgentBudget200Response** | [**GetBusinessAgentBudget200Response**](GetBusinessAgentBudget200Response.md)|  | |

### Return type

[**GetBusinessAgentBudget200Response**](GetBusinessAgentBudget200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Budgets after the update |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## replaceBusinessAgentBudgetWithHttpInfo

> ApiResponse<GetBusinessAgentBudget200Response> replaceBusinessAgentBudget replaceBusinessAgentBudgetWithHttpInfo(accountId, getBusinessAgentBudget200Response)

Replace usage budgets

The full desired set: budgets left out are removed, an empty list returns to unlimited. Pass &#x60;budget_id&#x60; to edit one in place. When a cap is hit the agent finishes its turn, stops answering and hands the thread to a human until the window rolls over.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        GetBusinessAgentBudget200Response getBusinessAgentBudget200Response = new GetBusinessAgentBudget200Response(); // GetBusinessAgentBudget200Response | 
        try {
            ApiResponse<GetBusinessAgentBudget200Response> response = apiInstance.replaceBusinessAgentBudgetWithHttpInfo(accountId, getBusinessAgentBudget200Response);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#replaceBusinessAgentBudget");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **getBusinessAgentBudget200Response** | [**GetBusinessAgentBudget200Response**](GetBusinessAgentBudget200Response.md)|  | |

### Return type

ApiResponse<[**GetBusinessAgentBudget200Response**](GetBusinessAgentBudget200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Budgets after the update |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## replaceBusinessAgentBusinessInformation

> BusinessAgentBusinessInformation replaceBusinessAgentBusinessInformation(accountId, businessAgentBusinessInformation)

Replace business information

Full replacement: every field you send overwrites the stored value; fields you omit are cleared.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        BusinessAgentBusinessInformation businessAgentBusinessInformation = new BusinessAgentBusinessInformation(); // BusinessAgentBusinessInformation | 
        try {
            BusinessAgentBusinessInformation result = apiInstance.replaceBusinessAgentBusinessInformation(accountId, businessAgentBusinessInformation);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#replaceBusinessAgentBusinessInformation");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **businessAgentBusinessInformation** | [**BusinessAgentBusinessInformation**](BusinessAgentBusinessInformation.md)|  | |

### Return type

[**BusinessAgentBusinessInformation**](BusinessAgentBusinessInformation.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Stored business information |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## replaceBusinessAgentBusinessInformationWithHttpInfo

> ApiResponse<BusinessAgentBusinessInformation> replaceBusinessAgentBusinessInformation replaceBusinessAgentBusinessInformationWithHttpInfo(accountId, businessAgentBusinessInformation)

Replace business information

Full replacement: every field you send overwrites the stored value; fields you omit are cleared.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        BusinessAgentBusinessInformation businessAgentBusinessInformation = new BusinessAgentBusinessInformation(); // BusinessAgentBusinessInformation | 
        try {
            ApiResponse<BusinessAgentBusinessInformation> response = apiInstance.replaceBusinessAgentBusinessInformationWithHttpInfo(accountId, businessAgentBusinessInformation);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#replaceBusinessAgentBusinessInformation");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **businessAgentBusinessInformation** | [**BusinessAgentBusinessInformation**](BusinessAgentBusinessInformation.md)|  | |

### Return type

ApiResponse<[**BusinessAgentBusinessInformation**](BusinessAgentBusinessInformation.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Stored business information |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## resetBusinessAgentBusinessInformation

> InlineObject resetBusinessAgentBusinessInformation(accountId)

Reset business information

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        try {
            InlineObject result = apiInstance.resetBusinessAgentBusinessInformation(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#resetBusinessAgentBusinessInformation");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |

### Return type

[**InlineObject**](InlineObject.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## resetBusinessAgentBusinessInformationWithHttpInfo

> ApiResponse<InlineObject> resetBusinessAgentBusinessInformation resetBusinessAgentBusinessInformationWithHttpInfo(accountId)

Reset business information

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        try {
            ApiResponse<InlineObject> response = apiInstance.resetBusinessAgentBusinessInformationWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#resetBusinessAgentBusinessInformation");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |

### Return type

ApiResponse<[**InlineObject**](InlineObject.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deleted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## runBusinessAgentConnectorTool

> RunBusinessAgentConnectorTool200Response runBusinessAgentConnectorTool(accountId, connectorId, toolId, runBusinessAgentConnectorToolRequest)

Run a connector tool once

Executes the tool against the merchant API and returns the raw upstream result, to check a connector before the agent relies on it.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String connectorId = "connectorId_example"; // String | 
        String toolId = "toolId_example"; // String | 
        RunBusinessAgentConnectorToolRequest runBusinessAgentConnectorToolRequest = new RunBusinessAgentConnectorToolRequest(); // RunBusinessAgentConnectorToolRequest | 
        try {
            RunBusinessAgentConnectorTool200Response result = apiInstance.runBusinessAgentConnectorTool(accountId, connectorId, toolId, runBusinessAgentConnectorToolRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#runBusinessAgentConnectorTool");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **connectorId** | **String**|  | |
| **toolId** | **String**|  | |
| **runBusinessAgentConnectorToolRequest** | [**RunBusinessAgentConnectorToolRequest**](RunBusinessAgentConnectorToolRequest.md)|  | |

### Return type

[**RunBusinessAgentConnectorTool200Response**](RunBusinessAgentConnectorTool200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tool result |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## runBusinessAgentConnectorToolWithHttpInfo

> ApiResponse<RunBusinessAgentConnectorTool200Response> runBusinessAgentConnectorTool runBusinessAgentConnectorToolWithHttpInfo(accountId, connectorId, toolId, runBusinessAgentConnectorToolRequest)

Run a connector tool once

Executes the tool against the merchant API and returns the raw upstream result, to check a connector before the agent relies on it.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String connectorId = "connectorId_example"; // String | 
        String toolId = "toolId_example"; // String | 
        RunBusinessAgentConnectorToolRequest runBusinessAgentConnectorToolRequest = new RunBusinessAgentConnectorToolRequest(); // RunBusinessAgentConnectorToolRequest | 
        try {
            ApiResponse<RunBusinessAgentConnectorTool200Response> response = apiInstance.runBusinessAgentConnectorToolWithHttpInfo(accountId, connectorId, toolId, runBusinessAgentConnectorToolRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#runBusinessAgentConnectorTool");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **connectorId** | **String**|  | |
| **toolId** | **String**|  | |
| **runBusinessAgentConnectorToolRequest** | [**RunBusinessAgentConnectorToolRequest**](RunBusinessAgentConnectorToolRequest.md)|  | |

### Return type

ApiResponse<[**RunBusinessAgentConnectorTool200Response**](RunBusinessAgentConnectorTool200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tool result |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## sendBusinessAgentEvent

> SendBusinessAgentEvent202Response sendBusinessAgentEvent(accountId, sendBusinessAgentEventRequest)

Send a business event

Tell the agent something happened in your systems (order shipped, document verified) so it messages the consumer about it. The consumer must already have a conversation with the number. Answers 202 with the event id; poll it for the outcome.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        SendBusinessAgentEventRequest sendBusinessAgentEventRequest = new SendBusinessAgentEventRequest(); // SendBusinessAgentEventRequest | 
        try {
            SendBusinessAgentEvent202Response result = apiInstance.sendBusinessAgentEvent(accountId, sendBusinessAgentEventRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#sendBusinessAgentEvent");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **sendBusinessAgentEventRequest** | [**SendBusinessAgentEventRequest**](SendBusinessAgentEventRequest.md)|  | |

### Return type

[**SendBusinessAgentEvent202Response**](SendBusinessAgentEvent202Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Event accepted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## sendBusinessAgentEventWithHttpInfo

> ApiResponse<SendBusinessAgentEvent202Response> sendBusinessAgentEvent sendBusinessAgentEventWithHttpInfo(accountId, sendBusinessAgentEventRequest)

Send a business event

Tell the agent something happened in your systems (order shipped, document verified) so it messages the consumer about it. The consumer must already have a conversation with the number. Answers 202 with the event id; poll it for the outcome.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        SendBusinessAgentEventRequest sendBusinessAgentEventRequest = new SendBusinessAgentEventRequest(); // SendBusinessAgentEventRequest | 
        try {
            ApiResponse<SendBusinessAgentEvent202Response> response = apiInstance.sendBusinessAgentEventWithHttpInfo(accountId, sendBusinessAgentEventRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#sendBusinessAgentEvent");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **sendBusinessAgentEventRequest** | [**SendBusinessAgentEventRequest**](SendBusinessAgentEventRequest.md)|  | |

### Return type

ApiResponse<[**SendBusinessAgentEvent202Response**](SendBusinessAgentEvent202Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Event accepted |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## sendBusinessAgentTestMessage

> BusinessAgentTestMessageResponse sendBusinessAgentTestMessage(accountId, sendBusinessAgentTestMessageRequest)

Send a test message

Runs the message through the full agent pipeline in Meta sandbox with no WhatsApp user and no token billing. Pass back &#x60;conversationId&#x60; to continue a thread. Meta rate-limits it per number per hour.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        SendBusinessAgentTestMessageRequest sendBusinessAgentTestMessageRequest = new SendBusinessAgentTestMessageRequest(); // SendBusinessAgentTestMessageRequest | 
        try {
            BusinessAgentTestMessageResponse result = apiInstance.sendBusinessAgentTestMessage(accountId, sendBusinessAgentTestMessageRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#sendBusinessAgentTestMessage");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **sendBusinessAgentTestMessageRequest** | [**SendBusinessAgentTestMessageRequest**](SendBusinessAgentTestMessageRequest.md)|  | |

### Return type

[**BusinessAgentTestMessageResponse**](BusinessAgentTestMessageResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Agent reply |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |
| **429** | Meta hourly test-message limit reached (code rate_limited, Retry-After when known). |  -  |

## sendBusinessAgentTestMessageWithHttpInfo

> ApiResponse<BusinessAgentTestMessageResponse> sendBusinessAgentTestMessage sendBusinessAgentTestMessageWithHttpInfo(accountId, sendBusinessAgentTestMessageRequest)

Send a test message

Runs the message through the full agent pipeline in Meta sandbox with no WhatsApp user and no token billing. Pass back &#x60;conversationId&#x60; to continue a thread. Meta rate-limits it per number per hour.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        SendBusinessAgentTestMessageRequest sendBusinessAgentTestMessageRequest = new SendBusinessAgentTestMessageRequest(); // SendBusinessAgentTestMessageRequest | 
        try {
            ApiResponse<BusinessAgentTestMessageResponse> response = apiInstance.sendBusinessAgentTestMessageWithHttpInfo(accountId, sendBusinessAgentTestMessageRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#sendBusinessAgentTestMessage");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **sendBusinessAgentTestMessageRequest** | [**SendBusinessAgentTestMessageRequest**](SendBusinessAgentTestMessageRequest.md)|  | |

### Return type

ApiResponse<[**BusinessAgentTestMessageResponse**](BusinessAgentTestMessageResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Agent reply |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |
| **429** | Meta hourly test-message limit reached (code rate_limited, Retry-After when known). |  -  |


## setBusinessAgentConnectorCredentials

> BusinessAgentConnector setBusinessAgentConnectorCredentials(accountId, connectorId, setBusinessAgentConnectorCredentialsRequest)

Set connector credentials

Set or rotate the connector&#39;s credentials in place: &#x60;kind: api_key&#x60;, &#x60;kind: oauth&#x60; (client credentials) or &#x60;kind: certificate&#x60; (mTLS client certificate). Meta has no call that removes a credential layer; change the connector&#39;s &#x60;auth_type&#x60; or delete it instead. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String connectorId = "connectorId_example"; // String | 
        SetBusinessAgentConnectorCredentialsRequest setBusinessAgentConnectorCredentialsRequest = new SetBusinessAgentConnectorCredentialsRequest(); // SetBusinessAgentConnectorCredentialsRequest | 
        try {
            BusinessAgentConnector result = apiInstance.setBusinessAgentConnectorCredentials(accountId, connectorId, setBusinessAgentConnectorCredentialsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#setBusinessAgentConnectorCredentials");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **connectorId** | **String**|  | |
| **setBusinessAgentConnectorCredentialsRequest** | [**SetBusinessAgentConnectorCredentialsRequest**](SetBusinessAgentConnectorCredentialsRequest.md)|  | |

### Return type

[**BusinessAgentConnector**](BusinessAgentConnector.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Connector with the new credential metadata |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## setBusinessAgentConnectorCredentialsWithHttpInfo

> ApiResponse<BusinessAgentConnector> setBusinessAgentConnectorCredentials setBusinessAgentConnectorCredentialsWithHttpInfo(accountId, connectorId, setBusinessAgentConnectorCredentialsRequest)

Set connector credentials

Set or rotate the connector&#39;s credentials in place: &#x60;kind: api_key&#x60;, &#x60;kind: oauth&#x60; (client credentials) or &#x60;kind: certificate&#x60; (mTLS client certificate). Meta has no call that removes a credential layer; change the connector&#39;s &#x60;auth_type&#x60; or delete it instead. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String connectorId = "connectorId_example"; // String | 
        SetBusinessAgentConnectorCredentialsRequest setBusinessAgentConnectorCredentialsRequest = new SetBusinessAgentConnectorCredentialsRequest(); // SetBusinessAgentConnectorCredentialsRequest | 
        try {
            ApiResponse<BusinessAgentConnector> response = apiInstance.setBusinessAgentConnectorCredentialsWithHttpInfo(accountId, connectorId, setBusinessAgentConnectorCredentialsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#setBusinessAgentConnectorCredentials");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **connectorId** | **String**|  | |
| **setBusinessAgentConnectorCredentialsRequest** | [**SetBusinessAgentConnectorCredentialsRequest**](SetBusinessAgentConnectorCredentialsRequest.md)|  | |

### Return type

ApiResponse<[**BusinessAgentConnector**](BusinessAgentConnector.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Connector with the new credential metadata |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## startBusinessAgentEvalRun

> StartBusinessAgentEvalRun202Response startBusinessAgentEvalRun(accountId, startBusinessAgentEvalRunRequest)

Start an evaluation run

Simulates the given scenarios against the agent and scores them. Answers 202 with a &#x60;job_id&#x60; to poll with GET.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        StartBusinessAgentEvalRunRequest startBusinessAgentEvalRunRequest = new StartBusinessAgentEvalRunRequest(); // StartBusinessAgentEvalRunRequest | 
        try {
            StartBusinessAgentEvalRun202Response result = apiInstance.startBusinessAgentEvalRun(accountId, startBusinessAgentEvalRunRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#startBusinessAgentEvalRun");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **startBusinessAgentEvalRunRequest** | [**StartBusinessAgentEvalRunRequest**](StartBusinessAgentEvalRunRequest.md)|  | |

### Return type

[**StartBusinessAgentEvalRun202Response**](StartBusinessAgentEvalRun202Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Run started |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## startBusinessAgentEvalRunWithHttpInfo

> ApiResponse<StartBusinessAgentEvalRun202Response> startBusinessAgentEvalRun startBusinessAgentEvalRunWithHttpInfo(accountId, startBusinessAgentEvalRunRequest)

Start an evaluation run

Simulates the given scenarios against the agent and scores them. Answers 202 with a &#x60;job_id&#x60; to poll with GET.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        StartBusinessAgentEvalRunRequest startBusinessAgentEvalRunRequest = new StartBusinessAgentEvalRunRequest(); // StartBusinessAgentEvalRunRequest | 
        try {
            ApiResponse<StartBusinessAgentEvalRun202Response> response = apiInstance.startBusinessAgentEvalRunWithHttpInfo(accountId, startBusinessAgentEvalRunRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#startBusinessAgentEvalRun");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **startBusinessAgentEvalRunRequest** | [**StartBusinessAgentEvalRunRequest**](StartBusinessAgentEvalRunRequest.md)|  | |

### Return type

ApiResponse<[**StartBusinessAgentEvalRun202Response**](StartBusinessAgentEvalRun202Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Run started |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## updateBusinessAgentConnector

> BusinessAgentConnector updateBusinessAgentConnector(accountId, connectorId, businessAgentConnectorInput)

Update a connector

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String connectorId = "connectorId_example"; // String | 
        BusinessAgentConnectorInput businessAgentConnectorInput = new BusinessAgentConnectorInput(); // BusinessAgentConnectorInput | 
        try {
            BusinessAgentConnector result = apiInstance.updateBusinessAgentConnector(accountId, connectorId, businessAgentConnectorInput);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#updateBusinessAgentConnector");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **connectorId** | **String**|  | |
| **businessAgentConnectorInput** | [**BusinessAgentConnectorInput**](BusinessAgentConnectorInput.md)|  | |

### Return type

[**BusinessAgentConnector**](BusinessAgentConnector.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Connector updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## updateBusinessAgentConnectorWithHttpInfo

> ApiResponse<BusinessAgentConnector> updateBusinessAgentConnector updateBusinessAgentConnectorWithHttpInfo(accountId, connectorId, businessAgentConnectorInput)

Update a connector

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String connectorId = "connectorId_example"; // String | 
        BusinessAgentConnectorInput businessAgentConnectorInput = new BusinessAgentConnectorInput(); // BusinessAgentConnectorInput | 
        try {
            ApiResponse<BusinessAgentConnector> response = apiInstance.updateBusinessAgentConnectorWithHttpInfo(accountId, connectorId, businessAgentConnectorInput);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#updateBusinessAgentConnector");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **connectorId** | **String**|  | |
| **businessAgentConnectorInput** | [**BusinessAgentConnectorInput**](BusinessAgentConnectorInput.md)|  | |

### Return type

ApiResponse<[**BusinessAgentConnector**](BusinessAgentConnector.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Connector updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## updateBusinessAgentConnectorTool

> BusinessAgentConnectorTool updateBusinessAgentConnectorTool(accountId, connectorId, toolId, businessAgentConnectorToolInput)

Update a connector tool

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String connectorId = "connectorId_example"; // String | 
        String toolId = "toolId_example"; // String | 
        BusinessAgentConnectorToolInput businessAgentConnectorToolInput = new BusinessAgentConnectorToolInput(); // BusinessAgentConnectorToolInput | 
        try {
            BusinessAgentConnectorTool result = apiInstance.updateBusinessAgentConnectorTool(accountId, connectorId, toolId, businessAgentConnectorToolInput);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#updateBusinessAgentConnectorTool");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **connectorId** | **String**|  | |
| **toolId** | **String**|  | |
| **businessAgentConnectorToolInput** | [**BusinessAgentConnectorToolInput**](BusinessAgentConnectorToolInput.md)|  | |

### Return type

[**BusinessAgentConnectorTool**](BusinessAgentConnectorTool.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tool updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## updateBusinessAgentConnectorToolWithHttpInfo

> ApiResponse<BusinessAgentConnectorTool> updateBusinessAgentConnectorTool updateBusinessAgentConnectorToolWithHttpInfo(accountId, connectorId, toolId, businessAgentConnectorToolInput)

Update a connector tool

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String connectorId = "connectorId_example"; // String | 
        String toolId = "toolId_example"; // String | 
        BusinessAgentConnectorToolInput businessAgentConnectorToolInput = new BusinessAgentConnectorToolInput(); // BusinessAgentConnectorToolInput | 
        try {
            ApiResponse<BusinessAgentConnectorTool> response = apiInstance.updateBusinessAgentConnectorToolWithHttpInfo(accountId, connectorId, toolId, businessAgentConnectorToolInput);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#updateBusinessAgentConnectorTool");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **connectorId** | **String**|  | |
| **toolId** | **String**|  | |
| **businessAgentConnectorToolInput** | [**BusinessAgentConnectorToolInput**](BusinessAgentConnectorToolInput.md)|  | |

### Return type

ApiResponse<[**BusinessAgentConnectorTool**](BusinessAgentConnectorTool.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tool updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## updateBusinessAgentFaq

> BusinessAgentFaq updateBusinessAgentFaq(accountId, faqId, businessAgentFaqInput)

Update a FAQ

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String faqId = "faqId_example"; // String | 
        BusinessAgentFaqInput businessAgentFaqInput = new BusinessAgentFaqInput(); // BusinessAgentFaqInput | 
        try {
            BusinessAgentFaq result = apiInstance.updateBusinessAgentFaq(accountId, faqId, businessAgentFaqInput);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#updateBusinessAgentFaq");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **faqId** | **String**|  | |
| **businessAgentFaqInput** | [**BusinessAgentFaqInput**](BusinessAgentFaqInput.md)|  | |

### Return type

[**BusinessAgentFaq**](BusinessAgentFaq.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | FAQ updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## updateBusinessAgentFaqWithHttpInfo

> ApiResponse<BusinessAgentFaq> updateBusinessAgentFaq updateBusinessAgentFaqWithHttpInfo(accountId, faqId, businessAgentFaqInput)

Update a FAQ

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String faqId = "faqId_example"; // String | 
        BusinessAgentFaqInput businessAgentFaqInput = new BusinessAgentFaqInput(); // BusinessAgentFaqInput | 
        try {
            ApiResponse<BusinessAgentFaq> response = apiInstance.updateBusinessAgentFaqWithHttpInfo(accountId, faqId, businessAgentFaqInput);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#updateBusinessAgentFaq");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **faqId** | **String**|  | |
| **businessAgentFaqInput** | [**BusinessAgentFaqInput**](BusinessAgentFaqInput.md)|  | |

### Return type

ApiResponse<[**BusinessAgentFaq**](BusinessAgentFaq.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | FAQ updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## updateBusinessAgentSettings

> BusinessAgentSettings updateBusinessAgentSettings(accountId, updateBusinessAgentSettingsRequest, agentId)

Update agent settings

Partial update: fields you omit keep their value. &#x60;rollout.enabled: true&#x60; turns the agent on for new conversations; &#x60;false&#x60; stops it on every thread. Turning it on for &#x60;EVERYONE&#x60; needs a payment method on the Business Agent billable account (Meta accepts the call but delivers nothing without one); &#x60;ALLOWLISTED_ONLY&#x60; does not, which is how you test with a few numbers before billing. &#x60;never_say_phrases&#x60; replaces the whole list. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        UpdateBusinessAgentSettingsRequest updateBusinessAgentSettingsRequest = new UpdateBusinessAgentSettingsRequest(); // UpdateBusinessAgentSettingsRequest | 
        String agentId = "agentId_example"; // String | 
        try {
            BusinessAgentSettings result = apiInstance.updateBusinessAgentSettings(accountId, updateBusinessAgentSettingsRequest, agentId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#updateBusinessAgentSettings");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **updateBusinessAgentSettingsRequest** | [**UpdateBusinessAgentSettingsRequest**](UpdateBusinessAgentSettingsRequest.md)|  | |
| **agentId** | **String**|  | [optional] |

### Return type

[**BusinessAgentSettings**](BusinessAgentSettings.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated settings |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## updateBusinessAgentSettingsWithHttpInfo

> ApiResponse<BusinessAgentSettings> updateBusinessAgentSettings updateBusinessAgentSettingsWithHttpInfo(accountId, updateBusinessAgentSettingsRequest, agentId)

Update agent settings

Partial update: fields you omit keep their value. &#x60;rollout.enabled: true&#x60; turns the agent on for new conversations; &#x60;false&#x60; stops it on every thread. Turning it on for &#x60;EVERYONE&#x60; needs a payment method on the Business Agent billable account (Meta accepts the call but delivers nothing without one); &#x60;ALLOWLISTED_ONLY&#x60; does not, which is how you test with a few numbers before billing. &#x60;never_say_phrases&#x60; replaces the whole list. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        UpdateBusinessAgentSettingsRequest updateBusinessAgentSettingsRequest = new UpdateBusinessAgentSettingsRequest(); // UpdateBusinessAgentSettingsRequest | 
        String agentId = "agentId_example"; // String | 
        try {
            ApiResponse<BusinessAgentSettings> response = apiInstance.updateBusinessAgentSettingsWithHttpInfo(accountId, updateBusinessAgentSettingsRequest, agentId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#updateBusinessAgentSettings");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **updateBusinessAgentSettingsRequest** | [**UpdateBusinessAgentSettingsRequest**](UpdateBusinessAgentSettingsRequest.md)|  | |
| **agentId** | **String**|  | [optional] |

### Return type

ApiResponse<[**BusinessAgentSettings**](BusinessAgentSettings.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated settings |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## updateBusinessAgentSkill

> BusinessAgentSkill updateBusinessAgentSkill(accountId, skillId, businessAgentSkillInput)

Update a skill

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String skillId = "skillId_example"; // String | 
        BusinessAgentSkillInput businessAgentSkillInput = new BusinessAgentSkillInput(); // BusinessAgentSkillInput | 
        try {
            BusinessAgentSkill result = apiInstance.updateBusinessAgentSkill(accountId, skillId, businessAgentSkillInput);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#updateBusinessAgentSkill");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **skillId** | **String**|  | |
| **businessAgentSkillInput** | [**BusinessAgentSkillInput**](BusinessAgentSkillInput.md)|  | |

### Return type

[**BusinessAgentSkill**](BusinessAgentSkill.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Skill updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## updateBusinessAgentSkillWithHttpInfo

> ApiResponse<BusinessAgentSkill> updateBusinessAgentSkill updateBusinessAgentSkillWithHttpInfo(accountId, skillId, businessAgentSkillInput)

Update a skill

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String skillId = "skillId_example"; // String | 
        BusinessAgentSkillInput businessAgentSkillInput = new BusinessAgentSkillInput(); // BusinessAgentSkillInput | 
        try {
            ApiResponse<BusinessAgentSkill> response = apiInstance.updateBusinessAgentSkillWithHttpInfo(accountId, skillId, businessAgentSkillInput);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#updateBusinessAgentSkill");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **skillId** | **String**|  | |
| **businessAgentSkillInput** | [**BusinessAgentSkillInput**](BusinessAgentSkillInput.md)|  | |

### Return type

ApiResponse<[**BusinessAgentSkill**](BusinessAgentSkill.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Skill updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## updateBusinessAgentUiSkill

> BusinessAgentUiSkill updateBusinessAgentUiSkill(accountId, uiSkillId, businessAgentUiSkillInput)

Update a UI skill

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String uiSkillId = "uiSkillId_example"; // String | 
        BusinessAgentUiSkillInput businessAgentUiSkillInput = new BusinessAgentUiSkillInput(); // BusinessAgentUiSkillInput | 
        try {
            BusinessAgentUiSkill result = apiInstance.updateBusinessAgentUiSkill(accountId, uiSkillId, businessAgentUiSkillInput);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#updateBusinessAgentUiSkill");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **uiSkillId** | **String**|  | |
| **businessAgentUiSkillInput** | [**BusinessAgentUiSkillInput**](BusinessAgentUiSkillInput.md)|  | |

### Return type

[**BusinessAgentUiSkill**](BusinessAgentUiSkill.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | UI skill updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## updateBusinessAgentUiSkillWithHttpInfo

> ApiResponse<BusinessAgentUiSkill> updateBusinessAgentUiSkill updateBusinessAgentUiSkillWithHttpInfo(accountId, uiSkillId, businessAgentUiSkillInput)

Update a UI skill

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String uiSkillId = "uiSkillId_example"; // String | 
        BusinessAgentUiSkillInput businessAgentUiSkillInput = new BusinessAgentUiSkillInput(); // BusinessAgentUiSkillInput | 
        try {
            ApiResponse<BusinessAgentUiSkill> response = apiInstance.updateBusinessAgentUiSkillWithHttpInfo(accountId, uiSkillId, businessAgentUiSkillInput);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#updateBusinessAgentUiSkill");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **uiSkillId** | **String**|  | |
| **businessAgentUiSkillInput** | [**BusinessAgentUiSkillInput**](BusinessAgentUiSkillInput.md)|  | |

### Return type

ApiResponse<[**BusinessAgentUiSkill**](BusinessAgentUiSkill.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | UI skill updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## updateBusinessAgentWebsite

> BusinessAgentWebsite updateBusinessAgentWebsite(accountId, websiteId, businessAgentWebsiteInput)

Update a crawled website

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String websiteId = "websiteId_example"; // String | 
        BusinessAgentWebsiteInput businessAgentWebsiteInput = new BusinessAgentWebsiteInput(); // BusinessAgentWebsiteInput | 
        try {
            BusinessAgentWebsite result = apiInstance.updateBusinessAgentWebsite(accountId, websiteId, businessAgentWebsiteInput);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#updateBusinessAgentWebsite");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **websiteId** | **String**|  | |
| **businessAgentWebsiteInput** | [**BusinessAgentWebsiteInput**](BusinessAgentWebsiteInput.md)|  | |

### Return type

[**BusinessAgentWebsite**](BusinessAgentWebsite.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Website updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |

## updateBusinessAgentWebsiteWithHttpInfo

> ApiResponse<BusinessAgentWebsite> updateBusinessAgentWebsite updateBusinessAgentWebsiteWithHttpInfo(accountId, websiteId, businessAgentWebsiteInput)

Update a crawled website

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        String websiteId = "websiteId_example"; // String | 
        BusinessAgentWebsiteInput businessAgentWebsiteInput = new BusinessAgentWebsiteInput(); // BusinessAgentWebsiteInput | 
        try {
            ApiResponse<BusinessAgentWebsite> response = apiInstance.updateBusinessAgentWebsiteWithHttpInfo(accountId, websiteId, businessAgentWebsiteInput);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#updateBusinessAgentWebsite");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **websiteId** | **String**|  | |
| **businessAgentWebsiteInput** | [**BusinessAgentWebsiteInput**](BusinessAgentWebsiteInput.md)|  | |

### Return type

ApiResponse<[**BusinessAgentWebsite**](BusinessAgentWebsite.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Website updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |


## uploadBusinessAgentFile

> BusinessAgentKnowledgeFile uploadBusinessAgentFile(accountId, uploadBusinessAgentFileRequest)

Upload a knowledge file

Accepted types: pdf, doc, docx, png, jpg, jpeg, plus csv and xlsx when Meta enabled extraction on the asset. Meta&#39;s limit is 100 MB. Two ways to send the file: - JSON &#x60;{ url, fileName }&#x60;: Zernio downloads the file (public https URL, no redirects,   capped at 100 MB) and forwards it. Use this for anything above a few megabytes. - multipart form-data with a &#x60;file&#x60; part (and an optional &#x60;fileName&#x60;): bounded by the   request body limit of about 4.5 MB; larger uploads must use the &#x60;url&#x60; form. Not idempotent. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        UploadBusinessAgentFileRequest uploadBusinessAgentFileRequest = new UploadBusinessAgentFileRequest(); // UploadBusinessAgentFileRequest | 
        try {
            BusinessAgentKnowledgeFile result = apiInstance.uploadBusinessAgentFile(accountId, uploadBusinessAgentFileRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#uploadBusinessAgentFile");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **uploadBusinessAgentFileRequest** | [**UploadBusinessAgentFileRequest**](UploadBusinessAgentFileRequest.md)|  | |

### Return type

[**BusinessAgentKnowledgeFile**](BusinessAgentKnowledgeFile.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | File uploaded |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |
| **413** | File larger than 100 MB (code payload_too_large). A multipart body above the request limit is rejected by the host before the route runs. |  -  |

## uploadBusinessAgentFileWithHttpInfo

> ApiResponse<BusinessAgentKnowledgeFile> uploadBusinessAgentFile uploadBusinessAgentFileWithHttpInfo(accountId, uploadBusinessAgentFileRequest)

Upload a knowledge file

Accepted types: pdf, doc, docx, png, jpg, jpeg, plus csv and xlsx when Meta enabled extraction on the asset. Meta&#39;s limit is 100 MB. Two ways to send the file: - JSON &#x60;{ url, fileName }&#x60;: Zernio downloads the file (public https URL, no redirects,   capped at 100 MB) and forwards it. Use this for anything above a few megabytes. - multipart form-data with a &#x60;file&#x60; part (and an optional &#x60;fileName&#x60;): bounded by the   request body limit of about 4.5 MB; larger uploads must use the &#x60;url&#x60; form. Not idempotent. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.BusinessAgentApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        BusinessAgentApi apiInstance = new BusinessAgentApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account id (the number must be managed through the Cloud API).
        UploadBusinessAgentFileRequest uploadBusinessAgentFileRequest = new UploadBusinessAgentFileRequest(); // UploadBusinessAgentFileRequest | 
        try {
            ApiResponse<BusinessAgentKnowledgeFile> response = apiInstance.uploadBusinessAgentFileWithHttpInfo(accountId, uploadBusinessAgentFileRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling BusinessAgentApi#uploadBusinessAgentFile");
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
| **accountId** | **String**| WhatsApp social account id (the number must be managed through the Cloud API). | |
| **uploadBusinessAgentFileRequest** | [**UploadBusinessAgentFileRequest**](UploadBusinessAgentFileRequest.md)|  | |

### Return type

ApiResponse<[**BusinessAgentKnowledgeFile**](BusinessAgentKnowledgeFile.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | File uploaded |  -  |
| **400** | Invalid request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Inbox add-on required, the WhatsApp token lacks the Business Agent permissions (code reconnect_required), or the merchant has not accepted the Meta Business Agent terms in WhatsApp Manager (code business_agent_terms_not_accepted). |  -  |
| **404** | Account not found, or no agent exists on the number yet or the referenced item does not exist (code business_agent_not_found). |  -  |
| **413** | File larger than 100 MB (code payload_too_large). A multipart body above the request limit is rejected by the host before the route runs. |  -  |

