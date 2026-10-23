

# WebhookPayloadAdRuleTriggeredRun


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | ID of the rule run that triggered. |  |
|**ranAt** | **OffsetDateTime** | Scheduled time of the run (UTC). |  |
|**today** | **LocalDate** | The ad account&#39;s calendar date (YYYY-MM-DD) the condition windows were resolved against, so &#x60;today&#x60; and &#x60;last_7d&#x60; mean the account&#39;s days, not UTC days. |  |
|**timezone** | **String** | IANA timezone used for &#x60;today&#x60;, for example &#x60;Europe/Madrid&#x60;. |  |
|**timezoneAssumed** | **Boolean** | True when the ad account has no known timezone and UTC was assumed. |  |
|**currency** | **String** | ISO 4217 currency of the ad account, which money metrics (&#x60;spend&#x60;, &#x60;cpc&#x60;, &#x60;cpm&#x60;, &#x60;cpa&#x60;) and condition values are in. Null when unknown. |  |



