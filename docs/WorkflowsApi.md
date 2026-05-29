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
| [**getWorkflow**](WorkflowsApi.md#getWorkflow) | **GET** /v1/workflows/{workflowId} | Get workflow with graph |
| [**getWorkflowWithHttpInfo**](WorkflowsApi.md#getWorkflowWithHttpInfo) | **GET** /v1/workflows/{workflowId} | Get workflow with graph |
| [**listWorkflowExecutions**](WorkflowsApi.md#listWorkflowExecutions) | **GET** /v1/workflows/{workflowId}/executions | List workflow runs |
| [**listWorkflowExecutionsWithHttpInfo**](WorkflowsApi.md#listWorkflowExecutionsWithHttpInfo) | **GET** /v1/workflows/{workflowId}/executions | List workflow runs |
| [**listWorkflows**](WorkflowsApi.md#listWorkflows) | **GET** /v1/workflows | List workflows |
| [**listWorkflowsWithHttpInfo**](WorkflowsApi.md#listWorkflowsWithHttpInfo) | **GET** /v1/workflows | List workflows |
| [**pauseWorkflow**](WorkflowsApi.md#pauseWorkflow) | **POST** /v1/workflows/{workflowId}/pause | Pause workflow |
| [**pauseWorkflowWithHttpInfo**](WorkflowsApi.md#pauseWorkflowWithHttpInfo) | **POST** /v1/workflows/{workflowId}/pause | Pause workflow |
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
| **400** | Invalid graph (duplicate node ids |  -  |
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
| **400** | Invalid graph (duplicate node ids |  -  |
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
| **400** | Missing target |  -  |
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
| **400** | Missing target |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## updateWorkflow

> UpdateWorkflow200Response updateWorkflow(workflowId, updateWorkflowRequest)

Update workflow

Update name, description, or the graph. The graph can only be modified while the workflow is draft or paused.

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
| **400** | Invalid graph |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## updateWorkflowWithHttpInfo

> ApiResponse<UpdateWorkflow200Response> updateWorkflow updateWorkflowWithHttpInfo(workflowId, updateWorkflowRequest)

Update workflow

Update name, description, or the graph. The graph can only be modified while the workflow is draft or paused.

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
| **400** | Invalid graph |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

