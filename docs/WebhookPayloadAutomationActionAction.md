

# WebhookPayloadAutomationActionAction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  |
|**subjectId** | **String** | The platform&#39;s id of the object changed: an ad, ad set or campaign for ad rules. |  |
|**type** | **String** | &#x60;pause&#x60;, &#x60;activate&#x60;, &#x60;adjust_budget&#x60; or &#x60;notify&#x60; for ad rules. New values may be added. |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**reason** | **String** |  |  |
|**previous** | **Map&lt;String, Object&gt;** | The value before the change, such as &#x60;{ \&quot;dailyBudget\&quot;: 40 }&#x60;. |  |
|**target** | **Map&lt;String, Object&gt;** | The value the change sets, such as &#x60;{ \&quot;dailyBudget\&quot;: 48 }&#x60; or &#x60;{ \&quot;status\&quot;: \&quot;paused\&quot; }&#x60;. |  |
|**actedAt** | **OffsetDateTime** |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| APPLIED | &quot;applied&quot; |
| SKIPPED | &quot;skipped&quot; |
| FAILED | &quot;failed&quot; |
| UNKNOWN | &quot;unknown&quot; |



