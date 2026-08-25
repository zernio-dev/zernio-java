

# UpdateWebhookSettingsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Webhook ID to update (required) |  |
|**name** | **String** | Webhook name (1-50 characters). Must be non-empty if provided. |  [optional] |
|**url** | **URI** | Webhook endpoint URL (must be a valid URL, whitespace trimmed). Must be a valid URL if provided. |  [optional] |
|**secret** | **String** | Secret key for HMAC-SHA256 signature verification |  [optional] |
|**events** | [**List&lt;EventsEnum&gt;**](#List&lt;EventsEnum&gt;) | Events to subscribe to. Must contain at least one event if provided. |  [optional] |
|**isActive** | **Boolean** | Enable or disable webhook delivery |  [optional] |
|**customHeaders** | **Map&lt;String, String&gt;** | Custom headers to include in webhook requests |  [optional] |
|**disabledResourceGroups** | [**List&lt;DisabledResourceGroupsEnum&gt;**](#List&lt;DisabledResourceGroupsEnum&gt;) | Replaces the subscription&#39;s denylist. Send an empty array to clear it and receive every event in &#x60;events&#x60; again. Omitting the field leaves the current denylist untouched. Applies to events emitted after the update; already-queued events can still deliver for up to five minutes after they were enqueued. When the caller is a restricted (zrk_) key, that key&#39;s own disabled groups are unioned back in either way, so a restricted key can neither clear nor widen a subscription past its own groups. |  [optional] |



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



