

# AdRuleActionOneOf3


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | Copy the campaign or ad set with its ads, on Meta and TikTok campaigns and ad sets and LinkedIn campaigns. Not on ad-level rules. |  |
|**status** | [**StatusEnum**](#StatusEnum) | How the copy starts. Defaults to &#x60;paused&#x60;. |  [optional] |
|**renameSuffix** | **String** | Text added to the copy&#39;s name. |  [optional] |
|**maxChangesPerDay** | **Integer** | At most this many objects changed in any 24 hours, across runs. Matches over the limit are skipped with &#x60;daily_limit_reached&#x60; and tried again later. |  [optional] |
|**maxChangesPerObject** | **Integer** | At most this many changes to one object by this rule, counted over the last 400 days. An object at the limit is left alone like one in cooldown. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| DUPLICATE | &quot;duplicate&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PAUSED | &quot;paused&quot; |
| ACTIVE | &quot;active&quot; |



