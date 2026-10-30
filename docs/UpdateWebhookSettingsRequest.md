

# UpdateWebhookSettingsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**webhookId** | **String** | Webhook ID to update. Required unless the deprecated &#x60;_id&#x60; is sent instead. |  [optional] |
|**id** | **String** | Alias of webhookId, kept for existing callers |  [optional] |
|**name** | **String** | Webhook name (1-50 characters). Must be non-empty if provided. |  [optional] |
|**url** | **URI** | Webhook endpoint URL (must be a valid URL, whitespace trimmed). Must be a valid URL if provided. |  [optional] |
|**secret** | **String** | Secret key for HMAC-SHA256 signature verification |  [optional] |
|**events** | [**List&lt;EventsEnum&gt;**](#List&lt;EventsEnum&gt;) | Events to subscribe to. Must contain at least one event if provided. |  [optional] |
|**isActive** | **Boolean** | Enable or disable webhook delivery |  [optional] |
|**customHeaders** | **Map&lt;String, String&gt;** | Custom headers to include in webhook requests |  [optional] |
|**disabledResourceGroups** | [**List&lt;DisabledResourceGroupsEnum&gt;**](#List&lt;DisabledResourceGroupsEnum&gt;) | Replaces the subscription&#39;s denylist.  - Send an empty array to clear it and receive every event in &#x60;events&#x60; again. - Omit the field to leave the current denylist untouched. - Applies to events emitted after the update; already-queued events can still deliver for up to five minutes after they were enqueued. - With a restricted (zrk_) key, that key&#39;s own disabled groups are unioned back in either way, so it can neither clear nor widen a subscription past its own groups.  |  [optional] |
|**profileIds** | **List&lt;String&gt;** | Replaces the subscription&#39;s profile allowlist. Applies to events emitted after the update.  - Empty array: receive every profile again. - Omitted: the current list is left untouched. - Every id must be a profile in your team, otherwise the request fails with 404 &#x60;profile_not_found&#x60; and nothing changes.  Sending the stored list back unchanged is accepted without re-validation, so an endpoint stays editable after a listed profile is deleted.  |  [optional] |
|**accountIds** | **List&lt;String&gt;** | Replaces the subscription&#39;s account allowlist.  - Send an empty array to receive every account again. - Omit the field to leave the current list untouched. - Every id must be an account in your team, otherwise the request fails with 404 &#x60;account_not_found&#x60; and nothing changes. - Sending the stored list back unchanged is accepted without re-validation.  |  [optional] |



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
| ACCOUNT_PERMISSIONS_CHANGED | &quot;account.permissions_changed&quot; |
| ACCOUNT_ADS_INITIAL_SYNC_COMPLETED | &quot;account.ads.initial_sync_completed&quot; |
| ACCOUNT_ADS_SYNC_FAILED | &quot;account.ads.sync_failed&quot; |
| ACCOUNT_ADS_SYNC_RECOVERED | &quot;account.ads.sync_recovered&quot; |
| ANALYTICS_SYNCED | &quot;analytics.synced&quot; |
| POST_TRACKING_COMPLETED | &quot;post.tracking_completed&quot; |
| POST_AUTHENTICITY_CHANGED | &quot;post.authenticity_changed&quot; |
| MESSAGE_RECEIVED | &quot;message.received&quot; |
| CONVERSATION_STARTED | &quot;conversation.started&quot; |
| CONVERSATION_CONTROL_CHANGED | &quot;conversation.control_changed&quot; |
| CALL_RECEIVED | &quot;call.received&quot; |
| CALL_ENDED | &quot;call.ended&quot; |
| CALL_FAILED | &quot;call.failed&quot; |
| CALL_PERMISSION_REQUEST | &quot;call.permission_request&quot; |
| MESSAGE_SENT | &quot;message.sent&quot; |
| MESSAGE_EDITED | &quot;message.edited&quot; |
| MESSAGE_DELETED | &quot;message.deleted&quot; |
| MESSAGE_DELIVERED | &quot;message.delivered&quot; |
| MESSAGE_READ | &quot;message.read&quot; |
| MESSAGE_PLAYED | &quot;message.played&quot; |
| MESSAGE_FAILED | &quot;message.failed&quot; |
| REACTION_RECEIVED | &quot;reaction.received&quot; |
| REFERRAL_RECEIVED | &quot;referral.received&quot; |
| COMMENT_RECEIVED | &quot;comment.received&quot; |
| REVIEW_NEW | &quot;review.new&quot; |
| REVIEW_UPDATED | &quot;review.updated&quot; |
| REVIEW_DELETED | &quot;review.deleted&quot; |
| REVIEW_RESTORED | &quot;review.restored&quot; |
| LEAD_RECEIVED | &quot;lead.received&quot; |
| AD_STATUS_CHANGED | &quot;ad.status_changed&quot; |
| AD_REVIEW_APPROVED | &quot;ad.review.approved&quot; |
| AD_REVIEW_REJECTED | &quot;ad.review.rejected&quot; |
| AD_DELIVERY_ISSUE | &quot;ad.delivery_issue&quot; |
| CAMPAIGN_BUDGET_DEPLETED | &quot;campaign.budget.depleted&quot; |
| AD_ACCOUNT_STATUS_CHANGED | &quot;ad_account.status_changed&quot; |
| AD_VIDEO_PROCESSED | &quot;ad.video.processed&quot; |
| AD_RULE_TRIGGERED | &quot;ad_rule.triggered&quot; |
| WHATSAPP_TEMPLATE_STATUS_UPDATED | &quot;whatsapp.template.status_updated&quot; |
| WHATSAPP_TEMPLATE_CATEGORY_UPDATED | &quot;whatsapp.template.category_updated&quot; |
| WHATSAPP_ACCOUNT_NAME_STATUS_UPDATED | &quot;whatsapp.account.name_status_updated&quot; |
| WHATSAPP_ACCOUNT_QUALITY_UPDATED | &quot;whatsapp.account.quality_updated&quot; |
| WHATSAPP_ACCOUNT_STATUS_UPDATED | &quot;whatsapp.account.status_updated&quot; |
| WHATSAPP_ACCOUNT_ALERT_RECEIVED | &quot;whatsapp.account.alert_received&quot; |
| WHATSAPP_CONTACT_IDENTITY_CHANGED | &quot;whatsapp.contact.identity_changed&quot; |
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
| API_CHANGELOG_PUBLISHED | &quot;api.changelog.published&quot; |
| SMS_REGISTRATION_ACTION_REQUIRED | &quot;sms.registration.action_required&quot; |
| SMS_REGISTRATION_STATUS_UPDATED | &quot;sms.registration.status_updated&quot; |
| BRANDED_CALLING_IDENTITY_STATUS_UPDATED | &quot;branded_calling.identity.status_updated&quot; |
| BRANDED_CALLING_IDENTITY_ACTION_REQUIRED | &quot;branded_calling.identity.action_required&quot; |
| BRANDED_CALLING_NUMBER_STATUS_UPDATED | &quot;branded_calling.number.status_updated&quot; |
| RCS_AGENT_STATUS_UPDATED | &quot;rcs.agent.status_updated&quot; |
| COMMERCE_PRODUCT_CREATED | &quot;commerce.product.created&quot; |
| COMMERCE_PRODUCT_UPDATED | &quot;commerce.product.updated&quot; |
| COMMERCE_PRODUCT_DELETED | &quot;commerce.product.deleted&quot; |
| COMMERCE_ORDER_CREATED | &quot;commerce.order.created&quot; |
| COMMERCE_ORDER_UPDATED | &quot;commerce.order.updated&quot; |
| COMMERCE_ORDER_REFUNDED | &quot;commerce.order.refunded&quot; |
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
| CAMPAIGN_SUBMISSION_RECEIVED | &quot;campaign_submission.received&quot; |
| CAMPAIGN_SUBMISSION_FLAGGED | &quot;campaign_submission.flagged&quot; |
| CAMPAIGN_SUBMISSION_PENDING_REVIEW | &quot;campaign_submission.pending_review&quot; |
| CAMPAIGN_SUBMISSION_APPROVED | &quot;campaign_submission.approved&quot; |
| CAMPAIGN_SUBMISSION_REJECTED | &quot;campaign_submission.rejected&quot; |
| CREATOR_CAMPAIGN_BUDGET_EXHAUSTED | &quot;creator_campaign.budget_exhausted&quot; |
| CREATOR_CAMPAIGN_CLOSED | &quot;creator_campaign.closed&quot; |
| CAMPAIGN_PAYOUT_PAYABLE | &quot;campaign_payout.payable&quot; |
| CAMPAIGN_PAYOUT_SETTLED | &quot;campaign_payout.settled&quot; |
| CAMPAIGN_PAYOUT_FAILED | &quot;campaign_payout.failed&quot; |
| CAMPAIGN_PARTICIPANT_JOINED | &quot;campaign_participant.joined&quot; |
| CAMPAIGN_PARTICIPANT_SUSPENDED | &quot;campaign_participant.suspended&quot; |
| CAMPAIGN_PARTICIPANT_REMOVED | &quot;campaign_participant.removed&quot; |



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
| COMMERCE | &quot;commerce&quot; |
| CREATOR_CAMPAIGNS | &quot;creator_campaigns&quot; |
| MONEY | &quot;money&quot; |
| CALENDAR | &quot;calendar&quot; |
| FILES | &quot;files&quot; |



