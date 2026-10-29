

# DuplicateAdSet200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**copiedAdSetId** | **String** | Platform ID of the new ad set |  [optional] |
|**copiedAdIds** | **List&lt;String&gt;** | Platform IDs of the copied ads |  [optional] |
|**adIdMap** | **Map&lt;String, String&gt;** | Meta only: source ad ID to copied ad ID. Empty when &#x60;deepCopy&#x60; is false. |  [optional] |
|**discovery** | [**DiscoveryEnum**](#DiscoveryEnum) |  |  [optional] |
|**raw** | **Object** | Platform-native response from the copy (TikTok). Absent on Meta, which returns &#x60;adIdMap&#x60; instead. |  [optional] |



## Enum: DiscoveryEnum

| Name | Value |
|---- | -----|
| TRIGGERED | &quot;triggered&quot; |
| SKIPPED | &quot;skipped&quot; |
| FAILED | &quot;failed&quot; |



