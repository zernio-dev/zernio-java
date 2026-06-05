

# Webhook

Individual webhook configuration for receiving real-time notifications

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Unique webhook identifier |  [optional] |
|**name** | **String** | Webhook name (for identification) |  [optional] |
|**url** | **URI** | Webhook endpoint URL |  [optional] |
|**secret** | **String** | Secret key for HMAC-SHA256 signature verification. |  [optional] |
|**events** | [**List&lt;EventsEnum&gt;**](#List&lt;EventsEnum&gt;) | Events subscribed to |  [optional] |
|**isActive** | **Boolean** | Whether webhook delivery is enabled |  [optional] |
|**lastFiredAt** | **OffsetDateTime** | Timestamp of last successful webhook delivery |  [optional] |
|**failureCount** | **Integer** | Consecutive delivery failures (resets on success, webhook disabled at 10) |  [optional] |
|**customHeaders** | **Map&lt;String, String&gt;** | Custom headers included in webhook requests |  [optional] |



## Enum: List&lt;EventsEnum&gt;

| Name | Value |
|---- | -----|
| POST_SCHEDULED | &quot;post.scheduled&quot; |
| POST_PUBLISHED | &quot;post.published&quot; |
| POST_FAILED | &quot;post.failed&quot; |
| POST_PARTIAL | &quot;post.partial&quot; |
| POST_CANCELLED | &quot;post.cancelled&quot; |
| POST_RECYCLED | &quot;post.recycled&quot; |
| POST_PLATFORM_PUBLISHED | &quot;post.platform.published&quot; |
| POST_PLATFORM_FAILED | &quot;post.platform.failed&quot; |
| POST_EXTERNAL_CREATED | &quot;post.external.created&quot; |
| POST_EXTERNAL_UPDATED | &quot;post.external.updated&quot; |
| POST_EXTERNAL_DELETED | &quot;post.external.deleted&quot; |
| ACCOUNT_CONNECTED | &quot;account.connected&quot; |
| ACCOUNT_DISCONNECTED | &quot;account.disconnected&quot; |
| ACCOUNT_ADS_INITIAL_SYNC_COMPLETED | &quot;account.ads.initial_sync_completed&quot; |
| MESSAGE_RECEIVED | &quot;message.received&quot; |
| MESSAGE_SENT | &quot;message.sent&quot; |
| MESSAGE_EDITED | &quot;message.edited&quot; |
| MESSAGE_DELETED | &quot;message.deleted&quot; |
| MESSAGE_DELIVERED | &quot;message.delivered&quot; |
| MESSAGE_READ | &quot;message.read&quot; |
| MESSAGE_FAILED | &quot;message.failed&quot; |
| REACTION_RECEIVED | &quot;reaction.received&quot; |
| COMMENT_RECEIVED | &quot;comment.received&quot; |
| REVIEW_NEW | &quot;review.new&quot; |
| REVIEW_UPDATED | &quot;review.updated&quot; |
| AD_STATUS_CHANGED | &quot;ad.status_changed&quot; |
| WHATSAPP_TEMPLATE_STATUS_UPDATED | &quot;whatsapp.template.status_updated&quot; |
| WHATSAPP_NUMBER_ACTIVATED | &quot;whatsapp.number.activated&quot; |
| WHATSAPP_NUMBER_DECLINED | &quot;whatsapp.number.declined&quot; |
| WHATSAPP_NUMBER_VERIFICATION_REQUIRED | &quot;whatsapp.number.verification_required&quot; |
| WHATSAPP_NUMBER_SUSPENDED | &quot;whatsapp.number.suspended&quot; |
| WHATSAPP_NUMBER_REACTIVATED | &quot;whatsapp.number.reactivated&quot; |
| WHATSAPP_NUMBER_RELEASED | &quot;whatsapp.number.released&quot; |



