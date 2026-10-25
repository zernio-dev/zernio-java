

# WebhookPayloadAdRuleTriggeredObjectsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**platformId** | **String** | Platform-native ID of the campaign or ad set. |  |
|**name** | **String** | Name on the platform. Falls back to &#x60;platformId&#x60; when the platform reports none. |  |
|**platformCampaignId** | **String** | Platform-native ID of the campaign the object belongs to (on a campaign-level rule, the campaign&#39;s own ID). Null when unknown. |  |
|**conditions** | [**List&lt;WebhookPayloadAdRuleTriggeredObjectsInnerConditionsInner&gt;**](WebhookPayloadAdRuleTriggeredObjectsInnerConditionsInner.md) | Every condition of the rule, with the value the object reached. |  |
|**actions** | [**List&lt;WebhookPayloadAdRuleTriggeredObjectsInnerActionsInner&gt;**](WebhookPayloadAdRuleTriggeredObjectsInnerActionsInner.md) | What the rule did to the object. Empty on a rule that only notifies. |  |



