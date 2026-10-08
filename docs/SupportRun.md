

# SupportRun


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**runId** | **String** | Run id, a 24-character hex string. |  |
|**threadId** | **String** | Conversation thread id. Send it back as &#x60;threadId&#x60; to ask a follow-up in the same thread. |  |
|**status** | [**StatusEnum**](#StatusEnum) | queued and running are in progress. needs_human means Ana handed the question to a person instead of answering. |  |
|**stopReason** | [**StopReasonEnum**](#StopReasonEnum) | Why the run stopped. Null while it is in progress. |  |
|**answer** | **String** | Ana&#39;s answer. Null while the run is in progress or when it failed. |  |
|**usage** | [**SupportRunUsage**](SupportRunUsage.md) |  |  |
|**costUsd** | **BigDecimal** | The amount billed for the run, in USD: the model cost plus 20%, never above &#x60;maxCostUsd&#x60;. 0 for a failed run. |  |
|**maxCostUsd** | **BigDecimal** | The cost cap this run was started with, in USD. |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**startedAt** | **OffsetDateTime** |  |  |
|**finishedAt** | **OffsetDateTime** |  |  |
|**pollAfterSeconds** | **Integer** | Seconds to wait before polling again. Present only while the run is queued or running. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| QUEUED | &quot;queued&quot; |
| RUNNING | &quot;running&quot; |
| COMPLETED | &quot;completed&quot; |
| NEEDS_HUMAN | &quot;needs_human&quot; |
| FAILED | &quot;failed&quot; |



## Enum: StopReasonEnum

| Name | Value |
|---- | -----|
| ANSWERED | &quot;answered&quot; |
| HUMAN_REVIEW | &quot;human_review&quot; |
| COST_CAP | &quot;cost_cap&quot; |
| DEADLINE | &quot;deadline&quot; |
| MAX_ITERATIONS | &quot;max_iterations&quot; |
| ERROR | &quot;error&quot; |
| EXPIRED | &quot;expired&quot; |



