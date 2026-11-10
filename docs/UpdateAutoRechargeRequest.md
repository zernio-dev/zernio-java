

# UpdateAutoRechargeRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Turns auto top-up on or off. A rule switched off by failed charges stays off until the card is updated. |  [optional] |
|**belowCents** | **Integer** | Auto top-up charges the card when the balance drops below this, in cents. At least $5. |  [optional] |
|**toCents** | **Integer** | Top back up to this, in cents. More than $5 above belowCents. |  [optional] |
|**monthlyLimitCents** | **Integer** | Most auto top-up may add per calendar month (UTC), before tax. At least toCents while auto top-up is on. Null for no limit. |  [optional] |
|**alertBelowCents** | **Integer** | Email the billing owner once each time the balance drops below this. Null for no email. |  [optional] |



