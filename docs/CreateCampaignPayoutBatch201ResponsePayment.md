

# CreateCampaignPayoutBatch201ResponsePayment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**clientSecret** | **String** | PaymentIntent client secret for Stripe.js handleNextAction; set only when status is requires_action |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;succeeded&quot; |
| PROCESSING | &quot;processing&quot; |
| REQUIRES_ACTION | &quot;requires_action&quot; |



