

# MetaRecoveredWritesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**id** | **String** | The Meta object id this response uses. |  |
|**adopted** | **Boolean** | Always true when present. Zernio found this object by name under its parent and reused it instead of creating it again. |  [optional] |
|**repostedAfter** | [**RepostedAfterEnum**](#RepostedAfterEnum) | Zernio sent the create again after Meta answered a 5xx and the read-back found no such object. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CAMPAIGN | &quot;campaign&quot; |
| ADSET | &quot;adset&quot; |
| AD | &quot;ad&quot; |



## Enum: RepostedAfterEnum

| Name | Value |
|---- | -----|
| SERVER_ERROR | &quot;server_error&quot; |



