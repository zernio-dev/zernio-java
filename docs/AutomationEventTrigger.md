

# AutomationEventTrigger

Starts the automation when something happens in Zernio, in one profile. `GET /v1/automations/catalog` lists every event with its facts. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | The Zernio event that starts it. |  |
|**profileId** | **String** | The profile whose events start it, from &#x60;GET /v1/profiles&#x60;. |  |
|**accountIds** | **List&lt;String&gt;** | Only events of these accounts. Leave out for every account of the profile. |  [optional] |
|**filter** | [**AutomationFactCondition**](AutomationFactCondition.md) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| POST_FAILED | &quot;post.failed&quot; |
| POST_PARTIAL | &quot;post.partial&quot; |
| POST_PUBLISHED | &quot;post.published&quot; |
| POST_SCHEDULED | &quot;post.scheduled&quot; |
| POST_RECYCLED | &quot;post.recycled&quot; |
| POST_PLATFORM_PUBLISHED | &quot;post.platform.published&quot; |
| POST_PLATFORM_FAILED | &quot;post.platform.failed&quot; |
| POST_PLATFORM_DELETED | &quot;post.platform.deleted&quot; |
| POST_EXTERNAL_CREATED | &quot;post.external.created&quot; |
| ACCOUNT_CONNECTED | &quot;account.connected&quot; |
| ACCOUNT_DISCONNECTED | &quot;account.disconnected&quot; |
| ACCOUNT_PERMISSIONS_CHANGED | &quot;account.permissions_changed&quot; |
| ACCOUNT_RATE_LIMITED | &quot;account.rate_limited&quot; |
| ACCOUNT_ADS_SYNC_FAILED | &quot;account.ads.sync_failed&quot; |
| AD_STATUS_CHANGED | &quot;ad.status_changed&quot; |
| AD_REVIEW_REJECTED | &quot;ad.review.rejected&quot; |
| AD_DELIVERY_ISSUE | &quot;ad.delivery_issue&quot; |
| CAMPAIGN_BUDGET_DEPLETED | &quot;campaign.budget.depleted&quot; |
| AD_ACCOUNT_STATUS_CHANGED | &quot;ad_account.status_changed&quot; |
| CAMPAIGN_STATUS_CHANGED | &quot;campaign.status_changed&quot; |
| WHATSAPP_TEMPLATE_STATUS_UPDATED | &quot;whatsapp.template.status_updated&quot; |
| WHATSAPP_ACCOUNT_QUALITY_UPDATED | &quot;whatsapp.account.quality_updated&quot; |
| COMMERCE_ORDER_CREATED | &quot;commerce.order.created&quot; |
| COMMERCE_ORDER_UPDATED | &quot;commerce.order.updated&quot; |
| COMMERCE_ORDER_REFUNDED | &quot;commerce.order.refunded&quot; |
| MESSAGE_RECEIVED | &quot;message.received&quot; |
| MESSAGE_FAILED | &quot;message.failed&quot; |
| CONVERSATION_STARTED | &quot;conversation.started&quot; |
| REACTION_RECEIVED | &quot;reaction.received&quot; |
| REFERRAL_RECEIVED | &quot;referral.received&quot; |
| COMMENT_RECEIVED | &quot;comment.received&quot; |
| REVIEW_NEW | &quot;review.new&quot; |
| CALL_RECEIVED | &quot;call.received&quot; |
| CALL_ENDED | &quot;call.ended&quot; |
| CALL_FAILED | &quot;call.failed&quot; |
| LEAD_RECEIVED | &quot;lead.received&quot; |



