# WebhookEventsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**onAccountAdsInitialSyncCompleted**](WebhookEventsApi.md#onAccountAdsInitialSyncCompleted) | **POST** /account.ads.initial_sync_completed | Ads initial sync completed event |
| [**onAccountAdsInitialSyncCompletedWithHttpInfo**](WebhookEventsApi.md#onAccountAdsInitialSyncCompletedWithHttpInfo) | **POST** /account.ads.initial_sync_completed | Ads initial sync completed event |
| [**onAccountAdsSyncFailed**](WebhookEventsApi.md#onAccountAdsSyncFailed) | **POST** /account.ads.sync_failed | Ads sync failed event |
| [**onAccountAdsSyncFailedWithHttpInfo**](WebhookEventsApi.md#onAccountAdsSyncFailedWithHttpInfo) | **POST** /account.ads.sync_failed | Ads sync failed event |
| [**onAccountAdsSyncRecovered**](WebhookEventsApi.md#onAccountAdsSyncRecovered) | **POST** /account.ads.sync_recovered | Ads sync recovered event |
| [**onAccountAdsSyncRecoveredWithHttpInfo**](WebhookEventsApi.md#onAccountAdsSyncRecoveredWithHttpInfo) | **POST** /account.ads.sync_recovered | Ads sync recovered event |
| [**onAccountConnected**](WebhookEventsApi.md#onAccountConnected) | **POST** /account.connected | Account connected event |
| [**onAccountConnectedWithHttpInfo**](WebhookEventsApi.md#onAccountConnectedWithHttpInfo) | **POST** /account.connected | Account connected event |
| [**onAccountDisconnected**](WebhookEventsApi.md#onAccountDisconnected) | **POST** /account.disconnected | Account disconnected event |
| [**onAccountDisconnectedWithHttpInfo**](WebhookEventsApi.md#onAccountDisconnectedWithHttpInfo) | **POST** /account.disconnected | Account disconnected event |
| [**onAccountPermissionsChanged**](WebhookEventsApi.md#onAccountPermissionsChanged) | **POST** /account.permissions_changed | Account permissions changed event |
| [**onAccountPermissionsChangedWithHttpInfo**](WebhookEventsApi.md#onAccountPermissionsChangedWithHttpInfo) | **POST** /account.permissions_changed | Account permissions changed event |
| [**onAccountRateLimited**](WebhookEventsApi.md#onAccountRateLimited) | **POST** /account.rate_limited | Mailbox sending cooldown started |
| [**onAccountRateLimitedWithHttpInfo**](WebhookEventsApi.md#onAccountRateLimitedWithHttpInfo) | **POST** /account.rate_limited | Mailbox sending cooldown started |
| [**onAdAccountStatusChanged**](WebhookEventsApi.md#onAdAccountStatusChanged) | **POST** /ad_account.status_changed | Ad account status changed event |
| [**onAdAccountStatusChangedWithHttpInfo**](WebhookEventsApi.md#onAdAccountStatusChangedWithHttpInfo) | **POST** /ad_account.status_changed | Ad account status changed event |
| [**onAdDeliveryIssue**](WebhookEventsApi.md#onAdDeliveryIssue) | **POST** /ad.delivery_issue | Ad delivery issue event |
| [**onAdDeliveryIssueWithHttpInfo**](WebhookEventsApi.md#onAdDeliveryIssueWithHttpInfo) | **POST** /ad.delivery_issue | Ad delivery issue event |
| [**onAdReviewApproved**](WebhookEventsApi.md#onAdReviewApproved) | **POST** /ad.review.approved | Ad review approved event |
| [**onAdReviewApprovedWithHttpInfo**](WebhookEventsApi.md#onAdReviewApprovedWithHttpInfo) | **POST** /ad.review.approved | Ad review approved event |
| [**onAdReviewRejected**](WebhookEventsApi.md#onAdReviewRejected) | **POST** /ad.review.rejected | Ad review rejected event |
| [**onAdReviewRejectedWithHttpInfo**](WebhookEventsApi.md#onAdReviewRejectedWithHttpInfo) | **POST** /ad.review.rejected | Ad review rejected event |
| [**onAdRuleTriggered**](WebhookEventsApi.md#onAdRuleTriggered) | **POST** /ad_rule.triggered | Ad rule triggered event |
| [**onAdRuleTriggeredWithHttpInfo**](WebhookEventsApi.md#onAdRuleTriggeredWithHttpInfo) | **POST** /ad_rule.triggered | Ad rule triggered event |
| [**onAdStatusChanged**](WebhookEventsApi.md#onAdStatusChanged) | **POST** /ad.status_changed | Ad status changed event |
| [**onAdStatusChangedWithHttpInfo**](WebhookEventsApi.md#onAdStatusChangedWithHttpInfo) | **POST** /ad.status_changed | Ad status changed event |
| [**onAdVideoProcessed**](WebhookEventsApi.md#onAdVideoProcessed) | **POST** /ad.video.processed | Ad video processed event |
| [**onAdVideoProcessedWithHttpInfo**](WebhookEventsApi.md#onAdVideoProcessedWithHttpInfo) | **POST** /ad.video.processed | Ad video processed event |
| [**onAnalyticsSynced**](WebhookEventsApi.md#onAnalyticsSynced) | **POST** /analytics.synced | Analytics synced event |
| [**onAnalyticsSyncedWithHttpInfo**](WebhookEventsApi.md#onAnalyticsSyncedWithHttpInfo) | **POST** /analytics.synced | Analytics synced event |
| [**onApiChangelogPublished**](WebhookEventsApi.md#onApiChangelogPublished) | **POST** /api.changelog.published | API changelog entry published event |
| [**onApiChangelogPublishedWithHttpInfo**](WebhookEventsApi.md#onApiChangelogPublishedWithHttpInfo) | **POST** /api.changelog.published | API changelog entry published event |
| [**onBrandedCallingIdentityActionRequired**](WebhookEventsApi.md#onBrandedCallingIdentityActionRequired) | **POST** /branded_calling.identity.action_required | Caller identity action required event |
| [**onBrandedCallingIdentityActionRequiredWithHttpInfo**](WebhookEventsApi.md#onBrandedCallingIdentityActionRequiredWithHttpInfo) | **POST** /branded_calling.identity.action_required | Caller identity action required event |
| [**onBrandedCallingIdentityStatusUpdated**](WebhookEventsApi.md#onBrandedCallingIdentityStatusUpdated) | **POST** /branded_calling.identity.status_updated | Caller identity status updated event |
| [**onBrandedCallingIdentityStatusUpdatedWithHttpInfo**](WebhookEventsApi.md#onBrandedCallingIdentityStatusUpdatedWithHttpInfo) | **POST** /branded_calling.identity.status_updated | Caller identity status updated event |
| [**onBrandedCallingNumberStatusUpdated**](WebhookEventsApi.md#onBrandedCallingNumberStatusUpdated) | **POST** /branded_calling.number.status_updated | Branded number status updated event |
| [**onBrandedCallingNumberStatusUpdatedWithHttpInfo**](WebhookEventsApi.md#onBrandedCallingNumberStatusUpdatedWithHttpInfo) | **POST** /branded_calling.number.status_updated | Branded number status updated event |
| [**onCalendarEventCreated**](WebhookEventsApi.md#onCalendarEventCreated) | **POST** /calendar.event.created | Calendar event created |
| [**onCalendarEventCreatedWithHttpInfo**](WebhookEventsApi.md#onCalendarEventCreatedWithHttpInfo) | **POST** /calendar.event.created | Calendar event created |
| [**onCalendarEventDeleted**](WebhookEventsApi.md#onCalendarEventDeleted) | **POST** /calendar.event.deleted | Calendar event deleted |
| [**onCalendarEventDeletedWithHttpInfo**](WebhookEventsApi.md#onCalendarEventDeletedWithHttpInfo) | **POST** /calendar.event.deleted | Calendar event deleted |
| [**onCalendarEventUpdated**](WebhookEventsApi.md#onCalendarEventUpdated) | **POST** /calendar.event.updated | Calendar event updated |
| [**onCalendarEventUpdatedWithHttpInfo**](WebhookEventsApi.md#onCalendarEventUpdatedWithHttpInfo) | **POST** /calendar.event.updated | Calendar event updated |
| [**onCallEnded**](WebhookEventsApi.md#onCallEnded) | **POST** /call.ended | Call ended event |
| [**onCallEndedWithHttpInfo**](WebhookEventsApi.md#onCallEndedWithHttpInfo) | **POST** /call.ended | Call ended event |
| [**onCallFailed**](WebhookEventsApi.md#onCallFailed) | **POST** /call.failed | Call failed event |
| [**onCallFailedWithHttpInfo**](WebhookEventsApi.md#onCallFailedWithHttpInfo) | **POST** /call.failed | Call failed event |
| [**onCallPermissionRequest**](WebhookEventsApi.md#onCallPermissionRequest) | **POST** /call.permission_request | Call permission request reply event |
| [**onCallPermissionRequestWithHttpInfo**](WebhookEventsApi.md#onCallPermissionRequestWithHttpInfo) | **POST** /call.permission_request | Call permission request reply event |
| [**onCallReceived**](WebhookEventsApi.md#onCallReceived) | **POST** /call.received | Call received event |
| [**onCallReceivedWithHttpInfo**](WebhookEventsApi.md#onCallReceivedWithHttpInfo) | **POST** /call.received | Call received event |
| [**onCampaignBudgetDepleted**](WebhookEventsApi.md#onCampaignBudgetDepleted) | **POST** /campaign.budget.depleted | Campaign budget depleted event |
| [**onCampaignBudgetDepletedWithHttpInfo**](WebhookEventsApi.md#onCampaignBudgetDepletedWithHttpInfo) | **POST** /campaign.budget.depleted | Campaign budget depleted event |
| [**onCampaignParticipantJoined**](WebhookEventsApi.md#onCampaignParticipantJoined) | **POST** /campaign_participant.joined | Campaign participant joined event |
| [**onCampaignParticipantJoinedWithHttpInfo**](WebhookEventsApi.md#onCampaignParticipantJoinedWithHttpInfo) | **POST** /campaign_participant.joined | Campaign participant joined event |
| [**onCampaignParticipantRemoved**](WebhookEventsApi.md#onCampaignParticipantRemoved) | **POST** /campaign_participant.removed | Campaign participant removed event |
| [**onCampaignParticipantRemovedWithHttpInfo**](WebhookEventsApi.md#onCampaignParticipantRemovedWithHttpInfo) | **POST** /campaign_participant.removed | Campaign participant removed event |
| [**onCampaignParticipantSuspended**](WebhookEventsApi.md#onCampaignParticipantSuspended) | **POST** /campaign_participant.suspended | Campaign participant suspended event |
| [**onCampaignParticipantSuspendedWithHttpInfo**](WebhookEventsApi.md#onCampaignParticipantSuspendedWithHttpInfo) | **POST** /campaign_participant.suspended | Campaign participant suspended event |
| [**onCampaignPayoutFailed**](WebhookEventsApi.md#onCampaignPayoutFailed) | **POST** /campaign_payout.failed | Campaign payout failed event |
| [**onCampaignPayoutFailedWithHttpInfo**](WebhookEventsApi.md#onCampaignPayoutFailedWithHttpInfo) | **POST** /campaign_payout.failed | Campaign payout failed event |
| [**onCampaignPayoutPayable**](WebhookEventsApi.md#onCampaignPayoutPayable) | **POST** /campaign_payout.payable | Campaign payout payable event |
| [**onCampaignPayoutPayableWithHttpInfo**](WebhookEventsApi.md#onCampaignPayoutPayableWithHttpInfo) | **POST** /campaign_payout.payable | Campaign payout payable event |
| [**onCampaignPayoutSettled**](WebhookEventsApi.md#onCampaignPayoutSettled) | **POST** /campaign_payout.settled | Campaign payout settled event |
| [**onCampaignPayoutSettledWithHttpInfo**](WebhookEventsApi.md#onCampaignPayoutSettledWithHttpInfo) | **POST** /campaign_payout.settled | Campaign payout settled event |
| [**onCampaignSubmissionApproved**](WebhookEventsApi.md#onCampaignSubmissionApproved) | **POST** /campaign_submission.approved | Campaign submission approved event |
| [**onCampaignSubmissionApprovedWithHttpInfo**](WebhookEventsApi.md#onCampaignSubmissionApprovedWithHttpInfo) | **POST** /campaign_submission.approved | Campaign submission approved event |
| [**onCampaignSubmissionFlagged**](WebhookEventsApi.md#onCampaignSubmissionFlagged) | **POST** /campaign_submission.flagged | Campaign submission flagged event |
| [**onCampaignSubmissionFlaggedWithHttpInfo**](WebhookEventsApi.md#onCampaignSubmissionFlaggedWithHttpInfo) | **POST** /campaign_submission.flagged | Campaign submission flagged event |
| [**onCampaignSubmissionPendingReview**](WebhookEventsApi.md#onCampaignSubmissionPendingReview) | **POST** /campaign_submission.pending_review | Campaign submission pending review event |
| [**onCampaignSubmissionPendingReviewWithHttpInfo**](WebhookEventsApi.md#onCampaignSubmissionPendingReviewWithHttpInfo) | **POST** /campaign_submission.pending_review | Campaign submission pending review event |
| [**onCampaignSubmissionReceived**](WebhookEventsApi.md#onCampaignSubmissionReceived) | **POST** /campaign_submission.received | Campaign submission received event |
| [**onCampaignSubmissionReceivedWithHttpInfo**](WebhookEventsApi.md#onCampaignSubmissionReceivedWithHttpInfo) | **POST** /campaign_submission.received | Campaign submission received event |
| [**onCampaignSubmissionRejected**](WebhookEventsApi.md#onCampaignSubmissionRejected) | **POST** /campaign_submission.rejected | Campaign submission rejected event |
| [**onCampaignSubmissionRejectedWithHttpInfo**](WebhookEventsApi.md#onCampaignSubmissionRejectedWithHttpInfo) | **POST** /campaign_submission.rejected | Campaign submission rejected event |
| [**onCommentReceived**](WebhookEventsApi.md#onCommentReceived) | **POST** /comment.received | Comment received event |
| [**onCommentReceivedWithHttpInfo**](WebhookEventsApi.md#onCommentReceivedWithHttpInfo) | **POST** /comment.received | Comment received event |
| [**onCommerceOrderCreated**](WebhookEventsApi.md#onCommerceOrderCreated) | **POST** /commerce.order.created | Commerce order created event |
| [**onCommerceOrderCreatedWithHttpInfo**](WebhookEventsApi.md#onCommerceOrderCreatedWithHttpInfo) | **POST** /commerce.order.created | Commerce order created event |
| [**onCommerceOrderRefunded**](WebhookEventsApi.md#onCommerceOrderRefunded) | **POST** /commerce.order.refunded | Commerce order refunded event |
| [**onCommerceOrderRefundedWithHttpInfo**](WebhookEventsApi.md#onCommerceOrderRefundedWithHttpInfo) | **POST** /commerce.order.refunded | Commerce order refunded event |
| [**onCommerceOrderUpdated**](WebhookEventsApi.md#onCommerceOrderUpdated) | **POST** /commerce.order.updated | Commerce order updated event |
| [**onCommerceOrderUpdatedWithHttpInfo**](WebhookEventsApi.md#onCommerceOrderUpdatedWithHttpInfo) | **POST** /commerce.order.updated | Commerce order updated event |
| [**onCommerceProductCreated**](WebhookEventsApi.md#onCommerceProductCreated) | **POST** /commerce.product.created | Commerce product created event |
| [**onCommerceProductCreatedWithHttpInfo**](WebhookEventsApi.md#onCommerceProductCreatedWithHttpInfo) | **POST** /commerce.product.created | Commerce product created event |
| [**onCommerceProductDeleted**](WebhookEventsApi.md#onCommerceProductDeleted) | **POST** /commerce.product.deleted | Commerce product deleted event |
| [**onCommerceProductDeletedWithHttpInfo**](WebhookEventsApi.md#onCommerceProductDeletedWithHttpInfo) | **POST** /commerce.product.deleted | Commerce product deleted event |
| [**onCommerceProductUpdated**](WebhookEventsApi.md#onCommerceProductUpdated) | **POST** /commerce.product.updated | Commerce product updated event |
| [**onCommerceProductUpdatedWithHttpInfo**](WebhookEventsApi.md#onCommerceProductUpdatedWithHttpInfo) | **POST** /commerce.product.updated | Commerce product updated event |
| [**onContactDeleted**](WebhookEventsApi.md#onContactDeleted) | **POST** /contact.deleted | Contact deleted |
| [**onContactDeletedWithHttpInfo**](WebhookEventsApi.md#onContactDeletedWithHttpInfo) | **POST** /contact.deleted | Contact deleted |
| [**onContactFieldChanged**](WebhookEventsApi.md#onContactFieldChanged) | **POST** /contact.field_changed | Contact field changed event |
| [**onContactFieldChangedWithHttpInfo**](WebhookEventsApi.md#onContactFieldChangedWithHttpInfo) | **POST** /contact.field_changed | Contact field changed event |
| [**onContactTagAdded**](WebhookEventsApi.md#onContactTagAdded) | **POST** /contact.tag_added | Contact tag added event |
| [**onContactTagAddedWithHttpInfo**](WebhookEventsApi.md#onContactTagAddedWithHttpInfo) | **POST** /contact.tag_added | Contact tag added event |
| [**onContactTagRemoved**](WebhookEventsApi.md#onContactTagRemoved) | **POST** /contact.tag_removed | Contact tag removed event |
| [**onContactTagRemovedWithHttpInfo**](WebhookEventsApi.md#onContactTagRemovedWithHttpInfo) | **POST** /contact.tag_removed | Contact tag removed event |
| [**onContactUpdated**](WebhookEventsApi.md#onContactUpdated) | **POST** /contact.updated | Contact updated |
| [**onContactUpdatedWithHttpInfo**](WebhookEventsApi.md#onContactUpdatedWithHttpInfo) | **POST** /contact.updated | Contact updated |
| [**onConversationControlChanged**](WebhookEventsApi.md#onConversationControlChanged) | **POST** /conversation.control_changed | Conversation control changed event |
| [**onConversationControlChangedWithHttpInfo**](WebhookEventsApi.md#onConversationControlChangedWithHttpInfo) | **POST** /conversation.control_changed | Conversation control changed event |
| [**onConversationStarted**](WebhookEventsApi.md#onConversationStarted) | **POST** /conversation.started | Conversation started event |
| [**onConversationStartedWithHttpInfo**](WebhookEventsApi.md#onConversationStartedWithHttpInfo) | **POST** /conversation.started | Conversation started event |
| [**onCreatorCampaignBudgetExhausted**](WebhookEventsApi.md#onCreatorCampaignBudgetExhausted) | **POST** /creator_campaign.budget_exhausted | Creator campaign budget exhausted event |
| [**onCreatorCampaignBudgetExhaustedWithHttpInfo**](WebhookEventsApi.md#onCreatorCampaignBudgetExhaustedWithHttpInfo) | **POST** /creator_campaign.budget_exhausted | Creator campaign budget exhausted event |
| [**onCreatorCampaignClosed**](WebhookEventsApi.md#onCreatorCampaignClosed) | **POST** /creator_campaign.closed | Creator campaign closed event |
| [**onCreatorCampaignClosedWithHttpInfo**](WebhookEventsApi.md#onCreatorCampaignClosedWithHttpInfo) | **POST** /creator_campaign.closed | Creator campaign closed event |
| [**onFileCreated**](WebhookEventsApi.md#onFileCreated) | **POST** /file.created | File created |
| [**onFileCreatedWithHttpInfo**](WebhookEventsApi.md#onFileCreatedWithHttpInfo) | **POST** /file.created | File created |
| [**onFileDeleted**](WebhookEventsApi.md#onFileDeleted) | **POST** /file.deleted | File deleted |
| [**onFileDeletedWithHttpInfo**](WebhookEventsApi.md#onFileDeletedWithHttpInfo) | **POST** /file.deleted | File deleted |
| [**onFilePicked**](WebhookEventsApi.md#onFilePicked) | **POST** /file.picked | Files picked |
| [**onFilePickedWithHttpInfo**](WebhookEventsApi.md#onFilePickedWithHttpInfo) | **POST** /file.picked | Files picked |
| [**onFileUpdated**](WebhookEventsApi.md#onFileUpdated) | **POST** /file.updated | File updated |
| [**onFileUpdatedWithHttpInfo**](WebhookEventsApi.md#onFileUpdatedWithHttpInfo) | **POST** /file.updated | File updated |
| [**onLeadReceived**](WebhookEventsApi.md#onLeadReceived) | **POST** /lead.received | Lead received event |
| [**onLeadReceivedWithHttpInfo**](WebhookEventsApi.md#onLeadReceivedWithHttpInfo) | **POST** /lead.received | Lead received event |
| [**onMessageDeleted**](WebhookEventsApi.md#onMessageDeleted) | **POST** /message.deleted | Message deleted event |
| [**onMessageDeletedWithHttpInfo**](WebhookEventsApi.md#onMessageDeletedWithHttpInfo) | **POST** /message.deleted | Message deleted event |
| [**onMessageDelivered**](WebhookEventsApi.md#onMessageDelivered) | **POST** /message.delivered | Message delivered event |
| [**onMessageDeliveredWithHttpInfo**](WebhookEventsApi.md#onMessageDeliveredWithHttpInfo) | **POST** /message.delivered | Message delivered event |
| [**onMessageEdited**](WebhookEventsApi.md#onMessageEdited) | **POST** /message.edited | Message edited event |
| [**onMessageEditedWithHttpInfo**](WebhookEventsApi.md#onMessageEditedWithHttpInfo) | **POST** /message.edited | Message edited event |
| [**onMessageFailed**](WebhookEventsApi.md#onMessageFailed) | **POST** /message.failed | Message delivery failed event |
| [**onMessageFailedWithHttpInfo**](WebhookEventsApi.md#onMessageFailedWithHttpInfo) | **POST** /message.failed | Message delivery failed event |
| [**onMessagePlayed**](WebhookEventsApi.md#onMessagePlayed) | **POST** /message.played | Message played event |
| [**onMessagePlayedWithHttpInfo**](WebhookEventsApi.md#onMessagePlayedWithHttpInfo) | **POST** /message.played | Message played event |
| [**onMessageRead**](WebhookEventsApi.md#onMessageRead) | **POST** /message.read | Message read event |
| [**onMessageReadWithHttpInfo**](WebhookEventsApi.md#onMessageReadWithHttpInfo) | **POST** /message.read | Message read event |
| [**onMessageReceived**](WebhookEventsApi.md#onMessageReceived) | **POST** /message.received | Message received event |
| [**onMessageReceivedWithHttpInfo**](WebhookEventsApi.md#onMessageReceivedWithHttpInfo) | **POST** /message.received | Message received event |
| [**onMessageSent**](WebhookEventsApi.md#onMessageSent) | **POST** /message.sent | Message sent event |
| [**onMessageSentWithHttpInfo**](WebhookEventsApi.md#onMessageSentWithHttpInfo) | **POST** /message.sent | Message sent event |
| [**onPhoneNumberStockAvailable**](WebhookEventsApi.md#onPhoneNumberStockAvailable) | **POST** /phone_number.stock_available | Phone-number stock available event |
| [**onPhoneNumberStockAvailableWithHttpInfo**](WebhookEventsApi.md#onPhoneNumberStockAvailableWithHttpInfo) | **POST** /phone_number.stock_available | Phone-number stock available event |
| [**onPostAuthenticityChanged**](WebhookEventsApi.md#onPostAuthenticityChanged) | **POST** /post.authenticity_changed | Post authenticity changed event |
| [**onPostAuthenticityChangedWithHttpInfo**](WebhookEventsApi.md#onPostAuthenticityChangedWithHttpInfo) | **POST** /post.authenticity_changed | Post authenticity changed event |
| [**onPostCancelled**](WebhookEventsApi.md#onPostCancelled) | **POST** /post.cancelled | Post cancelled event |
| [**onPostCancelledWithHttpInfo**](WebhookEventsApi.md#onPostCancelledWithHttpInfo) | **POST** /post.cancelled | Post cancelled event |
| [**onPostExternalCreated**](WebhookEventsApi.md#onPostExternalCreated) | **POST** /post.external.created | External post created event |
| [**onPostExternalCreatedWithHttpInfo**](WebhookEventsApi.md#onPostExternalCreatedWithHttpInfo) | **POST** /post.external.created | External post created event |
| [**onPostExternalDeleted**](WebhookEventsApi.md#onPostExternalDeleted) | **POST** /post.external.deleted | External post deleted event |
| [**onPostExternalDeletedWithHttpInfo**](WebhookEventsApi.md#onPostExternalDeletedWithHttpInfo) | **POST** /post.external.deleted | External post deleted event |
| [**onPostExternalUpdated**](WebhookEventsApi.md#onPostExternalUpdated) | **POST** /post.external.updated | External post updated event |
| [**onPostExternalUpdatedWithHttpInfo**](WebhookEventsApi.md#onPostExternalUpdatedWithHttpInfo) | **POST** /post.external.updated | External post updated event |
| [**onPostFailed**](WebhookEventsApi.md#onPostFailed) | **POST** /post.failed | Post failed event |
| [**onPostFailedWithHttpInfo**](WebhookEventsApi.md#onPostFailedWithHttpInfo) | **POST** /post.failed | Post failed event |
| [**onPostPartial**](WebhookEventsApi.md#onPostPartial) | **POST** /post.partial | Post partial event |
| [**onPostPartialWithHttpInfo**](WebhookEventsApi.md#onPostPartialWithHttpInfo) | **POST** /post.partial | Post partial event |
| [**onPostPlatformDeleted**](WebhookEventsApi.md#onPostPlatformDeleted) | **POST** /post.platform.deleted | Post platform deleted event |
| [**onPostPlatformDeletedWithHttpInfo**](WebhookEventsApi.md#onPostPlatformDeletedWithHttpInfo) | **POST** /post.platform.deleted | Post platform deleted event |
| [**onPostPlatformFailed**](WebhookEventsApi.md#onPostPlatformFailed) | **POST** /post.platform.failed | Post platform failed event |
| [**onPostPlatformFailedWithHttpInfo**](WebhookEventsApi.md#onPostPlatformFailedWithHttpInfo) | **POST** /post.platform.failed | Post platform failed event |
| [**onPostPlatformPublished**](WebhookEventsApi.md#onPostPlatformPublished) | **POST** /post.platform.published | Post platform published event |
| [**onPostPlatformPublishedWithHttpInfo**](WebhookEventsApi.md#onPostPlatformPublishedWithHttpInfo) | **POST** /post.platform.published | Post platform published event |
| [**onPostPublished**](WebhookEventsApi.md#onPostPublished) | **POST** /post.published | Post published event |
| [**onPostPublishedWithHttpInfo**](WebhookEventsApi.md#onPostPublishedWithHttpInfo) | **POST** /post.published | Post published event |
| [**onPostRecycled**](WebhookEventsApi.md#onPostRecycled) | **POST** /post.recycled | Post recycled event |
| [**onPostRecycledWithHttpInfo**](WebhookEventsApi.md#onPostRecycledWithHttpInfo) | **POST** /post.recycled | Post recycled event |
| [**onPostScheduled**](WebhookEventsApi.md#onPostScheduled) | **POST** /post.scheduled | Post scheduled event |
| [**onPostScheduledWithHttpInfo**](WebhookEventsApi.md#onPostScheduledWithHttpInfo) | **POST** /post.scheduled | Post scheduled event |
| [**onPostTikTokUrlResolved**](WebhookEventsApi.md#onPostTikTokUrlResolved) | **POST** /post.tiktok.url_resolved | TikTok post URL resolved event |
| [**onPostTikTokUrlResolvedWithHttpInfo**](WebhookEventsApi.md#onPostTikTokUrlResolvedWithHttpInfo) | **POST** /post.tiktok.url_resolved | TikTok post URL resolved event |
| [**onPostTrackingCompleted**](WebhookEventsApi.md#onPostTrackingCompleted) | **POST** /post.tracking_completed | Post tracking completed event |
| [**onPostTrackingCompletedWithHttpInfo**](WebhookEventsApi.md#onPostTrackingCompletedWithHttpInfo) | **POST** /post.tracking_completed | Post tracking completed event |
| [**onRcsAgentStatusUpdated**](WebhookEventsApi.md#onRcsAgentStatusUpdated) | **POST** /rcs.agent.status_updated | RCS agent status updated event |
| [**onRcsAgentStatusUpdatedWithHttpInfo**](WebhookEventsApi.md#onRcsAgentStatusUpdatedWithHttpInfo) | **POST** /rcs.agent.status_updated | RCS agent status updated event |
| [**onReactionReceived**](WebhookEventsApi.md#onReactionReceived) | **POST** /reaction.received | Reaction received event |
| [**onReactionReceivedWithHttpInfo**](WebhookEventsApi.md#onReactionReceivedWithHttpInfo) | **POST** /reaction.received | Reaction received event |
| [**onReferralReceived**](WebhookEventsApi.md#onReferralReceived) | **POST** /referral.received | Referral received event |
| [**onReferralReceivedWithHttpInfo**](WebhookEventsApi.md#onReferralReceivedWithHttpInfo) | **POST** /referral.received | Referral received event |
| [**onReviewNew**](WebhookEventsApi.md#onReviewNew) | **POST** /review.new | Review new event |
| [**onReviewNewWithHttpInfo**](WebhookEventsApi.md#onReviewNewWithHttpInfo) | **POST** /review.new | Review new event |
| [**onReviewUpdated**](WebhookEventsApi.md#onReviewUpdated) | **POST** /review.updated | Review updated event |
| [**onReviewUpdatedWithHttpInfo**](WebhookEventsApi.md#onReviewUpdatedWithHttpInfo) | **POST** /review.updated | Review updated event |
| [**onSequenceEnrolled**](WebhookEventsApi.md#onSequenceEnrolled) | **POST** /sequence.enrolled | Sequence enrolled event |
| [**onSequenceEnrolledWithHttpInfo**](WebhookEventsApi.md#onSequenceEnrolledWithHttpInfo) | **POST** /sequence.enrolled | Sequence enrolled event |
| [**onSequenceExited**](WebhookEventsApi.md#onSequenceExited) | **POST** /sequence.exited | Sequence exited event |
| [**onSequenceExitedWithHttpInfo**](WebhookEventsApi.md#onSequenceExitedWithHttpInfo) | **POST** /sequence.exited | Sequence exited event |
| [**onSmsRegistrationActionRequired**](WebhookEventsApi.md#onSmsRegistrationActionRequired) | **POST** /sms.registration.action_required | SMS registration action required event |
| [**onSmsRegistrationActionRequiredWithHttpInfo**](WebhookEventsApi.md#onSmsRegistrationActionRequiredWithHttpInfo) | **POST** /sms.registration.action_required | SMS registration action required event |
| [**onSmsRegistrationStatusUpdated**](WebhookEventsApi.md#onSmsRegistrationStatusUpdated) | **POST** /sms.registration.status_updated | SMS registration status updated event |
| [**onSmsRegistrationStatusUpdatedWithHttpInfo**](WebhookEventsApi.md#onSmsRegistrationStatusUpdatedWithHttpInfo) | **POST** /sms.registration.status_updated | SMS registration status updated event |
| [**onSupportRunCompleted**](WebhookEventsApi.md#onSupportRunCompleted) | **POST** /support.run.completed | Support Assistant finished event |
| [**onSupportRunCompletedWithHttpInfo**](WebhookEventsApi.md#onSupportRunCompletedWithHttpInfo) | **POST** /support.run.completed | Support Assistant finished event |
| [**onSupportRunFailed**](WebhookEventsApi.md#onSupportRunFailed) | **POST** /support.run.failed | Support Assistant failed event |
| [**onSupportRunFailedWithHttpInfo**](WebhookEventsApi.md#onSupportRunFailedWithHttpInfo) | **POST** /support.run.failed | Support Assistant failed event |
| [**onVerificationApproved**](WebhookEventsApi.md#onVerificationApproved) | **POST** /verification.approved | Verification approved event |
| [**onVerificationApprovedWithHttpInfo**](WebhookEventsApi.md#onVerificationApprovedWithHttpInfo) | **POST** /verification.approved | Verification approved event |
| [**onVerificationFailed**](WebhookEventsApi.md#onVerificationFailed) | **POST** /verification.failed | Verification failed event |
| [**onVerificationFailedWithHttpInfo**](WebhookEventsApi.md#onVerificationFailedWithHttpInfo) | **POST** /verification.failed | Verification failed event |
| [**onWebhookTest**](WebhookEventsApi.md#onWebhookTest) | **POST** /webhook.test | Webhook test event |
| [**onWebhookTestWithHttpInfo**](WebhookEventsApi.md#onWebhookTestWithHttpInfo) | **POST** /webhook.test | Webhook test event |
| [**onWhatsAppAccountAlertReceived**](WebhookEventsApi.md#onWhatsAppAccountAlertReceived) | **POST** /whatsapp.account.alert_received | WhatsApp account alert received |
| [**onWhatsAppAccountAlertReceivedWithHttpInfo**](WebhookEventsApi.md#onWhatsAppAccountAlertReceivedWithHttpInfo) | **POST** /whatsapp.account.alert_received | WhatsApp account alert received |
| [**onWhatsAppAccountNameStatusUpdated**](WebhookEventsApi.md#onWhatsAppAccountNameStatusUpdated) | **POST** /whatsapp.account.name_status_updated | WhatsApp display-name review outcome event |
| [**onWhatsAppAccountNameStatusUpdatedWithHttpInfo**](WebhookEventsApi.md#onWhatsAppAccountNameStatusUpdatedWithHttpInfo) | **POST** /whatsapp.account.name_status_updated | WhatsApp display-name review outcome event |
| [**onWhatsAppAccountQualityUpdated**](WebhookEventsApi.md#onWhatsAppAccountQualityUpdated) | **POST** /whatsapp.account.quality_updated | WhatsApp quality rating or messaging limit changed |
| [**onWhatsAppAccountQualityUpdatedWithHttpInfo**](WebhookEventsApi.md#onWhatsAppAccountQualityUpdatedWithHttpInfo) | **POST** /whatsapp.account.quality_updated | WhatsApp quality rating or messaging limit changed |
| [**onWhatsAppAccountStatusUpdated**](WebhookEventsApi.md#onWhatsAppAccountStatusUpdated) | **POST** /whatsapp.account.status_updated | WhatsApp Business Account restricted or reinstated |
| [**onWhatsAppAccountStatusUpdatedWithHttpInfo**](WebhookEventsApi.md#onWhatsAppAccountStatusUpdatedWithHttpInfo) | **POST** /whatsapp.account.status_updated | WhatsApp Business Account restricted or reinstated |
| [**onWhatsAppAutomaticEvent**](WebhookEventsApi.md#onWhatsAppAutomaticEvent) | **POST** /whatsapp.automatic_event | WhatsApp automatic event detected |
| [**onWhatsAppAutomaticEventWithHttpInfo**](WebhookEventsApi.md#onWhatsAppAutomaticEventWithHttpInfo) | **POST** /whatsapp.automatic_event | WhatsApp automatic event detected |
| [**onWhatsAppContactIdentityChanged**](WebhookEventsApi.md#onWhatsAppContactIdentityChanged) | **POST** /whatsapp.contact.identity_changed | WhatsApp contact identity changed event |
| [**onWhatsAppContactIdentityChangedWithHttpInfo**](WebhookEventsApi.md#onWhatsAppContactIdentityChangedWithHttpInfo) | **POST** /whatsapp.contact.identity_changed | WhatsApp contact identity changed event |
| [**onWhatsAppNumberActionRequired**](WebhookEventsApi.md#onWhatsAppNumberActionRequired) | **POST** /whatsapp.number.action_required | WhatsApp number action required event |
| [**onWhatsAppNumberActionRequiredWithHttpInfo**](WebhookEventsApi.md#onWhatsAppNumberActionRequiredWithHttpInfo) | **POST** /whatsapp.number.action_required | WhatsApp number action required event |
| [**onWhatsAppNumberActivated**](WebhookEventsApi.md#onWhatsAppNumberActivated) | **POST** /whatsapp.number.activated | WhatsApp number activated event |
| [**onWhatsAppNumberActivatedWithHttpInfo**](WebhookEventsApi.md#onWhatsAppNumberActivatedWithHttpInfo) | **POST** /whatsapp.number.activated | WhatsApp number activated event |
| [**onWhatsAppNumberDeclined**](WebhookEventsApi.md#onWhatsAppNumberDeclined) | **POST** /whatsapp.number.declined | WhatsApp number declined event |
| [**onWhatsAppNumberDeclinedWithHttpInfo**](WebhookEventsApi.md#onWhatsAppNumberDeclinedWithHttpInfo) | **POST** /whatsapp.number.declined | WhatsApp number declined event |
| [**onWhatsAppNumberKycSubmitted**](WebhookEventsApi.md#onWhatsAppNumberKycSubmitted) | **POST** /whatsapp.number.kyc_submitted | WhatsApp number KYC submitted event |
| [**onWhatsAppNumberKycSubmittedWithHttpInfo**](WebhookEventsApi.md#onWhatsAppNumberKycSubmittedWithHttpInfo) | **POST** /whatsapp.number.kyc_submitted | WhatsApp number KYC submitted event |
| [**onWhatsAppNumberReactivated**](WebhookEventsApi.md#onWhatsAppNumberReactivated) | **POST** /whatsapp.number.reactivated | WhatsApp number reactivated event |
| [**onWhatsAppNumberReactivatedWithHttpInfo**](WebhookEventsApi.md#onWhatsAppNumberReactivatedWithHttpInfo) | **POST** /whatsapp.number.reactivated | WhatsApp number reactivated event |
| [**onWhatsAppNumberReleased**](WebhookEventsApi.md#onWhatsAppNumberReleased) | **POST** /whatsapp.number.released | WhatsApp number released event |
| [**onWhatsAppNumberReleasedWithHttpInfo**](WebhookEventsApi.md#onWhatsAppNumberReleasedWithHttpInfo) | **POST** /whatsapp.number.released | WhatsApp number released event |
| [**onWhatsAppNumberSuspended**](WebhookEventsApi.md#onWhatsAppNumberSuspended) | **POST** /whatsapp.number.suspended | WhatsApp number suspended event |
| [**onWhatsAppNumberSuspendedWithHttpInfo**](WebhookEventsApi.md#onWhatsAppNumberSuspendedWithHttpInfo) | **POST** /whatsapp.number.suspended | WhatsApp number suspended event |
| [**onWhatsAppNumberVerificationRequired**](WebhookEventsApi.md#onWhatsAppNumberVerificationRequired) | **POST** /whatsapp.number.verification_required | WhatsApp number verification-required event |
| [**onWhatsAppNumberVerificationRequiredWithHttpInfo**](WebhookEventsApi.md#onWhatsAppNumberVerificationRequiredWithHttpInfo) | **POST** /whatsapp.number.verification_required | WhatsApp number verification-required event |
| [**onWhatsAppTemplateCategoryUpdated**](WebhookEventsApi.md#onWhatsAppTemplateCategoryUpdated) | **POST** /whatsapp.template.category_updated | WhatsApp template category updated event |
| [**onWhatsAppTemplateCategoryUpdatedWithHttpInfo**](WebhookEventsApi.md#onWhatsAppTemplateCategoryUpdatedWithHttpInfo) | **POST** /whatsapp.template.category_updated | WhatsApp template category updated event |
| [**onWhatsAppTemplateStatusUpdated**](WebhookEventsApi.md#onWhatsAppTemplateStatusUpdated) | **POST** /whatsapp.template.status_updated | WhatsApp template status updated event |
| [**onWhatsAppTemplateStatusUpdatedWithHttpInfo**](WebhookEventsApi.md#onWhatsAppTemplateStatusUpdatedWithHttpInfo) | **POST** /whatsapp.template.status_updated | WhatsApp template status updated event |
| [**onWorkflowRunCompleted**](WebhookEventsApi.md#onWorkflowRunCompleted) | **POST** /workflow.run.completed | Workflow run completed event |
| [**onWorkflowRunCompletedWithHttpInfo**](WebhookEventsApi.md#onWorkflowRunCompletedWithHttpInfo) | **POST** /workflow.run.completed | Workflow run completed event |
| [**onWorkflowRunFailed**](WebhookEventsApi.md#onWorkflowRunFailed) | **POST** /workflow.run.failed | Workflow run failed event |
| [**onWorkflowRunFailedWithHttpInfo**](WebhookEventsApi.md#onWorkflowRunFailedWithHttpInfo) | **POST** /workflow.run.failed | Workflow run failed event |
| [**onWorkflowRunStarted**](WebhookEventsApi.md#onWorkflowRunStarted) | **POST** /workflow.run.started | Workflow run started event |
| [**onWorkflowRunStartedWithHttpInfo**](WebhookEventsApi.md#onWorkflowRunStartedWithHttpInfo) | **POST** /workflow.run.started | Workflow run started event |



## onAccountAdsInitialSyncCompleted

> void onAccountAdsInitialSyncCompleted(webhookPayloadAccountAdsInitialSyncCompleted)

Ads initial sync completed event

Fired once per ads-enabled account when the initial sync (ad-account discovery + 90-day historical ad backfill) completes. The &#x60;sync&#x60; block reports whether the backfill succeeded and how many ads were synced. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAccountAdsInitialSyncCompleted webhookPayloadAccountAdsInitialSyncCompleted = new WebhookPayloadAccountAdsInitialSyncCompleted(); // WebhookPayloadAccountAdsInitialSyncCompleted | 
        try {
            apiInstance.onAccountAdsInitialSyncCompleted(webhookPayloadAccountAdsInitialSyncCompleted);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAccountAdsInitialSyncCompleted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAccountAdsInitialSyncCompleted** | [**WebhookPayloadAccountAdsInitialSyncCompleted**](WebhookPayloadAccountAdsInitialSyncCompleted.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onAccountAdsInitialSyncCompletedWithHttpInfo

> ApiResponse<Void> onAccountAdsInitialSyncCompleted onAccountAdsInitialSyncCompletedWithHttpInfo(webhookPayloadAccountAdsInitialSyncCompleted)

Ads initial sync completed event

Fired once per ads-enabled account when the initial sync (ad-account discovery + 90-day historical ad backfill) completes. The &#x60;sync&#x60; block reports whether the backfill succeeded and how many ads were synced. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAccountAdsInitialSyncCompleted webhookPayloadAccountAdsInitialSyncCompleted = new WebhookPayloadAccountAdsInitialSyncCompleted(); // WebhookPayloadAccountAdsInitialSyncCompleted | 
        try {
            ApiResponse<Void> response = apiInstance.onAccountAdsInitialSyncCompletedWithHttpInfo(webhookPayloadAccountAdsInitialSyncCompleted);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAccountAdsInitialSyncCompleted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAccountAdsInitialSyncCompleted** | [**WebhookPayloadAccountAdsInitialSyncCompleted**](WebhookPayloadAccountAdsInitialSyncCompleted.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onAccountAdsSyncFailed

> void onAccountAdsSyncFailed(webhookPayloadAccountAdsSyncFailed)

Ads sync failed event

Fired once per ad account when its ads stop syncing (no successful sync for 24 hours, or every live ad at the retry cap). Checked hourly. Metrics for the ad account are stale until &#x60;account.ads.sync_recovered&#x60; fires for it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAccountAdsSyncFailed webhookPayloadAccountAdsSyncFailed = new WebhookPayloadAccountAdsSyncFailed(); // WebhookPayloadAccountAdsSyncFailed | 
        try {
            apiInstance.onAccountAdsSyncFailed(webhookPayloadAccountAdsSyncFailed);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAccountAdsSyncFailed");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAccountAdsSyncFailed** | [**WebhookPayloadAccountAdsSyncFailed**](WebhookPayloadAccountAdsSyncFailed.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onAccountAdsSyncFailedWithHttpInfo

> ApiResponse<Void> onAccountAdsSyncFailed onAccountAdsSyncFailedWithHttpInfo(webhookPayloadAccountAdsSyncFailed)

Ads sync failed event

Fired once per ad account when its ads stop syncing (no successful sync for 24 hours, or every live ad at the retry cap). Checked hourly. Metrics for the ad account are stale until &#x60;account.ads.sync_recovered&#x60; fires for it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAccountAdsSyncFailed webhookPayloadAccountAdsSyncFailed = new WebhookPayloadAccountAdsSyncFailed(); // WebhookPayloadAccountAdsSyncFailed | 
        try {
            ApiResponse<Void> response = apiInstance.onAccountAdsSyncFailedWithHttpInfo(webhookPayloadAccountAdsSyncFailed);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAccountAdsSyncFailed");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAccountAdsSyncFailed** | [**WebhookPayloadAccountAdsSyncFailed**](WebhookPayloadAccountAdsSyncFailed.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onAccountAdsSyncRecovered

> void onAccountAdsSyncRecovered(webhookPayloadAccountAdsSyncRecovered)

Ads sync recovered event

Fired once when an ad account previously reported by &#x60;account.ads.sync_failed&#x60; syncs successfully again. Checked hourly. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAccountAdsSyncRecovered webhookPayloadAccountAdsSyncRecovered = new WebhookPayloadAccountAdsSyncRecovered(); // WebhookPayloadAccountAdsSyncRecovered | 
        try {
            apiInstance.onAccountAdsSyncRecovered(webhookPayloadAccountAdsSyncRecovered);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAccountAdsSyncRecovered");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAccountAdsSyncRecovered** | [**WebhookPayloadAccountAdsSyncRecovered**](WebhookPayloadAccountAdsSyncRecovered.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onAccountAdsSyncRecoveredWithHttpInfo

> ApiResponse<Void> onAccountAdsSyncRecovered onAccountAdsSyncRecoveredWithHttpInfo(webhookPayloadAccountAdsSyncRecovered)

Ads sync recovered event

Fired once when an ad account previously reported by &#x60;account.ads.sync_failed&#x60; syncs successfully again. Checked hourly. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAccountAdsSyncRecovered webhookPayloadAccountAdsSyncRecovered = new WebhookPayloadAccountAdsSyncRecovered(); // WebhookPayloadAccountAdsSyncRecovered | 
        try {
            ApiResponse<Void> response = apiInstance.onAccountAdsSyncRecoveredWithHttpInfo(webhookPayloadAccountAdsSyncRecovered);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAccountAdsSyncRecovered");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAccountAdsSyncRecovered** | [**WebhookPayloadAccountAdsSyncRecovered**](WebhookPayloadAccountAdsSyncRecovered.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onAccountConnected

> void onAccountConnected(webhookPayloadAccountConnected)

Account connected event

Fired when a account is successfully connected.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAccountConnected webhookPayloadAccountConnected = new WebhookPayloadAccountConnected(); // WebhookPayloadAccountConnected | 
        try {
            apiInstance.onAccountConnected(webhookPayloadAccountConnected);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAccountConnected");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAccountConnected** | [**WebhookPayloadAccountConnected**](WebhookPayloadAccountConnected.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onAccountConnectedWithHttpInfo

> ApiResponse<Void> onAccountConnected onAccountConnectedWithHttpInfo(webhookPayloadAccountConnected)

Account connected event

Fired when a account is successfully connected.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAccountConnected webhookPayloadAccountConnected = new WebhookPayloadAccountConnected(); // WebhookPayloadAccountConnected | 
        try {
            ApiResponse<Void> response = apiInstance.onAccountConnectedWithHttpInfo(webhookPayloadAccountConnected);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAccountConnected");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAccountConnected** | [**WebhookPayloadAccountConnected**](WebhookPayloadAccountConnected.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onAccountDisconnected

> void onAccountDisconnected(webhookPayloadAccountDisconnected)

Account disconnected event

Fired when a connected account becomes disconnected.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAccountDisconnected webhookPayloadAccountDisconnected = new WebhookPayloadAccountDisconnected(); // WebhookPayloadAccountDisconnected | 
        try {
            apiInstance.onAccountDisconnected(webhookPayloadAccountDisconnected);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAccountDisconnected");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAccountDisconnected** | [**WebhookPayloadAccountDisconnected**](WebhookPayloadAccountDisconnected.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onAccountDisconnectedWithHttpInfo

> ApiResponse<Void> onAccountDisconnected onAccountDisconnectedWithHttpInfo(webhookPayloadAccountDisconnected)

Account disconnected event

Fired when a connected account becomes disconnected.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAccountDisconnected webhookPayloadAccountDisconnected = new WebhookPayloadAccountDisconnected(); // WebhookPayloadAccountDisconnected | 
        try {
            ApiResponse<Void> response = apiInstance.onAccountDisconnectedWithHttpInfo(webhookPayloadAccountDisconnected);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAccountDisconnected");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAccountDisconnected** | [**WebhookPayloadAccountDisconnected**](WebhookPayloadAccountDisconnected.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onAccountPermissionsChanged

> void onAccountPermissionsChanged(webhookPayloadAccountPermissionsChanged)

Account permissions changed event

Fired when a publish on an account connected through your own OAuth app fails for a missing permission. The account stays connected; only the missing area stops working until the permission is granted and the account reconnected.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAccountPermissionsChanged webhookPayloadAccountPermissionsChanged = new WebhookPayloadAccountPermissionsChanged(); // WebhookPayloadAccountPermissionsChanged | 
        try {
            apiInstance.onAccountPermissionsChanged(webhookPayloadAccountPermissionsChanged);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAccountPermissionsChanged");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAccountPermissionsChanged** | [**WebhookPayloadAccountPermissionsChanged**](WebhookPayloadAccountPermissionsChanged.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onAccountPermissionsChangedWithHttpInfo

> ApiResponse<Void> onAccountPermissionsChanged onAccountPermissionsChangedWithHttpInfo(webhookPayloadAccountPermissionsChanged)

Account permissions changed event

Fired when a publish on an account connected through your own OAuth app fails for a missing permission. The account stays connected; only the missing area stops working until the permission is granted and the account reconnected.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAccountPermissionsChanged webhookPayloadAccountPermissionsChanged = new WebhookPayloadAccountPermissionsChanged(); // WebhookPayloadAccountPermissionsChanged | 
        try {
            ApiResponse<Void> response = apiInstance.onAccountPermissionsChangedWithHttpInfo(webhookPayloadAccountPermissionsChanged);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAccountPermissionsChanged");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAccountPermissionsChanged** | [**WebhookPayloadAccountPermissionsChanged**](WebhookPayloadAccountPermissionsChanged.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onAccountRateLimited

> void onAccountRateLimited(webhookPayloadAccountRateLimited)

Mailbox sending cooldown started

Fired when a Google or Microsoft mailbox enters a sending cooldown (same body to more than 50 recipients in an hour, or a later trigger). Sends answer 429 until &#x60;account.resetsAt&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAccountRateLimited webhookPayloadAccountRateLimited = new WebhookPayloadAccountRateLimited(); // WebhookPayloadAccountRateLimited | 
        try {
            apiInstance.onAccountRateLimited(webhookPayloadAccountRateLimited);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAccountRateLimited");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAccountRateLimited** | [**WebhookPayloadAccountRateLimited**](WebhookPayloadAccountRateLimited.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onAccountRateLimitedWithHttpInfo

> ApiResponse<Void> onAccountRateLimited onAccountRateLimitedWithHttpInfo(webhookPayloadAccountRateLimited)

Mailbox sending cooldown started

Fired when a Google or Microsoft mailbox enters a sending cooldown (same body to more than 50 recipients in an hour, or a later trigger). Sends answer 429 until &#x60;account.resetsAt&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAccountRateLimited webhookPayloadAccountRateLimited = new WebhookPayloadAccountRateLimited(); // WebhookPayloadAccountRateLimited | 
        try {
            ApiResponse<Void> response = apiInstance.onAccountRateLimitedWithHttpInfo(webhookPayloadAccountRateLimited);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAccountRateLimited");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAccountRateLimited** | [**WebhookPayloadAccountRateLimited**](WebhookPayloadAccountRateLimited.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onAdAccountStatusChanged

> void onAdAccountStatusChanged(webhookPayloadAdAccountStatusChanged)

Ad account status changed event

Fired when an ad account Zernio already tracked changes status (Meta, Google, TikTok, X). See &#x60;WebhookPayloadAdAccountStatusChanged&#x60; for when it fires and when it does not. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAdAccountStatusChanged webhookPayloadAdAccountStatusChanged = new WebhookPayloadAdAccountStatusChanged(); // WebhookPayloadAdAccountStatusChanged | 
        try {
            apiInstance.onAdAccountStatusChanged(webhookPayloadAdAccountStatusChanged);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAdAccountStatusChanged");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAdAccountStatusChanged** | [**WebhookPayloadAdAccountStatusChanged**](WebhookPayloadAdAccountStatusChanged.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onAdAccountStatusChangedWithHttpInfo

> ApiResponse<Void> onAdAccountStatusChanged onAdAccountStatusChangedWithHttpInfo(webhookPayloadAdAccountStatusChanged)

Ad account status changed event

Fired when an ad account Zernio already tracked changes status (Meta, Google, TikTok, X). See &#x60;WebhookPayloadAdAccountStatusChanged&#x60; for when it fires and when it does not. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAdAccountStatusChanged webhookPayloadAdAccountStatusChanged = new WebhookPayloadAdAccountStatusChanged(); // WebhookPayloadAdAccountStatusChanged | 
        try {
            ApiResponse<Void> response = apiInstance.onAdAccountStatusChangedWithHttpInfo(webhookPayloadAdAccountStatusChanged);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAdAccountStatusChanged");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAdAccountStatusChanged** | [**WebhookPayloadAdAccountStatusChanged**](WebhookPayloadAdAccountStatusChanged.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onAdDeliveryIssue

> void onAdDeliveryIssue(webhookPayloadAdDeliveryIssue)

Ad delivery issue event

Fired when an ad Zernio already tracked stops delivering for a platform reason (Meta, TikTok, LinkedIn). See &#x60;WebhookPayloadAdDeliveryIssue&#x60; for when it fires and when it does not. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAdDeliveryIssue webhookPayloadAdDeliveryIssue = new WebhookPayloadAdDeliveryIssue(); // WebhookPayloadAdDeliveryIssue | 
        try {
            apiInstance.onAdDeliveryIssue(webhookPayloadAdDeliveryIssue);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAdDeliveryIssue");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAdDeliveryIssue** | [**WebhookPayloadAdDeliveryIssue**](WebhookPayloadAdDeliveryIssue.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onAdDeliveryIssueWithHttpInfo

> ApiResponse<Void> onAdDeliveryIssue onAdDeliveryIssueWithHttpInfo(webhookPayloadAdDeliveryIssue)

Ad delivery issue event

Fired when an ad Zernio already tracked stops delivering for a platform reason (Meta, TikTok, LinkedIn). See &#x60;WebhookPayloadAdDeliveryIssue&#x60; for when it fires and when it does not. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAdDeliveryIssue webhookPayloadAdDeliveryIssue = new WebhookPayloadAdDeliveryIssue(); // WebhookPayloadAdDeliveryIssue | 
        try {
            ApiResponse<Void> response = apiInstance.onAdDeliveryIssueWithHttpInfo(webhookPayloadAdDeliveryIssue);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAdDeliveryIssue");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAdDeliveryIssue** | [**WebhookPayloadAdDeliveryIssue**](WebhookPayloadAdDeliveryIssue.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onAdReviewApproved

> void onAdReviewApproved(webhookPayloadAdReview)

Ad review approved event

Fired when an ad Zernio already tracked passes platform review, or a rejection is overturned on appeal. Every ad network. See &#x60;WebhookPayloadAdReview&#x60; for when it fires and when it does not. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAdReview webhookPayloadAdReview = new WebhookPayloadAdReview(); // WebhookPayloadAdReview | 
        try {
            apiInstance.onAdReviewApproved(webhookPayloadAdReview);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAdReviewApproved");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAdReview** | [**WebhookPayloadAdReview**](WebhookPayloadAdReview.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onAdReviewApprovedWithHttpInfo

> ApiResponse<Void> onAdReviewApproved onAdReviewApprovedWithHttpInfo(webhookPayloadAdReview)

Ad review approved event

Fired when an ad Zernio already tracked passes platform review, or a rejection is overturned on appeal. Every ad network. See &#x60;WebhookPayloadAdReview&#x60; for when it fires and when it does not. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAdReview webhookPayloadAdReview = new WebhookPayloadAdReview(); // WebhookPayloadAdReview | 
        try {
            ApiResponse<Void> response = apiInstance.onAdReviewApprovedWithHttpInfo(webhookPayloadAdReview);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAdReviewApproved");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAdReview** | [**WebhookPayloadAdReview**](WebhookPayloadAdReview.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onAdReviewRejected

> void onAdReviewRejected(webhookPayloadAdReview)

Ad review rejected event

Fired when the platform rejects an ad Zernio already tracked. Every ad network. See &#x60;WebhookPayloadAdReview&#x60; for when it fires and when it does not. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAdReview webhookPayloadAdReview = new WebhookPayloadAdReview(); // WebhookPayloadAdReview | 
        try {
            apiInstance.onAdReviewRejected(webhookPayloadAdReview);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAdReviewRejected");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAdReview** | [**WebhookPayloadAdReview**](WebhookPayloadAdReview.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onAdReviewRejectedWithHttpInfo

> ApiResponse<Void> onAdReviewRejected onAdReviewRejectedWithHttpInfo(webhookPayloadAdReview)

Ad review rejected event

Fired when the platform rejects an ad Zernio already tracked. Every ad network. See &#x60;WebhookPayloadAdReview&#x60; for when it fires and when it does not. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAdReview webhookPayloadAdReview = new WebhookPayloadAdReview(); // WebhookPayloadAdReview | 
        try {
            ApiResponse<Void> response = apiInstance.onAdReviewRejectedWithHttpInfo(webhookPayloadAdReview);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAdReviewRejected");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAdReview** | [**WebhookPayloadAdReview**](WebhookPayloadAdReview.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onAdRuleTriggered

> void onAdRuleTriggered(webhookPayloadAdRuleTriggered)

Ad rule triggered event

Fired when a scheduled ad rule run finds campaigns or ad sets meeting every condition, once per object per cooldown. See &#x60;WebhookPayloadAdRuleTriggered&#x60; for when it fires and when it does not. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAdRuleTriggered webhookPayloadAdRuleTriggered = new WebhookPayloadAdRuleTriggered(); // WebhookPayloadAdRuleTriggered | 
        try {
            apiInstance.onAdRuleTriggered(webhookPayloadAdRuleTriggered);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAdRuleTriggered");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAdRuleTriggered** | [**WebhookPayloadAdRuleTriggered**](WebhookPayloadAdRuleTriggered.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onAdRuleTriggeredWithHttpInfo

> ApiResponse<Void> onAdRuleTriggered onAdRuleTriggeredWithHttpInfo(webhookPayloadAdRuleTriggered)

Ad rule triggered event

Fired when a scheduled ad rule run finds campaigns or ad sets meeting every condition, once per object per cooldown. See &#x60;WebhookPayloadAdRuleTriggered&#x60; for when it fires and when it does not. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAdRuleTriggered webhookPayloadAdRuleTriggered = new WebhookPayloadAdRuleTriggered(); // WebhookPayloadAdRuleTriggered | 
        try {
            ApiResponse<Void> response = apiInstance.onAdRuleTriggeredWithHttpInfo(webhookPayloadAdRuleTriggered);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAdRuleTriggered");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAdRuleTriggered** | [**WebhookPayloadAdRuleTriggered**](WebhookPayloadAdRuleTriggered.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onAdStatusChanged

> void onAdStatusChanged(webhookPayloadAdStatusChanged)

Ad status changed event

Fired when a campaign, ad set, or ad on a connected ad platform changes status. Currently emitted only for Meta (&#x60;metaads&#x60;).  Subscribed to two Meta &#x60;ad_account&#x60; webhook fields:   - &#x60;in_process_ad_objects&#x60; - the ad object finished processing and exited     the &#x60;IN_PROCESS&#x60; state. &#x60;status.raw&#x60; carries Meta&#39;s &#x60;status_name&#x60;     (e.g. &#x60;ACTIVE&#x60;, &#x60;PAUSED&#x60;, &#x60;ARCHIVED&#x60;, &#x60;DELETED&#x60;).   - &#x60;with_issues_ad_objects&#x60; - the ad object entered the &#x60;WITH_ISSUES&#x60;     state. &#x60;status.raw&#x60; is set to &#x60;WITH_ISSUES&#x60; and the &#x60;error&#x60; block is     populated from Meta&#39;s &#x60;error_code&#x60; / &#x60;error_summary&#x60; / &#x60;error_message&#x60;.  &#x60;adObject.level&#x60; mirrors Meta&#39;s &#x60;level&#x60; and is one of &#x60;CAMPAIGN&#x60;, &#x60;AD_SET&#x60;, or &#x60;AD&#x60;. Creative-level events are not forwarded.  Branch on &#x60;status.raw&#x60; to handle each transition; use &#x60;error.code&#x60; (when present) as the stable discriminator, since &#x60;error.summary&#x60; and &#x60;error.message&#x60; are localized to the ad-account owner&#39;s Meta locale.  The &#x60;error&#x60; block is optional. It&#39;s present on most &#x60;WITH_ISSUES&#x60; events but can be absent (Meta does not always include diagnostics), and is never present on any other status. Always null-check &#x60;error&#x60; before reading &#x60;error.code&#x60;.  **Fan-out:** matching is keyed on &#x60;adObject.platformAdAccountId&#x60;. When multiple connected Zernio &#x60;metaads&#x60; accounts are linked to the same Meta ad account, each receives its own delivery. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAdStatusChanged webhookPayloadAdStatusChanged = new WebhookPayloadAdStatusChanged(); // WebhookPayloadAdStatusChanged | 
        try {
            apiInstance.onAdStatusChanged(webhookPayloadAdStatusChanged);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAdStatusChanged");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAdStatusChanged** | [**WebhookPayloadAdStatusChanged**](WebhookPayloadAdStatusChanged.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onAdStatusChangedWithHttpInfo

> ApiResponse<Void> onAdStatusChanged onAdStatusChangedWithHttpInfo(webhookPayloadAdStatusChanged)

Ad status changed event

Fired when a campaign, ad set, or ad on a connected ad platform changes status. Currently emitted only for Meta (&#x60;metaads&#x60;).  Subscribed to two Meta &#x60;ad_account&#x60; webhook fields:   - &#x60;in_process_ad_objects&#x60; - the ad object finished processing and exited     the &#x60;IN_PROCESS&#x60; state. &#x60;status.raw&#x60; carries Meta&#39;s &#x60;status_name&#x60;     (e.g. &#x60;ACTIVE&#x60;, &#x60;PAUSED&#x60;, &#x60;ARCHIVED&#x60;, &#x60;DELETED&#x60;).   - &#x60;with_issues_ad_objects&#x60; - the ad object entered the &#x60;WITH_ISSUES&#x60;     state. &#x60;status.raw&#x60; is set to &#x60;WITH_ISSUES&#x60; and the &#x60;error&#x60; block is     populated from Meta&#39;s &#x60;error_code&#x60; / &#x60;error_summary&#x60; / &#x60;error_message&#x60;.  &#x60;adObject.level&#x60; mirrors Meta&#39;s &#x60;level&#x60; and is one of &#x60;CAMPAIGN&#x60;, &#x60;AD_SET&#x60;, or &#x60;AD&#x60;. Creative-level events are not forwarded.  Branch on &#x60;status.raw&#x60; to handle each transition; use &#x60;error.code&#x60; (when present) as the stable discriminator, since &#x60;error.summary&#x60; and &#x60;error.message&#x60; are localized to the ad-account owner&#39;s Meta locale.  The &#x60;error&#x60; block is optional. It&#39;s present on most &#x60;WITH_ISSUES&#x60; events but can be absent (Meta does not always include diagnostics), and is never present on any other status. Always null-check &#x60;error&#x60; before reading &#x60;error.code&#x60;.  **Fan-out:** matching is keyed on &#x60;adObject.platformAdAccountId&#x60;. When multiple connected Zernio &#x60;metaads&#x60; accounts are linked to the same Meta ad account, each receives its own delivery. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAdStatusChanged webhookPayloadAdStatusChanged = new WebhookPayloadAdStatusChanged(); // WebhookPayloadAdStatusChanged | 
        try {
            ApiResponse<Void> response = apiInstance.onAdStatusChangedWithHttpInfo(webhookPayloadAdStatusChanged);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAdStatusChanged");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAdStatusChanged** | [**WebhookPayloadAdStatusChanged**](WebhookPayloadAdStatusChanged.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onAdVideoProcessed

> void onAdVideoProcessed(webhookPayloadAdVideoProcessed)

Ad video processed event

Fired once per &#x60;POST /v1/ads/videos&#x60; call made with &#x60;async: true&#x60;, when Meta finishes processing the uploaded video. &#x60;video.status&#x60; is &#x60;ready&#x60; (reference it as &#x60;video.id&#x60; on the create endpoints) or &#x60;error&#x60; (Meta could not process it; &#x60;video.error&#x60; carries the reason).  Zernio watches the video for up to about 13 minutes after the upload request. A video still processing after that sends no event, so keep &#x60;GET /v1/ads/videos/{videoId}&#x60; as the source of truth for long videos. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAdVideoProcessed webhookPayloadAdVideoProcessed = new WebhookPayloadAdVideoProcessed(); // WebhookPayloadAdVideoProcessed | 
        try {
            apiInstance.onAdVideoProcessed(webhookPayloadAdVideoProcessed);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAdVideoProcessed");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAdVideoProcessed** | [**WebhookPayloadAdVideoProcessed**](WebhookPayloadAdVideoProcessed.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onAdVideoProcessedWithHttpInfo

> ApiResponse<Void> onAdVideoProcessed onAdVideoProcessedWithHttpInfo(webhookPayloadAdVideoProcessed)

Ad video processed event

Fired once per &#x60;POST /v1/ads/videos&#x60; call made with &#x60;async: true&#x60;, when Meta finishes processing the uploaded video. &#x60;video.status&#x60; is &#x60;ready&#x60; (reference it as &#x60;video.id&#x60; on the create endpoints) or &#x60;error&#x60; (Meta could not process it; &#x60;video.error&#x60; carries the reason).  Zernio watches the video for up to about 13 minutes after the upload request. A video still processing after that sends no event, so keep &#x60;GET /v1/ads/videos/{videoId}&#x60; as the source of truth for long videos. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAdVideoProcessed webhookPayloadAdVideoProcessed = new WebhookPayloadAdVideoProcessed(); // WebhookPayloadAdVideoProcessed | 
        try {
            ApiResponse<Void> response = apiInstance.onAdVideoProcessedWithHttpInfo(webhookPayloadAdVideoProcessed);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAdVideoProcessed");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAdVideoProcessed** | [**WebhookPayloadAdVideoProcessed**](WebhookPayloadAdVideoProcessed.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onAnalyticsSynced

> void onAnalyticsSynced(webhookPayloadAnalyticsSynced)

Analytics synced event

Fired once per connected account each time its analytics sync cycle completes successfully. Poll-driven (roughly hourly per account), not real-time, and never fired for a skipped or failed cycle.  A trigger, not a transport: the payload carries no metrics and no cursor. On receipt, call &#x60;GET /v1/analytics/delta&#x60; with your own last &#x60;nextCursor&#x60; to read every post whose analytics changed, across every account, in one paginated stream instead of polling analytics once per account.  The feed holds back its most recent few seconds of writes, so a read issued the instant this event lands often returns an empty page for that account. Poll again with the same cursor rather than reading an empty page as \&quot;nothing changed\&quot;.  High volume (roughly one delivery per connected account per hour). Subscribe to it on a dedicated webhook endpoint: a subscription&#39;s consecutive-failure count is shared across all of its events, so an outage while this event is flowing can suppress the low-volume publishing events on the same subscription. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAnalyticsSynced webhookPayloadAnalyticsSynced = new WebhookPayloadAnalyticsSynced(); // WebhookPayloadAnalyticsSynced | 
        try {
            apiInstance.onAnalyticsSynced(webhookPayloadAnalyticsSynced);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAnalyticsSynced");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAnalyticsSynced** | [**WebhookPayloadAnalyticsSynced**](WebhookPayloadAnalyticsSynced.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onAnalyticsSyncedWithHttpInfo

> ApiResponse<Void> onAnalyticsSynced onAnalyticsSyncedWithHttpInfo(webhookPayloadAnalyticsSynced)

Analytics synced event

Fired once per connected account each time its analytics sync cycle completes successfully. Poll-driven (roughly hourly per account), not real-time, and never fired for a skipped or failed cycle.  A trigger, not a transport: the payload carries no metrics and no cursor. On receipt, call &#x60;GET /v1/analytics/delta&#x60; with your own last &#x60;nextCursor&#x60; to read every post whose analytics changed, across every account, in one paginated stream instead of polling analytics once per account.  The feed holds back its most recent few seconds of writes, so a read issued the instant this event lands often returns an empty page for that account. Poll again with the same cursor rather than reading an empty page as \&quot;nothing changed\&quot;.  High volume (roughly one delivery per connected account per hour). Subscribe to it on a dedicated webhook endpoint: a subscription&#39;s consecutive-failure count is shared across all of its events, so an outage while this event is flowing can suppress the low-volume publishing events on the same subscription. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadAnalyticsSynced webhookPayloadAnalyticsSynced = new WebhookPayloadAnalyticsSynced(); // WebhookPayloadAnalyticsSynced | 
        try {
            ApiResponse<Void> response = apiInstance.onAnalyticsSyncedWithHttpInfo(webhookPayloadAnalyticsSynced);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAnalyticsSynced");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadAnalyticsSynced** | [**WebhookPayloadAnalyticsSynced**](WebhookPayloadAnalyticsSynced.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onApiChangelogPublished

> void onApiChangelogPublished(webhookPayloadApiChangelogPublished)

API changelog entry published event

Fired when an entry is published to the API changelog (https://docs.zernio.com/changelog), which happens when a change to this OpenAPI spec goes live. The event belongs to no profile or account: every active subscription that opted in receives it, scoped subscriptions (&#x60;profileIds&#x60; / &#x60;accountIds&#x60;) do not. &#x60;entry.changes&#x60; is the deterministic diff of the spec (operations and schemas added, removed and modified); &#x60;entry.impact&#x60; says whether an existing integration must act (&#x60;action_required&#x60;), only gained something (&#x60;additive&#x60;) or nothing changed beyond descriptions (&#x60;none&#x60;); &#x60;entry.message&#x60; is the written announcement. Act on &#x60;impact&#x60; and &#x60;changes&#x60;, read &#x60;message&#x60; for the why. Entries are listed by &#x60;GET /v1/changelog&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadApiChangelogPublished webhookPayloadApiChangelogPublished = new WebhookPayloadApiChangelogPublished(); // WebhookPayloadApiChangelogPublished | 
        try {
            apiInstance.onApiChangelogPublished(webhookPayloadApiChangelogPublished);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onApiChangelogPublished");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadApiChangelogPublished** | [**WebhookPayloadApiChangelogPublished**](WebhookPayloadApiChangelogPublished.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onApiChangelogPublishedWithHttpInfo

> ApiResponse<Void> onApiChangelogPublished onApiChangelogPublishedWithHttpInfo(webhookPayloadApiChangelogPublished)

API changelog entry published event

Fired when an entry is published to the API changelog (https://docs.zernio.com/changelog), which happens when a change to this OpenAPI spec goes live. The event belongs to no profile or account: every active subscription that opted in receives it, scoped subscriptions (&#x60;profileIds&#x60; / &#x60;accountIds&#x60;) do not. &#x60;entry.changes&#x60; is the deterministic diff of the spec (operations and schemas added, removed and modified); &#x60;entry.impact&#x60; says whether an existing integration must act (&#x60;action_required&#x60;), only gained something (&#x60;additive&#x60;) or nothing changed beyond descriptions (&#x60;none&#x60;); &#x60;entry.message&#x60; is the written announcement. Act on &#x60;impact&#x60; and &#x60;changes&#x60;, read &#x60;message&#x60; for the why. Entries are listed by &#x60;GET /v1/changelog&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadApiChangelogPublished webhookPayloadApiChangelogPublished = new WebhookPayloadApiChangelogPublished(); // WebhookPayloadApiChangelogPublished | 
        try {
            ApiResponse<Void> response = apiInstance.onApiChangelogPublishedWithHttpInfo(webhookPayloadApiChangelogPublished);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onApiChangelogPublished");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadApiChangelogPublished** | [**WebhookPayloadApiChangelogPublished**](WebhookPayloadApiChangelogPublished.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onBrandedCallingIdentityActionRequired

> void onBrandedCallingIdentityActionRequired(onBrandedCallingIdentityActionRequiredRequest)

Caller identity action required event

Fired when a caller identity waits on you. &#x60;reason&#x60; says what: &#x60;changes_requested&#x60; (answer the review with PATCH), &#x60;email_code&#x60; (the authorizer got a 6-digit code from the carrier; confirm it with the verify-email endpoint), &#x60;rejected&#x60; (the carrier rejected it; fix and PATCH), &#x60;infringement_claim&#x60; (a third party disputes the name or logo; reply to our email with evidence) or &#x60;expired&#x60; (resubmit). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnBrandedCallingIdentityActionRequiredRequest onBrandedCallingIdentityActionRequiredRequest = new OnBrandedCallingIdentityActionRequiredRequest(); // OnBrandedCallingIdentityActionRequiredRequest | 
        try {
            apiInstance.onBrandedCallingIdentityActionRequired(onBrandedCallingIdentityActionRequiredRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onBrandedCallingIdentityActionRequired");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onBrandedCallingIdentityActionRequiredRequest** | [**OnBrandedCallingIdentityActionRequiredRequest**](OnBrandedCallingIdentityActionRequiredRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onBrandedCallingIdentityActionRequiredWithHttpInfo

> ApiResponse<Void> onBrandedCallingIdentityActionRequired onBrandedCallingIdentityActionRequiredWithHttpInfo(onBrandedCallingIdentityActionRequiredRequest)

Caller identity action required event

Fired when a caller identity waits on you. &#x60;reason&#x60; says what: &#x60;changes_requested&#x60; (answer the review with PATCH), &#x60;email_code&#x60; (the authorizer got a 6-digit code from the carrier; confirm it with the verify-email endpoint), &#x60;rejected&#x60; (the carrier rejected it; fix and PATCH), &#x60;infringement_claim&#x60; (a third party disputes the name or logo; reply to our email with evidence) or &#x60;expired&#x60; (resubmit). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnBrandedCallingIdentityActionRequiredRequest onBrandedCallingIdentityActionRequiredRequest = new OnBrandedCallingIdentityActionRequiredRequest(); // OnBrandedCallingIdentityActionRequiredRequest | 
        try {
            ApiResponse<Void> response = apiInstance.onBrandedCallingIdentityActionRequiredWithHttpInfo(onBrandedCallingIdentityActionRequiredRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onBrandedCallingIdentityActionRequired");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onBrandedCallingIdentityActionRequiredRequest** | [**OnBrandedCallingIdentityActionRequiredRequest**](OnBrandedCallingIdentityActionRequiredRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onBrandedCallingIdentityStatusUpdated

> void onBrandedCallingIdentityStatusUpdated(onBrandedCallingIdentityStatusUpdatedRequest)

Caller identity status updated event

Fired on every status change of a Branded Calling caller identity: &#x60;requested&#x60; (a new submission or resubmit, in our review), &#x60;changes_requested&#x60; (we need answers, see &#x60;branded_calling.identity.action_required&#x60;), &#x60;rejected&#x60; (by our review or by the carrier; &#x60;reason&#x60; says why), &#x60;pending_email_verification&#x60; (filed with the carrier; the authorizer enters the emailed code), &#x60;in_review&#x60; (carrier vetting), &#x60;verified&#x60; (live for a year: attach numbers), &#x60;suspended&#x60; (an infringement claim is open), &#x60;expired&#x60; and &#x60;permanently_rejected&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnBrandedCallingIdentityStatusUpdatedRequest onBrandedCallingIdentityStatusUpdatedRequest = new OnBrandedCallingIdentityStatusUpdatedRequest(); // OnBrandedCallingIdentityStatusUpdatedRequest | 
        try {
            apiInstance.onBrandedCallingIdentityStatusUpdated(onBrandedCallingIdentityStatusUpdatedRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onBrandedCallingIdentityStatusUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onBrandedCallingIdentityStatusUpdatedRequest** | [**OnBrandedCallingIdentityStatusUpdatedRequest**](OnBrandedCallingIdentityStatusUpdatedRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onBrandedCallingIdentityStatusUpdatedWithHttpInfo

> ApiResponse<Void> onBrandedCallingIdentityStatusUpdated onBrandedCallingIdentityStatusUpdatedWithHttpInfo(onBrandedCallingIdentityStatusUpdatedRequest)

Caller identity status updated event

Fired on every status change of a Branded Calling caller identity: &#x60;requested&#x60; (a new submission or resubmit, in our review), &#x60;changes_requested&#x60; (we need answers, see &#x60;branded_calling.identity.action_required&#x60;), &#x60;rejected&#x60; (by our review or by the carrier; &#x60;reason&#x60; says why), &#x60;pending_email_verification&#x60; (filed with the carrier; the authorizer enters the emailed code), &#x60;in_review&#x60; (carrier vetting), &#x60;verified&#x60; (live for a year: attach numbers), &#x60;suspended&#x60; (an infringement claim is open), &#x60;expired&#x60; and &#x60;permanently_rejected&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnBrandedCallingIdentityStatusUpdatedRequest onBrandedCallingIdentityStatusUpdatedRequest = new OnBrandedCallingIdentityStatusUpdatedRequest(); // OnBrandedCallingIdentityStatusUpdatedRequest | 
        try {
            ApiResponse<Void> response = apiInstance.onBrandedCallingIdentityStatusUpdatedWithHttpInfo(onBrandedCallingIdentityStatusUpdatedRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onBrandedCallingIdentityStatusUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onBrandedCallingIdentityStatusUpdatedRequest** | [**OnBrandedCallingIdentityStatusUpdatedRequest**](OnBrandedCallingIdentityStatusUpdatedRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onBrandedCallingNumberStatusUpdated

> void onBrandedCallingNumberStatusUpdated(onBrandedCallingNumberStatusUpdatedRequest)

Branded number status updated event

Fired when a number attached to a caller identity changes vetting status: &#x60;in_review&#x60;, &#x60;verified&#x60; (calls from it now show the identity), &#x60;unsuccessful&#x60; (refused; detach and re-add to retry), &#x60;suspended&#x60;, &#x60;expired&#x60; or &#x60;permanently_rejected&#x60; (can never be branded again). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnBrandedCallingNumberStatusUpdatedRequest onBrandedCallingNumberStatusUpdatedRequest = new OnBrandedCallingNumberStatusUpdatedRequest(); // OnBrandedCallingNumberStatusUpdatedRequest | 
        try {
            apiInstance.onBrandedCallingNumberStatusUpdated(onBrandedCallingNumberStatusUpdatedRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onBrandedCallingNumberStatusUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onBrandedCallingNumberStatusUpdatedRequest** | [**OnBrandedCallingNumberStatusUpdatedRequest**](OnBrandedCallingNumberStatusUpdatedRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onBrandedCallingNumberStatusUpdatedWithHttpInfo

> ApiResponse<Void> onBrandedCallingNumberStatusUpdated onBrandedCallingNumberStatusUpdatedWithHttpInfo(onBrandedCallingNumberStatusUpdatedRequest)

Branded number status updated event

Fired when a number attached to a caller identity changes vetting status: &#x60;in_review&#x60;, &#x60;verified&#x60; (calls from it now show the identity), &#x60;unsuccessful&#x60; (refused; detach and re-add to retry), &#x60;suspended&#x60;, &#x60;expired&#x60; or &#x60;permanently_rejected&#x60; (can never be branded again). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnBrandedCallingNumberStatusUpdatedRequest onBrandedCallingNumberStatusUpdatedRequest = new OnBrandedCallingNumberStatusUpdatedRequest(); // OnBrandedCallingNumberStatusUpdatedRequest | 
        try {
            ApiResponse<Void> response = apiInstance.onBrandedCallingNumberStatusUpdatedWithHttpInfo(onBrandedCallingNumberStatusUpdatedRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onBrandedCallingNumberStatusUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onBrandedCallingNumberStatusUpdatedRequest** | [**OnBrandedCallingNumberStatusUpdatedRequest**](OnBrandedCallingNumberStatusUpdatedRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCalendarEventCreated

> void onCalendarEventCreated(webhookPayloadCalendarEvent)

Calendar event created

A new event appeared on a connected Microsoft calendar (push, seconds after the change).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCalendarEvent webhookPayloadCalendarEvent = new WebhookPayloadCalendarEvent(); // WebhookPayloadCalendarEvent | 
        try {
            apiInstance.onCalendarEventCreated(webhookPayloadCalendarEvent);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCalendarEventCreated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCalendarEvent** | [**WebhookPayloadCalendarEvent**](WebhookPayloadCalendarEvent.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCalendarEventCreatedWithHttpInfo

> ApiResponse<Void> onCalendarEventCreated onCalendarEventCreatedWithHttpInfo(webhookPayloadCalendarEvent)

Calendar event created

A new event appeared on a connected Microsoft calendar (push, seconds after the change).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCalendarEvent webhookPayloadCalendarEvent = new WebhookPayloadCalendarEvent(); // WebhookPayloadCalendarEvent | 
        try {
            ApiResponse<Void> response = apiInstance.onCalendarEventCreatedWithHttpInfo(webhookPayloadCalendarEvent);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCalendarEventCreated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCalendarEvent** | [**WebhookPayloadCalendarEvent**](WebhookPayloadCalendarEvent.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCalendarEventDeleted

> void onCalendarEventDeleted(webhookPayloadCalendarEvent)

Calendar event deleted

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCalendarEvent webhookPayloadCalendarEvent = new WebhookPayloadCalendarEvent(); // WebhookPayloadCalendarEvent | 
        try {
            apiInstance.onCalendarEventDeleted(webhookPayloadCalendarEvent);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCalendarEventDeleted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCalendarEvent** | [**WebhookPayloadCalendarEvent**](WebhookPayloadCalendarEvent.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCalendarEventDeletedWithHttpInfo

> ApiResponse<Void> onCalendarEventDeleted onCalendarEventDeletedWithHttpInfo(webhookPayloadCalendarEvent)

Calendar event deleted

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCalendarEvent webhookPayloadCalendarEvent = new WebhookPayloadCalendarEvent(); // WebhookPayloadCalendarEvent | 
        try {
            ApiResponse<Void> response = apiInstance.onCalendarEventDeletedWithHttpInfo(webhookPayloadCalendarEvent);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCalendarEventDeleted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCalendarEvent** | [**WebhookPayloadCalendarEvent**](WebhookPayloadCalendarEvent.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCalendarEventUpdated

> void onCalendarEventUpdated(webhookPayloadCalendarEvent)

Calendar event updated

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCalendarEvent webhookPayloadCalendarEvent = new WebhookPayloadCalendarEvent(); // WebhookPayloadCalendarEvent | 
        try {
            apiInstance.onCalendarEventUpdated(webhookPayloadCalendarEvent);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCalendarEventUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCalendarEvent** | [**WebhookPayloadCalendarEvent**](WebhookPayloadCalendarEvent.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCalendarEventUpdatedWithHttpInfo

> ApiResponse<Void> onCalendarEventUpdated onCalendarEventUpdatedWithHttpInfo(webhookPayloadCalendarEvent)

Calendar event updated

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCalendarEvent webhookPayloadCalendarEvent = new WebhookPayloadCalendarEvent(); // WebhookPayloadCalendarEvent | 
        try {
            ApiResponse<Void> response = apiInstance.onCalendarEventUpdatedWithHttpInfo(webhookPayloadCalendarEvent);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCalendarEventUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCalendarEvent** | [**WebhookPayloadCalendarEvent**](WebhookPayloadCalendarEvent.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCallEnded

> void onCallEnded(webhookPayloadCallEnded)

Call ended event

Fired on call hangup with the duration and a zero-markup billing breakdown (Meta cost, Telnyx cost, recording surcharge, total). Costs are pass-through; no margin is applied. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCallEnded webhookPayloadCallEnded = new WebhookPayloadCallEnded(); // WebhookPayloadCallEnded | 
        try {
            apiInstance.onCallEnded(webhookPayloadCallEnded);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCallEnded");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCallEnded** | [**WebhookPayloadCallEnded**](WebhookPayloadCallEnded.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCallEndedWithHttpInfo

> ApiResponse<Void> onCallEnded onCallEndedWithHttpInfo(webhookPayloadCallEnded)

Call ended event

Fired on call hangup with the duration and a zero-markup billing breakdown (Meta cost, Telnyx cost, recording surcharge, total). Costs are pass-through; no margin is applied. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCallEnded webhookPayloadCallEnded = new WebhookPayloadCallEnded(); // WebhookPayloadCallEnded | 
        try {
            ApiResponse<Void> response = apiInstance.onCallEndedWithHttpInfo(webhookPayloadCallEnded);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCallEnded");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCallEnded** | [**WebhookPayloadCallEnded**](WebhookPayloadCallEnded.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCallFailed

> void onCallFailed(webhookPayloadCallFailed)

Call failed event

Fired when a call setup or in-progress call fails (Meta rejected the connect, Telnyx returned an error, etc.). Payload carries the upstream error code and message. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCallFailed webhookPayloadCallFailed = new WebhookPayloadCallFailed(); // WebhookPayloadCallFailed | 
        try {
            apiInstance.onCallFailed(webhookPayloadCallFailed);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCallFailed");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCallFailed** | [**WebhookPayloadCallFailed**](WebhookPayloadCallFailed.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCallFailedWithHttpInfo

> ApiResponse<Void> onCallFailed onCallFailedWithHttpInfo(webhookPayloadCallFailed)

Call failed event

Fired when a call setup or in-progress call fails (Meta rejected the connect, Telnyx returned an error, etc.). Payload carries the upstream error code and message. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCallFailed webhookPayloadCallFailed = new WebhookPayloadCallFailed(); // WebhookPayloadCallFailed | 
        try {
            ApiResponse<Void> response = apiInstance.onCallFailedWithHttpInfo(webhookPayloadCallFailed);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCallFailed");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCallFailed** | [**WebhookPayloadCallFailed**](WebhookPayloadCallFailed.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCallPermissionRequest

> void onCallPermissionRequest(webhookPayloadCallPermissionRequest)

Call permission request reply event

Fired when a consumer replies to a &#x60;call_permission_request&#x60; interactive message (or its marketing-template variant). Carries the response (&#x60;accept&#x60; / &#x60;reject&#x60;), whether the grant is permanent, and the expiration timestamp when it is temporary. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCallPermissionRequest webhookPayloadCallPermissionRequest = new WebhookPayloadCallPermissionRequest(); // WebhookPayloadCallPermissionRequest | 
        try {
            apiInstance.onCallPermissionRequest(webhookPayloadCallPermissionRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCallPermissionRequest");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCallPermissionRequest** | [**WebhookPayloadCallPermissionRequest**](WebhookPayloadCallPermissionRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCallPermissionRequestWithHttpInfo

> ApiResponse<Void> onCallPermissionRequest onCallPermissionRequestWithHttpInfo(webhookPayloadCallPermissionRequest)

Call permission request reply event

Fired when a consumer replies to a &#x60;call_permission_request&#x60; interactive message (or its marketing-template variant). Carries the response (&#x60;accept&#x60; / &#x60;reject&#x60;), whether the grant is permanent, and the expiration timestamp when it is temporary. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCallPermissionRequest webhookPayloadCallPermissionRequest = new WebhookPayloadCallPermissionRequest(); // WebhookPayloadCallPermissionRequest | 
        try {
            ApiResponse<Void> response = apiInstance.onCallPermissionRequestWithHttpInfo(webhookPayloadCallPermissionRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCallPermissionRequest");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCallPermissionRequest** | [**WebhookPayloadCallPermissionRequest**](WebhookPayloadCallPermissionRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCallReceived

> void onCallReceived(webhookPayloadCallReceived)

Call received event

Fired when a WhatsApp Business Call connects. For inbound (UIC) calls the event fires at the moment our Telnyx trunk bridges the consumer leg to the customer&amp;apos;s forward-to destination; for outbound (BIC) calls it fires immediately after Meta accepts the connect. Branch on &#x60;call.direction&#x60; to distinguish. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCallReceived webhookPayloadCallReceived = new WebhookPayloadCallReceived(); // WebhookPayloadCallReceived | 
        try {
            apiInstance.onCallReceived(webhookPayloadCallReceived);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCallReceived");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCallReceived** | [**WebhookPayloadCallReceived**](WebhookPayloadCallReceived.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCallReceivedWithHttpInfo

> ApiResponse<Void> onCallReceived onCallReceivedWithHttpInfo(webhookPayloadCallReceived)

Call received event

Fired when a WhatsApp Business Call connects. For inbound (UIC) calls the event fires at the moment our Telnyx trunk bridges the consumer leg to the customer&amp;apos;s forward-to destination; for outbound (BIC) calls it fires immediately after Meta accepts the connect. Branch on &#x60;call.direction&#x60; to distinguish. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCallReceived webhookPayloadCallReceived = new WebhookPayloadCallReceived(); // WebhookPayloadCallReceived | 
        try {
            ApiResponse<Void> response = apiInstance.onCallReceivedWithHttpInfo(webhookPayloadCallReceived);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCallReceived");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCallReceived** | [**WebhookPayloadCallReceived**](WebhookPayloadCallReceived.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCampaignBudgetDepleted

> void onCampaignBudgetDepleted(webhookPayloadCampaignBudgetDepleted)

Campaign budget depleted event

Fired when a campaign Zernio already tracked runs out of budget (TikTok). See &#x60;WebhookPayloadCampaignBudgetDepleted&#x60; for when it fires and when it does not. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCampaignBudgetDepleted webhookPayloadCampaignBudgetDepleted = new WebhookPayloadCampaignBudgetDepleted(); // WebhookPayloadCampaignBudgetDepleted | 
        try {
            apiInstance.onCampaignBudgetDepleted(webhookPayloadCampaignBudgetDepleted);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignBudgetDepleted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCampaignBudgetDepleted** | [**WebhookPayloadCampaignBudgetDepleted**](WebhookPayloadCampaignBudgetDepleted.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCampaignBudgetDepletedWithHttpInfo

> ApiResponse<Void> onCampaignBudgetDepleted onCampaignBudgetDepletedWithHttpInfo(webhookPayloadCampaignBudgetDepleted)

Campaign budget depleted event

Fired when a campaign Zernio already tracked runs out of budget (TikTok). See &#x60;WebhookPayloadCampaignBudgetDepleted&#x60; for when it fires and when it does not. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCampaignBudgetDepleted webhookPayloadCampaignBudgetDepleted = new WebhookPayloadCampaignBudgetDepleted(); // WebhookPayloadCampaignBudgetDepleted | 
        try {
            ApiResponse<Void> response = apiInstance.onCampaignBudgetDepletedWithHttpInfo(webhookPayloadCampaignBudgetDepleted);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignBudgetDepleted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCampaignBudgetDepleted** | [**WebhookPayloadCampaignBudgetDepleted**](WebhookPayloadCampaignBudgetDepleted.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCampaignParticipantJoined

> void onCampaignParticipantJoined(webhookPayloadCampaignParticipant)

Campaign participant joined event

Fired once when a creator joins a campaign, from their invite link or the open link.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCampaignParticipant webhookPayloadCampaignParticipant = new WebhookPayloadCampaignParticipant(); // WebhookPayloadCampaignParticipant | 
        try {
            apiInstance.onCampaignParticipantJoined(webhookPayloadCampaignParticipant);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignParticipantJoined");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCampaignParticipant** | [**WebhookPayloadCampaignParticipant**](WebhookPayloadCampaignParticipant.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCampaignParticipantJoinedWithHttpInfo

> ApiResponse<Void> onCampaignParticipantJoined onCampaignParticipantJoinedWithHttpInfo(webhookPayloadCampaignParticipant)

Campaign participant joined event

Fired once when a creator joins a campaign, from their invite link or the open link.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCampaignParticipant webhookPayloadCampaignParticipant = new WebhookPayloadCampaignParticipant(); // WebhookPayloadCampaignParticipant | 
        try {
            ApiResponse<Void> response = apiInstance.onCampaignParticipantJoinedWithHttpInfo(webhookPayloadCampaignParticipant);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignParticipantJoined");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCampaignParticipant** | [**WebhookPayloadCampaignParticipant**](WebhookPayloadCampaignParticipant.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCampaignParticipantRemoved

> void onCampaignParticipantRemoved(webhookPayloadCampaignParticipant)

Campaign participant removed event

Fired when an operator removes a participant.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCampaignParticipant webhookPayloadCampaignParticipant = new WebhookPayloadCampaignParticipant(); // WebhookPayloadCampaignParticipant | 
        try {
            apiInstance.onCampaignParticipantRemoved(webhookPayloadCampaignParticipant);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignParticipantRemoved");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCampaignParticipant** | [**WebhookPayloadCampaignParticipant**](WebhookPayloadCampaignParticipant.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCampaignParticipantRemovedWithHttpInfo

> ApiResponse<Void> onCampaignParticipantRemoved onCampaignParticipantRemovedWithHttpInfo(webhookPayloadCampaignParticipant)

Campaign participant removed event

Fired when an operator removes a participant.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCampaignParticipant webhookPayloadCampaignParticipant = new WebhookPayloadCampaignParticipant(); // WebhookPayloadCampaignParticipant | 
        try {
            ApiResponse<Void> response = apiInstance.onCampaignParticipantRemovedWithHttpInfo(webhookPayloadCampaignParticipant);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignParticipantRemoved");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCampaignParticipant** | [**WebhookPayloadCampaignParticipant**](WebhookPayloadCampaignParticipant.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCampaignParticipantSuspended

> void onCampaignParticipantSuspended(webhookPayloadCampaignParticipant)

Campaign participant suspended event

Fired when an operator suspends a participant.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCampaignParticipant webhookPayloadCampaignParticipant = new WebhookPayloadCampaignParticipant(); // WebhookPayloadCampaignParticipant | 
        try {
            apiInstance.onCampaignParticipantSuspended(webhookPayloadCampaignParticipant);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignParticipantSuspended");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCampaignParticipant** | [**WebhookPayloadCampaignParticipant**](WebhookPayloadCampaignParticipant.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCampaignParticipantSuspendedWithHttpInfo

> ApiResponse<Void> onCampaignParticipantSuspended onCampaignParticipantSuspendedWithHttpInfo(webhookPayloadCampaignParticipant)

Campaign participant suspended event

Fired when an operator suspends a participant.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCampaignParticipant webhookPayloadCampaignParticipant = new WebhookPayloadCampaignParticipant(); // WebhookPayloadCampaignParticipant | 
        try {
            ApiResponse<Void> response = apiInstance.onCampaignParticipantSuspendedWithHttpInfo(webhookPayloadCampaignParticipant);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignParticipantSuspended");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCampaignParticipant** | [**WebhookPayloadCampaignParticipant**](WebhookPayloadCampaignParticipant.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCampaignPayoutFailed

> void onCampaignPayoutFailed(webhookPayloadCampaignPayout)

Campaign payout failed event

Fired when a treasury payout to a participant is refused, cannot be confirmed, or is reversed. The amount returns to payable, minus anything a rejection claws back.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCampaignPayout webhookPayloadCampaignPayout = new WebhookPayloadCampaignPayout(); // WebhookPayloadCampaignPayout | 
        try {
            apiInstance.onCampaignPayoutFailed(webhookPayloadCampaignPayout);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignPayoutFailed");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCampaignPayout** | [**WebhookPayloadCampaignPayout**](WebhookPayloadCampaignPayout.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCampaignPayoutFailedWithHttpInfo

> ApiResponse<Void> onCampaignPayoutFailed onCampaignPayoutFailedWithHttpInfo(webhookPayloadCampaignPayout)

Campaign payout failed event

Fired when a treasury payout to a participant is refused, cannot be confirmed, or is reversed. The amount returns to payable, minus anything a rejection claws back.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCampaignPayout webhookPayloadCampaignPayout = new WebhookPayloadCampaignPayout(); // WebhookPayloadCampaignPayout | 
        try {
            ApiResponse<Void> response = apiInstance.onCampaignPayoutFailedWithHttpInfo(webhookPayloadCampaignPayout);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignPayoutFailed");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCampaignPayout** | [**WebhookPayloadCampaignPayout**](WebhookPayloadCampaignPayout.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCampaignPayoutPayable

> void onCampaignPayoutPayable(webhookPayloadCampaignPayout)

Campaign payout payable event

Fired when a participant&#39;s held earnings mature and become payable.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCampaignPayout webhookPayloadCampaignPayout = new WebhookPayloadCampaignPayout(); // WebhookPayloadCampaignPayout | 
        try {
            apiInstance.onCampaignPayoutPayable(webhookPayloadCampaignPayout);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignPayoutPayable");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCampaignPayout** | [**WebhookPayloadCampaignPayout**](WebhookPayloadCampaignPayout.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCampaignPayoutPayableWithHttpInfo

> ApiResponse<Void> onCampaignPayoutPayable onCampaignPayoutPayableWithHttpInfo(webhookPayloadCampaignPayout)

Campaign payout payable event

Fired when a participant&#39;s held earnings mature and become payable.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCampaignPayout webhookPayloadCampaignPayout = new WebhookPayloadCampaignPayout(); // WebhookPayloadCampaignPayout | 
        try {
            ApiResponse<Void> response = apiInstance.onCampaignPayoutPayableWithHttpInfo(webhookPayloadCampaignPayout);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignPayoutPayable");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCampaignPayout** | [**WebhookPayloadCampaignPayout**](WebhookPayloadCampaignPayout.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCampaignPayoutSettled

> void onCampaignPayoutSettled(webhookPayloadCampaignPayout)

Campaign payout settled event

Fired when a settlement to a participant is recorded.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCampaignPayout webhookPayloadCampaignPayout = new WebhookPayloadCampaignPayout(); // WebhookPayloadCampaignPayout | 
        try {
            apiInstance.onCampaignPayoutSettled(webhookPayloadCampaignPayout);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignPayoutSettled");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCampaignPayout** | [**WebhookPayloadCampaignPayout**](WebhookPayloadCampaignPayout.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCampaignPayoutSettledWithHttpInfo

> ApiResponse<Void> onCampaignPayoutSettled onCampaignPayoutSettledWithHttpInfo(webhookPayloadCampaignPayout)

Campaign payout settled event

Fired when a settlement to a participant is recorded.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCampaignPayout webhookPayloadCampaignPayout = new WebhookPayloadCampaignPayout(); // WebhookPayloadCampaignPayout | 
        try {
            ApiResponse<Void> response = apiInstance.onCampaignPayoutSettledWithHttpInfo(webhookPayloadCampaignPayout);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignPayoutSettled");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCampaignPayout** | [**WebhookPayloadCampaignPayout**](WebhookPayloadCampaignPayout.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCampaignSubmissionApproved

> void onCampaignSubmissionApproved(webhookPayloadCampaignSubmission)

Campaign submission approved event

Fired when an operator approves a submission.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCampaignSubmission webhookPayloadCampaignSubmission = new WebhookPayloadCampaignSubmission(); // WebhookPayloadCampaignSubmission | 
        try {
            apiInstance.onCampaignSubmissionApproved(webhookPayloadCampaignSubmission);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignSubmissionApproved");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCampaignSubmission** | [**WebhookPayloadCampaignSubmission**](WebhookPayloadCampaignSubmission.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCampaignSubmissionApprovedWithHttpInfo

> ApiResponse<Void> onCampaignSubmissionApproved onCampaignSubmissionApprovedWithHttpInfo(webhookPayloadCampaignSubmission)

Campaign submission approved event

Fired when an operator approves a submission.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCampaignSubmission webhookPayloadCampaignSubmission = new WebhookPayloadCampaignSubmission(); // WebhookPayloadCampaignSubmission | 
        try {
            ApiResponse<Void> response = apiInstance.onCampaignSubmissionApprovedWithHttpInfo(webhookPayloadCampaignSubmission);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignSubmissionApproved");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCampaignSubmission** | [**WebhookPayloadCampaignSubmission**](WebhookPayloadCampaignSubmission.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCampaignSubmissionFlagged

> void onCampaignSubmissionFlagged(webhookPayloadCampaignSubmission)

Campaign submission flagged event

Fired when a submission gains a fraud flag it did not carry before, at submission or on a later sync.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCampaignSubmission webhookPayloadCampaignSubmission = new WebhookPayloadCampaignSubmission(); // WebhookPayloadCampaignSubmission | 
        try {
            apiInstance.onCampaignSubmissionFlagged(webhookPayloadCampaignSubmission);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignSubmissionFlagged");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCampaignSubmission** | [**WebhookPayloadCampaignSubmission**](WebhookPayloadCampaignSubmission.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCampaignSubmissionFlaggedWithHttpInfo

> ApiResponse<Void> onCampaignSubmissionFlagged onCampaignSubmissionFlaggedWithHttpInfo(webhookPayloadCampaignSubmission)

Campaign submission flagged event

Fired when a submission gains a fraud flag it did not carry before, at submission or on a later sync.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCampaignSubmission webhookPayloadCampaignSubmission = new WebhookPayloadCampaignSubmission(); // WebhookPayloadCampaignSubmission | 
        try {
            ApiResponse<Void> response = apiInstance.onCampaignSubmissionFlaggedWithHttpInfo(webhookPayloadCampaignSubmission);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignSubmissionFlagged");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCampaignSubmission** | [**WebhookPayloadCampaignSubmission**](WebhookPayloadCampaignSubmission.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCampaignSubmissionPendingReview

> void onCampaignSubmissionPendingReview(webhookPayloadCampaignSubmission)

Campaign submission pending review event

Fired when a submission becomes ready for review: a CPM submission reached minViewsToEarn or a pool submission minViewsToQualify; per-post submissions on the first accrual pass after submission.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCampaignSubmission webhookPayloadCampaignSubmission = new WebhookPayloadCampaignSubmission(); // WebhookPayloadCampaignSubmission | 
        try {
            apiInstance.onCampaignSubmissionPendingReview(webhookPayloadCampaignSubmission);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignSubmissionPendingReview");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCampaignSubmission** | [**WebhookPayloadCampaignSubmission**](WebhookPayloadCampaignSubmission.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCampaignSubmissionPendingReviewWithHttpInfo

> ApiResponse<Void> onCampaignSubmissionPendingReview onCampaignSubmissionPendingReviewWithHttpInfo(webhookPayloadCampaignSubmission)

Campaign submission pending review event

Fired when a submission becomes ready for review: a CPM submission reached minViewsToEarn or a pool submission minViewsToQualify; per-post submissions on the first accrual pass after submission.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCampaignSubmission webhookPayloadCampaignSubmission = new WebhookPayloadCampaignSubmission(); // WebhookPayloadCampaignSubmission | 
        try {
            ApiResponse<Void> response = apiInstance.onCampaignSubmissionPendingReviewWithHttpInfo(webhookPayloadCampaignSubmission);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignSubmissionPendingReview");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCampaignSubmission** | [**WebhookPayloadCampaignSubmission**](WebhookPayloadCampaignSubmission.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCampaignSubmissionReceived

> void onCampaignSubmissionReceived(webhookPayloadCampaignSubmission)

Campaign submission received event

Fired when a creator submits a post to a campaign and its tracking window opens.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCampaignSubmission webhookPayloadCampaignSubmission = new WebhookPayloadCampaignSubmission(); // WebhookPayloadCampaignSubmission | 
        try {
            apiInstance.onCampaignSubmissionReceived(webhookPayloadCampaignSubmission);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignSubmissionReceived");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCampaignSubmission** | [**WebhookPayloadCampaignSubmission**](WebhookPayloadCampaignSubmission.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCampaignSubmissionReceivedWithHttpInfo

> ApiResponse<Void> onCampaignSubmissionReceived onCampaignSubmissionReceivedWithHttpInfo(webhookPayloadCampaignSubmission)

Campaign submission received event

Fired when a creator submits a post to a campaign and its tracking window opens.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCampaignSubmission webhookPayloadCampaignSubmission = new WebhookPayloadCampaignSubmission(); // WebhookPayloadCampaignSubmission | 
        try {
            ApiResponse<Void> response = apiInstance.onCampaignSubmissionReceivedWithHttpInfo(webhookPayloadCampaignSubmission);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignSubmissionReceived");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCampaignSubmission** | [**WebhookPayloadCampaignSubmission**](WebhookPayloadCampaignSubmission.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCampaignSubmissionRejected

> void onCampaignSubmissionRejected(webhookPayloadCampaignSubmission)

Campaign submission rejected event

Fired when an operator rejects a submission.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCampaignSubmission webhookPayloadCampaignSubmission = new WebhookPayloadCampaignSubmission(); // WebhookPayloadCampaignSubmission | 
        try {
            apiInstance.onCampaignSubmissionRejected(webhookPayloadCampaignSubmission);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignSubmissionRejected");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCampaignSubmission** | [**WebhookPayloadCampaignSubmission**](WebhookPayloadCampaignSubmission.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCampaignSubmissionRejectedWithHttpInfo

> ApiResponse<Void> onCampaignSubmissionRejected onCampaignSubmissionRejectedWithHttpInfo(webhookPayloadCampaignSubmission)

Campaign submission rejected event

Fired when an operator rejects a submission.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCampaignSubmission webhookPayloadCampaignSubmission = new WebhookPayloadCampaignSubmission(); // WebhookPayloadCampaignSubmission | 
        try {
            ApiResponse<Void> response = apiInstance.onCampaignSubmissionRejectedWithHttpInfo(webhookPayloadCampaignSubmission);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignSubmissionRejected");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCampaignSubmission** | [**WebhookPayloadCampaignSubmission**](WebhookPayloadCampaignSubmission.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCommentReceived

> void onCommentReceived(webhookPayloadComment)

Comment received event

Fired when a new comment is received on a tracked post. Delivered for Instagram, Facebook, Threads, YouTube, LinkedIn, Bluesky, Reddit and TikTok. X/Twitter does NOT fire this event. Instagram, Facebook and TikTok arrive in real time from the platform&#39;s own webhook; the rest are poll-driven, so delivery is not instant. TikTok needs an account connected through the TikTok for Business app. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadComment webhookPayloadComment = new WebhookPayloadComment(); // WebhookPayloadComment | 
        try {
            apiInstance.onCommentReceived(webhookPayloadComment);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCommentReceived");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadComment** | [**WebhookPayloadComment**](WebhookPayloadComment.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCommentReceivedWithHttpInfo

> ApiResponse<Void> onCommentReceived onCommentReceivedWithHttpInfo(webhookPayloadComment)

Comment received event

Fired when a new comment is received on a tracked post. Delivered for Instagram, Facebook, Threads, YouTube, LinkedIn, Bluesky, Reddit and TikTok. X/Twitter does NOT fire this event. Instagram, Facebook and TikTok arrive in real time from the platform&#39;s own webhook; the rest are poll-driven, so delivery is not instant. TikTok needs an account connected through the TikTok for Business app. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadComment webhookPayloadComment = new WebhookPayloadComment(); // WebhookPayloadComment | 
        try {
            ApiResponse<Void> response = apiInstance.onCommentReceivedWithHttpInfo(webhookPayloadComment);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCommentReceived");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadComment** | [**WebhookPayloadComment**](WebhookPayloadComment.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCommerceOrderCreated

> void onCommerceOrderCreated(webhookPayloadCommerceOrder)

Commerce order created event

Fired when an order is placed on a connected store. The payload carries identifiers only; read the order with &#x60;GET /v1/commerce/orders/{orderId}?accountId&#x3D;...&#x60;. Fired once per Zernio account connected to the store. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCommerceOrder webhookPayloadCommerceOrder = new WebhookPayloadCommerceOrder(); // WebhookPayloadCommerceOrder | 
        try {
            apiInstance.onCommerceOrderCreated(webhookPayloadCommerceOrder);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCommerceOrderCreated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCommerceOrder** | [**WebhookPayloadCommerceOrder**](WebhookPayloadCommerceOrder.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCommerceOrderCreatedWithHttpInfo

> ApiResponse<Void> onCommerceOrderCreated onCommerceOrderCreatedWithHttpInfo(webhookPayloadCommerceOrder)

Commerce order created event

Fired when an order is placed on a connected store. The payload carries identifiers only; read the order with &#x60;GET /v1/commerce/orders/{orderId}?accountId&#x3D;...&#x60;. Fired once per Zernio account connected to the store. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCommerceOrder webhookPayloadCommerceOrder = new WebhookPayloadCommerceOrder(); // WebhookPayloadCommerceOrder | 
        try {
            ApiResponse<Void> response = apiInstance.onCommerceOrderCreatedWithHttpInfo(webhookPayloadCommerceOrder);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCommerceOrderCreated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCommerceOrder** | [**WebhookPayloadCommerceOrder**](WebhookPayloadCommerceOrder.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCommerceOrderRefunded

> void onCommerceOrderRefunded(webhookPayloadCommerceOrder)

Commerce order refunded event

Fired when a refund is issued on an order of a connected store. A commerce.order.updated usually follows for the same change. The payload carries identifiers only; read the order with &#x60;GET /v1/commerce/orders/{orderId}?accountId&#x3D;...&#x60;. Fired once per Zernio account connected to the store. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCommerceOrder webhookPayloadCommerceOrder = new WebhookPayloadCommerceOrder(); // WebhookPayloadCommerceOrder | 
        try {
            apiInstance.onCommerceOrderRefunded(webhookPayloadCommerceOrder);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCommerceOrderRefunded");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCommerceOrder** | [**WebhookPayloadCommerceOrder**](WebhookPayloadCommerceOrder.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCommerceOrderRefundedWithHttpInfo

> ApiResponse<Void> onCommerceOrderRefunded onCommerceOrderRefundedWithHttpInfo(webhookPayloadCommerceOrder)

Commerce order refunded event

Fired when a refund is issued on an order of a connected store. A commerce.order.updated usually follows for the same change. The payload carries identifiers only; read the order with &#x60;GET /v1/commerce/orders/{orderId}?accountId&#x3D;...&#x60;. Fired once per Zernio account connected to the store. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCommerceOrder webhookPayloadCommerceOrder = new WebhookPayloadCommerceOrder(); // WebhookPayloadCommerceOrder | 
        try {
            ApiResponse<Void> response = apiInstance.onCommerceOrderRefundedWithHttpInfo(webhookPayloadCommerceOrder);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCommerceOrderRefunded");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCommerceOrder** | [**WebhookPayloadCommerceOrder**](WebhookPayloadCommerceOrder.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCommerceOrderUpdated

> void onCommerceOrderUpdated(webhookPayloadCommerceOrder)

Commerce order updated event

Fired when an order on a connected store changes: payment, fulfilment, cancellation, edits, and refunds too. The payload carries identifiers only; read the order with &#x60;GET /v1/commerce/orders/{orderId}?accountId&#x3D;...&#x60;. Fired once per Zernio account connected to the store. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCommerceOrder webhookPayloadCommerceOrder = new WebhookPayloadCommerceOrder(); // WebhookPayloadCommerceOrder | 
        try {
            apiInstance.onCommerceOrderUpdated(webhookPayloadCommerceOrder);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCommerceOrderUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCommerceOrder** | [**WebhookPayloadCommerceOrder**](WebhookPayloadCommerceOrder.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCommerceOrderUpdatedWithHttpInfo

> ApiResponse<Void> onCommerceOrderUpdated onCommerceOrderUpdatedWithHttpInfo(webhookPayloadCommerceOrder)

Commerce order updated event

Fired when an order on a connected store changes: payment, fulfilment, cancellation, edits, and refunds too. The payload carries identifiers only; read the order with &#x60;GET /v1/commerce/orders/{orderId}?accountId&#x3D;...&#x60;. Fired once per Zernio account connected to the store. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCommerceOrder webhookPayloadCommerceOrder = new WebhookPayloadCommerceOrder(); // WebhookPayloadCommerceOrder | 
        try {
            ApiResponse<Void> response = apiInstance.onCommerceOrderUpdatedWithHttpInfo(webhookPayloadCommerceOrder);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCommerceOrderUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCommerceOrder** | [**WebhookPayloadCommerceOrder**](WebhookPayloadCommerceOrder.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCommerceProductCreated

> void onCommerceProductCreated(webhookPayloadCommerceProduct)

Commerce product created event

Fired when a product is created on a connected store. The payload carries identifiers only; read the product with &#x60;GET /v1/commerce/products/{productId}?accountId&#x3D;...&#x60;. Fired once per Zernio account connected to the store. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCommerceProduct webhookPayloadCommerceProduct = new WebhookPayloadCommerceProduct(); // WebhookPayloadCommerceProduct | 
        try {
            apiInstance.onCommerceProductCreated(webhookPayloadCommerceProduct);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCommerceProductCreated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCommerceProduct** | [**WebhookPayloadCommerceProduct**](WebhookPayloadCommerceProduct.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCommerceProductCreatedWithHttpInfo

> ApiResponse<Void> onCommerceProductCreated onCommerceProductCreatedWithHttpInfo(webhookPayloadCommerceProduct)

Commerce product created event

Fired when a product is created on a connected store. The payload carries identifiers only; read the product with &#x60;GET /v1/commerce/products/{productId}?accountId&#x3D;...&#x60;. Fired once per Zernio account connected to the store. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCommerceProduct webhookPayloadCommerceProduct = new WebhookPayloadCommerceProduct(); // WebhookPayloadCommerceProduct | 
        try {
            ApiResponse<Void> response = apiInstance.onCommerceProductCreatedWithHttpInfo(webhookPayloadCommerceProduct);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCommerceProductCreated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCommerceProduct** | [**WebhookPayloadCommerceProduct**](WebhookPayloadCommerceProduct.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCommerceProductDeleted

> void onCommerceProductDeleted(webhookPayloadCommerceProduct)

Commerce product deleted event

Fired when a product is deleted from a connected store. &#x60;status&#x60; and &#x60;platformStatus&#x60; are null. The payload carries identifiers only; read the product with &#x60;GET /v1/commerce/products/{productId}?accountId&#x3D;...&#x60;. Fired once per Zernio account connected to the store. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCommerceProduct webhookPayloadCommerceProduct = new WebhookPayloadCommerceProduct(); // WebhookPayloadCommerceProduct | 
        try {
            apiInstance.onCommerceProductDeleted(webhookPayloadCommerceProduct);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCommerceProductDeleted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCommerceProduct** | [**WebhookPayloadCommerceProduct**](WebhookPayloadCommerceProduct.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCommerceProductDeletedWithHttpInfo

> ApiResponse<Void> onCommerceProductDeleted onCommerceProductDeletedWithHttpInfo(webhookPayloadCommerceProduct)

Commerce product deleted event

Fired when a product is deleted from a connected store. &#x60;status&#x60; and &#x60;platformStatus&#x60; are null. The payload carries identifiers only; read the product with &#x60;GET /v1/commerce/products/{productId}?accountId&#x3D;...&#x60;. Fired once per Zernio account connected to the store. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCommerceProduct webhookPayloadCommerceProduct = new WebhookPayloadCommerceProduct(); // WebhookPayloadCommerceProduct | 
        try {
            ApiResponse<Void> response = apiInstance.onCommerceProductDeletedWithHttpInfo(webhookPayloadCommerceProduct);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCommerceProductDeleted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCommerceProduct** | [**WebhookPayloadCommerceProduct**](WebhookPayloadCommerceProduct.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCommerceProductUpdated

> void onCommerceProductUpdated(webhookPayloadCommerceProduct)

Commerce product updated event

Fired when a product on a connected store changes: its fields, status, variants or prices. The payload carries identifiers only; read the product with &#x60;GET /v1/commerce/products/{productId}?accountId&#x3D;...&#x60;. Fired once per Zernio account connected to the store. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCommerceProduct webhookPayloadCommerceProduct = new WebhookPayloadCommerceProduct(); // WebhookPayloadCommerceProduct | 
        try {
            apiInstance.onCommerceProductUpdated(webhookPayloadCommerceProduct);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCommerceProductUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCommerceProduct** | [**WebhookPayloadCommerceProduct**](WebhookPayloadCommerceProduct.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCommerceProductUpdatedWithHttpInfo

> ApiResponse<Void> onCommerceProductUpdated onCommerceProductUpdatedWithHttpInfo(webhookPayloadCommerceProduct)

Commerce product updated event

Fired when a product on a connected store changes: its fields, status, variants or prices. The payload carries identifiers only; read the product with &#x60;GET /v1/commerce/products/{productId}?accountId&#x3D;...&#x60;. Fired once per Zernio account connected to the store. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCommerceProduct webhookPayloadCommerceProduct = new WebhookPayloadCommerceProduct(); // WebhookPayloadCommerceProduct | 
        try {
            ApiResponse<Void> response = apiInstance.onCommerceProductUpdatedWithHttpInfo(webhookPayloadCommerceProduct);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCommerceProductUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCommerceProduct** | [**WebhookPayloadCommerceProduct**](WebhookPayloadCommerceProduct.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onContactDeleted

> void onContactDeleted(webhookPayloadContact)

Contact deleted

The provider contact was deleted; its email channel is removed, the contact row stays when other channels remain.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadContact webhookPayloadContact = new WebhookPayloadContact(); // WebhookPayloadContact | 
        try {
            apiInstance.onContactDeleted(webhookPayloadContact);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onContactDeleted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadContact** | [**WebhookPayloadContact**](WebhookPayloadContact.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onContactDeletedWithHttpInfo

> ApiResponse<Void> onContactDeleted onContactDeletedWithHttpInfo(webhookPayloadContact)

Contact deleted

The provider contact was deleted; its email channel is removed, the contact row stays when other channels remain.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadContact webhookPayloadContact = new WebhookPayloadContact(); // WebhookPayloadContact | 
        try {
            ApiResponse<Void> response = apiInstance.onContactDeletedWithHttpInfo(webhookPayloadContact);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onContactDeleted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadContact** | [**WebhookPayloadContact**](WebhookPayloadContact.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onContactFieldChanged

> void onContactFieldChanged(webhookPayloadContactFieldChanged)

Contact field changed event

Fired once per custom field whose value a write changed, with the previous and new value.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadContactFieldChanged webhookPayloadContactFieldChanged = new WebhookPayloadContactFieldChanged(); // WebhookPayloadContactFieldChanged | 
        try {
            apiInstance.onContactFieldChanged(webhookPayloadContactFieldChanged);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onContactFieldChanged");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadContactFieldChanged** | [**WebhookPayloadContactFieldChanged**](WebhookPayloadContactFieldChanged.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onContactFieldChangedWithHttpInfo

> ApiResponse<Void> onContactFieldChanged onContactFieldChangedWithHttpInfo(webhookPayloadContactFieldChanged)

Contact field changed event

Fired once per custom field whose value a write changed, with the previous and new value.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadContactFieldChanged webhookPayloadContactFieldChanged = new WebhookPayloadContactFieldChanged(); // WebhookPayloadContactFieldChanged | 
        try {
            ApiResponse<Void> response = apiInstance.onContactFieldChangedWithHttpInfo(webhookPayloadContactFieldChanged);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onContactFieldChanged");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadContactFieldChanged** | [**WebhookPayloadContactFieldChanged**](WebhookPayloadContactFieldChanged.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onContactTagAdded

> void onContactTagAdded(webhookPayloadContactTag)

Contact tag added event

Fired once per tag a write actually added to a contact, whether the API, a workflow add_tag node or a comment-automation click made it.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadContactTag webhookPayloadContactTag = new WebhookPayloadContactTag(); // WebhookPayloadContactTag | 
        try {
            apiInstance.onContactTagAdded(webhookPayloadContactTag);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onContactTagAdded");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadContactTag** | [**WebhookPayloadContactTag**](WebhookPayloadContactTag.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onContactTagAddedWithHttpInfo

> ApiResponse<Void> onContactTagAdded onContactTagAddedWithHttpInfo(webhookPayloadContactTag)

Contact tag added event

Fired once per tag a write actually added to a contact, whether the API, a workflow add_tag node or a comment-automation click made it.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadContactTag webhookPayloadContactTag = new WebhookPayloadContactTag(); // WebhookPayloadContactTag | 
        try {
            ApiResponse<Void> response = apiInstance.onContactTagAddedWithHttpInfo(webhookPayloadContactTag);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onContactTagAdded");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadContactTag** | [**WebhookPayloadContactTag**](WebhookPayloadContactTag.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onContactTagRemoved

> void onContactTagRemoved(webhookPayloadContactTag)

Contact tag removed event

Fired once per tag a write actually removed from a contact.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadContactTag webhookPayloadContactTag = new WebhookPayloadContactTag(); // WebhookPayloadContactTag | 
        try {
            apiInstance.onContactTagRemoved(webhookPayloadContactTag);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onContactTagRemoved");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadContactTag** | [**WebhookPayloadContactTag**](WebhookPayloadContactTag.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onContactTagRemovedWithHttpInfo

> ApiResponse<Void> onContactTagRemoved onContactTagRemovedWithHttpInfo(webhookPayloadContactTag)

Contact tag removed event

Fired once per tag a write actually removed from a contact.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadContactTag webhookPayloadContactTag = new WebhookPayloadContactTag(); // WebhookPayloadContactTag | 
        try {
            ApiResponse<Void> response = apiInstance.onContactTagRemovedWithHttpInfo(webhookPayloadContactTag);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onContactTagRemoved");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadContactTag** | [**WebhookPayloadContactTag**](WebhookPayloadContactTag.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onContactUpdated

> void onContactUpdated(webhookPayloadContact)

Contact updated

A provider contacts sync created or changed a contact.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadContact webhookPayloadContact = new WebhookPayloadContact(); // WebhookPayloadContact | 
        try {
            apiInstance.onContactUpdated(webhookPayloadContact);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onContactUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadContact** | [**WebhookPayloadContact**](WebhookPayloadContact.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onContactUpdatedWithHttpInfo

> ApiResponse<Void> onContactUpdated onContactUpdatedWithHttpInfo(webhookPayloadContact)

Contact updated

A provider contacts sync created or changed a contact.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadContact webhookPayloadContact = new WebhookPayloadContact(); // WebhookPayloadContact | 
        try {
            ApiResponse<Void> response = apiInstance.onContactUpdatedWithHttpInfo(webhookPayloadContact);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onContactUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadContact** | [**WebhookPayloadContact**](WebhookPayloadContact.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onConversationControlChanged

> void onConversationControlChanged(webhookPayloadConversationControlChanged)

Conversation control changed event

Fired on Meta&#39;s handover protocol (&#x60;messaging_handovers&#x60;). WhatsApp: control moves between Meta Business Agent and your app, or the agent is first seen answering a thread; while &#x60;control.owner&#x60; is &#x60;ai_agent&#x60;, inbound messages arrive on &#x60;message.received&#x60; with &#x60;metadata.standby: true&#x60; and the agent&#39;s replies on &#x60;message.sent&#x60; with &#x60;source: meta_business_agent&#x60;, and sending any message takes control back. Facebook and Instagram: another app passed you the thread (&#x60;owner: app&#x60;) or took or received it (&#x60;owner: other&#x60;, with &#x60;ownerAppId&#x60;); while you are not the owner, inbound arrive with &#x60;metadata.standby: true&#x60;, no automation runs, and sends fail with &#x60;not_thread_owner&#x60;. Change control with &#x60;POST /v1/inbox/conversations/{conversationId}/thread-control&#x60;. &#x60;take&#x60; and &#x60;request&#x60; answer 400 &#x60;platform_not_supported&#x60; on Instagram Login connections. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadConversationControlChanged webhookPayloadConversationControlChanged = new WebhookPayloadConversationControlChanged(); // WebhookPayloadConversationControlChanged | 
        try {
            apiInstance.onConversationControlChanged(webhookPayloadConversationControlChanged);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onConversationControlChanged");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadConversationControlChanged** | [**WebhookPayloadConversationControlChanged**](WebhookPayloadConversationControlChanged.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onConversationControlChangedWithHttpInfo

> ApiResponse<Void> onConversationControlChanged onConversationControlChangedWithHttpInfo(webhookPayloadConversationControlChanged)

Conversation control changed event

Fired on Meta&#39;s handover protocol (&#x60;messaging_handovers&#x60;). WhatsApp: control moves between Meta Business Agent and your app, or the agent is first seen answering a thread; while &#x60;control.owner&#x60; is &#x60;ai_agent&#x60;, inbound messages arrive on &#x60;message.received&#x60; with &#x60;metadata.standby: true&#x60; and the agent&#39;s replies on &#x60;message.sent&#x60; with &#x60;source: meta_business_agent&#x60;, and sending any message takes control back. Facebook and Instagram: another app passed you the thread (&#x60;owner: app&#x60;) or took or received it (&#x60;owner: other&#x60;, with &#x60;ownerAppId&#x60;); while you are not the owner, inbound arrive with &#x60;metadata.standby: true&#x60;, no automation runs, and sends fail with &#x60;not_thread_owner&#x60;. Change control with &#x60;POST /v1/inbox/conversations/{conversationId}/thread-control&#x60;. &#x60;take&#x60; and &#x60;request&#x60; answer 400 &#x60;platform_not_supported&#x60; on Instagram Login connections. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadConversationControlChanged webhookPayloadConversationControlChanged = new WebhookPayloadConversationControlChanged(); // WebhookPayloadConversationControlChanged | 
        try {
            ApiResponse<Void> response = apiInstance.onConversationControlChangedWithHttpInfo(webhookPayloadConversationControlChanged);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onConversationControlChanged");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadConversationControlChanged** | [**WebhookPayloadConversationControlChanged**](WebhookPayloadConversationControlChanged.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onConversationStarted

> void onConversationStarted(webhookPayloadConversationStarted)

Conversation started event

Fired once when a new conversation begins between one of your connected accounts and a contact, in either direction. Works across every DM platform (Instagram, Messenger/Facebook, Telegram, WhatsApp, X, Reddit, Bluesky, TikTok). Naturally deduped: a given conversation only fires this event the very first time it appears. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadConversationStarted webhookPayloadConversationStarted = new WebhookPayloadConversationStarted(); // WebhookPayloadConversationStarted | 
        try {
            apiInstance.onConversationStarted(webhookPayloadConversationStarted);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onConversationStarted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadConversationStarted** | [**WebhookPayloadConversationStarted**](WebhookPayloadConversationStarted.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onConversationStartedWithHttpInfo

> ApiResponse<Void> onConversationStarted onConversationStartedWithHttpInfo(webhookPayloadConversationStarted)

Conversation started event

Fired once when a new conversation begins between one of your connected accounts and a contact, in either direction. Works across every DM platform (Instagram, Messenger/Facebook, Telegram, WhatsApp, X, Reddit, Bluesky, TikTok). Naturally deduped: a given conversation only fires this event the very first time it appears. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadConversationStarted webhookPayloadConversationStarted = new WebhookPayloadConversationStarted(); // WebhookPayloadConversationStarted | 
        try {
            ApiResponse<Void> response = apiInstance.onConversationStartedWithHttpInfo(webhookPayloadConversationStarted);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onConversationStarted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadConversationStarted** | [**WebhookPayloadConversationStarted**](WebhookPayloadConversationStarted.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCreatorCampaignBudgetExhausted

> void onCreatorCampaignBudgetExhausted(webhookPayloadCreatorCampaign)

Creator campaign budget exhausted event

Fired once when a campaign&#39;s earnings reach its budget.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCreatorCampaign webhookPayloadCreatorCampaign = new WebhookPayloadCreatorCampaign(); // WebhookPayloadCreatorCampaign | 
        try {
            apiInstance.onCreatorCampaignBudgetExhausted(webhookPayloadCreatorCampaign);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCreatorCampaignBudgetExhausted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCreatorCampaign** | [**WebhookPayloadCreatorCampaign**](WebhookPayloadCreatorCampaign.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCreatorCampaignBudgetExhaustedWithHttpInfo

> ApiResponse<Void> onCreatorCampaignBudgetExhausted onCreatorCampaignBudgetExhaustedWithHttpInfo(webhookPayloadCreatorCampaign)

Creator campaign budget exhausted event

Fired once when a campaign&#39;s earnings reach its budget.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCreatorCampaign webhookPayloadCreatorCampaign = new WebhookPayloadCreatorCampaign(); // WebhookPayloadCreatorCampaign | 
        try {
            ApiResponse<Void> response = apiInstance.onCreatorCampaignBudgetExhaustedWithHttpInfo(webhookPayloadCreatorCampaign);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCreatorCampaignBudgetExhausted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCreatorCampaign** | [**WebhookPayloadCreatorCampaign**](WebhookPayloadCreatorCampaign.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onCreatorCampaignClosed

> void onCreatorCampaignClosed(webhookPayloadCreatorCampaign)

Creator campaign closed event

Fired once when a campaign closes; a pool campaign is split among participants at this moment.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCreatorCampaign webhookPayloadCreatorCampaign = new WebhookPayloadCreatorCampaign(); // WebhookPayloadCreatorCampaign | 
        try {
            apiInstance.onCreatorCampaignClosed(webhookPayloadCreatorCampaign);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCreatorCampaignClosed");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCreatorCampaign** | [**WebhookPayloadCreatorCampaign**](WebhookPayloadCreatorCampaign.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onCreatorCampaignClosedWithHttpInfo

> ApiResponse<Void> onCreatorCampaignClosed onCreatorCampaignClosedWithHttpInfo(webhookPayloadCreatorCampaign)

Creator campaign closed event

Fired once when a campaign closes; a pool campaign is split among participants at this moment.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadCreatorCampaign webhookPayloadCreatorCampaign = new WebhookPayloadCreatorCampaign(); // WebhookPayloadCreatorCampaign | 
        try {
            ApiResponse<Void> response = apiInstance.onCreatorCampaignClosedWithHttpInfo(webhookPayloadCreatorCampaign);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCreatorCampaignClosed");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadCreatorCampaign** | [**WebhookPayloadCreatorCampaign**](WebhookPayloadCreatorCampaign.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onFileCreated

> void onFileCreated(webhookPayloadFile)

File created

A file or folder appeared in a connected Drive or OneDrive (push, seconds after the change).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadFile webhookPayloadFile = new WebhookPayloadFile(); // WebhookPayloadFile | 
        try {
            apiInstance.onFileCreated(webhookPayloadFile);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onFileCreated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadFile** | [**WebhookPayloadFile**](WebhookPayloadFile.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onFileCreatedWithHttpInfo

> ApiResponse<Void> onFileCreated onFileCreatedWithHttpInfo(webhookPayloadFile)

File created

A file or folder appeared in a connected Drive or OneDrive (push, seconds after the change).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadFile webhookPayloadFile = new WebhookPayloadFile(); // WebhookPayloadFile | 
        try {
            ApiResponse<Void> response = apiInstance.onFileCreatedWithHttpInfo(webhookPayloadFile);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onFileCreated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadFile** | [**WebhookPayloadFile**](WebhookPayloadFile.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onFileDeleted

> void onFileDeleted(webhookPayloadFile)

File deleted

The item was trashed or removed on the provider.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadFile webhookPayloadFile = new WebhookPayloadFile(); // WebhookPayloadFile | 
        try {
            apiInstance.onFileDeleted(webhookPayloadFile);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onFileDeleted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadFile** | [**WebhookPayloadFile**](WebhookPayloadFile.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onFileDeletedWithHttpInfo

> ApiResponse<Void> onFileDeleted onFileDeletedWithHttpInfo(webhookPayloadFile)

File deleted

The item was trashed or removed on the provider.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadFile webhookPayloadFile = new WebhookPayloadFile(); // WebhookPayloadFile | 
        try {
            ApiResponse<Void> response = apiInstance.onFileDeletedWithHttpInfo(webhookPayloadFile);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onFileDeleted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadFile** | [**WebhookPayloadFile**](WebhookPayloadFile.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onFilePicked

> void onFilePicked(webhookPayloadFilePicked)

Files picked

The user finished a hosted picker session (&#x60;POST /v1/files/picker-sessions&#x60;) and picked at least one file. The app can now open those files. Not sent on cancel.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadFilePicked webhookPayloadFilePicked = new WebhookPayloadFilePicked(); // WebhookPayloadFilePicked | 
        try {
            apiInstance.onFilePicked(webhookPayloadFilePicked);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onFilePicked");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadFilePicked** | [**WebhookPayloadFilePicked**](WebhookPayloadFilePicked.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onFilePickedWithHttpInfo

> ApiResponse<Void> onFilePicked onFilePickedWithHttpInfo(webhookPayloadFilePicked)

Files picked

The user finished a hosted picker session (&#x60;POST /v1/files/picker-sessions&#x60;) and picked at least one file. The app can now open those files. Not sent on cancel.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadFilePicked webhookPayloadFilePicked = new WebhookPayloadFilePicked(); // WebhookPayloadFilePicked | 
        try {
            ApiResponse<Void> response = apiInstance.onFilePickedWithHttpInfo(webhookPayloadFilePicked);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onFilePicked");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadFilePicked** | [**WebhookPayloadFilePicked**](WebhookPayloadFilePicked.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onFileUpdated

> void onFileUpdated(webhookPayloadFile)

File updated

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadFile webhookPayloadFile = new WebhookPayloadFile(); // WebhookPayloadFile | 
        try {
            apiInstance.onFileUpdated(webhookPayloadFile);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onFileUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadFile** | [**WebhookPayloadFile**](WebhookPayloadFile.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onFileUpdatedWithHttpInfo

> ApiResponse<Void> onFileUpdated onFileUpdatedWithHttpInfo(webhookPayloadFile)

File updated

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadFile webhookPayloadFile = new WebhookPayloadFile(); // WebhookPayloadFile | 
        try {
            ApiResponse<Void> response = apiInstance.onFileUpdatedWithHttpInfo(webhookPayloadFile);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onFileUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadFile** | [**WebhookPayloadFile**](WebhookPayloadFile.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onLeadReceived

> void onLeadReceived(webhookPayloadLead)

Lead received event

Fired when a new lead is submitted against a Meta Lead Gen (Instant) Form and ingested via the Page &#x60;leadgen&#x60; webhook. &#x60;lead.fields&#x60; is the question-key to answer map; &#x60;lead.formId&#x60; / &#x60;lead.adId&#x60; give provenance. Requires the Ads add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadLead webhookPayloadLead = new WebhookPayloadLead(); // WebhookPayloadLead | 
        try {
            apiInstance.onLeadReceived(webhookPayloadLead);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onLeadReceived");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadLead** | [**WebhookPayloadLead**](WebhookPayloadLead.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onLeadReceivedWithHttpInfo

> ApiResponse<Void> onLeadReceived onLeadReceivedWithHttpInfo(webhookPayloadLead)

Lead received event

Fired when a new lead is submitted against a Meta Lead Gen (Instant) Form and ingested via the Page &#x60;leadgen&#x60; webhook. &#x60;lead.fields&#x60; is the question-key to answer map; &#x60;lead.formId&#x60; / &#x60;lead.adId&#x60; give provenance. Requires the Ads add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadLead webhookPayloadLead = new WebhookPayloadLead(); // WebhookPayloadLead | 
        try {
            ApiResponse<Void> response = apiInstance.onLeadReceivedWithHttpInfo(webhookPayloadLead);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onLeadReceived");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadLead** | [**WebhookPayloadLead**](WebhookPayloadLead.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onMessageDeleted

> void onMessageDeleted(webhookPayloadMessageDeleted)

Message deleted event

Fired when a sender deletes (unsends) a message. Supported on Instagram (incoming unsend) and WhatsApp in both directions: an outgoing message the business deleted (via the Cloud API, or from the WhatsApp Business app on a Coexistence number) and an incoming message the customer deleted. Read &#x60;message.direction&#x60; to tell the two apart. The payload retains the pre-delete text and attachments so API consumers can access the original content for moderation or compliance; the Zernio dashboard UI hides it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessageDeleted webhookPayloadMessageDeleted = new WebhookPayloadMessageDeleted(); // WebhookPayloadMessageDeleted | 
        try {
            apiInstance.onMessageDeleted(webhookPayloadMessageDeleted);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessageDeleted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadMessageDeleted** | [**WebhookPayloadMessageDeleted**](WebhookPayloadMessageDeleted.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onMessageDeletedWithHttpInfo

> ApiResponse<Void> onMessageDeleted onMessageDeletedWithHttpInfo(webhookPayloadMessageDeleted)

Message deleted event

Fired when a sender deletes (unsends) a message. Supported on Instagram (incoming unsend) and WhatsApp in both directions: an outgoing message the business deleted (via the Cloud API, or from the WhatsApp Business app on a Coexistence number) and an incoming message the customer deleted. Read &#x60;message.direction&#x60; to tell the two apart. The payload retains the pre-delete text and attachments so API consumers can access the original content for moderation or compliance; the Zernio dashboard UI hides it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessageDeleted webhookPayloadMessageDeleted = new WebhookPayloadMessageDeleted(); // WebhookPayloadMessageDeleted | 
        try {
            ApiResponse<Void> response = apiInstance.onMessageDeletedWithHttpInfo(webhookPayloadMessageDeleted);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessageDeleted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadMessageDeleted** | [**WebhookPayloadMessageDeleted**](WebhookPayloadMessageDeleted.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onMessageDelivered

> void onMessageDelivered(webhookPayloadMessageDeliveryStatus)

Message delivered event

Fired when an outgoing message is delivered to the recipient. Supported on WhatsApp and Facebook Messenger. On WhatsApp, &#x60;pricing&#x60; and &#x60;billingConversation&#x60; carry Meta&#39;s billing context for the message (also on &#x60;message.sent&#x60;, &#x60;message.read&#x60; and &#x60;message.failed&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessageDeliveryStatus webhookPayloadMessageDeliveryStatus = new WebhookPayloadMessageDeliveryStatus(); // WebhookPayloadMessageDeliveryStatus | 
        try {
            apiInstance.onMessageDelivered(webhookPayloadMessageDeliveryStatus);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessageDelivered");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadMessageDeliveryStatus** | [**WebhookPayloadMessageDeliveryStatus**](WebhookPayloadMessageDeliveryStatus.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onMessageDeliveredWithHttpInfo

> ApiResponse<Void> onMessageDelivered onMessageDeliveredWithHttpInfo(webhookPayloadMessageDeliveryStatus)

Message delivered event

Fired when an outgoing message is delivered to the recipient. Supported on WhatsApp and Facebook Messenger. On WhatsApp, &#x60;pricing&#x60; and &#x60;billingConversation&#x60; carry Meta&#39;s billing context for the message (also on &#x60;message.sent&#x60;, &#x60;message.read&#x60; and &#x60;message.failed&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessageDeliveryStatus webhookPayloadMessageDeliveryStatus = new WebhookPayloadMessageDeliveryStatus(); // WebhookPayloadMessageDeliveryStatus | 
        try {
            ApiResponse<Void> response = apiInstance.onMessageDeliveredWithHttpInfo(webhookPayloadMessageDeliveryStatus);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessageDelivered");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadMessageDeliveryStatus** | [**WebhookPayloadMessageDeliveryStatus**](WebhookPayloadMessageDeliveryStatus.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onMessageEdited

> void onMessageEdited(webhookPayloadMessageEdited)

Message edited event

Fired when a sender edits a previously-sent message. Supported on Instagram, Facebook Messenger, Telegram, and WhatsApp. The payload includes the full editHistory so consumers can show prior versions. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessageEdited webhookPayloadMessageEdited = new WebhookPayloadMessageEdited(); // WebhookPayloadMessageEdited | 
        try {
            apiInstance.onMessageEdited(webhookPayloadMessageEdited);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessageEdited");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadMessageEdited** | [**WebhookPayloadMessageEdited**](WebhookPayloadMessageEdited.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onMessageEditedWithHttpInfo

> ApiResponse<Void> onMessageEdited onMessageEditedWithHttpInfo(webhookPayloadMessageEdited)

Message edited event

Fired when a sender edits a previously-sent message. Supported on Instagram, Facebook Messenger, Telegram, and WhatsApp. The payload includes the full editHistory so consumers can show prior versions. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessageEdited webhookPayloadMessageEdited = new WebhookPayloadMessageEdited(); // WebhookPayloadMessageEdited | 
        try {
            ApiResponse<Void> response = apiInstance.onMessageEditedWithHttpInfo(webhookPayloadMessageEdited);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessageEdited");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadMessageEdited** | [**WebhookPayloadMessageEdited**](WebhookPayloadMessageEdited.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onMessageFailed

> void onMessageFailed(webhookPayloadMessageDeliveryStatus)

Message delivery failed event

Fired when an outgoing message fails to deliver. Currently only emitted for WhatsApp (other platforms don&#39;t expose per-message failure via webhook). The payload error object contains code, title, and message from the platform. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessageDeliveryStatus webhookPayloadMessageDeliveryStatus = new WebhookPayloadMessageDeliveryStatus(); // WebhookPayloadMessageDeliveryStatus | 
        try {
            apiInstance.onMessageFailed(webhookPayloadMessageDeliveryStatus);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessageFailed");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadMessageDeliveryStatus** | [**WebhookPayloadMessageDeliveryStatus**](WebhookPayloadMessageDeliveryStatus.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onMessageFailedWithHttpInfo

> ApiResponse<Void> onMessageFailed onMessageFailedWithHttpInfo(webhookPayloadMessageDeliveryStatus)

Message delivery failed event

Fired when an outgoing message fails to deliver. Currently only emitted for WhatsApp (other platforms don&#39;t expose per-message failure via webhook). The payload error object contains code, title, and message from the platform. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessageDeliveryStatus webhookPayloadMessageDeliveryStatus = new WebhookPayloadMessageDeliveryStatus(); // WebhookPayloadMessageDeliveryStatus | 
        try {
            ApiResponse<Void> response = apiInstance.onMessageFailedWithHttpInfo(webhookPayloadMessageDeliveryStatus);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessageFailed");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadMessageDeliveryStatus** | [**WebhookPayloadMessageDeliveryStatus**](WebhookPayloadMessageDeliveryStatus.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onMessagePlayed

> void onMessagePlayed(webhookPayloadMessageDeliveryStatus)

Message played event

Fires the first time the recipient plays a voice message you sent on WhatsApp.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessageDeliveryStatus webhookPayloadMessageDeliveryStatus = new WebhookPayloadMessageDeliveryStatus(); // WebhookPayloadMessageDeliveryStatus | 
        try {
            apiInstance.onMessagePlayed(webhookPayloadMessageDeliveryStatus);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessagePlayed");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadMessageDeliveryStatus** | [**WebhookPayloadMessageDeliveryStatus**](WebhookPayloadMessageDeliveryStatus.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onMessagePlayedWithHttpInfo

> ApiResponse<Void> onMessagePlayed onMessagePlayedWithHttpInfo(webhookPayloadMessageDeliveryStatus)

Message played event

Fires the first time the recipient plays a voice message you sent on WhatsApp.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessageDeliveryStatus webhookPayloadMessageDeliveryStatus = new WebhookPayloadMessageDeliveryStatus(); // WebhookPayloadMessageDeliveryStatus | 
        try {
            ApiResponse<Void> response = apiInstance.onMessagePlayedWithHttpInfo(webhookPayloadMessageDeliveryStatus);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessagePlayed");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadMessageDeliveryStatus** | [**WebhookPayloadMessageDeliveryStatus**](WebhookPayloadMessageDeliveryStatus.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onMessageRead

> void onMessageRead(webhookPayloadMessageDeliveryStatus)

Message read event

Fired when an outgoing message is read by the recipient. Supported on WhatsApp, Facebook Messenger, Instagram, and RCS. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessageDeliveryStatus webhookPayloadMessageDeliveryStatus = new WebhookPayloadMessageDeliveryStatus(); // WebhookPayloadMessageDeliveryStatus | 
        try {
            apiInstance.onMessageRead(webhookPayloadMessageDeliveryStatus);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessageRead");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadMessageDeliveryStatus** | [**WebhookPayloadMessageDeliveryStatus**](WebhookPayloadMessageDeliveryStatus.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onMessageReadWithHttpInfo

> ApiResponse<Void> onMessageRead onMessageReadWithHttpInfo(webhookPayloadMessageDeliveryStatus)

Message read event

Fired when an outgoing message is read by the recipient. Supported on WhatsApp, Facebook Messenger, Instagram, and RCS. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessageDeliveryStatus webhookPayloadMessageDeliveryStatus = new WebhookPayloadMessageDeliveryStatus(); // WebhookPayloadMessageDeliveryStatus | 
        try {
            ApiResponse<Void> response = apiInstance.onMessageReadWithHttpInfo(webhookPayloadMessageDeliveryStatus);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessageRead");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadMessageDeliveryStatus** | [**WebhookPayloadMessageDeliveryStatus**](WebhookPayloadMessageDeliveryStatus.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onMessageReceived

> void onMessageReceived(webhookPayloadMessage)

Message received event

Fired when a new inbox message is received.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessage webhookPayloadMessage = new WebhookPayloadMessage(); // WebhookPayloadMessage | 
        try {
            apiInstance.onMessageReceived(webhookPayloadMessage);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessageReceived");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadMessage** | [**WebhookPayloadMessage**](WebhookPayloadMessage.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onMessageReceivedWithHttpInfo

> ApiResponse<Void> onMessageReceived onMessageReceivedWithHttpInfo(webhookPayloadMessage)

Message received event

Fired when a new inbox message is received.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessage webhookPayloadMessage = new WebhookPayloadMessage(); // WebhookPayloadMessage | 
        try {
            ApiResponse<Void> response = apiInstance.onMessageReceivedWithHttpInfo(webhookPayloadMessage);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessageReceived");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadMessage** | [**WebhookPayloadMessage**](WebhookPayloadMessage.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onMessageSent

> void onMessageSent(webhookPayloadMessageSent)

Message sent event

Fired when a message is sent via the API, or from the WhatsApp Business app on Coexistence numbers. Sends that carry platform-specific context deliver it under &#x60;metadata&#x60;, so a quote-reply sent through the API arrives with &#x60;metadata.quotedMessageId&#x60; and mirroring CRMs can thread it without a lookup. Which surfaces actually carry that reference is documented on &#x60;WebhookPayloadMessageSent.metadata.quotedMessageId&#x60;; a quote-reply sent from the WhatsApp Business or Instagram app is not one of them. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessageSent webhookPayloadMessageSent = new WebhookPayloadMessageSent(); // WebhookPayloadMessageSent | 
        try {
            apiInstance.onMessageSent(webhookPayloadMessageSent);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessageSent");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadMessageSent** | [**WebhookPayloadMessageSent**](WebhookPayloadMessageSent.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onMessageSentWithHttpInfo

> ApiResponse<Void> onMessageSent onMessageSentWithHttpInfo(webhookPayloadMessageSent)

Message sent event

Fired when a message is sent via the API, or from the WhatsApp Business app on Coexistence numbers. Sends that carry platform-specific context deliver it under &#x60;metadata&#x60;, so a quote-reply sent through the API arrives with &#x60;metadata.quotedMessageId&#x60; and mirroring CRMs can thread it without a lookup. Which surfaces actually carry that reference is documented on &#x60;WebhookPayloadMessageSent.metadata.quotedMessageId&#x60;; a quote-reply sent from the WhatsApp Business or Instagram app is not one of them. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadMessageSent webhookPayloadMessageSent = new WebhookPayloadMessageSent(); // WebhookPayloadMessageSent | 
        try {
            ApiResponse<Void> response = apiInstance.onMessageSentWithHttpInfo(webhookPayloadMessageSent);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMessageSent");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadMessageSent** | [**WebhookPayloadMessageSent**](WebhookPayloadMessageSent.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onPhoneNumberStockAvailable

> void onPhoneNumberStockAvailable(webhookPayloadPhoneNumberStockAvailable)

Phone-number stock available event

Fired by the stock sweep (every 6h) the first time a country you watch via POST /v1/phone-numbers/stock-watches has deliverable numbers again. The watch is consumed, so the event fires once per watch; the stock counts are a snapshot and numbers are sold first come, first served. Buy with POST /v1/phone-numbers/purchase. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPhoneNumberStockAvailable webhookPayloadPhoneNumberStockAvailable = new WebhookPayloadPhoneNumberStockAvailable(); // WebhookPayloadPhoneNumberStockAvailable | 
        try {
            apiInstance.onPhoneNumberStockAvailable(webhookPayloadPhoneNumberStockAvailable);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPhoneNumberStockAvailable");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadPhoneNumberStockAvailable** | [**WebhookPayloadPhoneNumberStockAvailable**](WebhookPayloadPhoneNumberStockAvailable.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onPhoneNumberStockAvailableWithHttpInfo

> ApiResponse<Void> onPhoneNumberStockAvailable onPhoneNumberStockAvailableWithHttpInfo(webhookPayloadPhoneNumberStockAvailable)

Phone-number stock available event

Fired by the stock sweep (every 6h) the first time a country you watch via POST /v1/phone-numbers/stock-watches has deliverable numbers again. The watch is consumed, so the event fires once per watch; the stock counts are a snapshot and numbers are sold first come, first served. Buy with POST /v1/phone-numbers/purchase. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPhoneNumberStockAvailable webhookPayloadPhoneNumberStockAvailable = new WebhookPayloadPhoneNumberStockAvailable(); // WebhookPayloadPhoneNumberStockAvailable | 
        try {
            ApiResponse<Void> response = apiInstance.onPhoneNumberStockAvailableWithHttpInfo(webhookPayloadPhoneNumberStockAvailable);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPhoneNumberStockAvailable");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadPhoneNumberStockAvailable** | [**WebhookPayloadPhoneNumberStockAvailable**](WebhookPayloadPhoneNumberStockAvailable.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onPostAuthenticityChanged

> void onPostAuthenticityChanged(webhookPayloadPostAuthenticityChanged)

Post authenticity changed event

Fired when a tracked post&#39;s authenticity score crosses 40 in either direction. Carries the new and previous score, confidence and reasons. A first score never fires it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPostAuthenticityChanged webhookPayloadPostAuthenticityChanged = new WebhookPayloadPostAuthenticityChanged(); // WebhookPayloadPostAuthenticityChanged | 
        try {
            apiInstance.onPostAuthenticityChanged(webhookPayloadPostAuthenticityChanged);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostAuthenticityChanged");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadPostAuthenticityChanged** | [**WebhookPayloadPostAuthenticityChanged**](WebhookPayloadPostAuthenticityChanged.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onPostAuthenticityChangedWithHttpInfo

> ApiResponse<Void> onPostAuthenticityChanged onPostAuthenticityChangedWithHttpInfo(webhookPayloadPostAuthenticityChanged)

Post authenticity changed event

Fired when a tracked post&#39;s authenticity score crosses 40 in either direction. Carries the new and previous score, confidence and reasons. A first score never fires it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPostAuthenticityChanged webhookPayloadPostAuthenticityChanged = new WebhookPayloadPostAuthenticityChanged(); // WebhookPayloadPostAuthenticityChanged | 
        try {
            ApiResponse<Void> response = apiInstance.onPostAuthenticityChangedWithHttpInfo(webhookPayloadPostAuthenticityChanged);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostAuthenticityChanged");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadPostAuthenticityChanged** | [**WebhookPayloadPostAuthenticityChanged**](WebhookPayloadPostAuthenticityChanged.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onPostCancelled

> void onPostCancelled(webhookPayloadPost)

Post cancelled event

Fired when a scheduled post is cancelled because its account was disconnected and nothing published. Not sent when a post is deleted.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPost webhookPayloadPost = new WebhookPayloadPost(); // WebhookPayloadPost | 
        try {
            apiInstance.onPostCancelled(webhookPayloadPost);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostCancelled");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadPost** | [**WebhookPayloadPost**](WebhookPayloadPost.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onPostCancelledWithHttpInfo

> ApiResponse<Void> onPostCancelled onPostCancelledWithHttpInfo(webhookPayloadPost)

Post cancelled event

Fired when a scheduled post is cancelled because its account was disconnected and nothing published. Not sent when a post is deleted.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPost webhookPayloadPost = new WebhookPayloadPost(); // WebhookPayloadPost | 
        try {
            ApiResponse<Void> response = apiInstance.onPostCancelledWithHttpInfo(webhookPayloadPost);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostCancelled");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadPost** | [**WebhookPayloadPost**](WebhookPayloadPost.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onPostExternalCreated

> void onPostExternalCreated(webhookPayloadExternalPost)

External post created event

Fired when Zernio&#39;s background sync detects a natively-authored post (created outside Zernio, e.g. a Google Business Profile localPost made in the Google UI) for the first time. Poll-driven (~hourly), not real-time. &#x60;post.source&#x60; is always \&quot;external\&quot;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadExternalPost webhookPayloadExternalPost = new WebhookPayloadExternalPost(); // WebhookPayloadExternalPost | 
        try {
            apiInstance.onPostExternalCreated(webhookPayloadExternalPost);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostExternalCreated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadExternalPost** | [**WebhookPayloadExternalPost**](WebhookPayloadExternalPost.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onPostExternalCreatedWithHttpInfo

> ApiResponse<Void> onPostExternalCreated onPostExternalCreatedWithHttpInfo(webhookPayloadExternalPost)

External post created event

Fired when Zernio&#39;s background sync detects a natively-authored post (created outside Zernio, e.g. a Google Business Profile localPost made in the Google UI) for the first time. Poll-driven (~hourly), not real-time. &#x60;post.source&#x60; is always \&quot;external\&quot;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadExternalPost webhookPayloadExternalPost = new WebhookPayloadExternalPost(); // WebhookPayloadExternalPost | 
        try {
            ApiResponse<Void> response = apiInstance.onPostExternalCreatedWithHttpInfo(webhookPayloadExternalPost);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostExternalCreated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadExternalPost** | [**WebhookPayloadExternalPost**](WebhookPayloadExternalPost.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onPostExternalDeleted

> void onPostExternalDeleted(webhookPayloadExternalPost)

External post deleted event

Fired when a tracked native post is detected as removed from the platform. &#x60;post.deletedAt&#x60; carries the detection time. Coverage is bounded to the most recent posts the platform listing returns. Detection is a diff against the posts a prior sync already indexed, so an account for which no post has ever been indexed can never emit this event, no matter how the subscription is configured. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadExternalPost webhookPayloadExternalPost = new WebhookPayloadExternalPost(); // WebhookPayloadExternalPost | 
        try {
            apiInstance.onPostExternalDeleted(webhookPayloadExternalPost);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostExternalDeleted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadExternalPost** | [**WebhookPayloadExternalPost**](WebhookPayloadExternalPost.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onPostExternalDeletedWithHttpInfo

> ApiResponse<Void> onPostExternalDeleted onPostExternalDeletedWithHttpInfo(webhookPayloadExternalPost)

External post deleted event

Fired when a tracked native post is detected as removed from the platform. &#x60;post.deletedAt&#x60; carries the detection time. Coverage is bounded to the most recent posts the platform listing returns. Detection is a diff against the posts a prior sync already indexed, so an account for which no post has ever been indexed can never emit this event, no matter how the subscription is configured. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadExternalPost webhookPayloadExternalPost = new WebhookPayloadExternalPost(); // WebhookPayloadExternalPost | 
        try {
            ApiResponse<Void> response = apiInstance.onPostExternalDeletedWithHttpInfo(webhookPayloadExternalPost);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostExternalDeleted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadExternalPost** | [**WebhookPayloadExternalPost**](WebhookPayloadExternalPost.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onPostExternalUpdated

> void onPostExternalUpdated(webhookPayloadExternalPost)

External post updated event

Fired when a tracked native post&#39;s text or media changed on the platform. Detected by comparing text/media structure and, where available, the platform&#39;s own edit timestamp; a media-URL-only refresh does not fire this. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadExternalPost webhookPayloadExternalPost = new WebhookPayloadExternalPost(); // WebhookPayloadExternalPost | 
        try {
            apiInstance.onPostExternalUpdated(webhookPayloadExternalPost);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostExternalUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadExternalPost** | [**WebhookPayloadExternalPost**](WebhookPayloadExternalPost.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onPostExternalUpdatedWithHttpInfo

> ApiResponse<Void> onPostExternalUpdated onPostExternalUpdatedWithHttpInfo(webhookPayloadExternalPost)

External post updated event

Fired when a tracked native post&#39;s text or media changed on the platform. Detected by comparing text/media structure and, where available, the platform&#39;s own edit timestamp; a media-URL-only refresh does not fire this. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadExternalPost webhookPayloadExternalPost = new WebhookPayloadExternalPost(); // WebhookPayloadExternalPost | 
        try {
            ApiResponse<Void> response = apiInstance.onPostExternalUpdatedWithHttpInfo(webhookPayloadExternalPost);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostExternalUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadExternalPost** | [**WebhookPayloadExternalPost**](WebhookPayloadExternalPost.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onPostFailed

> void onPostFailed(webhookPayloadPost)

Post failed event

Fired when a post fails to publish on all target platforms.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPost webhookPayloadPost = new WebhookPayloadPost(); // WebhookPayloadPost | 
        try {
            apiInstance.onPostFailed(webhookPayloadPost);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostFailed");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadPost** | [**WebhookPayloadPost**](WebhookPayloadPost.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onPostFailedWithHttpInfo

> ApiResponse<Void> onPostFailed onPostFailedWithHttpInfo(webhookPayloadPost)

Post failed event

Fired when a post fails to publish on all target platforms.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPost webhookPayloadPost = new WebhookPayloadPost(); // WebhookPayloadPost | 
        try {
            ApiResponse<Void> response = apiInstance.onPostFailedWithHttpInfo(webhookPayloadPost);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostFailed");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadPost** | [**WebhookPayloadPost**](WebhookPayloadPost.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onPostPartial

> void onPostPartial(webhookPayloadPost)

Post partial event

Fired when a post publishes on some platforms and fails on others.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPost webhookPayloadPost = new WebhookPayloadPost(); // WebhookPayloadPost | 
        try {
            apiInstance.onPostPartial(webhookPayloadPost);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostPartial");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadPost** | [**WebhookPayloadPost**](WebhookPayloadPost.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onPostPartialWithHttpInfo

> ApiResponse<Void> onPostPartial onPostPartialWithHttpInfo(webhookPayloadPost)

Post partial event

Fired when a post publishes on some platforms and fails on others.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPost webhookPayloadPost = new WebhookPayloadPost(); // WebhookPayloadPost | 
        try {
            ApiResponse<Void> response = apiInstance.onPostPartialWithHttpInfo(webhookPayloadPost);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostPartial");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadPost** | [**WebhookPayloadPost**](WebhookPayloadPost.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onPostPlatformDeleted

> void onPostPlatformDeleted(webhookPayloadPostPlatform)

Post platform deleted event

Fired when Zernio&#39;s background sync detects that a platform target published through Zernio was later deleted on the platform (e.g. the user deleted the Instagram post natively). Detection is poll-driven (~hourly), not real-time, and fires once per platform target. &#x60;platform.deletedAt&#x60; carries the detection time. Detection is listing-based: a false positive self-heals in Zernio&#39;s data when the post reappears, but the event is not retracted. Coverage is bounded to the posts the platform listing returns. Detection is a diff against the posts a prior sync already indexed, so an account for which no post has ever been indexed can never emit this event, no matter how the subscription is configured. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPostPlatform webhookPayloadPostPlatform = new WebhookPayloadPostPlatform(); // WebhookPayloadPostPlatform | 
        try {
            apiInstance.onPostPlatformDeleted(webhookPayloadPostPlatform);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostPlatformDeleted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadPostPlatform** | [**WebhookPayloadPostPlatform**](WebhookPayloadPostPlatform.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onPostPlatformDeletedWithHttpInfo

> ApiResponse<Void> onPostPlatformDeleted onPostPlatformDeletedWithHttpInfo(webhookPayloadPostPlatform)

Post platform deleted event

Fired when Zernio&#39;s background sync detects that a platform target published through Zernio was later deleted on the platform (e.g. the user deleted the Instagram post natively). Detection is poll-driven (~hourly), not real-time, and fires once per platform target. &#x60;platform.deletedAt&#x60; carries the detection time. Detection is listing-based: a false positive self-heals in Zernio&#39;s data when the post reappears, but the event is not retracted. Coverage is bounded to the posts the platform listing returns. Detection is a diff against the posts a prior sync already indexed, so an account for which no post has ever been indexed can never emit this event, no matter how the subscription is configured. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPostPlatform webhookPayloadPostPlatform = new WebhookPayloadPostPlatform(); // WebhookPayloadPostPlatform | 
        try {
            ApiResponse<Void> response = apiInstance.onPostPlatformDeletedWithHttpInfo(webhookPayloadPostPlatform);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostPlatformDeleted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadPostPlatform** | [**WebhookPayloadPostPlatform**](WebhookPayloadPostPlatform.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onPostPlatformFailed

> void onPostPlatformFailed(webhookPayloadPostPlatform)

Post platform failed event

Fired once per platform target inside a post as that platform fails permanently. Temporary/retryable failures do NOT fire this event, only permanent ones do, so retry loops stay quiet. The envelope event (&#x60;post.failed&#x60; / &#x60;post.partial&#x60;) fires separately AFTER all platforms have terminated. Can also fire a second time for a target that already emitted &#x60;post.platform.published&#x60;, if background reconciliation later discovers the publish never actually completed. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPostPlatform webhookPayloadPostPlatform = new WebhookPayloadPostPlatform(); // WebhookPayloadPostPlatform | 
        try {
            apiInstance.onPostPlatformFailed(webhookPayloadPostPlatform);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostPlatformFailed");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadPostPlatform** | [**WebhookPayloadPostPlatform**](WebhookPayloadPostPlatform.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onPostPlatformFailedWithHttpInfo

> ApiResponse<Void> onPostPlatformFailed onPostPlatformFailedWithHttpInfo(webhookPayloadPostPlatform)

Post platform failed event

Fired once per platform target inside a post as that platform fails permanently. Temporary/retryable failures do NOT fire this event, only permanent ones do, so retry loops stay quiet. The envelope event (&#x60;post.failed&#x60; / &#x60;post.partial&#x60;) fires separately AFTER all platforms have terminated. Can also fire a second time for a target that already emitted &#x60;post.platform.published&#x60;, if background reconciliation later discovers the publish never actually completed. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPostPlatform webhookPayloadPostPlatform = new WebhookPayloadPostPlatform(); // WebhookPayloadPostPlatform | 
        try {
            ApiResponse<Void> response = apiInstance.onPostPlatformFailedWithHttpInfo(webhookPayloadPostPlatform);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostPlatformFailed");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadPostPlatform** | [**WebhookPayloadPostPlatform**](WebhookPayloadPostPlatform.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onPostPlatformPublished

> void onPostPlatformPublished(webhookPayloadPostPlatform)

Post platform published event

Fired once per platform target inside a post as that platform finishes publishing successfully. Does NOT wait for the post-level rollup, so consumers building incremental UIs get notified immediately, even when other platforms on the same post are still processing. The envelope event (&#x60;post.published&#x60; / &#x60;post.partial&#x60;) fires separately AFTER all platforms have terminated. A target that later fails background reconciliation (e.g. a Facebook video Meta accepted but never actually published) emits &#x60;post.platform.failed&#x60; for the same target afterward. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPostPlatform webhookPayloadPostPlatform = new WebhookPayloadPostPlatform(); // WebhookPayloadPostPlatform | 
        try {
            apiInstance.onPostPlatformPublished(webhookPayloadPostPlatform);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostPlatformPublished");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadPostPlatform** | [**WebhookPayloadPostPlatform**](WebhookPayloadPostPlatform.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onPostPlatformPublishedWithHttpInfo

> ApiResponse<Void> onPostPlatformPublished onPostPlatformPublishedWithHttpInfo(webhookPayloadPostPlatform)

Post platform published event

Fired once per platform target inside a post as that platform finishes publishing successfully. Does NOT wait for the post-level rollup, so consumers building incremental UIs get notified immediately, even when other platforms on the same post are still processing. The envelope event (&#x60;post.published&#x60; / &#x60;post.partial&#x60;) fires separately AFTER all platforms have terminated. A target that later fails background reconciliation (e.g. a Facebook video Meta accepted but never actually published) emits &#x60;post.platform.failed&#x60; for the same target afterward. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPostPlatform webhookPayloadPostPlatform = new WebhookPayloadPostPlatform(); // WebhookPayloadPostPlatform | 
        try {
            ApiResponse<Void> response = apiInstance.onPostPlatformPublishedWithHttpInfo(webhookPayloadPostPlatform);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostPlatformPublished");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadPostPlatform** | [**WebhookPayloadPostPlatform**](WebhookPayloadPostPlatform.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onPostPublished

> void onPostPublished(webhookPayloadPost)

Post published event

Fired when a post is successfully published.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPost webhookPayloadPost = new WebhookPayloadPost(); // WebhookPayloadPost | 
        try {
            apiInstance.onPostPublished(webhookPayloadPost);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostPublished");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadPost** | [**WebhookPayloadPost**](WebhookPayloadPost.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onPostPublishedWithHttpInfo

> ApiResponse<Void> onPostPublished onPostPublishedWithHttpInfo(webhookPayloadPost)

Post published event

Fired when a post is successfully published.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPost webhookPayloadPost = new WebhookPayloadPost(); // WebhookPayloadPost | 
        try {
            ApiResponse<Void> response = apiInstance.onPostPublishedWithHttpInfo(webhookPayloadPost);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostPublished");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadPost** | [**WebhookPayloadPost**](WebhookPayloadPost.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onPostRecycled

> void onPostRecycled(webhookPayloadPost)

Post recycled event

Fired when a post is recycled (cloned and re-scheduled for publishing). The new clone also fires a post.scheduled event.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPost webhookPayloadPost = new WebhookPayloadPost(); // WebhookPayloadPost | 
        try {
            apiInstance.onPostRecycled(webhookPayloadPost);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostRecycled");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadPost** | [**WebhookPayloadPost**](WebhookPayloadPost.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onPostRecycledWithHttpInfo

> ApiResponse<Void> onPostRecycled onPostRecycledWithHttpInfo(webhookPayloadPost)

Post recycled event

Fired when a post is recycled (cloned and re-scheduled for publishing). The new clone also fires a post.scheduled event.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPost webhookPayloadPost = new WebhookPayloadPost(); // WebhookPayloadPost | 
        try {
            ApiResponse<Void> response = apiInstance.onPostRecycledWithHttpInfo(webhookPayloadPost);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostRecycled");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadPost** | [**WebhookPayloadPost**](WebhookPayloadPost.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onPostScheduled

> void onPostScheduled(webhookPayloadPost)

Post scheduled event

Fired whenever a post enters the scheduled state: created with a schedule, added to a queue, a draft promoted to scheduled or queued, a failed or partial post retried, or a recycled clone created. Not fired when an already-scheduled post is edited or rescheduled.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPost webhookPayloadPost = new WebhookPayloadPost(); // WebhookPayloadPost | 
        try {
            apiInstance.onPostScheduled(webhookPayloadPost);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostScheduled");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadPost** | [**WebhookPayloadPost**](WebhookPayloadPost.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onPostScheduledWithHttpInfo

> ApiResponse<Void> onPostScheduled onPostScheduledWithHttpInfo(webhookPayloadPost)

Post scheduled event

Fired whenever a post enters the scheduled state: created with a schedule, added to a queue, a draft promoted to scheduled or queued, a failed or partial post retried, or a recycled clone created. Not fired when an already-scheduled post is edited or rescheduled.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPost webhookPayloadPost = new WebhookPayloadPost(); // WebhookPayloadPost | 
        try {
            ApiResponse<Void> response = apiInstance.onPostScheduledWithHttpInfo(webhookPayloadPost);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostScheduled");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadPost** | [**WebhookPayloadPost**](WebhookPayloadPost.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onPostTikTokUrlResolved

> void onPostTikTokUrlResolved(webhookPayloadPostPlatform)

TikTok post URL resolved event

Fired when an already-published TikTok platform entry gets its public URL backfilled. TikTok exposes the numeric video id asynchronously (often minutes after PUBLISH_COMPLETE), so the terminal events can carry an empty &#x60;publishedUrl&#x60; for TikTok. This event delivers &#x60;platform.publishedUrl&#x60; and the resolved &#x60;platform.platformPostId&#x60; once available. At most once per platform target; never fires for drafts or private posts (no public URL exists). Payload shape is identical to &#x60;post.platform.published&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPostPlatform webhookPayloadPostPlatform = new WebhookPayloadPostPlatform(); // WebhookPayloadPostPlatform | 
        try {
            apiInstance.onPostTikTokUrlResolved(webhookPayloadPostPlatform);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostTikTokUrlResolved");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadPostPlatform** | [**WebhookPayloadPostPlatform**](WebhookPayloadPostPlatform.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onPostTikTokUrlResolvedWithHttpInfo

> ApiResponse<Void> onPostTikTokUrlResolved onPostTikTokUrlResolvedWithHttpInfo(webhookPayloadPostPlatform)

TikTok post URL resolved event

Fired when an already-published TikTok platform entry gets its public URL backfilled. TikTok exposes the numeric video id asynchronously (often minutes after PUBLISH_COMPLETE), so the terminal events can carry an empty &#x60;publishedUrl&#x60; for TikTok. This event delivers &#x60;platform.publishedUrl&#x60; and the resolved &#x60;platform.platformPostId&#x60; once available. At most once per platform target; never fires for drafts or private posts (no public URL exists). Payload shape is identical to &#x60;post.platform.published&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPostPlatform webhookPayloadPostPlatform = new WebhookPayloadPostPlatform(); // WebhookPayloadPostPlatform | 
        try {
            ApiResponse<Void> response = apiInstance.onPostTikTokUrlResolvedWithHttpInfo(webhookPayloadPostPlatform);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostTikTokUrlResolved");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadPostPlatform** | [**WebhookPayloadPostPlatform**](WebhookPayloadPostPlatform.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onPostTrackingCompleted

> void onPostTrackingCompleted(webhookPayloadPostTrackingCompleted)

Post tracking completed event

Fired once when a post&#39;s tracking window ends and its final analytics read has run. &#x60;final&#x60; carries the closing metrics, or null when none could be read, and &#x60;window.completionReason&#x60; is &#x60;final_read&#x60;, &#x60;unreachable&#x60; or &#x60;post_deleted&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPostTrackingCompleted webhookPayloadPostTrackingCompleted = new WebhookPayloadPostTrackingCompleted(); // WebhookPayloadPostTrackingCompleted | 
        try {
            apiInstance.onPostTrackingCompleted(webhookPayloadPostTrackingCompleted);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostTrackingCompleted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadPostTrackingCompleted** | [**WebhookPayloadPostTrackingCompleted**](WebhookPayloadPostTrackingCompleted.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onPostTrackingCompletedWithHttpInfo

> ApiResponse<Void> onPostTrackingCompleted onPostTrackingCompletedWithHttpInfo(webhookPayloadPostTrackingCompleted)

Post tracking completed event

Fired once when a post&#39;s tracking window ends and its final analytics read has run. &#x60;final&#x60; carries the closing metrics, or null when none could be read, and &#x60;window.completionReason&#x60; is &#x60;final_read&#x60;, &#x60;unreachable&#x60; or &#x60;post_deleted&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadPostTrackingCompleted webhookPayloadPostTrackingCompleted = new WebhookPayloadPostTrackingCompleted(); // WebhookPayloadPostTrackingCompleted | 
        try {
            ApiResponse<Void> response = apiInstance.onPostTrackingCompletedWithHttpInfo(webhookPayloadPostTrackingCompleted);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onPostTrackingCompleted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadPostTrackingCompleted** | [**WebhookPayloadPostTrackingCompleted**](WebhookPayloadPostTrackingCompleted.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onRcsAgentStatusUpdated

> void onRcsAgentStatusUpdated(onRcsAgentStatusUpdatedRequest)

RCS agent status updated event

Fired on every customer-visible status change of an RCS agent: &#x60;changes_requested&#x60; (we need changes before filing, &#x60;reason&#x60; is our note), &#x60;brand_vetting&#x60;, &#x60;agent_review&#x60;, &#x60;testing&#x60; (add test phones, then send the launch filing; with a &#x60;reason&#x60; the launch filing bounced), &#x60;launch_review&#x60;, &#x60;launching&#x60;, &#x60;live&#x60; (the agent can message any RCS-capable phone), &#x60;rejected&#x60; (&#x60;reason&#x60; says why) and &#x60;deactivated&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnRcsAgentStatusUpdatedRequest onRcsAgentStatusUpdatedRequest = new OnRcsAgentStatusUpdatedRequest(); // OnRcsAgentStatusUpdatedRequest | 
        try {
            apiInstance.onRcsAgentStatusUpdated(onRcsAgentStatusUpdatedRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onRcsAgentStatusUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onRcsAgentStatusUpdatedRequest** | [**OnRcsAgentStatusUpdatedRequest**](OnRcsAgentStatusUpdatedRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onRcsAgentStatusUpdatedWithHttpInfo

> ApiResponse<Void> onRcsAgentStatusUpdated onRcsAgentStatusUpdatedWithHttpInfo(onRcsAgentStatusUpdatedRequest)

RCS agent status updated event

Fired on every customer-visible status change of an RCS agent: &#x60;changes_requested&#x60; (we need changes before filing, &#x60;reason&#x60; is our note), &#x60;brand_vetting&#x60;, &#x60;agent_review&#x60;, &#x60;testing&#x60; (add test phones, then send the launch filing; with a &#x60;reason&#x60; the launch filing bounced), &#x60;launch_review&#x60;, &#x60;launching&#x60;, &#x60;live&#x60; (the agent can message any RCS-capable phone), &#x60;rejected&#x60; (&#x60;reason&#x60; says why) and &#x60;deactivated&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnRcsAgentStatusUpdatedRequest onRcsAgentStatusUpdatedRequest = new OnRcsAgentStatusUpdatedRequest(); // OnRcsAgentStatusUpdatedRequest | 
        try {
            ApiResponse<Void> response = apiInstance.onRcsAgentStatusUpdatedWithHttpInfo(onRcsAgentStatusUpdatedRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onRcsAgentStatusUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onRcsAgentStatusUpdatedRequest** | [**OnRcsAgentStatusUpdatedRequest**](OnRcsAgentStatusUpdatedRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onReactionReceived

> void onReactionReceived(webhookPayloadReaction)

Reaction received event

Fired when a participant adds or removes an emoji reaction on a message. Supported on WhatsApp, Telegram, Slack, Instagram, Facebook Messenger and TikTok. Distinct from message.received so a reaction (e.g. a thumbs-up) is not mistaken for an inbound message. On TikTok a like or emoji reaction on a DM arrives only as this event (never as an empty message.received), with &#x60;reaction.platformMessageId&#x60; set to the TikTok id of the liked message. The &#x60;reaction.action&#x60; field is &#x60;added&#x60; or &#x60;removed&#x60;. On WhatsApp and Meta removals the platform does not report which emoji was removed, so &#x60;reaction.emoji&#x60; may be an empty string. Instagram and Facebook accounts connected before reactions shipped only emit this event after their webhook subscription is refreshed; reconnect the account if reactions never arrive. Requires the Inbox add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadReaction webhookPayloadReaction = new WebhookPayloadReaction(); // WebhookPayloadReaction | 
        try {
            apiInstance.onReactionReceived(webhookPayloadReaction);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onReactionReceived");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadReaction** | [**WebhookPayloadReaction**](WebhookPayloadReaction.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onReactionReceivedWithHttpInfo

> ApiResponse<Void> onReactionReceived onReactionReceivedWithHttpInfo(webhookPayloadReaction)

Reaction received event

Fired when a participant adds or removes an emoji reaction on a message. Supported on WhatsApp, Telegram, Slack, Instagram, Facebook Messenger and TikTok. Distinct from message.received so a reaction (e.g. a thumbs-up) is not mistaken for an inbound message. On TikTok a like or emoji reaction on a DM arrives only as this event (never as an empty message.received), with &#x60;reaction.platformMessageId&#x60; set to the TikTok id of the liked message. The &#x60;reaction.action&#x60; field is &#x60;added&#x60; or &#x60;removed&#x60;. On WhatsApp and Meta removals the platform does not report which emoji was removed, so &#x60;reaction.emoji&#x60; may be an empty string. Instagram and Facebook accounts connected before reactions shipped only emit this event after their webhook subscription is refreshed; reconnect the account if reactions never arrive. Requires the Inbox add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadReaction webhookPayloadReaction = new WebhookPayloadReaction(); // WebhookPayloadReaction | 
        try {
            ApiResponse<Void> response = apiInstance.onReactionReceivedWithHttpInfo(webhookPayloadReaction);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onReactionReceived");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadReaction** | [**WebhookPayloadReaction**](WebhookPayloadReaction.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onReferralReceived

> void onReferralReceived(webhookPayloadReferral)

Referral received event

Fired when someone opens an EXISTING Instagram or Messenger thread through an attributable entry point - an ig.me / m.me link with a &#x60;ref&#x60; parameter, or (Messenger) a returning Click-to-Message ad click - which Meta delivers as a standalone referral with no message attached. A referral that rides an inbound message (first message of a thread, icebreaker taps, returning ad clicks on Instagram) arrives on &#x60;message.received&#x60; under &#x60;metadata.referral&#x60; instead; the two never fire for the same click. The first referral captured on a conversation is also persisted on it (see &#x60;metadata&#x60; on &#x60;GET /v1/inbox/conversations&#x60;). Requires the Inbox add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadReferral webhookPayloadReferral = new WebhookPayloadReferral(); // WebhookPayloadReferral | 
        try {
            apiInstance.onReferralReceived(webhookPayloadReferral);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onReferralReceived");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadReferral** | [**WebhookPayloadReferral**](WebhookPayloadReferral.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onReferralReceivedWithHttpInfo

> ApiResponse<Void> onReferralReceived onReferralReceivedWithHttpInfo(webhookPayloadReferral)

Referral received event

Fired when someone opens an EXISTING Instagram or Messenger thread through an attributable entry point - an ig.me / m.me link with a &#x60;ref&#x60; parameter, or (Messenger) a returning Click-to-Message ad click - which Meta delivers as a standalone referral with no message attached. A referral that rides an inbound message (first message of a thread, icebreaker taps, returning ad clicks on Instagram) arrives on &#x60;message.received&#x60; under &#x60;metadata.referral&#x60; instead; the two never fire for the same click. The first referral captured on a conversation is also persisted on it (see &#x60;metadata&#x60; on &#x60;GET /v1/inbox/conversations&#x60;). Requires the Inbox add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadReferral webhookPayloadReferral = new WebhookPayloadReferral(); // WebhookPayloadReferral | 
        try {
            ApiResponse<Void> response = apiInstance.onReferralReceivedWithHttpInfo(webhookPayloadReferral);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onReferralReceived");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadReferral** | [**WebhookPayloadReferral**](WebhookPayloadReferral.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onReviewNew

> void onReviewNew(webhookPayloadReviewNew)

Review new event

Fired when a new review is posted on a connected account. Currently supported for Google Business Profile (real-time via Pub/Sub). Requires the Inbox add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadReviewNew webhookPayloadReviewNew = new WebhookPayloadReviewNew(); // WebhookPayloadReviewNew | 
        try {
            apiInstance.onReviewNew(webhookPayloadReviewNew);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onReviewNew");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadReviewNew** | [**WebhookPayloadReviewNew**](WebhookPayloadReviewNew.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onReviewNewWithHttpInfo

> ApiResponse<Void> onReviewNew onReviewNewWithHttpInfo(webhookPayloadReviewNew)

Review new event

Fired when a new review is posted on a connected account. Currently supported for Google Business Profile (real-time via Pub/Sub). Requires the Inbox add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadReviewNew webhookPayloadReviewNew = new WebhookPayloadReviewNew(); // WebhookPayloadReviewNew | 
        try {
            ApiResponse<Void> response = apiInstance.onReviewNewWithHttpInfo(webhookPayloadReviewNew);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onReviewNew");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadReviewNew** | [**WebhookPayloadReviewNew**](WebhookPayloadReviewNew.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onReviewUpdated

> void onReviewUpdated(webhookPayloadReviewUpdated)

Review updated event

Fired when a Google Business Profile reviewer edits their review text or rating, or when a reply is posted through POST /v1/inbox/reviews/{reviewId}/reply. A reply written directly in Google&#39;s own interface does NOT fire this event, because Google emits no notification for it. Payload shape matches review.new. Requires the Inbox add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadReviewUpdated webhookPayloadReviewUpdated = new WebhookPayloadReviewUpdated(); // WebhookPayloadReviewUpdated | 
        try {
            apiInstance.onReviewUpdated(webhookPayloadReviewUpdated);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onReviewUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadReviewUpdated** | [**WebhookPayloadReviewUpdated**](WebhookPayloadReviewUpdated.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onReviewUpdatedWithHttpInfo

> ApiResponse<Void> onReviewUpdated onReviewUpdatedWithHttpInfo(webhookPayloadReviewUpdated)

Review updated event

Fired when a Google Business Profile reviewer edits their review text or rating, or when a reply is posted through POST /v1/inbox/reviews/{reviewId}/reply. A reply written directly in Google&#39;s own interface does NOT fire this event, because Google emits no notification for it. Payload shape matches review.new. Requires the Inbox add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadReviewUpdated webhookPayloadReviewUpdated = new WebhookPayloadReviewUpdated(); // WebhookPayloadReviewUpdated | 
        try {
            ApiResponse<Void> response = apiInstance.onReviewUpdatedWithHttpInfo(webhookPayloadReviewUpdated);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onReviewUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadReviewUpdated** | [**WebhookPayloadReviewUpdated**](WebhookPayloadReviewUpdated.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onSequenceEnrolled

> void onSequenceEnrolled(webhookPayloadSequenceEnrollment)

Sequence enrolled event

Fired when a contact is enrolled in a sequence.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadSequenceEnrollment webhookPayloadSequenceEnrollment = new WebhookPayloadSequenceEnrollment(); // WebhookPayloadSequenceEnrollment | 
        try {
            apiInstance.onSequenceEnrolled(webhookPayloadSequenceEnrollment);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onSequenceEnrolled");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadSequenceEnrollment** | [**WebhookPayloadSequenceEnrollment**](WebhookPayloadSequenceEnrollment.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onSequenceEnrolledWithHttpInfo

> ApiResponse<Void> onSequenceEnrolled onSequenceEnrolledWithHttpInfo(webhookPayloadSequenceEnrollment)

Sequence enrolled event

Fired when a contact is enrolled in a sequence.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadSequenceEnrollment webhookPayloadSequenceEnrollment = new WebhookPayloadSequenceEnrollment(); // WebhookPayloadSequenceEnrollment | 
        try {
            ApiResponse<Void> response = apiInstance.onSequenceEnrolledWithHttpInfo(webhookPayloadSequenceEnrollment);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onSequenceEnrolled");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadSequenceEnrollment** | [**WebhookPayloadSequenceEnrollment**](WebhookPayloadSequenceEnrollment.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onSequenceExited

> void onSequenceExited(webhookPayloadSequenceEnrollment)

Sequence exited event

Fired when a contact leaves a sequence, finished or not; exitReason says why.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadSequenceEnrollment webhookPayloadSequenceEnrollment = new WebhookPayloadSequenceEnrollment(); // WebhookPayloadSequenceEnrollment | 
        try {
            apiInstance.onSequenceExited(webhookPayloadSequenceEnrollment);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onSequenceExited");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadSequenceEnrollment** | [**WebhookPayloadSequenceEnrollment**](WebhookPayloadSequenceEnrollment.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onSequenceExitedWithHttpInfo

> ApiResponse<Void> onSequenceExited onSequenceExitedWithHttpInfo(webhookPayloadSequenceEnrollment)

Sequence exited event

Fired when a contact leaves a sequence, finished or not; exitReason says why.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadSequenceEnrollment webhookPayloadSequenceEnrollment = new WebhookPayloadSequenceEnrollment(); // WebhookPayloadSequenceEnrollment | 
        try {
            ApiResponse<Void> response = apiInstance.onSequenceExitedWithHttpInfo(webhookPayloadSequenceEnrollment);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onSequenceExited");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadSequenceEnrollment** | [**WebhookPayloadSequenceEnrollment**](WebhookPayloadSequenceEnrollment.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onSmsRegistrationActionRequired

> void onSmsRegistrationActionRequired(onSmsRegistrationActionRequiredRequest)

SMS registration action required event

Fired when an SMS registration starts waiting on its owner. &#x60;reason&#x60; says why: &#x60;changes_requested&#x60; (we need answers to some points, before submission or to fix a carrier rejection; &#x60;message&#x60; is the request, answer with POST /v1/sms/registrations/{id}/respond), &#x60;otp_required&#x60; (a sole-proprietor brand needs the code texted to its mobile, submit it with POST /v1/sms/registrations/{id}/verify-otp) or &#x60;carrier_info_required&#x60; (the toll-free carrier asked for more information; the request expires after 7 days). A carrier rejection alone does not fire it: we handle the fix, see &#x60;sms.registration.status_updated&#x60;. Fires once per new request (not on follow-up messages) and once per OTP or carrier request. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnSmsRegistrationActionRequiredRequest onSmsRegistrationActionRequiredRequest = new OnSmsRegistrationActionRequiredRequest(); // OnSmsRegistrationActionRequiredRequest | 
        try {
            apiInstance.onSmsRegistrationActionRequired(onSmsRegistrationActionRequiredRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onSmsRegistrationActionRequired");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onSmsRegistrationActionRequiredRequest** | [**OnSmsRegistrationActionRequiredRequest**](OnSmsRegistrationActionRequiredRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onSmsRegistrationActionRequiredWithHttpInfo

> ApiResponse<Void> onSmsRegistrationActionRequired onSmsRegistrationActionRequiredWithHttpInfo(onSmsRegistrationActionRequiredRequest)

SMS registration action required event

Fired when an SMS registration starts waiting on its owner. &#x60;reason&#x60; says why: &#x60;changes_requested&#x60; (we need answers to some points, before submission or to fix a carrier rejection; &#x60;message&#x60; is the request, answer with POST /v1/sms/registrations/{id}/respond), &#x60;otp_required&#x60; (a sole-proprietor brand needs the code texted to its mobile, submit it with POST /v1/sms/registrations/{id}/verify-otp) or &#x60;carrier_info_required&#x60; (the toll-free carrier asked for more information; the request expires after 7 days). A carrier rejection alone does not fire it: we handle the fix, see &#x60;sms.registration.status_updated&#x60;. Fires once per new request (not on follow-up messages) and once per OTP or carrier request. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnSmsRegistrationActionRequiredRequest onSmsRegistrationActionRequiredRequest = new OnSmsRegistrationActionRequiredRequest(); // OnSmsRegistrationActionRequiredRequest | 
        try {
            ApiResponse<Void> response = apiInstance.onSmsRegistrationActionRequiredWithHttpInfo(onSmsRegistrationActionRequiredRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onSmsRegistrationActionRequired");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onSmsRegistrationActionRequiredRequest** | [**OnSmsRegistrationActionRequiredRequest**](OnSmsRegistrationActionRequiredRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onSmsRegistrationStatusUpdated

> void onSmsRegistrationStatusUpdated(onSmsRegistrationStatusUpdatedRequest)

SMS registration status updated event

Fired on every status change of an SMS registration: &#x60;changes_requested&#x60; (we need answers, see &#x60;sms.registration.action_required&#x60;), &#x60;requested&#x60; (a new submission or resubmit, or your answers are back in our review), &#x60;pending&#x60; (with the carriers, including after we fixed and resent a rejection), &#x60;approved&#x60; (live: attach numbers and send), &#x60;rejected&#x60; (the carriers declined it; &#x60;reason&#x60; is their words and we handle the fix) and &#x60;deactivated&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnSmsRegistrationStatusUpdatedRequest onSmsRegistrationStatusUpdatedRequest = new OnSmsRegistrationStatusUpdatedRequest(); // OnSmsRegistrationStatusUpdatedRequest | 
        try {
            apiInstance.onSmsRegistrationStatusUpdated(onSmsRegistrationStatusUpdatedRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onSmsRegistrationStatusUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onSmsRegistrationStatusUpdatedRequest** | [**OnSmsRegistrationStatusUpdatedRequest**](OnSmsRegistrationStatusUpdatedRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onSmsRegistrationStatusUpdatedWithHttpInfo

> ApiResponse<Void> onSmsRegistrationStatusUpdated onSmsRegistrationStatusUpdatedWithHttpInfo(onSmsRegistrationStatusUpdatedRequest)

SMS registration status updated event

Fired on every status change of an SMS registration: &#x60;changes_requested&#x60; (we need answers, see &#x60;sms.registration.action_required&#x60;), &#x60;requested&#x60; (a new submission or resubmit, or your answers are back in our review), &#x60;pending&#x60; (with the carriers, including after we fixed and resent a rejection), &#x60;approved&#x60; (live: attach numbers and send), &#x60;rejected&#x60; (the carriers declined it; &#x60;reason&#x60; is their words and we handle the fix) and &#x60;deactivated&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnSmsRegistrationStatusUpdatedRequest onSmsRegistrationStatusUpdatedRequest = new OnSmsRegistrationStatusUpdatedRequest(); // OnSmsRegistrationStatusUpdatedRequest | 
        try {
            ApiResponse<Void> response = apiInstance.onSmsRegistrationStatusUpdatedWithHttpInfo(onSmsRegistrationStatusUpdatedRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onSmsRegistrationStatusUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onSmsRegistrationStatusUpdatedRequest** | [**OnSmsRegistrationStatusUpdatedRequest**](OnSmsRegistrationStatusUpdatedRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onSupportRunCompleted

> void onSupportRunCompleted(webhookPayloadSupportRun)

Support Assistant finished event

Fired when the Support Assistant finishes a question. run.status is completed, or needs_human when the assistant handed the question to a person. The run object matches GET /v1/support/runs/{runId}.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadSupportRun webhookPayloadSupportRun = new WebhookPayloadSupportRun(); // WebhookPayloadSupportRun | 
        try {
            apiInstance.onSupportRunCompleted(webhookPayloadSupportRun);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onSupportRunCompleted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadSupportRun** | [**WebhookPayloadSupportRun**](WebhookPayloadSupportRun.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onSupportRunCompletedWithHttpInfo

> ApiResponse<Void> onSupportRunCompleted onSupportRunCompletedWithHttpInfo(webhookPayloadSupportRun)

Support Assistant finished event

Fired when the Support Assistant finishes a question. run.status is completed, or needs_human when the assistant handed the question to a person. The run object matches GET /v1/support/runs/{runId}.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadSupportRun webhookPayloadSupportRun = new WebhookPayloadSupportRun(); // WebhookPayloadSupportRun | 
        try {
            ApiResponse<Void> response = apiInstance.onSupportRunCompletedWithHttpInfo(webhookPayloadSupportRun);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onSupportRunCompleted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadSupportRun** | [**WebhookPayloadSupportRun**](WebhookPayloadSupportRun.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onSupportRunFailed

> void onSupportRunFailed(webhookPayloadSupportRun)

Support Assistant failed event

Fired when a Support Assistant question fails or expires. Failed runs are not billed.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadSupportRun webhookPayloadSupportRun = new WebhookPayloadSupportRun(); // WebhookPayloadSupportRun | 
        try {
            apiInstance.onSupportRunFailed(webhookPayloadSupportRun);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onSupportRunFailed");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadSupportRun** | [**WebhookPayloadSupportRun**](WebhookPayloadSupportRun.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onSupportRunFailedWithHttpInfo

> ApiResponse<Void> onSupportRunFailed onSupportRunFailedWithHttpInfo(webhookPayloadSupportRun)

Support Assistant failed event

Fired when a Support Assistant question fails or expires. Failed runs are not billed.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadSupportRun webhookPayloadSupportRun = new WebhookPayloadSupportRun(); // WebhookPayloadSupportRun | 
        try {
            ApiResponse<Void> response = apiInstance.onSupportRunFailedWithHttpInfo(webhookPayloadSupportRun);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onSupportRunFailed");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadSupportRun** | [**WebhookPayloadSupportRun**](WebhookPayloadSupportRun.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onVerificationApproved

> void onVerificationApproved(onVerificationApprovedRequest)

Verification approved event

Fired when a managed-OTP verification is approved (the user submitted the correct code to POST /v1/verify/verifications/{verificationId}/check). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnVerificationApprovedRequest onVerificationApprovedRequest = new OnVerificationApprovedRequest(); // OnVerificationApprovedRequest | 
        try {
            apiInstance.onVerificationApproved(onVerificationApprovedRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onVerificationApproved");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onVerificationApprovedRequest** | [**OnVerificationApprovedRequest**](OnVerificationApprovedRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onVerificationApprovedWithHttpInfo

> ApiResponse<Void> onVerificationApproved onVerificationApprovedWithHttpInfo(onVerificationApprovedRequest)

Verification approved event

Fired when a managed-OTP verification is approved (the user submitted the correct code to POST /v1/verify/verifications/{verificationId}/check). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnVerificationApprovedRequest onVerificationApprovedRequest = new OnVerificationApprovedRequest(); // OnVerificationApprovedRequest | 
        try {
            ApiResponse<Void> response = apiInstance.onVerificationApprovedWithHttpInfo(onVerificationApprovedRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onVerificationApproved");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onVerificationApprovedRequest** | [**OnVerificationApprovedRequest**](OnVerificationApprovedRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onVerificationFailed

> void onVerificationFailed(onVerificationFailedRequest)

Verification failed event

Fired when a managed-OTP verification is exhausted (the maximum number of wrong code attempts was reached). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnVerificationFailedRequest onVerificationFailedRequest = new OnVerificationFailedRequest(); // OnVerificationFailedRequest | 
        try {
            apiInstance.onVerificationFailed(onVerificationFailedRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onVerificationFailed");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onVerificationFailedRequest** | [**OnVerificationFailedRequest**](OnVerificationFailedRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onVerificationFailedWithHttpInfo

> ApiResponse<Void> onVerificationFailed onVerificationFailedWithHttpInfo(onVerificationFailedRequest)

Verification failed event

Fired when a managed-OTP verification is exhausted (the maximum number of wrong code attempts was reached). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnVerificationFailedRequest onVerificationFailedRequest = new OnVerificationFailedRequest(); // OnVerificationFailedRequest | 
        try {
            ApiResponse<Void> response = apiInstance.onVerificationFailedWithHttpInfo(onVerificationFailedRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onVerificationFailed");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onVerificationFailedRequest** | [**OnVerificationFailedRequest**](OnVerificationFailedRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onWebhookTest

> void onWebhookTest(webhookPayloadTest)

Webhook test event

Fired when sending a test webhook to verify the endpoint configuration.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadTest webhookPayloadTest = new WebhookPayloadTest(); // WebhookPayloadTest | 
        try {
            apiInstance.onWebhookTest(webhookPayloadTest);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWebhookTest");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadTest** | [**WebhookPayloadTest**](WebhookPayloadTest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onWebhookTestWithHttpInfo

> ApiResponse<Void> onWebhookTest onWebhookTestWithHttpInfo(webhookPayloadTest)

Webhook test event

Fired when sending a test webhook to verify the endpoint configuration.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadTest webhookPayloadTest = new WebhookPayloadTest(); // WebhookPayloadTest | 
        try {
            ApiResponse<Void> response = apiInstance.onWebhookTestWithHttpInfo(webhookPayloadTest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWebhookTest");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadTest** | [**WebhookPayloadTest**](WebhookPayloadTest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onWhatsAppAccountAlertReceived

> void onWhatsAppAccountAlertReceived(webhookPayloadWhatsAppAccountAlertReceived)

WhatsApp account alert received

Fired for each Meta &#x60;account_alerts&#x60; notification on a connected WhatsApp Business Account. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadWhatsAppAccountAlertReceived webhookPayloadWhatsAppAccountAlertReceived = new WebhookPayloadWhatsAppAccountAlertReceived(); // WebhookPayloadWhatsAppAccountAlertReceived | 
        try {
            apiInstance.onWhatsAppAccountAlertReceived(webhookPayloadWhatsAppAccountAlertReceived);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppAccountAlertReceived");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadWhatsAppAccountAlertReceived** | [**WebhookPayloadWhatsAppAccountAlertReceived**](WebhookPayloadWhatsAppAccountAlertReceived.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onWhatsAppAccountAlertReceivedWithHttpInfo

> ApiResponse<Void> onWhatsAppAccountAlertReceived onWhatsAppAccountAlertReceivedWithHttpInfo(webhookPayloadWhatsAppAccountAlertReceived)

WhatsApp account alert received

Fired for each Meta &#x60;account_alerts&#x60; notification on a connected WhatsApp Business Account. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadWhatsAppAccountAlertReceived webhookPayloadWhatsAppAccountAlertReceived = new WebhookPayloadWhatsAppAccountAlertReceived(); // WebhookPayloadWhatsAppAccountAlertReceived | 
        try {
            ApiResponse<Void> response = apiInstance.onWhatsAppAccountAlertReceivedWithHttpInfo(webhookPayloadWhatsAppAccountAlertReceived);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppAccountAlertReceived");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadWhatsAppAccountAlertReceived** | [**WebhookPayloadWhatsAppAccountAlertReceived**](WebhookPayloadWhatsAppAccountAlertReceived.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onWhatsAppAccountNameStatusUpdated

> void onWhatsAppAccountNameStatusUpdated(webhookPayloadWhatsAppAccountNameStatusUpdated)

WhatsApp display-name review outcome event

Fired when Meta finishes reviewing a WhatsApp Business display-name change. Forwarded from Meta&#39;s &#x60;phone_number_name_update&#x60; webhook field on the WhatsApp Business Account. Fires only on a review outcome (&#x60;name.status&#x60; APPROVED, DECLINED, or PENDING_REVIEW); a name applied without review reports &#x60;name_status: AVAILABLE_WITHOUT_REVIEW&#x60; on the phone node instead and produces no event here. &#x60;decision&#x60; REJECTED maps to DECLINED and DEFERRED maps to PENDING_REVIEW, matching the &#x60;name_status&#x60; vocabulary returned by &#x60;GET /v1/whatsapp/number-info&#x60;. Delivery is at-least-once; dedupe on &#x60;(account.accountId, name.status, name.requestedName)&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadWhatsAppAccountNameStatusUpdated webhookPayloadWhatsAppAccountNameStatusUpdated = new WebhookPayloadWhatsAppAccountNameStatusUpdated(); // WebhookPayloadWhatsAppAccountNameStatusUpdated | 
        try {
            apiInstance.onWhatsAppAccountNameStatusUpdated(webhookPayloadWhatsAppAccountNameStatusUpdated);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppAccountNameStatusUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadWhatsAppAccountNameStatusUpdated** | [**WebhookPayloadWhatsAppAccountNameStatusUpdated**](WebhookPayloadWhatsAppAccountNameStatusUpdated.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onWhatsAppAccountNameStatusUpdatedWithHttpInfo

> ApiResponse<Void> onWhatsAppAccountNameStatusUpdated onWhatsAppAccountNameStatusUpdatedWithHttpInfo(webhookPayloadWhatsAppAccountNameStatusUpdated)

WhatsApp display-name review outcome event

Fired when Meta finishes reviewing a WhatsApp Business display-name change. Forwarded from Meta&#39;s &#x60;phone_number_name_update&#x60; webhook field on the WhatsApp Business Account. Fires only on a review outcome (&#x60;name.status&#x60; APPROVED, DECLINED, or PENDING_REVIEW); a name applied without review reports &#x60;name_status: AVAILABLE_WITHOUT_REVIEW&#x60; on the phone node instead and produces no event here. &#x60;decision&#x60; REJECTED maps to DECLINED and DEFERRED maps to PENDING_REVIEW, matching the &#x60;name_status&#x60; vocabulary returned by &#x60;GET /v1/whatsapp/number-info&#x60;. Delivery is at-least-once; dedupe on &#x60;(account.accountId, name.status, name.requestedName)&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadWhatsAppAccountNameStatusUpdated webhookPayloadWhatsAppAccountNameStatusUpdated = new WebhookPayloadWhatsAppAccountNameStatusUpdated(); // WebhookPayloadWhatsAppAccountNameStatusUpdated | 
        try {
            ApiResponse<Void> response = apiInstance.onWhatsAppAccountNameStatusUpdatedWithHttpInfo(webhookPayloadWhatsAppAccountNameStatusUpdated);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppAccountNameStatusUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadWhatsAppAccountNameStatusUpdated** | [**WebhookPayloadWhatsAppAccountNameStatusUpdated**](WebhookPayloadWhatsAppAccountNameStatusUpdated.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onWhatsAppAccountQualityUpdated

> void onWhatsAppAccountQualityUpdated(webhookPayloadWhatsAppAccountQualityUpdated)

WhatsApp quality rating or messaging limit changed

Fired when a connected WhatsApp number&#39;s quality rating or messaging limit tier changes. Delivery is at-least-once; dedupe on the event &#x60;id&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadWhatsAppAccountQualityUpdated webhookPayloadWhatsAppAccountQualityUpdated = new WebhookPayloadWhatsAppAccountQualityUpdated(); // WebhookPayloadWhatsAppAccountQualityUpdated | 
        try {
            apiInstance.onWhatsAppAccountQualityUpdated(webhookPayloadWhatsAppAccountQualityUpdated);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppAccountQualityUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadWhatsAppAccountQualityUpdated** | [**WebhookPayloadWhatsAppAccountQualityUpdated**](WebhookPayloadWhatsAppAccountQualityUpdated.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onWhatsAppAccountQualityUpdatedWithHttpInfo

> ApiResponse<Void> onWhatsAppAccountQualityUpdated onWhatsAppAccountQualityUpdatedWithHttpInfo(webhookPayloadWhatsAppAccountQualityUpdated)

WhatsApp quality rating or messaging limit changed

Fired when a connected WhatsApp number&#39;s quality rating or messaging limit tier changes. Delivery is at-least-once; dedupe on the event &#x60;id&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadWhatsAppAccountQualityUpdated webhookPayloadWhatsAppAccountQualityUpdated = new WebhookPayloadWhatsAppAccountQualityUpdated(); // WebhookPayloadWhatsAppAccountQualityUpdated | 
        try {
            ApiResponse<Void> response = apiInstance.onWhatsAppAccountQualityUpdatedWithHttpInfo(webhookPayloadWhatsAppAccountQualityUpdated);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppAccountQualityUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadWhatsAppAccountQualityUpdated** | [**WebhookPayloadWhatsAppAccountQualityUpdated**](WebhookPayloadWhatsAppAccountQualityUpdated.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onWhatsAppAccountStatusUpdated

> void onWhatsAppAccountStatusUpdated(webhookPayloadWhatsAppAccountStatusUpdated)

WhatsApp Business Account restricted or reinstated

Fired when Meta restricts, disables, deletes or reinstates the WhatsApp Business Account, once per connected number on it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadWhatsAppAccountStatusUpdated webhookPayloadWhatsAppAccountStatusUpdated = new WebhookPayloadWhatsAppAccountStatusUpdated(); // WebhookPayloadWhatsAppAccountStatusUpdated | 
        try {
            apiInstance.onWhatsAppAccountStatusUpdated(webhookPayloadWhatsAppAccountStatusUpdated);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppAccountStatusUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadWhatsAppAccountStatusUpdated** | [**WebhookPayloadWhatsAppAccountStatusUpdated**](WebhookPayloadWhatsAppAccountStatusUpdated.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onWhatsAppAccountStatusUpdatedWithHttpInfo

> ApiResponse<Void> onWhatsAppAccountStatusUpdated onWhatsAppAccountStatusUpdatedWithHttpInfo(webhookPayloadWhatsAppAccountStatusUpdated)

WhatsApp Business Account restricted or reinstated

Fired when Meta restricts, disables, deletes or reinstates the WhatsApp Business Account, once per connected number on it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadWhatsAppAccountStatusUpdated webhookPayloadWhatsAppAccountStatusUpdated = new WebhookPayloadWhatsAppAccountStatusUpdated(); // WebhookPayloadWhatsAppAccountStatusUpdated | 
        try {
            ApiResponse<Void> response = apiInstance.onWhatsAppAccountStatusUpdatedWithHttpInfo(webhookPayloadWhatsAppAccountStatusUpdated);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppAccountStatusUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadWhatsAppAccountStatusUpdated** | [**WebhookPayloadWhatsAppAccountStatusUpdated**](WebhookPayloadWhatsAppAccountStatusUpdated.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onWhatsAppAutomaticEvent

> void onWhatsAppAutomaticEvent(onWhatsAppAutomaticEventRequest)

WhatsApp automatic event detected

Fired when Meta&#39;s automatic event identification (opt-in during Embedded Signup; not available for EU/UK/JP businesses) detects a lead or purchase in a Click-to-WhatsApp conversation. Branch on &#x60;eventName&#x60; (&#x60;LeadSubmitted&#x60; | &#x60;Purchase&#x60;). Carries the &#x60;ctwa_clid&#x60;. Meta omits that clid on a minority of referrals on any number (coexistence or not, most often WhatsApp Status placements); when it does, this event can supply it and Zernio writes it back onto the conversation, so POST /v1/whatsapp/conversions becomes usable for the thread. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppAutomaticEventRequest onWhatsAppAutomaticEventRequest = new OnWhatsAppAutomaticEventRequest(); // OnWhatsAppAutomaticEventRequest | 
        try {
            apiInstance.onWhatsAppAutomaticEvent(onWhatsAppAutomaticEventRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppAutomaticEvent");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onWhatsAppAutomaticEventRequest** | [**OnWhatsAppAutomaticEventRequest**](OnWhatsAppAutomaticEventRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onWhatsAppAutomaticEventWithHttpInfo

> ApiResponse<Void> onWhatsAppAutomaticEvent onWhatsAppAutomaticEventWithHttpInfo(onWhatsAppAutomaticEventRequest)

WhatsApp automatic event detected

Fired when Meta&#39;s automatic event identification (opt-in during Embedded Signup; not available for EU/UK/JP businesses) detects a lead or purchase in a Click-to-WhatsApp conversation. Branch on &#x60;eventName&#x60; (&#x60;LeadSubmitted&#x60; | &#x60;Purchase&#x60;). Carries the &#x60;ctwa_clid&#x60;. Meta omits that clid on a minority of referrals on any number (coexistence or not, most often WhatsApp Status placements); when it does, this event can supply it and Zernio writes it back onto the conversation, so POST /v1/whatsapp/conversions becomes usable for the thread. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppAutomaticEventRequest onWhatsAppAutomaticEventRequest = new OnWhatsAppAutomaticEventRequest(); // OnWhatsAppAutomaticEventRequest | 
        try {
            ApiResponse<Void> response = apiInstance.onWhatsAppAutomaticEventWithHttpInfo(onWhatsAppAutomaticEventRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppAutomaticEvent");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onWhatsAppAutomaticEventRequest** | [**OnWhatsAppAutomaticEventRequest**](OnWhatsAppAutomaticEventRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onWhatsAppContactIdentityChanged

> void onWhatsAppContactIdentityChanged(webhookPayloadWhatsAppContactIdentityChanged)

WhatsApp contact identity changed event

Fired when a WhatsApp user changes phone number or Meta regenerates their business-scoped user id (BSUID). Carries the previous and current identifiers so you can re-key records stored against the old phone number or BSUID. Delivery is at-least-once; dedupe on the event &#x60;id&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadWhatsAppContactIdentityChanged webhookPayloadWhatsAppContactIdentityChanged = new WebhookPayloadWhatsAppContactIdentityChanged(); // WebhookPayloadWhatsAppContactIdentityChanged | 
        try {
            apiInstance.onWhatsAppContactIdentityChanged(webhookPayloadWhatsAppContactIdentityChanged);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppContactIdentityChanged");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadWhatsAppContactIdentityChanged** | [**WebhookPayloadWhatsAppContactIdentityChanged**](WebhookPayloadWhatsAppContactIdentityChanged.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onWhatsAppContactIdentityChangedWithHttpInfo

> ApiResponse<Void> onWhatsAppContactIdentityChanged onWhatsAppContactIdentityChangedWithHttpInfo(webhookPayloadWhatsAppContactIdentityChanged)

WhatsApp contact identity changed event

Fired when a WhatsApp user changes phone number or Meta regenerates their business-scoped user id (BSUID). Carries the previous and current identifiers so you can re-key records stored against the old phone number or BSUID. Delivery is at-least-once; dedupe on the event &#x60;id&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadWhatsAppContactIdentityChanged webhookPayloadWhatsAppContactIdentityChanged = new WebhookPayloadWhatsAppContactIdentityChanged(); // WebhookPayloadWhatsAppContactIdentityChanged | 
        try {
            ApiResponse<Void> response = apiInstance.onWhatsAppContactIdentityChangedWithHttpInfo(webhookPayloadWhatsAppContactIdentityChanged);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppContactIdentityChanged");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadWhatsAppContactIdentityChanged** | [**WebhookPayloadWhatsAppContactIdentityChanged**](WebhookPayloadWhatsAppContactIdentityChanged.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onWhatsAppNumberActionRequired

> void onWhatsAppNumberActionRequired(onWhatsAppNumberActionRequiredRequest)

WhatsApp number action required event

Fired when the regulator asks for more information on an already-placed regulated number order. The number stays pending (nothing was rejected); the customer can provide the missing information from the dashboard, or via the remediation endpoint. &#x60;reason&#x60; carries the regulator&#39;s request verbatim when available. &#x60;requirements&#x60; lists every requirement on the order with the reviewer&#39;s current verdict; the &#x60;declined&#x60; ones are what to fix, keyed by the same &#x60;requirementId&#x60; the remediation endpoint uses. Verdicts only change when a reviewer acts, so they describe the review at &#x60;reviewedAt&#x60;, the time of the reviewer&#39;s last comment. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppNumberActionRequiredRequest onWhatsAppNumberActionRequiredRequest = new OnWhatsAppNumberActionRequiredRequest(); // OnWhatsAppNumberActionRequiredRequest | 
        try {
            apiInstance.onWhatsAppNumberActionRequired(onWhatsAppNumberActionRequiredRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppNumberActionRequired");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onWhatsAppNumberActionRequiredRequest** | [**OnWhatsAppNumberActionRequiredRequest**](OnWhatsAppNumberActionRequiredRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onWhatsAppNumberActionRequiredWithHttpInfo

> ApiResponse<Void> onWhatsAppNumberActionRequired onWhatsAppNumberActionRequiredWithHttpInfo(onWhatsAppNumberActionRequiredRequest)

WhatsApp number action required event

Fired when the regulator asks for more information on an already-placed regulated number order. The number stays pending (nothing was rejected); the customer can provide the missing information from the dashboard, or via the remediation endpoint. &#x60;reason&#x60; carries the regulator&#39;s request verbatim when available. &#x60;requirements&#x60; lists every requirement on the order with the reviewer&#39;s current verdict; the &#x60;declined&#x60; ones are what to fix, keyed by the same &#x60;requirementId&#x60; the remediation endpoint uses. Verdicts only change when a reviewer acts, so they describe the review at &#x60;reviewedAt&#x60;, the time of the reviewer&#39;s last comment. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppNumberActionRequiredRequest onWhatsAppNumberActionRequiredRequest = new OnWhatsAppNumberActionRequiredRequest(); // OnWhatsAppNumberActionRequiredRequest | 
        try {
            ApiResponse<Void> response = apiInstance.onWhatsAppNumberActionRequiredWithHttpInfo(onWhatsAppNumberActionRequiredRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppNumberActionRequired");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onWhatsAppNumberActionRequiredRequest** | [**OnWhatsAppNumberActionRequiredRequest**](OnWhatsAppNumberActionRequiredRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onWhatsAppNumberActivated

> void onWhatsAppNumberActivated(onWhatsAppNumberActivatedRequest)

WhatsApp number activated event

Fired when a purchased WhatsApp number becomes active and usable. Both the synchronous (Tier 1/2) path and the asynchronous regulated (Tier 3/4) path land here. Lets integrators react without polling GET /v1/phone-numbers. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppNumberActivatedRequest onWhatsAppNumberActivatedRequest = new OnWhatsAppNumberActivatedRequest(); // OnWhatsAppNumberActivatedRequest | 
        try {
            apiInstance.onWhatsAppNumberActivated(onWhatsAppNumberActivatedRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppNumberActivated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onWhatsAppNumberActivatedRequest** | [**OnWhatsAppNumberActivatedRequest**](OnWhatsAppNumberActivatedRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onWhatsAppNumberActivatedWithHttpInfo

> ApiResponse<Void> onWhatsAppNumberActivated onWhatsAppNumberActivatedWithHttpInfo(onWhatsAppNumberActivatedRequest)

WhatsApp number activated event

Fired when a purchased WhatsApp number becomes active and usable. Both the synchronous (Tier 1/2) path and the asynchronous regulated (Tier 3/4) path land here. Lets integrators react without polling GET /v1/phone-numbers. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppNumberActivatedRequest onWhatsAppNumberActivatedRequest = new OnWhatsAppNumberActivatedRequest(); // OnWhatsAppNumberActivatedRequest | 
        try {
            ApiResponse<Void> response = apiInstance.onWhatsAppNumberActivatedWithHttpInfo(onWhatsAppNumberActivatedRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppNumberActivated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onWhatsAppNumberActivatedRequest** | [**OnWhatsAppNumberActivatedRequest**](OnWhatsAppNumberActivatedRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onWhatsAppNumberDeclined

> void onWhatsAppNumberDeclined(onWhatsAppNumberDeclinedRequest)

WhatsApp number declined event

Fired when a regulated (Tier 3/4) number order is declined or fails review. The number is never billed. &#x60;reason&#x60; carries the reviewer&#39;s rejection reason when available. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppNumberDeclinedRequest onWhatsAppNumberDeclinedRequest = new OnWhatsAppNumberDeclinedRequest(); // OnWhatsAppNumberDeclinedRequest | 
        try {
            apiInstance.onWhatsAppNumberDeclined(onWhatsAppNumberDeclinedRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppNumberDeclined");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onWhatsAppNumberDeclinedRequest** | [**OnWhatsAppNumberDeclinedRequest**](OnWhatsAppNumberDeclinedRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onWhatsAppNumberDeclinedWithHttpInfo

> ApiResponse<Void> onWhatsAppNumberDeclined onWhatsAppNumberDeclinedWithHttpInfo(onWhatsAppNumberDeclinedRequest)

WhatsApp number declined event

Fired when a regulated (Tier 3/4) number order is declined or fails review. The number is never billed. &#x60;reason&#x60; carries the reviewer&#39;s rejection reason when available. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppNumberDeclinedRequest onWhatsAppNumberDeclinedRequest = new OnWhatsAppNumberDeclinedRequest(); // OnWhatsAppNumberDeclinedRequest | 
        try {
            ApiResponse<Void> response = apiInstance.onWhatsAppNumberDeclinedWithHttpInfo(onWhatsAppNumberDeclinedRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppNumberDeclined");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onWhatsAppNumberDeclinedRequest** | [**OnWhatsAppNumberDeclinedRequest**](OnWhatsAppNumberDeclinedRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onWhatsAppNumberKycSubmitted

> void onWhatsAppNumberKycSubmitted(onWhatsAppNumberKycSubmittedRequest)

WhatsApp number KYC submitted event

Fired when an end customer completes a hosted KYC share link (POST /v1/phone-numbers/kyc/share). The number enters review (pending_regulatory) under your account; &#x60;whatsapp.number.activated&#x60; or &#x60;whatsapp.number.declined&#x60; follows once the provider rules on it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppNumberKycSubmittedRequest onWhatsAppNumberKycSubmittedRequest = new OnWhatsAppNumberKycSubmittedRequest(); // OnWhatsAppNumberKycSubmittedRequest | 
        try {
            apiInstance.onWhatsAppNumberKycSubmitted(onWhatsAppNumberKycSubmittedRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppNumberKycSubmitted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onWhatsAppNumberKycSubmittedRequest** | [**OnWhatsAppNumberKycSubmittedRequest**](OnWhatsAppNumberKycSubmittedRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onWhatsAppNumberKycSubmittedWithHttpInfo

> ApiResponse<Void> onWhatsAppNumberKycSubmitted onWhatsAppNumberKycSubmittedWithHttpInfo(onWhatsAppNumberKycSubmittedRequest)

WhatsApp number KYC submitted event

Fired when an end customer completes a hosted KYC share link (POST /v1/phone-numbers/kyc/share). The number enters review (pending_regulatory) under your account; &#x60;whatsapp.number.activated&#x60; or &#x60;whatsapp.number.declined&#x60; follows once the provider rules on it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppNumberKycSubmittedRequest onWhatsAppNumberKycSubmittedRequest = new OnWhatsAppNumberKycSubmittedRequest(); // OnWhatsAppNumberKycSubmittedRequest | 
        try {
            ApiResponse<Void> response = apiInstance.onWhatsAppNumberKycSubmittedWithHttpInfo(onWhatsAppNumberKycSubmittedRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppNumberKycSubmitted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onWhatsAppNumberKycSubmittedRequest** | [**OnWhatsAppNumberKycSubmittedRequest**](OnWhatsAppNumberKycSubmittedRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onWhatsAppNumberReactivated

> void onWhatsAppNumberReactivated(onWhatsAppNumberReactivatedRequest)

WhatsApp number reactivated event

Fired when a suspended number is reactivated (e.g. the payment recovered) and is usable again. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppNumberReactivatedRequest onWhatsAppNumberReactivatedRequest = new OnWhatsAppNumberReactivatedRequest(); // OnWhatsAppNumberReactivatedRequest | 
        try {
            apiInstance.onWhatsAppNumberReactivated(onWhatsAppNumberReactivatedRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppNumberReactivated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onWhatsAppNumberReactivatedRequest** | [**OnWhatsAppNumberReactivatedRequest**](OnWhatsAppNumberReactivatedRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onWhatsAppNumberReactivatedWithHttpInfo

> ApiResponse<Void> onWhatsAppNumberReactivated onWhatsAppNumberReactivatedWithHttpInfo(onWhatsAppNumberReactivatedRequest)

WhatsApp number reactivated event

Fired when a suspended number is reactivated (e.g. the payment recovered) and is usable again. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppNumberReactivatedRequest onWhatsAppNumberReactivatedRequest = new OnWhatsAppNumberReactivatedRequest(); // OnWhatsAppNumberReactivatedRequest | 
        try {
            ApiResponse<Void> response = apiInstance.onWhatsAppNumberReactivatedWithHttpInfo(onWhatsAppNumberReactivatedRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppNumberReactivated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onWhatsAppNumberReactivatedRequest** | [**OnWhatsAppNumberReactivatedRequest**](OnWhatsAppNumberReactivatedRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onWhatsAppNumberReleased

> void onWhatsAppNumberReleased(onWhatsAppNumberReleasedRequest)

WhatsApp number released event

Fired when a number is released and is no longer usable (by the user, a billing cleanup, or an admin). Terminal. &#x60;reason&#x60; carries the cause (e.g. &#x60;user_requested&#x60;, &#x60;cleanup_suspended&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppNumberReleasedRequest onWhatsAppNumberReleasedRequest = new OnWhatsAppNumberReleasedRequest(); // OnWhatsAppNumberReleasedRequest | 
        try {
            apiInstance.onWhatsAppNumberReleased(onWhatsAppNumberReleasedRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppNumberReleased");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onWhatsAppNumberReleasedRequest** | [**OnWhatsAppNumberReleasedRequest**](OnWhatsAppNumberReleasedRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onWhatsAppNumberReleasedWithHttpInfo

> ApiResponse<Void> onWhatsAppNumberReleased onWhatsAppNumberReleasedWithHttpInfo(onWhatsAppNumberReleasedRequest)

WhatsApp number released event

Fired when a number is released and is no longer usable (by the user, a billing cleanup, or an admin). Terminal. &#x60;reason&#x60; carries the cause (e.g. &#x60;user_requested&#x60;, &#x60;cleanup_suspended&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppNumberReleasedRequest onWhatsAppNumberReleasedRequest = new OnWhatsAppNumberReleasedRequest(); // OnWhatsAppNumberReleasedRequest | 
        try {
            ApiResponse<Void> response = apiInstance.onWhatsAppNumberReleasedWithHttpInfo(onWhatsAppNumberReleasedRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppNumberReleased");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onWhatsAppNumberReleasedRequest** | [**OnWhatsAppNumberReleasedRequest**](OnWhatsAppNumberReleasedRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onWhatsAppNumberSuspended

> void onWhatsAppNumberSuspended(onWhatsAppNumberSuspendedRequest)

WhatsApp number suspended event

Fired when an active number is suspended (e.g. a failed payment). The number stops working until the issue is resolved, after which a &#x60;whatsapp.number.reactivated&#x60; event is sent. &#x60;reason&#x60; carries the cause (e.g. &#x60;payment_failed&#x60;, &#x60;subscription_ended&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppNumberSuspendedRequest onWhatsAppNumberSuspendedRequest = new OnWhatsAppNumberSuspendedRequest(); // OnWhatsAppNumberSuspendedRequest | 
        try {
            apiInstance.onWhatsAppNumberSuspended(onWhatsAppNumberSuspendedRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppNumberSuspended");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onWhatsAppNumberSuspendedRequest** | [**OnWhatsAppNumberSuspendedRequest**](OnWhatsAppNumberSuspendedRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onWhatsAppNumberSuspendedWithHttpInfo

> ApiResponse<Void> onWhatsAppNumberSuspended onWhatsAppNumberSuspendedWithHttpInfo(onWhatsAppNumberSuspendedRequest)

WhatsApp number suspended event

Fired when an active number is suspended (e.g. a failed payment). The number stops working until the issue is resolved, after which a &#x60;whatsapp.number.reactivated&#x60; event is sent. &#x60;reason&#x60; carries the cause (e.g. &#x60;payment_failed&#x60;, &#x60;subscription_ended&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppNumberSuspendedRequest onWhatsAppNumberSuspendedRequest = new OnWhatsAppNumberSuspendedRequest(); // OnWhatsAppNumberSuspendedRequest | 
        try {
            ApiResponse<Void> response = apiInstance.onWhatsAppNumberSuspendedWithHttpInfo(onWhatsAppNumberSuspendedRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppNumberSuspended");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onWhatsAppNumberSuspendedRequest** | [**OnWhatsAppNumberSuspendedRequest**](OnWhatsAppNumberSuspendedRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onWhatsAppNumberVerificationRequired

> void onWhatsAppNumberVerificationRequired(onWhatsAppNumberVerificationRequiredRequest)

WhatsApp number verification-required event

Fired when a regulated number has an out-of-band identity-verification step (e.g. Onfido). &#x60;verificationUrl&#x60; is the link to forward to the number&#39;s end user; the order completes once they pass. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppNumberVerificationRequiredRequest onWhatsAppNumberVerificationRequiredRequest = new OnWhatsAppNumberVerificationRequiredRequest(); // OnWhatsAppNumberVerificationRequiredRequest | 
        try {
            apiInstance.onWhatsAppNumberVerificationRequired(onWhatsAppNumberVerificationRequiredRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppNumberVerificationRequired");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onWhatsAppNumberVerificationRequiredRequest** | [**OnWhatsAppNumberVerificationRequiredRequest**](OnWhatsAppNumberVerificationRequiredRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onWhatsAppNumberVerificationRequiredWithHttpInfo

> ApiResponse<Void> onWhatsAppNumberVerificationRequired onWhatsAppNumberVerificationRequiredWithHttpInfo(onWhatsAppNumberVerificationRequiredRequest)

WhatsApp number verification-required event

Fired when a regulated number has an out-of-band identity-verification step (e.g. Onfido). &#x60;verificationUrl&#x60; is the link to forward to the number&#39;s end user; the order completes once they pass. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        OnWhatsAppNumberVerificationRequiredRequest onWhatsAppNumberVerificationRequiredRequest = new OnWhatsAppNumberVerificationRequiredRequest(); // OnWhatsAppNumberVerificationRequiredRequest | 
        try {
            ApiResponse<Void> response = apiInstance.onWhatsAppNumberVerificationRequiredWithHttpInfo(onWhatsAppNumberVerificationRequiredRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppNumberVerificationRequired");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **onWhatsAppNumberVerificationRequiredRequest** | [**OnWhatsAppNumberVerificationRequiredRequest**](OnWhatsAppNumberVerificationRequiredRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onWhatsAppTemplateCategoryUpdated

> void onWhatsAppTemplateCategoryUpdated(webhookPayloadWhatsAppTemplateCategoryUpdated)

WhatsApp template category updated event

Fired when Meta reclassifies a WhatsApp Business template&#39;s category after approval. Forwarded from Meta&#39;s &#x60;template_category_update&#x60; webhook field on the WhatsApp Business Account. Category drives Meta&#39;s per-conversation tariff and whether the template is subject to the recipient&#39;s marketing opt-out. &#x60;template.changeType&#x60; is &#x60;scheduled&#x60; (24h advance notice) or &#x60;applied&#x60;; &#x60;template.category&#x60; is always the category right now. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadWhatsAppTemplateCategoryUpdated webhookPayloadWhatsAppTemplateCategoryUpdated = new WebhookPayloadWhatsAppTemplateCategoryUpdated(); // WebhookPayloadWhatsAppTemplateCategoryUpdated | 
        try {
            apiInstance.onWhatsAppTemplateCategoryUpdated(webhookPayloadWhatsAppTemplateCategoryUpdated);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppTemplateCategoryUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadWhatsAppTemplateCategoryUpdated** | [**WebhookPayloadWhatsAppTemplateCategoryUpdated**](WebhookPayloadWhatsAppTemplateCategoryUpdated.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onWhatsAppTemplateCategoryUpdatedWithHttpInfo

> ApiResponse<Void> onWhatsAppTemplateCategoryUpdated onWhatsAppTemplateCategoryUpdatedWithHttpInfo(webhookPayloadWhatsAppTemplateCategoryUpdated)

WhatsApp template category updated event

Fired when Meta reclassifies a WhatsApp Business template&#39;s category after approval. Forwarded from Meta&#39;s &#x60;template_category_update&#x60; webhook field on the WhatsApp Business Account. Category drives Meta&#39;s per-conversation tariff and whether the template is subject to the recipient&#39;s marketing opt-out. &#x60;template.changeType&#x60; is &#x60;scheduled&#x60; (24h advance notice) or &#x60;applied&#x60;; &#x60;template.category&#x60; is always the category right now. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadWhatsAppTemplateCategoryUpdated webhookPayloadWhatsAppTemplateCategoryUpdated = new WebhookPayloadWhatsAppTemplateCategoryUpdated(); // WebhookPayloadWhatsAppTemplateCategoryUpdated | 
        try {
            ApiResponse<Void> response = apiInstance.onWhatsAppTemplateCategoryUpdatedWithHttpInfo(webhookPayloadWhatsAppTemplateCategoryUpdated);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppTemplateCategoryUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadWhatsAppTemplateCategoryUpdated** | [**WebhookPayloadWhatsAppTemplateCategoryUpdated**](WebhookPayloadWhatsAppTemplateCategoryUpdated.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onWhatsAppTemplateStatusUpdated

> void onWhatsAppTemplateStatusUpdated(webhookPayloadWhatsAppTemplateStatusUpdated)

WhatsApp template status updated event

Fired when Meta finishes (re)reviewing a WhatsApp Business template attached to a connected WABA. Forwarded from Meta&#39;s &#x60;message_template_status_update&#x60; webhook field on the WhatsApp Business Account. Consumers branch on &#x60;template.status&#x60; (APPROVED, REJECTED, PENDING, PAUSED, DISABLED, IN_APPEAL, PENDING_DELETION). Meta does not include the previous status or the template&#39;s category in this event. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadWhatsAppTemplateStatusUpdated webhookPayloadWhatsAppTemplateStatusUpdated = new WebhookPayloadWhatsAppTemplateStatusUpdated(); // WebhookPayloadWhatsAppTemplateStatusUpdated | 
        try {
            apiInstance.onWhatsAppTemplateStatusUpdated(webhookPayloadWhatsAppTemplateStatusUpdated);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppTemplateStatusUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadWhatsAppTemplateStatusUpdated** | [**WebhookPayloadWhatsAppTemplateStatusUpdated**](WebhookPayloadWhatsAppTemplateStatusUpdated.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onWhatsAppTemplateStatusUpdatedWithHttpInfo

> ApiResponse<Void> onWhatsAppTemplateStatusUpdated onWhatsAppTemplateStatusUpdatedWithHttpInfo(webhookPayloadWhatsAppTemplateStatusUpdated)

WhatsApp template status updated event

Fired when Meta finishes (re)reviewing a WhatsApp Business template attached to a connected WABA. Forwarded from Meta&#39;s &#x60;message_template_status_update&#x60; webhook field on the WhatsApp Business Account. Consumers branch on &#x60;template.status&#x60; (APPROVED, REJECTED, PENDING, PAUSED, DISABLED, IN_APPEAL, PENDING_DELETION). Meta does not include the previous status or the template&#39;s category in this event. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadWhatsAppTemplateStatusUpdated webhookPayloadWhatsAppTemplateStatusUpdated = new WebhookPayloadWhatsAppTemplateStatusUpdated(); // WebhookPayloadWhatsAppTemplateStatusUpdated | 
        try {
            ApiResponse<Void> response = apiInstance.onWhatsAppTemplateStatusUpdatedWithHttpInfo(webhookPayloadWhatsAppTemplateStatusUpdated);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWhatsAppTemplateStatusUpdated");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadWhatsAppTemplateStatusUpdated** | [**WebhookPayloadWhatsAppTemplateStatusUpdated**](WebhookPayloadWhatsAppTemplateStatusUpdated.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onWorkflowRunCompleted

> void onWorkflowRunCompleted(webhookPayloadWorkflowRun)

Workflow run completed event

Fired when a workflow run ends; execution.status is completed, or exited for a run ended on purpose before its last node.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadWorkflowRun webhookPayloadWorkflowRun = new WebhookPayloadWorkflowRun(); // WebhookPayloadWorkflowRun | 
        try {
            apiInstance.onWorkflowRunCompleted(webhookPayloadWorkflowRun);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWorkflowRunCompleted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadWorkflowRun** | [**WebhookPayloadWorkflowRun**](WebhookPayloadWorkflowRun.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onWorkflowRunCompletedWithHttpInfo

> ApiResponse<Void> onWorkflowRunCompleted onWorkflowRunCompletedWithHttpInfo(webhookPayloadWorkflowRun)

Workflow run completed event

Fired when a workflow run ends; execution.status is completed, or exited for a run ended on purpose before its last node.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadWorkflowRun webhookPayloadWorkflowRun = new WebhookPayloadWorkflowRun(); // WebhookPayloadWorkflowRun | 
        try {
            ApiResponse<Void> response = apiInstance.onWorkflowRunCompletedWithHttpInfo(webhookPayloadWorkflowRun);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWorkflowRunCompleted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadWorkflowRun** | [**WebhookPayloadWorkflowRun**](WebhookPayloadWorkflowRun.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onWorkflowRunFailed

> void onWorkflowRunFailed(webhookPayloadWorkflowRun)

Workflow run failed event

Fired when a workflow run fails; error says which node failed and why.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadWorkflowRun webhookPayloadWorkflowRun = new WebhookPayloadWorkflowRun(); // WebhookPayloadWorkflowRun | 
        try {
            apiInstance.onWorkflowRunFailed(webhookPayloadWorkflowRun);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWorkflowRunFailed");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadWorkflowRun** | [**WebhookPayloadWorkflowRun**](WebhookPayloadWorkflowRun.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onWorkflowRunFailedWithHttpInfo

> ApiResponse<Void> onWorkflowRunFailed onWorkflowRunFailedWithHttpInfo(webhookPayloadWorkflowRun)

Workflow run failed event

Fired when a workflow run fails; error says which node failed and why.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadWorkflowRun webhookPayloadWorkflowRun = new WebhookPayloadWorkflowRun(); // WebhookPayloadWorkflowRun | 
        try {
            ApiResponse<Void> response = apiInstance.onWorkflowRunFailedWithHttpInfo(webhookPayloadWorkflowRun);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWorkflowRunFailed");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadWorkflowRun** | [**WebhookPayloadWorkflowRun**](WebhookPayloadWorkflowRun.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |


## onWorkflowRunStarted

> void onWorkflowRunStarted(webhookPayloadWorkflowRun)

Workflow run started event

Fired when a workflow run starts for a conversation.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadWorkflowRun webhookPayloadWorkflowRun = new WebhookPayloadWorkflowRun(); // WebhookPayloadWorkflowRun | 
        try {
            apiInstance.onWorkflowRunStarted(webhookPayloadWorkflowRun);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWorkflowRunStarted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadWorkflowRun** | [**WebhookPayloadWorkflowRun**](WebhookPayloadWorkflowRun.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

## onWorkflowRunStartedWithHttpInfo

> ApiResponse<Void> onWorkflowRunStarted onWorkflowRunStartedWithHttpInfo(webhookPayloadWorkflowRun)

Workflow run started event

Fired when a workflow run starts for a conversation.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.WebhookEventsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        WebhookEventsApi apiInstance = new WebhookEventsApi(defaultClient);
        WebhookPayloadWorkflowRun webhookPayloadWorkflowRun = new WebhookPayloadWorkflowRun(); // WebhookPayloadWorkflowRun | 
        try {
            ApiResponse<Void> response = apiInstance.onWorkflowRunStartedWithHttpInfo(webhookPayloadWorkflowRun);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onWorkflowRunStarted");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **webhookPayloadWorkflowRun** | [**WebhookPayloadWorkflowRun**](WebhookPayloadWorkflowRun.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Webhook received successfully |  -  |

