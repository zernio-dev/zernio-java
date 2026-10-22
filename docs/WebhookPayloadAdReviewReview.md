

# WebhookPayloadAdReviewReview


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**raw** | **String** | Platform-native status string, forwarded verbatim (Meta &#x60;ACTIVE&#x60; / &#x60;DISAPPROVED&#x60;, TikTok &#x60;DISABLE&#x60;, ...). |  |
|**reasons** | [**List&lt;WebhookPayloadAdReviewReviewReasonsInner&gt;**](WebhookPayloadAdReviewReviewReasonsInner.md) | Why the platform rejected the ad, when it says. Always empty on &#x60;approved&#x60;. Most networks only return a generic message today. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| APPROVED | &quot;approved&quot; |
| REJECTED | &quot;rejected&quot; |



