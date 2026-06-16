# WorkflowsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activateWorkflow**](WorkflowsApi.md#activateWorkflow) | **POST** /v1/workflows/{workflowId}/activate | Activate workflow |
| [**activateWorkflowWithHttpInfo**](WorkflowsApi.md#activateWorkflowWithHttpInfo) | **POST** /v1/workflows/{workflowId}/activate | Activate workflow |
| [**createWorkflow**](WorkflowsApi.md#createWorkflow) | **POST** /v1/workflows | Create workflow |
| [**createWorkflowWithHttpInfo**](WorkflowsApi.md#createWorkflowWithHttpInfo) | **POST** /v1/workflows | Create workflow |
| [**deleteWorkflow**](WorkflowsApi.md#deleteWorkflow) | **DELETE** /v1/workflows/{workflowId} | Delete workflow |
| [**deleteWorkflowWithHttpInfo**](WorkflowsApi.md#deleteWorkflowWithHttpInfo) | **DELETE** /v1/workflows/{workflowId} | Delete workflow |
| [**duplicateWorkflow**](WorkflowsApi.md#duplicateWorkflow) | **POST** /v1/workflows/{workflowId}/duplicate | Duplicate a workflow |
| [**duplicateWorkflowWithHttpInfo**](WorkflowsApi.md#duplicateWorkflowWithHttpInfo) | **POST** /v1/workflows/{workflowId}/duplicate | Duplicate a workflow |
| [**getWorkflow**](WorkflowsApi.md#getWorkflow) | **GET** /v1/workflows/{workflowId} | Get workflow with graph |
| [**getWorkflowWithHttpInfo**](WorkflowsApi.md#getWorkflowWithHttpInfo) | **GET** /v1/workflows/{workflowId} | Get workflow with graph |
| [**getWorkflowVersion**](WorkflowsApi.md#getWorkflowVersion) | **GET** /v1/workflows/{workflowId}/versions/{version} | Get a specific workflow version |
| [**getWorkflowVersionWithHttpInfo**](WorkflowsApi.md#getWorkflowVersionWithHttpInfo) | **GET** /v1/workflows/{workflowId}/versions/{version} | Get a specific workflow version |
| [**listWorkflowExecutionEvents**](WorkflowsApi.md#listWorkflowExecutionEvents) | **GET** /v1/workflows/{workflowId}/executions/{executionId}/events | Get an execution&#39;s timeline |
| [**listWorkflowExecutionEventsWithHttpInfo**](WorkflowsApi.md#listWorkflowExecutionEventsWithHttpInfo) | **GET** /v1/workflows/{workflowId}/executions/{executionId}/events | Get an execution&#39;s timeline |
| [**listWorkflowExecutions**](WorkflowsApi.md#listWorkflowExecutions) | **GET** /v1/workflows/{workflowId}/executions | List workflow runs |
| [**listWorkflowExecutionsWithHttpInfo**](WorkflowsApi.md#listWorkflowExecutionsWithHttpInfo) | **GET** /v1/workflows/{workflowId}/executions | List workflow runs |
| [**listWorkflowVersions**](WorkflowsApi.md#listWorkflowVersions) | **GET** /v1/workflows/{workflowId}/versions | List a workflow&#39;s version history |
| [**listWorkflowVersionsWithHttpInfo**](WorkflowsApi.md#listWorkflowVersionsWithHttpInfo) | **GET** /v1/workflows/{workflowId}/versions | List a workflow&#39;s version history |
| [**listWorkflows**](WorkflowsApi.md#listWorkflows) | **GET** /v1/workflows | List workflows |
| [**listWorkflowsWithHttpInfo**](WorkflowsApi.md#listWorkflowsWithHttpInfo) | **GET** /v1/workflows | List workflows |
| [**pauseWorkflow**](WorkflowsApi.md#pauseWorkflow) | **POST** /v1/workflows/{workflowId}/pause | Pause workflow |
| [**pauseWorkflowWithHttpInfo**](WorkflowsApi.md#pauseWorkflowWithHttpInfo) | **POST** /v1/workflows/{workflowId}/pause | Pause workflow |
| [**restoreWorkflowVersion**](WorkflowsApi.md#restoreWorkflowVersion) | **POST** /v1/workflows/{workflowId}/versions/{version}/restore | Restore a previous workflow version |
| [**restoreWorkflowVersionWithHttpInfo**](WorkflowsApi.md#restoreWorkflowVersionWithHttpInfo) | **POST** /v1/workflows/{workflowId}/versions/{version}/restore | Restore a previous workflow version |
| [**triggerWorkflow**](WorkflowsApi.md#triggerWorkflow) | **POST** /v1/workflows/{workflowId}/executions | Manually start a workflow run |
| [**triggerWorkflowWithHttpInfo**](WorkflowsApi.md#triggerWorkflowWithHttpInfo) | **POST** /v1/workflows/{workflowId}/executions | Manually start a workflow run |
| [**updateWorkflow**](WorkflowsApi.md#updateWorkflow) | **PATCH** /v1/workflows/{workflowId} | Update workflow |
| [**updateWorkflowWithHttpInfo**](WorkflowsApi.md#updateWorkflowWithHttpInfo) | **PATCH** /v1/workflows/{workflowId} | Update workflow |



## activateWorkflow

> ActivateWorkflow200Response activateWorkflow(workflowId)

Activate workflow

Validate the graph is runnable and set the workflow live. Once active, matching inbound messages start executions. Idempotent.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkflowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
        String workflowId = "workflowId_example"; // String | 
        try {
            ActivateWorkflow200Response result = apiInstance.activateWorkflow(workflowId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkflowsApi#activateWorkflow");
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
| **workflowId** | **String**|  | |

### Return type

[**ActivateWorkflow200Response**](ActivateWorkflow200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Workflow activated |  -  |
| **400** | Incomplete or invalid graph |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## activateWorkflowWithHttpInfo

> ApiResponse<ActivateWorkflow200Response> activateWorkflow activateWorkflowWithHttpInfo(workflowId)

Activate workflow

Validate the graph is runnable and set the workflow live. Once active, matching inbound messages start executions. Idempotent.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkflowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
        String workflowId = "workflowId_example"; // String | 
        try {
            ApiResponse<ActivateWorkflow200Response> response = apiInstance.activateWorkflowWithHttpInfo(workflowId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkflowsApi#activateWorkflow");
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
| **workflowId** | **String**|  | |

### Return type

ApiResponse<[**ActivateWorkflow200Response**](ActivateWorkflow200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Workflow activated |  -  |
| **400** | Incomplete or invalid graph |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## createWorkflow

> CreateWorkflow200Response createWorkflow(createWorkflowRequest)

Create workflow

Create a branching conversation workflow (draft) from a node/edge graph. Created in &#x60;draft&#x60; status; activate it to start matching inbound messages. The graph is validated structurally; completeness (a trigger node + reachable entry) is required at activation. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkflowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
        CreateWorkflowRequest createWorkflowRequest = new CreateWorkflowRequest(); // CreateWorkflowRequest | 
        try {
            CreateWorkflow200Response result = apiInstance.createWorkflow(createWorkflowRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkflowsApi#createWorkflow");
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
| **createWorkflowRequest** | [**CreateWorkflowRequest**](CreateWorkflowRequest.md)|  | |

### Return type

[**CreateWorkflow200Response**](CreateWorkflow200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Workflow created |  -  |
| **400** | Invalid graph (duplicate node ids, edges referencing missing nodes, or a WhatsApp-only node on another platform) |  -  |
| **401** | Unauthorized |  -  |

## createWorkflowWithHttpInfo

> ApiResponse<CreateWorkflow200Response> createWorkflow createWorkflowWithHttpInfo(createWorkflowRequest)

Create workflow

Create a branching conversation workflow (draft) from a node/edge graph. Created in &#x60;draft&#x60; status; activate it to start matching inbound messages. The graph is validated structurally; completeness (a trigger node + reachable entry) is required at activation. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkflowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
        CreateWorkflowRequest createWorkflowRequest = new CreateWorkflowRequest(); // CreateWorkflowRequest | 
        try {
            ApiResponse<CreateWorkflow200Response> response = apiInstance.createWorkflowWithHttpInfo(createWorkflowRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkflowsApi#createWorkflow");
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
| **createWorkflowRequest** | [**CreateWorkflowRequest**](CreateWorkflowRequest.md)|  | |

### Return type

ApiResponse<[**CreateWorkflow200Response**](CreateWorkflow200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Workflow created |  -  |
| **400** | Invalid graph (duplicate node ids, edges referencing missing nodes, or a WhatsApp-only node on another platform) |  -  |
| **401** | Unauthorized |  -  |


## deleteWorkflow

> void deleteWorkflow(workflowId)

Delete workflow

Permanently delete a workflow and all of its executions.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkflowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
        String workflowId = "workflowId_example"; // String | 
        try {
            apiInstance.deleteWorkflow(workflowId);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkflowsApi#deleteWorkflow");
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
| **workflowId** | **String**|  | |

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
| **200** | Workflow deleted |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## deleteWorkflowWithHttpInfo

> ApiResponse<Void> deleteWorkflow deleteWorkflowWithHttpInfo(workflowId)

Delete workflow

Permanently delete a workflow and all of its executions.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkflowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
        String workflowId = "workflowId_example"; // String | 
        try {
            ApiResponse<Void> response = apiInstance.deleteWorkflowWithHttpInfo(workflowId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkflowsApi#deleteWorkflow");
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
| **workflowId** | **String**|  | |

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
| **200** | Workflow deleted |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## duplicateWorkflow

> DuplicateWorkflow201Response duplicateWorkflow(workflowId)

Duplicate a workflow

Create an independent copy of a workflow&#39;s graph, name, description, and account binding. The copy is created in &#x60;draft&#x60; status with fresh execution counters and a new id — execution history is NOT copied. Useful for branching off a known-good workflow before making experimental edits. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkflowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
        String workflowId = "workflowId_example"; // String | 
        try {
            DuplicateWorkflow201Response result = apiInstance.duplicateWorkflow(workflowId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkflowsApi#duplicateWorkflow");
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
| **workflowId** | **String**|  | |

### Return type

[**DuplicateWorkflow201Response**](DuplicateWorkflow201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Workflow duplicated |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## duplicateWorkflowWithHttpInfo

> ApiResponse<DuplicateWorkflow201Response> duplicateWorkflow duplicateWorkflowWithHttpInfo(workflowId)

Duplicate a workflow

Create an independent copy of a workflow&#39;s graph, name, description, and account binding. The copy is created in &#x60;draft&#x60; status with fresh execution counters and a new id — execution history is NOT copied. Useful for branching off a known-good workflow before making experimental edits. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkflowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
        String workflowId = "workflowId_example"; // String | 
        try {
            ApiResponse<DuplicateWorkflow201Response> response = apiInstance.duplicateWorkflowWithHttpInfo(workflowId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkflowsApi#duplicateWorkflow");
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
| **workflowId** | **String**|  | |

### Return type

ApiResponse<[**DuplicateWorkflow201Response**](DuplicateWorkflow201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Workflow duplicated |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## getWorkflow

> GetWorkflow200Response getWorkflow(workflowId)

Get workflow with graph

Returns a workflow including its full node/edge graph and run stats.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkflowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
        String workflowId = "workflowId_example"; // String | 
        try {
            GetWorkflow200Response result = apiInstance.getWorkflow(workflowId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkflowsApi#getWorkflow");
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
| **workflowId** | **String**|  | |

### Return type

[**GetWorkflow200Response**](GetWorkflow200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Workflow details |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## getWorkflowWithHttpInfo

> ApiResponse<GetWorkflow200Response> getWorkflow getWorkflowWithHttpInfo(workflowId)

Get workflow with graph

Returns a workflow including its full node/edge graph and run stats.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkflowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
        String workflowId = "workflowId_example"; // String | 
        try {
            ApiResponse<GetWorkflow200Response> response = apiInstance.getWorkflowWithHttpInfo(workflowId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkflowsApi#getWorkflow");
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
| **workflowId** | **String**|  | |

### Return type

ApiResponse<[**GetWorkflow200Response**](GetWorkflow200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Workflow details |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## getWorkflowVersion

> GetWorkflowVersion200Response getWorkflowVersion(workflowId, version)

Get a specific workflow version

Returns the full snapshot for a single historical version, including the graph.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkflowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
        String workflowId = "workflowId_example"; // String | 
        Integer version = 56; // Integer | 
        try {
            GetWorkflowVersion200Response result = apiInstance.getWorkflowVersion(workflowId, version);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkflowsApi#getWorkflowVersion");
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
| **workflowId** | **String**|  | |
| **version** | **Integer**|  | |

### Return type

[**GetWorkflowVersion200Response**](GetWorkflowVersion200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Version snapshot |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## getWorkflowVersionWithHttpInfo

> ApiResponse<GetWorkflowVersion200Response> getWorkflowVersion getWorkflowVersionWithHttpInfo(workflowId, version)

Get a specific workflow version

Returns the full snapshot for a single historical version, including the graph.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkflowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
        String workflowId = "workflowId_example"; // String | 
        Integer version = 56; // Integer | 
        try {
            ApiResponse<GetWorkflowVersion200Response> response = apiInstance.getWorkflowVersionWithHttpInfo(workflowId, version);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkflowsApi#getWorkflowVersion");
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
| **workflowId** | **String**|  | |
| **version** | **Integer**|  | |

### Return type

ApiResponse<[**GetWorkflowVersion200Response**](GetWorkflowVersion200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Version snapshot |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## listWorkflowExecutionEvents

> ListWorkflowExecutionEvents200Response listWorkflowExecutionEvents(workflowId, executionId)

Get an execution&#39;s timeline

Returns the per-step run-log for a single workflow execution: trigger fired, each node visited, edge handles taken, errors, and durations. Backed by Tinybird (90-day retention). Used by the Runs UI drawer to render the timeline. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkflowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
        String workflowId = "workflowId_example"; // String | 
        String executionId = "executionId_example"; // String | 
        try {
            ListWorkflowExecutionEvents200Response result = apiInstance.listWorkflowExecutionEvents(workflowId, executionId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkflowsApi#listWorkflowExecutionEvents");
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
| **workflowId** | **String**|  | |
| **executionId** | **String**|  | |

### Return type

[**ListWorkflowExecutionEvents200Response**](ListWorkflowExecutionEvents200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Timeline events for the execution |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## listWorkflowExecutionEventsWithHttpInfo

> ApiResponse<ListWorkflowExecutionEvents200Response> listWorkflowExecutionEvents listWorkflowExecutionEventsWithHttpInfo(workflowId, executionId)

Get an execution&#39;s timeline

Returns the per-step run-log for a single workflow execution: trigger fired, each node visited, edge handles taken, errors, and durations. Backed by Tinybird (90-day retention). Used by the Runs UI drawer to render the timeline. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkflowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
        String workflowId = "workflowId_example"; // String | 
        String executionId = "executionId_example"; // String | 
        try {
            ApiResponse<ListWorkflowExecutionEvents200Response> response = apiInstance.listWorkflowExecutionEventsWithHttpInfo(workflowId, executionId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkflowsApi#listWorkflowExecutionEvents");
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
| **workflowId** | **String**|  | |
| **executionId** | **String**|  | |

### Return type

ApiResponse<[**ListWorkflowExecutionEvents200Response**](ListWorkflowExecutionEvents200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Timeline events for the execution |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## listWorkflowExecutions

> ListWorkflowExecutions200Response listWorkflowExecutions(workflowId, status, limit, skip)

List workflow runs

Returns recent executions (runs) with their status, current node, and accumulated variables.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkflowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
        String workflowId = "workflowId_example"; // String | 
        String status = "running"; // String | 
        Integer limit = 25; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ListWorkflowExecutions200Response result = apiInstance.listWorkflowExecutions(workflowId, status, limit, skip);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkflowsApi#listWorkflowExecutions");
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
| **workflowId** | **String**|  | |
| **status** | **String**|  | [optional] [enum: running, waiting, completed, exited, failed] |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

[**ListWorkflowExecutions200Response**](ListWorkflowExecutions200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Executions list |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## listWorkflowExecutionsWithHttpInfo

> ApiResponse<ListWorkflowExecutions200Response> listWorkflowExecutions listWorkflowExecutionsWithHttpInfo(workflowId, status, limit, skip)

List workflow runs

Returns recent executions (runs) with their status, current node, and accumulated variables.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkflowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
        String workflowId = "workflowId_example"; // String | 
        String status = "running"; // String | 
        Integer limit = 25; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ApiResponse<ListWorkflowExecutions200Response> response = apiInstance.listWorkflowExecutionsWithHttpInfo(workflowId, status, limit, skip);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkflowsApi#listWorkflowExecutions");
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
| **workflowId** | **String**|  | |
| **status** | **String**|  | [optional] [enum: running, waiting, completed, exited, failed] |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

ApiResponse<[**ListWorkflowExecutions200Response**](ListWorkflowExecutions200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Executions list |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## listWorkflowVersions

> ListWorkflowVersions200Response listWorkflowVersions(workflowId)

List a workflow&#39;s version history

Returns the snapshot history. A new version is recorded automatically before every PATCH to &#x60;nodes&#x60; / &#x60;edges&#x60; / &#x60;entryNodeId&#x60;, and explicitly when a previous version is restored. Lightweight list — call &#x60;getWorkflowVersion&#x60; for the full snapshot graph. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkflowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
        String workflowId = "workflowId_example"; // String | 
        try {
            ListWorkflowVersions200Response result = apiInstance.listWorkflowVersions(workflowId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkflowsApi#listWorkflowVersions");
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
| **workflowId** | **String**|  | |

### Return type

[**ListWorkflowVersions200Response**](ListWorkflowVersions200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Versions list |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## listWorkflowVersionsWithHttpInfo

> ApiResponse<ListWorkflowVersions200Response> listWorkflowVersions listWorkflowVersionsWithHttpInfo(workflowId)

List a workflow&#39;s version history

Returns the snapshot history. A new version is recorded automatically before every PATCH to &#x60;nodes&#x60; / &#x60;edges&#x60; / &#x60;entryNodeId&#x60;, and explicitly when a previous version is restored. Lightweight list — call &#x60;getWorkflowVersion&#x60; for the full snapshot graph. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkflowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
        String workflowId = "workflowId_example"; // String | 
        try {
            ApiResponse<ListWorkflowVersions200Response> response = apiInstance.listWorkflowVersionsWithHttpInfo(workflowId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkflowsApi#listWorkflowVersions");
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
| **workflowId** | **String**|  | |

### Return type

ApiResponse<[**ListWorkflowVersions200Response**](ListWorkflowVersions200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Versions list |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## listWorkflows

> ListWorkflows200Response listWorkflows(profileId, status, limit, skip)

List workflows

Returns workflows with run stats. Filter by status or profile.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkflowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
        String profileId = "profileId_example"; // String | Filter by profile. Omit to list across all profiles
        String status = "draft"; // String | 
        Integer limit = 50; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ListWorkflows200Response result = apiInstance.listWorkflows(profileId, status, limit, skip);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkflowsApi#listWorkflows");
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
| **profileId** | **String**| Filter by profile. Omit to list across all profiles | [optional] |
| **status** | **String**|  | [optional] [enum: draft, active, paused] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

[**ListWorkflows200Response**](ListWorkflows200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Workflows list |  -  |
| **401** | Unauthorized |  -  |

## listWorkflowsWithHttpInfo

> ApiResponse<ListWorkflows200Response> listWorkflows listWorkflowsWithHttpInfo(profileId, status, limit, skip)

List workflows

Returns workflows with run stats. Filter by status or profile.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkflowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
        String profileId = "profileId_example"; // String | Filter by profile. Omit to list across all profiles
        String status = "draft"; // String | 
        Integer limit = 50; // Integer | 
        Integer skip = 0; // Integer | 
        try {
            ApiResponse<ListWorkflows200Response> response = apiInstance.listWorkflowsWithHttpInfo(profileId, status, limit, skip);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkflowsApi#listWorkflows");
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
| **profileId** | **String**| Filter by profile. Omit to list across all profiles | [optional] |
| **status** | **String**|  | [optional] [enum: draft, active, paused] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **skip** | **Integer**|  | [optional] [default to 0] |

### Return type

ApiResponse<[**ListWorkflows200Response**](ListWorkflows200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Workflows list |  -  |
| **401** | Unauthorized |  -  |


## pauseWorkflow

> PauseWorkflow200Response pauseWorkflow(workflowId)

Pause workflow

Stop matching new inbound messages. In-flight executions continue to completion. Idempotent.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkflowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
        String workflowId = "workflowId_example"; // String | 
        try {
            PauseWorkflow200Response result = apiInstance.pauseWorkflow(workflowId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkflowsApi#pauseWorkflow");
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
| **workflowId** | **String**|  | |

### Return type

[**PauseWorkflow200Response**](PauseWorkflow200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Workflow paused |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## pauseWorkflowWithHttpInfo

> ApiResponse<PauseWorkflow200Response> pauseWorkflow pauseWorkflowWithHttpInfo(workflowId)

Pause workflow

Stop matching new inbound messages. In-flight executions continue to completion. Idempotent.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkflowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
        String workflowId = "workflowId_example"; // String | 
        try {
            ApiResponse<PauseWorkflow200Response> response = apiInstance.pauseWorkflowWithHttpInfo(workflowId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkflowsApi#pauseWorkflow");
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
| **workflowId** | **String**|  | |

### Return type

ApiResponse<[**PauseWorkflow200Response**](PauseWorkflow200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Workflow paused |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## restoreWorkflowVersion

> RestoreWorkflowVersion200Response restoreWorkflowVersion(workflowId, version)

Restore a previous workflow version

Replace the current graph with the named version&#39;s snapshot. Before the swap, the current graph is itself snapshotted as a new version, so a restore is reversible. The workflow must be in &#x60;draft&#x60; or &#x60;paused&#x60; status (same gate as a normal graph edit). The returned workflow carries &#x60;restoredFromVersion&#x60; so the UI can surface which version was rolled back to. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkflowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
        String workflowId = "workflowId_example"; // String | 
        Integer version = 56; // Integer | 
        try {
            RestoreWorkflowVersion200Response result = apiInstance.restoreWorkflowVersion(workflowId, version);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkflowsApi#restoreWorkflowVersion");
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
| **workflowId** | **String**|  | |
| **version** | **Integer**|  | |

### Return type

[**RestoreWorkflowVersion200Response**](RestoreWorkflowVersion200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Workflow restored to the named version |  -  |
| **400** | Workflow is not draft/paused, or the named version&#39;s graph is invalid for the current platform |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## restoreWorkflowVersionWithHttpInfo

> ApiResponse<RestoreWorkflowVersion200Response> restoreWorkflowVersion restoreWorkflowVersionWithHttpInfo(workflowId, version)

Restore a previous workflow version

Replace the current graph with the named version&#39;s snapshot. Before the swap, the current graph is itself snapshotted as a new version, so a restore is reversible. The workflow must be in &#x60;draft&#x60; or &#x60;paused&#x60; status (same gate as a normal graph edit). The returned workflow carries &#x60;restoredFromVersion&#x60; so the UI can surface which version was rolled back to. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkflowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
        String workflowId = "workflowId_example"; // String | 
        Integer version = 56; // Integer | 
        try {
            ApiResponse<RestoreWorkflowVersion200Response> response = apiInstance.restoreWorkflowVersionWithHttpInfo(workflowId, version);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkflowsApi#restoreWorkflowVersion");
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
| **workflowId** | **String**|  | |
| **version** | **Integer**|  | |

### Return type

ApiResponse<[**RestoreWorkflowVersion200Response**](RestoreWorkflowVersion200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Workflow restored to the named version |  -  |
| **400** | Workflow is not draft/paused, or the named version&#39;s graph is invalid for the current platform |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## triggerWorkflow

> TriggerWorkflow200Response triggerWorkflow(workflowId, triggerWorkflowRequest)

Manually start a workflow run

Kick off a run without waiting for an inbound message (useful for testing). Target an existing conversation by &#x60;conversationId&#x60;, or — WhatsApp only — a phone number via &#x60;to&#x60; (a conversation is found or created). &#x60;text&#x60; seeds the run&#39;s &#x60;lastMessage&#x60; variable. The graph must be runnable. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkflowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
        String workflowId = "workflowId_example"; // String | 
        TriggerWorkflowRequest triggerWorkflowRequest = new TriggerWorkflowRequest(); // TriggerWorkflowRequest | 
        try {
            TriggerWorkflow200Response result = apiInstance.triggerWorkflow(workflowId, triggerWorkflowRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkflowsApi#triggerWorkflow");
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
| **workflowId** | **String**|  | |
| **triggerWorkflowRequest** | [**TriggerWorkflowRequest**](TriggerWorkflowRequest.md)|  | |

### Return type

[**TriggerWorkflow200Response**](TriggerWorkflow200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Run started |  -  |
| **400** | Missing target, invalid graph, or &#x60;to&#x60; used on a non-WhatsApp workflow |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## triggerWorkflowWithHttpInfo

> ApiResponse<TriggerWorkflow200Response> triggerWorkflow triggerWorkflowWithHttpInfo(workflowId, triggerWorkflowRequest)

Manually start a workflow run

Kick off a run without waiting for an inbound message (useful for testing). Target an existing conversation by &#x60;conversationId&#x60;, or — WhatsApp only — a phone number via &#x60;to&#x60; (a conversation is found or created). &#x60;text&#x60; seeds the run&#39;s &#x60;lastMessage&#x60; variable. The graph must be runnable. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkflowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
        String workflowId = "workflowId_example"; // String | 
        TriggerWorkflowRequest triggerWorkflowRequest = new TriggerWorkflowRequest(); // TriggerWorkflowRequest | 
        try {
            ApiResponse<TriggerWorkflow200Response> response = apiInstance.triggerWorkflowWithHttpInfo(workflowId, triggerWorkflowRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkflowsApi#triggerWorkflow");
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
| **workflowId** | **String**|  | |
| **triggerWorkflowRequest** | [**TriggerWorkflowRequest**](TriggerWorkflowRequest.md)|  | |

### Return type

ApiResponse<[**TriggerWorkflow200Response**](TriggerWorkflow200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Run started |  -  |
| **400** | Missing target, invalid graph, or &#x60;to&#x60; used on a non-WhatsApp workflow |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## updateWorkflow

> UpdateWorkflow200Response updateWorkflow(workflowId, updateWorkflowRequest)

Update workflow

Update name, description, the graph, or reassign to a different account. The graph can only be modified while the workflow is draft or paused. Account swaps re-validate the graph against the new platform (so e.g. moving from WhatsApp to Facebook surfaces a &#x60;start_call&#x60; node as an error instead of silently saving an unrunnable graph). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkflowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
        String workflowId = "workflowId_example"; // String | 
        UpdateWorkflowRequest updateWorkflowRequest = new UpdateWorkflowRequest(); // UpdateWorkflowRequest | 
        try {
            UpdateWorkflow200Response result = apiInstance.updateWorkflow(workflowId, updateWorkflowRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkflowsApi#updateWorkflow");
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
| **workflowId** | **String**|  | |
| **updateWorkflowRequest** | [**UpdateWorkflowRequest**](UpdateWorkflowRequest.md)|  | [optional] |

### Return type

[**UpdateWorkflow200Response**](UpdateWorkflow200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Workflow updated |  -  |
| **400** | Invalid graph, or a graph edit attempted while the workflow is active |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## updateWorkflowWithHttpInfo

> ApiResponse<UpdateWorkflow200Response> updateWorkflow updateWorkflowWithHttpInfo(workflowId, updateWorkflowRequest)

Update workflow

Update name, description, the graph, or reassign to a different account. The graph can only be modified while the workflow is draft or paused. Account swaps re-validate the graph against the new platform (so e.g. moving from WhatsApp to Facebook surfaces a &#x60;start_call&#x60; node as an error instead of silently saving an unrunnable graph). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WorkflowsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
        String workflowId = "workflowId_example"; // String | 
        UpdateWorkflowRequest updateWorkflowRequest = new UpdateWorkflowRequest(); // UpdateWorkflowRequest | 
        try {
            ApiResponse<UpdateWorkflow200Response> response = apiInstance.updateWorkflowWithHttpInfo(workflowId, updateWorkflowRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling WorkflowsApi#updateWorkflow");
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
| **workflowId** | **String**|  | |
| **updateWorkflowRequest** | [**UpdateWorkflowRequest**](UpdateWorkflowRequest.md)|  | [optional] |

### Return type

ApiResponse<[**UpdateWorkflow200Response**](UpdateWorkflow200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Workflow updated |  -  |
| **400** | Invalid graph, or a graph edit attempted while the workflow is active |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

