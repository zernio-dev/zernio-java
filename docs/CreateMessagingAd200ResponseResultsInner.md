

# CreateMessagingAd200ResponseResultsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**node** | [**NodeEnum**](#NodeEnum) |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**reason** | **String** | On unverified: why Meta could not dry-run this node although the other nodes passed. |  [optional] |



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



