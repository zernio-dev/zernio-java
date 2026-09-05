

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
|**failureCount** | **Integer** | Consecutive terminal delivery failures (resets to 0 on any successful delivery). Auto-disable only triggers when the endpoint has had no successful delivery within a 3-day window AND either reaches 20 consecutive terminal failures or has been failing continuously for 3 days; any success within that window keeps the endpoint enabled regardless of the count. |  [optional] |
|**customHeaders** | **Map&lt;String, String&gt;** | Custom headers included in webhook requests |  [optional] |
|**disabledResourceGroups** | [**List&lt;DisabledResourceGroupsEnum&gt;**](#List&lt;DisabledResourceGroupsEnum&gt;) | Resource groups this subscription does not receive (opt-out denylist, same vocabulary and same semantics as the field on API keys). Absent or empty means the subscription receives every event listed in &#x60;events&#x60;, which is how every subscription created before this field existed behaves. An event whose group is listed here is dropped before delivery even when it is still present in &#x60;events&#x60;, and the same check runs on every replay path (test fire, redelivery, dead-letter requeue). Editing the denylist applies to every event emitted afterwards; events already queued when the edit landed can still be delivered for up to five minutes after they were enqueued. |  [optional] |



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
| POST_PLATFORM_DELETED | &quot;post.platform.deleted&quot; |
| POST_TIKTOK_URL_RESOLVED | &quot;post.tiktok.url_resolved&quot; |
| POST_EXTERNAL_CREATED | &quot;post.external.created&quot; |
| POST_EXTERNAL_UPDATED | &quot;post.external.updated&quot; |
| POST_EXTERNAL_DELETED | &quot;post.external.deleted&quot; |
| ACCOUNT_CONNECTED | &quot;account.connected&quot; |
| ACCOUNT_DISCONNECTED | &quot;account.disconnected&quot; |
| ACCOUNT_ADS_INITIAL_SYNC_COMPLETED | &quot;account.ads.initial_sync_completed&quot; |
| ANALYTICS_SYNCED | &quot;analytics.synced&quot; |
| MESSAGE_RECEIVED | &quot;message.received&quot; |
| CONVERSATION_STARTED | &quot;conversation.started&quot; |
| CALL_RECEIVED | &quot;call.received&quot; |
| CALL_ENDED | &quot;call.ended&quot; |
| CALL_FAILED | &quot;call.failed&quot; |
| CALL_PERMISSION_REQUEST | &quot;call.permission_request&quot; |
| MESSAGE_SENT | &quot;message.sent&quot; |
| MESSAGE_EDITED | &quot;message.edited&quot; |
| MESSAGE_DELETED | &quot;message.deleted&quot; |
| MESSAGE_DELIVERED | &quot;message.delivered&quot; |
| MESSAGE_READ | &quot;message.read&quot; |
| MESSAGE_FAILED | &quot;message.failed&quot; |
| REACTION_RECEIVED | &quot;reaction.received&quot; |
| REFERRAL_RECEIVED | &quot;referral.received&quot; |
| COMMENT_RECEIVED | &quot;comment.received&quot; |
| REVIEW_NEW | &quot;review.new&quot; |
| REVIEW_UPDATED | &quot;review.updated&quot; |
| LEAD_RECEIVED | &quot;lead.received&quot; |
| AD_STATUS_CHANGED | &quot;ad.status_changed&quot; |
| WHATSAPP_TEMPLATE_STATUS_UPDATED | &quot;whatsapp.template.status_updated&quot; |
| WHATSAPP_TEMPLATE_CATEGORY_UPDATED | &quot;whatsapp.template.category_updated&quot; |
| WHATSAPP_ACCOUNT_NAME_STATUS_UPDATED | &quot;whatsapp.account.name_status_updated&quot; |
| WHATSAPP_AUTOMATIC_EVENT | &quot;whatsapp.automatic_event&quot; |
| WHATSAPP_NUMBER_ACTIVATED | &quot;whatsapp.number.activated&quot; |
| WHATSAPP_NUMBER_DECLINED | &quot;whatsapp.number.declined&quot; |
| WHATSAPP_NUMBER_ACTION_REQUIRED | &quot;whatsapp.number.action_required&quot; |
| WHATSAPP_NUMBER_VERIFICATION_REQUIRED | &quot;whatsapp.number.verification_required&quot; |
| WHATSAPP_NUMBER_SUSPENDED | &quot;whatsapp.number.suspended&quot; |
| WHATSAPP_NUMBER_REACTIVATED | &quot;whatsapp.number.reactivated&quot; |
| WHATSAPP_NUMBER_RELEASED | &quot;whatsapp.number.released&quot; |
| WHATSAPP_NUMBER_KYC_SUBMITTED | &quot;whatsapp.number.kyc_submitted&quot; |
| PHONE_NUMBER_STOCK_AVAILABLE | &quot;phone_number.stock_available&quot; |
| VERIFICATION_APPROVED | &quot;verification.approved&quot; |
| VERIFICATION_FAILED | &quot;verification.failed&quot; |



## Enum: List&lt;DisabledResourceGroupsEnum&gt;

| Name | Value |
|---- | -----|
| PUBLISHING | &quot;publishing&quot; |
| ENGAGEMENT | &quot;engagement&quot; |
| MESSAGES | &quot;messages&quot; |
| CONTACTS | &quot;contacts&quot; |
| ANALYTICS | &quot;analytics&quot; |
| ADS | &quot;ads&quot; |
| TELEPHONY | &quot;telephony&quot; |
| ACCOUNTS | &quot;accounts&quot; |
| BILLING | &quot;billing&quot; |
| WEBHOOKS | &quot;webhooks&quot; |



