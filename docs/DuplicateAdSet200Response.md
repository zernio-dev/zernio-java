

# DuplicateAdSet200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**copiedAdSetId** | **String** | Platform ID of the new ad set |  [optional] |
|**copiedAdIds** | **List&lt;String&gt;** | Platform IDs of the copied ads |  [optional] |
|**adIdMap** | **Map&lt;String, String&gt;** | Meta only: source ad ID to copied ad ID. Empty when &#x60;deepCopy&#x60; is false. |  [optional] |
|**discovery** | [**DiscoveryEnum**](#DiscoveryEnum) | The copy exists on the platform in all three cases.  - &#x60;triggered&#x60;: an ads sync started and runs after this response, so the copy may not be readable through Zernio yet. - &#x60;skipped&#x60;: no sync started, so the copy appears on a later scheduled sync. - &#x60;failed&#x60;: the sync could not start. A sync that errors after the response is not reported here. |  [optional] |
|**raw** | **Object** | Platform-native response from the copy (TikTok). Absent on Meta, which returns &#x60;adIdMap&#x60; instead. |  [optional] |



## Enum: DiscoveryEnum

| Name | Value |
|---- | -----|
| TRIGGERED | &quot;triggered&quot; |
| SKIPPED | &quot;skipped&quot; |
| FAILED | &quot;failed&quot; |



