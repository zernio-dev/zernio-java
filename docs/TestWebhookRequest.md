

# TestWebhookRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**webhookId** | **String** | ID of the webhook to test |  |
|**event** | [**EventEnum**](#EventEnum) | Send a sample payload of this event instead of &#x60;webhook.test&#x60;. The sample is marked with &#x60;test: true&#x60;. |  [optional] |



## Enum: EventEnum

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
| ACCOUNT_ADS_SYNC_FAILED | &quot;account.ads.sync_failed&quot; |
| ACCOUNT_ADS_SYNC_RECOVERED | &quot;account.ads.sync_recovered&quot; |
| ANALYTICS_SYNCED | &quot;analytics.synced&quot; |
| MESSAGE_RECEIVED | &quot;message.received&quot; |
| MESSAGE_SENT | &quot;message.sent&quot; |
| MESSAGE_EDITED | &quot;message.edited&quot; |
| MESSAGE_DELETED | &quot;message.deleted&quot; |
| MESSAGE_DELIVERED | &quot;message.delivered&quot; |
| MESSAGE_READ | &quot;message.read&quot; |
| MESSAGE_PLAYED | &quot;message.played&quot; |
| MESSAGE_FAILED | &quot;message.failed&quot; |
| REACTION_RECEIVED | &quot;reaction.received&quot; |
| REFERRAL_RECEIVED | &quot;referral.received&quot; |
| CONVERSATION_STARTED | &quot;conversation.started&quot; |
| CONVERSATION_CONTROL_CHANGED | &quot;conversation.control_changed&quot; |
| CONTACT_TAG_ADDED | &quot;contact.tag_added&quot; |
| CONTACT_TAG_REMOVED | &quot;contact.tag_removed&quot; |
| CONTACT_FIELD_CHANGED | &quot;contact.field_changed&quot; |
| SEQUENCE_ENROLLED | &quot;sequence.enrolled&quot; |
| SEQUENCE_EXITED | &quot;sequence.exited&quot; |
| WORKFLOW_RUN_STARTED | &quot;workflow.run.started&quot; |
| WORKFLOW_RUN_COMPLETED | &quot;workflow.run.completed&quot; |
| WORKFLOW_RUN_FAILED | &quot;workflow.run.failed&quot; |
| SUPPORT_RUN_COMPLETED | &quot;support.run.completed&quot; |
| SUPPORT_RUN_FAILED | &quot;support.run.failed&quot; |
| CALL_RECEIVED | &quot;call.received&quot; |
| CALL_ENDED | &quot;call.ended&quot; |
| CALL_FAILED | &quot;call.failed&quot; |
| CALL_PERMISSION_REQUEST | &quot;call.permission_request&quot; |
| COMMENT_RECEIVED | &quot;comment.received&quot; |
| REVIEW_NEW | &quot;review.new&quot; |
| REVIEW_UPDATED | &quot;review.updated&quot; |
| AD_STATUS_CHANGED | &quot;ad.status_changed&quot; |
| AD_VIDEO_PROCESSED | &quot;ad.video.processed&quot; |
| LEAD_RECEIVED | &quot;lead.received&quot; |
| WHATSAPP_TEMPLATE_STATUS_UPDATED | &quot;whatsapp.template.status_updated&quot; |
| WHATSAPP_TEMPLATE_CATEGORY_UPDATED | &quot;whatsapp.template.category_updated&quot; |
| WHATSAPP_ACCOUNT_NAME_STATUS_UPDATED | &quot;whatsapp.account.name_status_updated&quot; |
| WHATSAPP_ACCOUNT_QUALITY_UPDATED | &quot;whatsapp.account.quality_updated&quot; |
| WHATSAPP_ACCOUNT_STATUS_UPDATED | &quot;whatsapp.account.status_updated&quot; |
| WHATSAPP_ACCOUNT_ALERT_RECEIVED | &quot;whatsapp.account.alert_received&quot; |
| WHATSAPP_CONTACT_IDENTITY_CHANGED | &quot;whatsapp.contact.identity_changed&quot; |
| WHATSAPP_NUMBER_ACTIVATED | &quot;whatsapp.number.activated&quot; |
| WHATSAPP_NUMBER_DECLINED | &quot;whatsapp.number.declined&quot; |
| WHATSAPP_NUMBER_ACTION_REQUIRED | &quot;whatsapp.number.action_required&quot; |
| WHATSAPP_AUTOMATIC_EVENT | &quot;whatsapp.automatic_event&quot; |
| WHATSAPP_NUMBER_VERIFICATION_REQUIRED | &quot;whatsapp.number.verification_required&quot; |
| WHATSAPP_NUMBER_SUSPENDED | &quot;whatsapp.number.suspended&quot; |
| WHATSAPP_NUMBER_REACTIVATED | &quot;whatsapp.number.reactivated&quot; |
| WHATSAPP_NUMBER_RELEASED | &quot;whatsapp.number.released&quot; |
| WHATSAPP_NUMBER_KYC_SUBMITTED | &quot;whatsapp.number.kyc_submitted&quot; |
| PHONE_NUMBER_STOCK_AVAILABLE | &quot;phone_number.stock_available&quot; |
| SMS_REGISTRATION_ACTION_REQUIRED | &quot;sms.registration.action_required&quot; |
| SMS_REGISTRATION_STATUS_UPDATED | &quot;sms.registration.status_updated&quot; |
| BRANDED_CALLING_IDENTITY_STATUS_UPDATED | &quot;branded_calling.identity.status_updated&quot; |
| BRANDED_CALLING_IDENTITY_ACTION_REQUIRED | &quot;branded_calling.identity.action_required&quot; |
| BRANDED_CALLING_NUMBER_STATUS_UPDATED | &quot;branded_calling.number.status_updated&quot; |
| RCS_AGENT_STATUS_UPDATED | &quot;rcs.agent.status_updated&quot; |
| VERIFICATION_APPROVED | &quot;verification.approved&quot; |
| VERIFICATION_FAILED | &quot;verification.failed&quot; |
| COMMERCE_PRODUCT_CREATED | &quot;commerce.product.created&quot; |
| COMMERCE_PRODUCT_UPDATED | &quot;commerce.product.updated&quot; |
| COMMERCE_PRODUCT_DELETED | &quot;commerce.product.deleted&quot; |
| API_CHANGELOG_PUBLISHED | &quot;api.changelog.published&quot; |



