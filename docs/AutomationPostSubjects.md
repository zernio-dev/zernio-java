

# AutomationPostSubjects

The posts a scheduled automation checks.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**each** | [**EachEnum**](#EachEnum) |  |  |
|**profileId** | **String** | The profile whose posts are checked. |  |
|**accountIds** | **List&lt;String&gt;** | Only posts of these accounts. Each must be active on the profile. |  [optional] |
|**publishedWithin** | **String** | How far back posts are checked, by when they were published. Whole days, from &#x60;1d&#x60; to &#x60;30d&#x60; (&#x60;48h&#x60; is 2 days). |  [optional] |



## Enum: EachEnum

| Name | Value |
|---- | -----|
| POST | &quot;post&quot; |



