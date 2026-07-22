

# CreateStandaloneAd200ResponseResultsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**node** | [**NodeEnum**](#NodeEnum) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**reason** | **String** | Why the node could not be validated (only on skipped). |  [optional] |



## Enum: NodeEnum

| Name | Value |
|---- | -----|
| CAMPAIGN | &quot;campaign&quot; |
| AD_SET | &quot;adSet&quot; |
| CREATIVE | &quot;creative&quot; |
| AD | &quot;ad&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| VALIDATED | &quot;validated&quot; |
| SKIPPED | &quot;skipped&quot; |



