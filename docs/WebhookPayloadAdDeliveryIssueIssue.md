

# WebhookPayloadAdDeliveryIssueIssue


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**raw** | **String** | Platform-native status string, forwarded verbatim (Meta &#x60;WITH_ISSUES&#x60;, TikTok &#x60;ADVERTISER_ACCOUNT_PUNISH&#x60;, LinkedIn &#x60;REMOVED&#x60;, ...). |  |
|**reasons** | [**List&lt;WebhookPayloadAdReviewReviewReasonsInner&gt;**](WebhookPayloadAdReviewReviewReasonsInner.md) | What the platform says is wrong. Meta reports it per campaign; other networks send no message today, so it is empty there. |  |



