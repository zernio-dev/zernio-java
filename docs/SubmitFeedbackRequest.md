

# SubmitFeedbackRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | What kind of feedback this is. |  |
|**summary** | **String** | One line describing the problem or the missing capability. Also the dedup key. |  |
|**details** | **String** | Longer explanation: what you were trying to do, steps to reproduce, the use case. |  [optional] |
|**endpoint** | **String** | The endpoint involved, e.g. &#x60;POST /v1/posts&#x60;. |  [optional] |
|**requestId** | **String** | The &#x60;x-request-id&#x60; header of the failing response, if any. |  [optional] |
|**expected** | **String** | What you expected to happen. |  [optional] |
|**actual** | **String** | What actually happened, e.g. the error message. |  [optional] |
|**agent** | [**SubmitFeedbackRequestAgent**](SubmitFeedbackRequestAgent.md) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BUG | &quot;bug&quot; |
| MISSING_FEATURE | &quot;missing_feature&quot; |
| DOCS | &quot;docs&quot; |
| OTHER | &quot;other&quot; |



