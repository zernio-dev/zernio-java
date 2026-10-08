

# CreateSupportRunRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | **String** | The question. Leading and trailing whitespace is trimmed. |  |
|**threadId** | **String** | Continue this thread. The thread must have a run started by your team, and no run in progress. |  [optional] |
|**context** | [**CreateSupportRunRequestContext**](CreateSupportRunRequestContext.md) |  |  [optional] |
|**maxCostUsd** | **BigDecimal** | Cost cap for this run, in USD. The run stops at the cap and bills at most this amount. |  [optional] |



