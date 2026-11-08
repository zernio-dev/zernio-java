

# WebhookPayloadBalanceChargedTopup


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The top-up id, as in GET /v1/balance (&#x60;recentTopups&#x60;) and its invoice and receipt endpoints. |  |
|**trigger** | [**TriggerEnum**](#TriggerEnum) | &#x60;manual&#x60;: someone topped up in Billing or through the API. &#x60;auto_top_up&#x60;: the auto top-up rule charged the card. |  |
|**amountCents** | **Integer** | Added to the balance, in USD cents. |  |
|**taxCents** | **Integer** | VAT charged on top, in USD cents (0 when none applies). |  |
|**chargedCents** | **Integer** | What the card was charged, in USD cents: amount plus tax. |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) |  |  |
|**card** | [**WebhookPayloadBalanceChargedTopupCard**](WebhookPayloadBalanceChargedTopupCard.md) |  |  |



## Enum: TriggerEnum

| Name | Value |
|---- | -----|
| MANUAL | &quot;manual&quot; |
| AUTO_TOP_UP | &quot;auto_top_up&quot; |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| USD | &quot;usd&quot; |



