

# CreatorPortalPayoutSetup


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mode** | [**ModeEnum**](#ModeEnum) | How the campaign pays: treasury means through Zernio, so the creator onboards for payouts, which they can do from the moment they join. Earnings wait until it is done. |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**country** | **String** |  |  |
|**suggestedCountry** | **String** | The country the request came from, to preselect before payout setup starts. Null once the payout account has a country, and outside treasury mode. |  |
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



