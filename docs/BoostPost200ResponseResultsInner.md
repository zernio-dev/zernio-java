

# BoostPost200ResponseResultsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**node** | [**NodeEnum**](#NodeEnum) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**reason** | **String** | Why the node was skipped (it already exists with adSetId), why Meta could not dry-run it (on unverified), or what the dry run could not check (on validated). |  [optional] |



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
| UNVERIFIED | &quot;unverified&quot; |



