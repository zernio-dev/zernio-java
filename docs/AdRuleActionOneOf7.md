

# AdRuleActionOneOf7

Exactly one of `add` and `remove`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | Tag the object by its name. Meta, TikTok and Reddit campaigns, ad sets and ads, and Google, LinkedIn and Pinterest campaigns and ad sets. An object whose name already has the tag (or lacks it, for &#x60;remove&#x60;) is skipped with &#x60;name_unchanged&#x60;. |  |
|**add** | **String** | Text to add, like &#x60;[WINNER]&#x60;. Compared without case. |  [optional] |
|**at** | [**AtEnum**](#AtEnum) | Where &#x60;add&#x60; goes. Defaults to &#x60;start&#x60;. |  [optional] |
|**remove** | **String** | Text to take out of the name, every copy of it. |  [optional] |
|**maxChangesPerDay** | **Integer** | At most this many objects changed in any 24 hours, across runs. Matches over the limit are skipped with &#x60;daily_limit_reached&#x60; and tried again later. |  [optional] |
|**maxChangesPerObject** | **Integer** | At most this many changes to one object by this rule, counted over the last 400 days. An object at the limit is left alone like one in cooldown. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| EDIT_NAME | &quot;edit_name&quot; |



## Enum: AtEnum

| Name | Value |
|---- | -----|
| START | &quot;start&quot; |
| END | &quot;end&quot; |



