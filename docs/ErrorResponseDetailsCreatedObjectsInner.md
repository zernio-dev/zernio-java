

# ErrorResponseDetailsCreatedObjectsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**id** | **String** | Meta object id; for &#x60;image&#x60; the image hash. |  [optional] |
|**cleanup** | [**CleanupEnum**](#CleanupEnum) | &#x60;deleted&#x60;: Zernio deleted it. &#x60;left_behind&#x60;: Meta refused the delete, so it still exists. &#x60;kept&#x60;: deliberately not deleted (image hashes are shared by every upload of the same file). |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CAMPAIGN | &quot;campaign&quot; |
| ADSET | &quot;adset&quot; |
| CREATIVE | &quot;creative&quot; |
| AD | &quot;ad&quot; |
| VIDEO | &quot;video&quot; |
| IMAGE | &quot;image&quot; |



## Enum: CleanupEnum

| Name | Value |
|---- | -----|
| DELETED | &quot;deleted&quot; |
| LEFT_BEHIND | &quot;left_behind&quot; |
| KEPT | &quot;kept&quot; |



