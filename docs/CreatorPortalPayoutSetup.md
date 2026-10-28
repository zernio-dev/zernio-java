

# CreatorPortalPayoutSetup


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mode** | [**ModeEnum**](#ModeEnum) | How the campaign pays: treasury means through Zernio, so the creator onboards for payouts. |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**country** | **String** |  |  |
|**transfers** | [**List&lt;CreatorPortalPayoutSetupTransfersInner&gt;**](CreatorPortalPayoutSetupTransfersInner.md) | Treasury payouts sent to the creator. |  |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| EXTERNAL | &quot;external&quot; |
| TREASURY | &quot;treasury&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NOT_STARTED | &quot;not_started&quot; |
| PENDING | &quot;pending&quot; |
| ENABLED | &quot;enabled&quot; |
| NOT_APPLICABLE | &quot;not_applicable&quot; |



