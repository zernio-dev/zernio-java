

# GetAdInsightsReport200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reportRunId** | **String** |  |  [optional] |
|**status** | **String** | Meta async_status: Job Not Started, Job Started, Job Running, Job Completed, Job Failed, Job Skipped. |  [optional] |
|**percentCompletion** | **Integer** |  |  [optional] |
|**dateStart** | **String** |  |  [optional] |
|**dateStop** | **String** |  |  [optional] |
|**data** | **List&lt;Object&gt;** | Present only when status is Job Completed. |  [optional] |
|**paging** | [**GetAdInsightsReport200ResponsePaging**](GetAdInsightsReport200ResponsePaging.md) |  |  [optional] |



