

# CampaignParticipantPayout

How far the creator got with Stripe payout setup. Only `ready` creators can be paid through the Zernio treasury.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) | &#x60;not_started&#x60;: no payout account yet. &#x60;onboarding&#x60;: setup started or under review. &#x60;ready&#x60;: payouts enabled. &#x60;restricted&#x60;: Stripe needs more information before paying out. |  |
|**country** | **String** | ISO 3166-1 alpha-2 country of the payout account, null before setup starts. Zernio pays out only to the US, Canada, the UK, the EEA, Switzerland and Gibraltar; pay creators elsewhere yourself and record it with &#x60;recordOnly: true&#x60;. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NOT_STARTED | &quot;not_started&quot; |
| ONBOARDING | &quot;onboarding&quot; |
| READY | &quot;ready&quot; |
| RESTRICTED | &quot;restricted&quot; |



