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
| [**onAdCreated**](WebhookEventsApi.md#onAdCreated) | **POST** /ad.created | Ad created event |
| [**onAdCreatedWithHttpInfo**](WebhookEventsApi.md#onAdCreatedWithHttpInfo) | **POST** /ad.created | Ad created event |
| [**onAdDeliveryIssue**](WebhookEventsApi.md#onAdDeliveryIssue) | **POST** /ad.delivery_issue | Ad delivery issue event |
| [**onAdDeliveryIssueWithHttpInfo**](WebhookEventsApi.md#onAdDeliveryIssueWithHttpInfo) | **POST** /ad.delivery_issue | Ad delivery issue event |
| [**onAdReviewApproved**](WebhookEventsApi.md#onAdReviewApproved) | **POST** /ad.review.approved | Ad review approved event |
| [**onAdReviewApprovedWithHttpInfo**](WebhookEventsApi.md#onAdReviewApprovedWithHttpInfo) | **POST** /ad.review.approved | Ad review approved event |
| [**onAdReviewRejected**](WebhookEventsApi.md#onAdReviewRejected) | **POST** /ad.review.rejected | Ad review rejected event |
| [**onAdReviewRejectedWithHttpInfo**](WebhookEventsApi.md#onAdReviewRejectedWithHttpInfo) | **POST** /ad.review.rejected | Ad review rejected event |
| [**onAdRuleTriggered**](WebhookEventsApi.md#onAdRuleTriggered) | **POST** /ad_rule.triggered | Ad rule triggered event |
| [**onAdRuleTriggeredWithHttpInfo**](WebhookEventsApi.md#onAdRuleTriggeredWithHttpInfo) | **POST** /ad_rule.triggered | Ad rule triggered event |
| [**onAdSetCreated**](WebhookEventsApi.md#onAdSetCreated) | **POST** /ad_set.created | Ad set created event |
| [**onAdSetCreatedWithHttpInfo**](WebhookEventsApi.md#onAdSetCreatedWithHttpInfo) | **POST** /ad_set.created | Ad set created event |
| [**onAdSetUpdated**](WebhookEventsApi.md#onAdSetUpdated) | **POST** /ad_set.updated | Ad set updated event |
| [**onAdSetUpdatedWithHttpInfo**](WebhookEventsApi.md#onAdSetUpdatedWithHttpInfo) | **POST** /ad_set.updated | Ad set updated event |
| [**onAdStatusChanged**](WebhookEventsApi.md#onAdStatusChanged) | **POST** /ad.status_changed | Ad status changed event |
| [**onAdStatusChangedWithHttpInfo**](WebhookEventsApi.md#onAdStatusChangedWithHttpInfo) | **POST** /ad.status_changed | Ad status changed event |
| [**onAdUpdated**](WebhookEventsApi.md#onAdUpdated) | **POST** /ad.updated | Ad updated event |
| [**onAdUpdatedWithHttpInfo**](WebhookEventsApi.md#onAdUpdatedWithHttpInfo) | **POST** /ad.updated | Ad updated event |
| [**onAdVideoProcessed**](WebhookEventsApi.md#onAdVideoProcessed) | **POST** /ad.video.processed | Ad video processed event |
| [**onAdVideoProcessedWithHttpInfo**](WebhookEventsApi.md#onAdVideoProcessedWithHttpInfo) | **POST** /ad.video.processed | Ad video processed event |
| [**onAnalyticsSynced**](WebhookEventsApi.md#onAnalyticsSynced) | **POST** /analytics.synced | Analytics synced event |
| [**onAnalyticsSyncedWithHttpInfo**](WebhookEventsApi.md#onAnalyticsSyncedWithHttpInfo) | **POST** /analytics.synced | Analytics synced event |
| [**onApiChangelogPublished**](WebhookEventsApi.md#onApiChangelogPublished) | **POST** /api.changelog.published | API changelog entry published event |
| [**onApiChangelogPublishedWithHttpInfo**](WebhookEventsApi.md#onApiChangelogPublishedWithHttpInfo) | **POST** /api.changelog.published | API changelog entry published event |
| [**onAutomationActionApplied**](WebhookEventsApi.md#onAutomationActionApplied) | **POST** /automation.action.applied | Automation action applied event |
| [**onAutomationActionAppliedWithHttpInfo**](WebhookEventsApi.md#onAutomationActionAppliedWithHttpInfo) | **POST** /automation.action.applied | Automation action applied event |
| [**onAutomationActionFailed**](WebhookEventsApi.md#onAutomationActionFailed) | **POST** /automation.action.failed | Automation action failed event |
| [**onAutomationActionFailedWithHttpInfo**](WebhookEventsApi.md#onAutomationActionFailedWithHttpInfo) | **POST** /automation.action.failed | Automation action failed event |
| [**onAutomationActionUnknown**](WebhookEventsApi.md#onAutomationActionUnknown) | **POST** /automation.action.unknown | Automation action unknown event |
| [**onAutomationActionUnknownWithHttpInfo**](WebhookEventsApi.md#onAutomationActionUnknownWithHttpInfo) | **POST** /automation.action.unknown | Automation action unknown event |
| [**onAutomationAlertEscalated**](WebhookEventsApi.md#onAutomationAlertEscalated) | **POST** /automation.alert.escalated | Automation alert escalated event |
| [**onAutomationAlertEscalatedWithHttpInfo**](WebhookEventsApi.md#onAutomationAlertEscalatedWithHttpInfo) | **POST** /automation.alert.escalated | Automation alert escalated event |
| [**onAutomationAlertOpened**](WebhookEventsApi.md#onAutomationAlertOpened) | **POST** /automation.alert.opened | Automation alert opened event |
| [**onAutomationAlertOpenedWithHttpInfo**](WebhookEventsApi.md#onAutomationAlertOpenedWithHttpInfo) | **POST** /automation.alert.opened | Automation alert opened event |
| [**onAutomationAlertResolved**](WebhookEventsApi.md#onAutomationAlertResolved) | **POST** /automation.alert.resolved | Automation alert resolved event |
| [**onAutomationAlertResolvedWithHttpInfo**](WebhookEventsApi.md#onAutomationAlertResolvedWithHttpInfo) | **POST** /automation.alert.resolved | Automation alert resolved event |
| [**onAutomationCheckCompleted**](WebhookEventsApi.md#onAutomationCheckCompleted) | **POST** /automation.check.completed | Automation check completed event |
| [**onAutomationCheckCompletedWithHttpInfo**](WebhookEventsApi.md#onAutomationCheckCompletedWithHttpInfo) | **POST** /automation.check.completed | Automation check completed event |
| [**onBalanceCharged**](WebhookEventsApi.md#onBalanceCharged) | **POST** /balance.charged | Balance charged event |
| [**onBalanceChargedWithHttpInfo**](WebhookEventsApi.md#onBalanceChargedWithHttpInfo) | **POST** /balance.charged | Balance charged event |
| [**onBalanceEmpty**](WebhookEventsApi.md#onBalanceEmpty) | **POST** /balance.empty | Balance empty event |
| [**onBalanceEmptyWithHttpInfo**](WebhookEventsApi.md#onBalanceEmptyWithHttpInfo) | **POST** /balance.empty | Balance empty event |
| [**onBalanceLow**](WebhookEventsApi.md#onBalanceLow) | **POST** /balance.low | Balance low event |
| [**onBalanceLowWithHttpInfo**](WebhookEventsApi.md#onBalanceLowWithHttpInfo) | **POST** /balance.low | Balance low event |
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
| [**onCallRecordingReady**](WebhookEventsApi.md#onCallRecordingReady) | **POST** /call.recording_ready | Call recording ready event |
| [**onCallRecordingReadyWithHttpInfo**](WebhookEventsApi.md#onCallRecordingReadyWithHttpInfo) | **POST** /call.recording_ready | Call recording ready event |
| [**onCallTranscriptSegment**](WebhookEventsApi.md#onCallTranscriptSegment) | **POST** /call.transcript_segment | Call transcript segment event |
| [**onCallTranscriptSegmentWithHttpInfo**](WebhookEventsApi.md#onCallTranscriptSegmentWithHttpInfo) | **POST** /call.transcript_segment | Call transcript segment event |
| [**onCampaignBudgetDepleted**](WebhookEventsApi.md#onCampaignBudgetDepleted) | **POST** /campaign.budget.depleted | Campaign budget depleted event |
| [**onCampaignBudgetDepletedWithHttpInfo**](WebhookEventsApi.md#onCampaignBudgetDepletedWithHttpInfo) | **POST** /campaign.budget.depleted | Campaign budget depleted event |
| [**onCampaignCreated**](WebhookEventsApi.md#onCampaignCreated) | **POST** /campaign.created | Campaign created event |
| [**onCampaignCreatedWithHttpInfo**](WebhookEventsApi.md#onCampaignCreatedWithHttpInfo) | **POST** /campaign.created | Campaign created event |
| [**onCampaignDraftApproved**](WebhookEventsApi.md#onCampaignDraftApproved) | **POST** /campaign_draft.approved | Campaign draft approved event |
| [**onCampaignDraftApprovedWithHttpInfo**](WebhookEventsApi.md#onCampaignDraftApprovedWithHttpInfo) | **POST** /campaign_draft.approved | Campaign draft approved event |
| [**onCampaignDraftRejected**](WebhookEventsApi.md#onCampaignDraftRejected) | **POST** /campaign_draft.rejected | Campaign draft rejected event |
| [**onCampaignDraftRejectedWithHttpInfo**](WebhookEventsApi.md#onCampaignDraftRejectedWithHttpInfo) | **POST** /campaign_draft.rejected | Campaign draft rejected event |
| [**onCampaignDraftRevisionRequested**](WebhookEventsApi.md#onCampaignDraftRevisionRequested) | **POST** /campaign_draft.revision_requested | Campaign draft revision requested event |
| [**onCampaignDraftRevisionRequestedWithHttpInfo**](WebhookEventsApi.md#onCampaignDraftRevisionRequestedWithHttpInfo) | **POST** /campaign_draft.revision_requested | Campaign draft revision requested event |
| [**onCampaignDraftSubmitted**](WebhookEventsApi.md#onCampaignDraftSubmitted) | **POST** /campaign_draft.submitted | Campaign draft submitted event |
| [**onCampaignDraftSubmittedWithHttpInfo**](WebhookEventsApi.md#onCampaignDraftSubmittedWithHttpInfo) | **POST** /campaign_draft.submitted | Campaign draft submitted event |
| [**onCampaignParticipantApproved**](WebhookEventsApi.md#onCampaignParticipantApproved) | **POST** /campaign_participant.approved | Campaign participant approved event |
| [**onCampaignParticipantApprovedWithHttpInfo**](WebhookEventsApi.md#onCampaignParticipantApprovedWithHttpInfo) | **POST** /campaign_participant.approved | Campaign participant approved event |
| [**onCampaignParticipantDenied**](WebhookEventsApi.md#onCampaignParticipantDenied) | **POST** /campaign_participant.denied | Campaign participant denied event |
| [**onCampaignParticipantDeniedWithHttpInfo**](WebhookEventsApi.md#onCampaignParticipantDeniedWithHttpInfo) | **POST** /campaign_participant.denied | Campaign participant denied event |
| [**onCampaignParticipantJoined**](WebhookEventsApi.md#onCampaignParticipantJoined) | **POST** /campaign_participant.joined | Campaign participant joined event |
| [**onCampaignParticipantJoinedWithHttpInfo**](WebhookEventsApi.md#onCampaignParticipantJoinedWithHttpInfo) | **POST** /campaign_participant.joined | Campaign participant joined event |
| [**onCampaignParticipantPending**](WebhookEventsApi.md#onCampaignParticipantPending) | **POST** /campaign_participant.pending | Campaign participant pending event |
| [**onCampaignParticipantPendingWithHttpInfo**](WebhookEventsApi.md#onCampaignParticipantPendingWithHttpInfo) | **POST** /campaign_participant.pending | Campaign participant pending event |
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
| [**onCampaignSampleApproved**](WebhookEventsApi.md#onCampaignSampleApproved) | **POST** /campaign_sample.approved | Campaign sample approved event |
| [**onCampaignSampleApprovedWithHttpInfo**](WebhookEventsApi.md#onCampaignSampleApprovedWithHttpInfo) | **POST** /campaign_sample.approved | Campaign sample approved event |
| [**onCampaignSampleDeclined**](WebhookEventsApi.md#onCampaignSampleDeclined) | **POST** /campaign_sample.declined | Campaign sample declined event |
| [**onCampaignSampleDeclinedWithHttpInfo**](WebhookEventsApi.md#onCampaignSampleDeclinedWithHttpInfo) | **POST** /campaign_sample.declined | Campaign sample declined event |
| [**onCampaignSampleRequested**](WebhookEventsApi.md#onCampaignSampleRequested) | **POST** /campaign_sample.requested | Campaign sample requested event |
| [**onCampaignSampleRequestedWithHttpInfo**](WebhookEventsApi.md#onCampaignSampleRequestedWithHttpInfo) | **POST** /campaign_sample.requested | Campaign sample requested event |
| [**onCampaignSampleShipped**](WebhookEventsApi.md#onCampaignSampleShipped) | **POST** /campaign_sample.shipped | Campaign sample shipped event |
| [**onCampaignSampleShippedWithHttpInfo**](WebhookEventsApi.md#onCampaignSampleShippedWithHttpInfo) | **POST** /campaign_sample.shipped | Campaign sample shipped event |
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
| [**onCampaignUpdated**](WebhookEventsApi.md#onCampaignUpdated) | **POST** /campaign.updated | Campaign updated event |
| [**onCampaignUpdatedWithHttpInfo**](WebhookEventsApi.md#onCampaignUpdatedWithHttpInfo) | **POST** /campaign.updated | Campaign updated event |
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
| [**onEmailBounced**](WebhookEventsApi.md#onEmailBounced) | **POST** /email.bounced | Email bounced |
| [**onEmailBouncedWithHttpInfo**](WebhookEventsApi.md#onEmailBouncedWithHttpInfo) | **POST** /email.bounced | Email bounced |
| [**onEmailLinkClicked**](WebhookEventsApi.md#onEmailLinkClicked) | **POST** /email.link_clicked | Email link clicked |
| [**onEmailLinkClickedWithHttpInfo**](WebhookEventsApi.md#onEmailLinkClickedWithHttpInfo) | **POST** /email.link_clicked | Email link clicked |
| [**onEmailOpened**](WebhookEventsApi.md#onEmailOpened) | **POST** /email.opened | Email opened |
| [**onEmailOpenedWithHttpInfo**](WebhookEventsApi.md#onEmailOpenedWithHttpInfo) | **POST** /email.opened | Email opened |
| [**onEmailSendFailed**](WebhookEventsApi.md#onEmailSendFailed) | **POST** /email.send_failed | Scheduled email failed |
| [**onEmailSendFailedWithHttpInfo**](WebhookEventsApi.md#onEmailSendFailedWithHttpInfo) | **POST** /email.send_failed | Scheduled email failed |
| [**onEmailSent**](WebhookEventsApi.md#onEmailSent) | **POST** /email.sent | Email sent |
| [**onEmailSentWithHttpInfo**](WebhookEventsApi.md#onEmailSentWithHttpInfo) | **POST** /email.sent | Email sent |
| [**onEmailThreadReplied**](WebhookEventsApi.md#onEmailThreadReplied) | **POST** /email.thread_replied | Email thread replied |
| [**onEmailThreadRepliedWithHttpInfo**](WebhookEventsApi.md#onEmailThreadRepliedWithHttpInfo) | **POST** /email.thread_replied | Email thread replied |
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
| [**onMentionReceived**](WebhookEventsApi.md#onMentionReceived) | **POST** /mention.received | Mention received event |
| [**onMentionReceivedWithHttpInfo**](WebhookEventsApi.md#onMentionReceivedWithHttpInfo) | **POST** /mention.received | Mention received event |
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
| [**onReviewDeleted**](WebhookEventsApi.md#onReviewDeleted) | **POST** /review.deleted | Review deleted event |
| [**onReviewDeletedWithHttpInfo**](WebhookEventsApi.md#onReviewDeletedWithHttpInfo) | **POST** /review.deleted | Review deleted event |
| [**onReviewNew**](WebhookEventsApi.md#onReviewNew) | **POST** /review.new | Review new event |
| [**onReviewNewWithHttpInfo**](WebhookEventsApi.md#onReviewNewWithHttpInfo) | **POST** /review.new | Review new event |
| [**onReviewRestored**](WebhookEventsApi.md#onReviewRestored) | **POST** /review.restored | Review restored event |
| [**onReviewRestoredWithHttpInfo**](WebhookEventsApi.md#onReviewRestoredWithHttpInfo) | **POST** /review.restored | Review restored event |
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

The initial sync, ad-account discovery plus a 90-day ad backfill, completed for an ads-enabled account.  ### When it fires  Fires once per ads-enabled account. &#x60;sync&#x60; reports whether the backfill succeeded fully or partially, and how many ads were synced versus failed.  ### Scoped connects  When scoping was applied at connect time, &#x60;account.platformAdAccountId&#x60; echoes the chosen ad account when the scope is exactly one. &#x60;account.platformAdAccountIds&#x60; lists every &#x60;act_*&#x60; synced.  ### On failure  When &#x60;sync.status&#x60; is &#x60;\&quot;failure\&quot;&#x60;, the payload adds &#x60;sync.error&#x60; (raw platform error, about 2 KB), &#x60;sync.errorCode&#x60; and &#x60;sync.errorSubcode&#x60; when parseable, and &#x60;sync.errorCategory&#x60;.  ### Error categories  &#x60;sync.errorCategory&#x60; is &#x60;token_invalid&#x60;, &#x60;permission_denied&#x60;, &#x60;no_ad_accounts&#x60;, &#x60;rate_limited&#x60;, &#x60;discovery_failed&#x60; or &#x60;unknown&#x60;. New values may be added; existing ones are stable.  ### Retrying  Reconnecting re-queues the backfill and the event fires again. It fixes &#x60;token_invalid&#x60;, &#x60;permission_denied&#x60; and &#x60;rate_limited&#x60;; &#x60;no_ad_accounts&#x60; needs an ad account on the grant first.  ### When a retry is skipped  Zernio skips the re-queue only when a backfill already completed with at least one ad, or one started less than 20 minutes ago. 

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

The initial sync, ad-account discovery plus a 90-day ad backfill, completed for an ads-enabled account.  ### When it fires  Fires once per ads-enabled account. &#x60;sync&#x60; reports whether the backfill succeeded fully or partially, and how many ads were synced versus failed.  ### Scoped connects  When scoping was applied at connect time, &#x60;account.platformAdAccountId&#x60; echoes the chosen ad account when the scope is exactly one. &#x60;account.platformAdAccountIds&#x60; lists every &#x60;act_*&#x60; synced.  ### On failure  When &#x60;sync.status&#x60; is &#x60;\&quot;failure\&quot;&#x60;, the payload adds &#x60;sync.error&#x60; (raw platform error, about 2 KB), &#x60;sync.errorCode&#x60; and &#x60;sync.errorSubcode&#x60; when parseable, and &#x60;sync.errorCategory&#x60;.  ### Error categories  &#x60;sync.errorCategory&#x60; is &#x60;token_invalid&#x60;, &#x60;permission_denied&#x60;, &#x60;no_ad_accounts&#x60;, &#x60;rate_limited&#x60;, &#x60;discovery_failed&#x60; or &#x60;unknown&#x60;. New values may be added; existing ones are stable.  ### Retrying  Reconnecting re-queues the backfill and the event fires again. It fixes &#x60;token_invalid&#x60;, &#x60;permission_denied&#x60; and &#x60;rate_limited&#x60;; &#x60;no_ad_accounts&#x60; needs an ad account on the grant first.  ### When a retry is skipped  Zernio skips the re-queue only when a backfill already completed with at least one ad, or one started less than 20 minutes ago. 

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

An ad account&#39;s ads stopped syncing: no success for 24 hours, or every live ad at the retry cap.  ### When it fires  An hourly check covers every ad account with live ads on a connected account, on any ads platform. Fires once per ad account until &#x60;account.ads.sync_recovered&#x60;.  ### Stale metrics  Metrics for the ad account are stale in between. Use this signal to flag the numbers in your UI rather than to poll.  ### Payload notes  &#x60;adAccount.platformAdAccountId&#x60; names the ad account (&#x60;act_*&#x60; on Meta). &#x60;account.accountId&#x60; names its connection, so one connection with several ad accounts reports each separately.  ### Sync fields  &#x60;sync.lastSuccessfulSyncAt&#x60; is the last good sync and &#x60;sync.failureCount&#x60; the consecutive failed attempts.  ### Error categories  Branch on &#x60;sync.errorCategory&#x60;: &#x60;ad_account_not_listed&#x60; (access removed or platform change; check permissions, reconnect), &#x60;sync_error&#x60; (see &#x60;sync.error&#x60;) or &#x60;stale&#x60; (no error recorded; retries usually clear it). New values may be added.  ### When it does not fire  A disconnected connection gets &#x60;account.disconnected&#x60; instead, and no recovery event follows. An ad account that never synced successfully, or whose last good sync is over 3 days old, is not announced. 

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

An ad account&#39;s ads stopped syncing: no success for 24 hours, or every live ad at the retry cap.  ### When it fires  An hourly check covers every ad account with live ads on a connected account, on any ads platform. Fires once per ad account until &#x60;account.ads.sync_recovered&#x60;.  ### Stale metrics  Metrics for the ad account are stale in between. Use this signal to flag the numbers in your UI rather than to poll.  ### Payload notes  &#x60;adAccount.platformAdAccountId&#x60; names the ad account (&#x60;act_*&#x60; on Meta). &#x60;account.accountId&#x60; names its connection, so one connection with several ad accounts reports each separately.  ### Sync fields  &#x60;sync.lastSuccessfulSyncAt&#x60; is the last good sync and &#x60;sync.failureCount&#x60; the consecutive failed attempts.  ### Error categories  Branch on &#x60;sync.errorCategory&#x60;: &#x60;ad_account_not_listed&#x60; (access removed or platform change; check permissions, reconnect), &#x60;sync_error&#x60; (see &#x60;sync.error&#x60;) or &#x60;stale&#x60; (no error recorded; retries usually clear it). New values may be added.  ### When it does not fire  A disconnected connection gets &#x60;account.disconnected&#x60; instead, and no recovery event follows. An ad account that never synced successfully, or whose last good sync is over 3 days old, is not announced. 

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

An ad account previously reported by &#x60;account.ads.sync_failed&#x60; synced successfully again.  ### When it fires  Fires once when a sync succeeds again, found by an hourly check.  ### Payload notes  &#x60;sync.failingSince&#x60; is the last successful sync before the failure started. 

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

An ad account previously reported by &#x60;account.ads.sync_failed&#x60; synced successfully again.  ### When it fires  Fires once when a sync succeeds again, found by an hourly check.  ### Payload notes  &#x60;sync.failingSince&#x60; is the last successful sync before the failure started. 

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

An account was connected to a profile, through OAuth or credentials.  ### Repeat events  Reconnecting an account you already hold fires it again with the same &#x60;accountId&#x60;, since the connect flow upserts per profile and platform. Key your upsert on &#x60;accountId&#x60;. 

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

An account was connected to a profile, through OAuth or credentials.  ### Repeat events  Reconnecting an account you already hold fires it again with the same &#x60;accountId&#x60;, since the connect flow upserts per profile and platform. Key your upsert on &#x60;accountId&#x60;. 

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

A connected account stopped working or was removed.  ### Intentional  Removed on purpose, such as &#x60;DELETE /v1/accounts/{id}&#x60; or a switch to the Free plan. Kept 1 hour (&#x60;gracePeriodEndsAt&#x60;), then deleted with no further event. Reconnecting within the hour restores the same &#x60;accountId&#x60;.  ### Unintentional  The connection broke (token expired or revoked, access lost). The account stays inactive until reconnected, keeping its &#x60;accountId&#x60;. Removing it instead sends a second event with &#x60;intentional&#x60;.  ### Immediate paths  An API removal emits at once with &#x60;disconnectionType: \&quot;intentional\&quot;&#x60;. A phone-side WhatsApp disconnect emits within seconds of Meta&#39;s notification, with &#x60;unintentional&#x60;.  ### WhatsApp reason  &#x60;reason&#x60; carries Meta&#39;s explanation. Deliberate: &#x60;BUSINESS_DOWNGRADE&#x60;, &#x60;CHANGE_NUMBER&#x60;, &#x60;USER_RE_REGISTERED&#x60;. Idle number dropped by Meta: &#x60;PRIMARY_INACTIVITY&#x60; after about 14 days, &#x60;COMPANION_INACTIVITY&#x60; after about 30.  ### Expired or revoked grants  A publish or analytics sync getting a definitive auth error deactivates the account. Publish tries a token refresh first, so the event means the refresh failed too. &#x60;reason&#x60; carries the platform&#39;s message.  ### Reconnection flags  A dead token on an ads or blog call flags the account, and the posting account sharing its token (&#x60;needsReconnection: true&#x60;). Each flagged account emits once; a later deactivation emits again, then not until reconnected.  ### Lead forms while disconnected  While a Facebook Page is flagged or deactivated, &#x60;GET /v1/ads/lead-forms/{formId}/leads&#x60; answers &#x60;409&#x60; with &#x60;code: \&quot;account_disconnected\&quot;&#x60;.  ### Reconciliation  Anything else (a number deleted in WhatsApp Manager, a channel Meta silently stops serving) is caught by periodic reconciliation, not a notification. It lags minutes to about a day.  ### Do not rely on its absence  Meta&#39;s notifications are best-effort. For WhatsApp, poll &#x60;GET /v1/whatsapp/number-info&#x60; or account health, which runs a live Meta link probe.  ### Subscribing  A webhook only receives the events it lists, so add &#x60;account.disconnected&#x60; explicitly. 

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

A connected account stopped working or was removed.  ### Intentional  Removed on purpose, such as &#x60;DELETE /v1/accounts/{id}&#x60; or a switch to the Free plan. Kept 1 hour (&#x60;gracePeriodEndsAt&#x60;), then deleted with no further event. Reconnecting within the hour restores the same &#x60;accountId&#x60;.  ### Unintentional  The connection broke (token expired or revoked, access lost). The account stays inactive until reconnected, keeping its &#x60;accountId&#x60;. Removing it instead sends a second event with &#x60;intentional&#x60;.  ### Immediate paths  An API removal emits at once with &#x60;disconnectionType: \&quot;intentional\&quot;&#x60;. A phone-side WhatsApp disconnect emits within seconds of Meta&#39;s notification, with &#x60;unintentional&#x60;.  ### WhatsApp reason  &#x60;reason&#x60; carries Meta&#39;s explanation. Deliberate: &#x60;BUSINESS_DOWNGRADE&#x60;, &#x60;CHANGE_NUMBER&#x60;, &#x60;USER_RE_REGISTERED&#x60;. Idle number dropped by Meta: &#x60;PRIMARY_INACTIVITY&#x60; after about 14 days, &#x60;COMPANION_INACTIVITY&#x60; after about 30.  ### Expired or revoked grants  A publish or analytics sync getting a definitive auth error deactivates the account. Publish tries a token refresh first, so the event means the refresh failed too. &#x60;reason&#x60; carries the platform&#39;s message.  ### Reconnection flags  A dead token on an ads or blog call flags the account, and the posting account sharing its token (&#x60;needsReconnection: true&#x60;). Each flagged account emits once; a later deactivation emits again, then not until reconnected.  ### Lead forms while disconnected  While a Facebook Page is flagged or deactivated, &#x60;GET /v1/ads/lead-forms/{formId}/leads&#x60; answers &#x60;409&#x60; with &#x60;code: \&quot;account_disconnected\&quot;&#x60;.  ### Reconciliation  Anything else (a number deleted in WhatsApp Manager, a channel Meta silently stops serving) is caught by periodic reconciliation, not a notification. It lags minutes to about a day.  ### Do not rely on its absence  Meta&#39;s notifications are best-effort. For WhatsApp, poll &#x60;GET /v1/whatsapp/number-info&#x60; or account health, which runs a live Meta link probe.  ### Subscribing  A webhook only receives the events it lists, so add &#x60;account.disconnected&#x60; explicitly. 

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

A publish on an account connected through your own OAuth app failed for a missing permission.  ### Behaviour  The account stays connected and its token still works. &#x60;account.missingScopeAreas&#x60; accumulates the affected areas, today &#x60;posting&#x60;. Each area sends one event, however many posts fail afterwards.  ### When it does not fire  Accounts not connected through your own OAuth app. 

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

A publish on an account connected through your own OAuth app failed for a missing permission.  ### Behaviour  The account stays connected and its token still works. &#x60;account.missingScopeAreas&#x60; accumulates the affected areas, today &#x60;posting&#x60;. Each area sends one event, however many posts fail afterwards.  ### When it does not fire  Accounts not connected through your own OAuth app. 

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

A Google or Microsoft mailbox was paused after sending one body to over 50 recipients in an hour.  ### Payload notes  &#x60;account.reason&#x60; says why and &#x60;account.resetsAt&#x60; says when sending resumes. Sends answer 429 until then. A later trigger can also start a cooldown. 

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

A Google or Microsoft mailbox was paused after sending one body to over 50 recipients in an hour.  ### Payload notes  &#x60;account.reason&#x60; says why and &#x60;account.resetsAt&#x60; says when sending resumes. Sends answer 429 until then. A later trigger can also start a cooldown. 

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

An ad account Zernio already tracked became &#x60;active&#x60;, &#x60;restricted&#x60;, &#x60;disabled&#x60; or &#x60;closed&#x60;.  ### When it fires  Fires when ad account discovery sees a tracked ad account change status, at most once per account per 24 hours. Covers Meta, Google, TikTok and X.  ### Status values  &#x60;restricted&#x60; needs something settled first (unpaid Meta balance, risk review, TikTok limit or pending verification, X review). &#x60;disabled&#x60; means the platform disabled or rejected it; &#x60;closed&#x60; means closed or pending closure.  ### Payload notes  &#x60;status.current&#x60; and &#x60;status.previous&#x60; use one vocabulary on every network. &#x60;status.raw&#x60; is the platform&#39;s own value, for example Meta&#39;s &#x60;account_status&#x60; code &#x60;2&#x60;.  ### When it does not fire  An account seen for the first time, an account Zernio has not seen in the last 48 hours, or a platform status Zernio does not recognize. 

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

An ad account Zernio already tracked became &#x60;active&#x60;, &#x60;restricted&#x60;, &#x60;disabled&#x60; or &#x60;closed&#x60;.  ### When it fires  Fires when ad account discovery sees a tracked ad account change status, at most once per account per 24 hours. Covers Meta, Google, TikTok and X.  ### Status values  &#x60;restricted&#x60; needs something settled first (unpaid Meta balance, risk review, TikTok limit or pending verification, X review). &#x60;disabled&#x60; means the platform disabled or rejected it; &#x60;closed&#x60; means closed or pending closure.  ### Payload notes  &#x60;status.current&#x60; and &#x60;status.previous&#x60; use one vocabulary on every network. &#x60;status.raw&#x60; is the platform&#39;s own value, for example Meta&#39;s &#x60;account_status&#x60; code &#x60;2&#x60;.  ### When it does not fire  An account seen for the first time, an account Zernio has not seen in the last 48 hours, or a platform status Zernio does not recognize. 

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


## onAdCreated

> void onAdCreated(webhookPayloadAdCreated)

Ad created event

An ad was created through Zernio (&#x60;source: \&quot;zernio\&quot;&#x60;) or detected by the sync (&#x60;source: \&quot;platform\&quot;&#x60;).  ### When it fires  Fires once the ad&#39;s campaign and ad set are recorded. A detected ad arrives up to one sync interval late; Meta ads entering review usually arrive within minutes.  ### When it does not fire  History loaded when an account connects, and ads created more than 7 days ago, are never announced. 

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
        WebhookPayloadAdCreated webhookPayloadAdCreated = new WebhookPayloadAdCreated(); // WebhookPayloadAdCreated | 
        try {
            apiInstance.onAdCreated(webhookPayloadAdCreated);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAdCreated");
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
| **webhookPayloadAdCreated** | [**WebhookPayloadAdCreated**](WebhookPayloadAdCreated.md)|  | |

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

## onAdCreatedWithHttpInfo

> ApiResponse<Void> onAdCreated onAdCreatedWithHttpInfo(webhookPayloadAdCreated)

Ad created event

An ad was created through Zernio (&#x60;source: \&quot;zernio\&quot;&#x60;) or detected by the sync (&#x60;source: \&quot;platform\&quot;&#x60;).  ### When it fires  Fires once the ad&#39;s campaign and ad set are recorded. A detected ad arrives up to one sync interval late; Meta ads entering review usually arrive within minutes.  ### When it does not fire  History loaded when an account connects, and ads created more than 7 days ago, are never announced. 

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
        WebhookPayloadAdCreated webhookPayloadAdCreated = new WebhookPayloadAdCreated(); // WebhookPayloadAdCreated | 
        try {
            ApiResponse<Void> response = apiInstance.onAdCreatedWithHttpInfo(webhookPayloadAdCreated);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAdCreated");
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
| **webhookPayloadAdCreated** | [**WebhookPayloadAdCreated**](WebhookPayloadAdCreated.md)|  | |

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

An ad Zernio already tracked moved into the platform&#39;s error state and stopped delivering.  ### What triggers it  Meta &#x60;WITH_ISSUES&#x60; (payment, policy or account problems), TikTok account punishment or missing balance, or any platform status Zernio does not recognize yet (check &#x60;issue.raw&#x60;).  ### When it fires  Fires at most once per ad per 24 hours. Ads seen for the first time by a sync never fire it.  ### Payload notes  &#x60;issue.raw&#x60; is the platform&#39;s status string. On Meta, &#x60;issue.reasons&#x60; carries Meta&#39;s messages for the campaign; other networks send none, so it is empty.  ### Platform notes  On Meta the same problem can also arrive as &#x60;ad.status_changed&#x60; with &#x60;WITH_ISSUES&#x60;, straight from Meta&#39;s webhook and usually sooner. Pick one of the two to act on. 

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

An ad Zernio already tracked moved into the platform&#39;s error state and stopped delivering.  ### What triggers it  Meta &#x60;WITH_ISSUES&#x60; (payment, policy or account problems), TikTok account punishment or missing balance, or any platform status Zernio does not recognize yet (check &#x60;issue.raw&#x60;).  ### When it fires  Fires at most once per ad per 24 hours. Ads seen for the first time by a sync never fire it.  ### Payload notes  &#x60;issue.raw&#x60; is the platform&#39;s status string. On Meta, &#x60;issue.reasons&#x60; carries Meta&#39;s messages for the campaign; other networks send none, so it is empty.  ### Platform notes  On Meta the same problem can also arrive as &#x60;ad.status_changed&#x60; with &#x60;WITH_ISSUES&#x60;, straight from Meta&#39;s webhook and usually sooner. Pick one of the two to act on. 

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

An ad Zernio already tracked passed platform review, or a rejected ad was approved on appeal.  ### When it fires  Fires within one sync cycle of the platform&#39;s decision, not instantly; on Meta the review poll usually reports sooner. Each outcome is delivered at most once per ad per 24 hours.  ### When it does not fire  Ads seen for the first time by a sync never fire it, including history loaded at connect. On Meta, Google, TikTok and Reddit an ad that leaves review while paused sends no &#x60;approved&#x60;.  ### Platform notes  Covers every ad network Zernio syncs, with one payload shape. On X, Pinterest and LinkedIn the review is read apart from delivery status, so an ad leaving review while paused still sends &#x60;approved&#x60;.  ### Payload notes  &#x60;review.raw&#x60; is the platform&#39;s own status string. &#x60;adObject.adId&#x60; is the Zernio ad id, ready for &#x60;GET /v1/ads/{adId}&#x60;. Deduplicate on the event &#x60;id&#x60;. 

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

An ad Zernio already tracked passed platform review, or a rejected ad was approved on appeal.  ### When it fires  Fires within one sync cycle of the platform&#39;s decision, not instantly; on Meta the review poll usually reports sooner. Each outcome is delivered at most once per ad per 24 hours.  ### When it does not fire  Ads seen for the first time by a sync never fire it, including history loaded at connect. On Meta, Google, TikTok and Reddit an ad that leaves review while paused sends no &#x60;approved&#x60;.  ### Platform notes  Covers every ad network Zernio syncs, with one payload shape. On X, Pinterest and LinkedIn the review is read apart from delivery status, so an ad leaving review while paused still sends &#x60;approved&#x60;.  ### Payload notes  &#x60;review.raw&#x60; is the platform&#39;s own status string. &#x60;adObject.adId&#x60; is the Zernio ad id, ready for &#x60;GET /v1/ads/{adId}&#x60;. Deduplicate on the event &#x60;id&#x60;. 

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

The platform rejected an ad Zernio already tracked; &#x60;review.reasons&#x60; carries its reason when it gives one.  ### When it fires  Fires within one sync cycle of the platform&#39;s decision, not instantly; on Meta the review poll usually reports sooner. Each outcome is delivered at most once per ad per 24 hours.  ### When it does not fire  Ads seen for the first time by a sync never fire it, including history loaded at connect.  ### Platform notes  Covers every ad network Zernio syncs. Pinterest, LinkedIn and Reddit send their own reasons, X sends none, and most other networks return a generic message.  ### Payload notes  &#x60;review.raw&#x60; is the platform&#39;s own status string. Show &#x60;review.reasons&#x60; rather than branching on it. &#x60;adObject.adId&#x60; is the Zernio ad id. Deduplicate on the event &#x60;id&#x60;. 

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

The platform rejected an ad Zernio already tracked; &#x60;review.reasons&#x60; carries its reason when it gives one.  ### When it fires  Fires within one sync cycle of the platform&#39;s decision, not instantly; on Meta the review poll usually reports sooner. Each outcome is delivered at most once per ad per 24 hours.  ### When it does not fire  Ads seen for the first time by a sync never fire it, including history loaded at connect.  ### Platform notes  Covers every ad network Zernio syncs. Pinterest, LinkedIn and Reddit send their own reasons, X sends none, and most other networks return a generic message.  ### Payload notes  &#x60;review.raw&#x60; is the platform&#39;s own status string. Show &#x60;review.reasons&#x60; rather than branching on it. &#x60;adObject.adId&#x60; is the Zernio ad id. Deduplicate on the event &#x60;id&#x60;. 

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

A scheduled run of an ad rule with a &#x60;notify&#x60; action found campaigns or ad sets meeting every condition.  ### When it fires  Each object is announced at most once per rule cooldown. A run where every object is still in cooldown sends nothing.  ### Failed actions  An object whose action &#x60;failed&#x60; gets no cooldown, so the next run retries it and reports it again.  ### Payload notes  &#x60;objects&#x60; lists only the objects the run acted on. &#x60;objects[].conditions&#x60; repeats every condition of the rule with &#x60;actual&#x60;, the value the object reached.  ### Actions  &#x60;objects[].actions&#x60; says what the rule did: &#x60;done&#x60;, &#x60;skipped&#x60; (with a &#x60;reason&#x60; such as &#x60;already_paused&#x60; or &#x60;at_limit&#x60;) or &#x60;failed&#x60;. On &#x60;adjust_budget&#x60; it carries &#x60;previousDailyBudget&#x60; and &#x60;newDailyBudget&#x60;; empty on a notify-only rule.  ### Run context  &#x60;run.today&#x60; and &#x60;run.timezone&#x60; give the ad account&#39;s calendar date the windows used. &#x60;run.timezoneAssumed&#x60; is &#x60;true&#x60; when UTC was assumed. &#x60;run.currency&#x60; is the currency of money metrics, or &#x60;null&#x60; when unknown. 

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

A scheduled run of an ad rule with a &#x60;notify&#x60; action found campaigns or ad sets meeting every condition.  ### When it fires  Each object is announced at most once per rule cooldown. A run where every object is still in cooldown sends nothing.  ### Failed actions  An object whose action &#x60;failed&#x60; gets no cooldown, so the next run retries it and reports it again.  ### Payload notes  &#x60;objects&#x60; lists only the objects the run acted on. &#x60;objects[].conditions&#x60; repeats every condition of the rule with &#x60;actual&#x60;, the value the object reached.  ### Actions  &#x60;objects[].actions&#x60; says what the rule did: &#x60;done&#x60;, &#x60;skipped&#x60; (with a &#x60;reason&#x60; such as &#x60;already_paused&#x60; or &#x60;at_limit&#x60;) or &#x60;failed&#x60;. On &#x60;adjust_budget&#x60; it carries &#x60;previousDailyBudget&#x60; and &#x60;newDailyBudget&#x60;; empty on a notify-only rule.  ### Run context  &#x60;run.today&#x60; and &#x60;run.timezone&#x60; give the ad account&#39;s calendar date the windows used. &#x60;run.timezoneAssumed&#x60; is &#x60;true&#x60; when UTC was assumed. &#x60;run.currency&#x60; is the currency of money metrics, or &#x60;null&#x60; when unknown. 

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


## onAdSetCreated

> void onAdSetCreated(webhookPayloadAdSetCreated)

Ad set created event

An ad set was created through Zernio (&#x60;source: \&quot;zernio\&quot;&#x60;) or detected by the sync (&#x60;source: \&quot;platform\&quot;&#x60;).  ### When it fires  Fires once the ad set row is recorded, so &#x60;GET /v1/ads/ad-sets/{adSetId}&#x60; finds it. A detected ad set arrives up to one sync interval late.  ### Payload notes  &#x60;adObject.campaign&#x60; is the campaign the ad set belongs to, or null when the platform has none.  ### When it does not fire  History loaded when an account connects, and ad sets created more than 7 days ago, are never announced. 

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
        WebhookPayloadAdSetCreated webhookPayloadAdSetCreated = new WebhookPayloadAdSetCreated(); // WebhookPayloadAdSetCreated | 
        try {
            apiInstance.onAdSetCreated(webhookPayloadAdSetCreated);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAdSetCreated");
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
| **webhookPayloadAdSetCreated** | [**WebhookPayloadAdSetCreated**](WebhookPayloadAdSetCreated.md)|  | |

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

## onAdSetCreatedWithHttpInfo

> ApiResponse<Void> onAdSetCreated onAdSetCreatedWithHttpInfo(webhookPayloadAdSetCreated)

Ad set created event

An ad set was created through Zernio (&#x60;source: \&quot;zernio\&quot;&#x60;) or detected by the sync (&#x60;source: \&quot;platform\&quot;&#x60;).  ### When it fires  Fires once the ad set row is recorded, so &#x60;GET /v1/ads/ad-sets/{adSetId}&#x60; finds it. A detected ad set arrives up to one sync interval late.  ### Payload notes  &#x60;adObject.campaign&#x60; is the campaign the ad set belongs to, or null when the platform has none.  ### When it does not fire  History loaded when an account connects, and ad sets created more than 7 days ago, are never announced. 

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
        WebhookPayloadAdSetCreated webhookPayloadAdSetCreated = new WebhookPayloadAdSetCreated(); // WebhookPayloadAdSetCreated | 
        try {
            ApiResponse<Void> response = apiInstance.onAdSetCreatedWithHttpInfo(webhookPayloadAdSetCreated);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAdSetCreated");
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
| **webhookPayloadAdSetCreated** | [**WebhookPayloadAdSetCreated**](WebhookPayloadAdSetCreated.md)|  | |

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


## onAdSetUpdated

> void onAdSetUpdated(webhookPayloadAdSetUpdated)

Ad set updated event

An ad set was edited through Zernio (&#x60;source: \&quot;zernio\&quot;&#x60;), or outside Zernio and detected by the sync (&#x60;source: \&quot;platform\&quot;&#x60;).  ### When it fires  Fires after the platform and Zernio both accepted the edit. Outside edits arrive up to one sync interval late, and only to the user whose sync saw them.  ### Deduplication  Events are not deduplicated, so every edit is announced. Use the event &#x60;id&#x60; to drop repeats.  ### Payload notes  &#x60;changes&#x60; lists the edited fields: &#x60;name&#x60;, &#x60;status&#x60; (the ad set&#39;s own on/off switch), &#x60;budget&#x60;, &#x60;bid&#x60;, &#x60;schedule&#x60;, &#x60;targeting&#x60; or &#x60;settings&#x60;. Ignore unknown values. It never carries old or new values, so read the ad set.  ### What the sync detects  From the sync, &#x60;changes&#x60; covers only &#x60;name&#x60; and &#x60;status&#x60;. Status is not detected on Reddit.  ### When it does not fire  History loaded when an account connects is never announced. Budget and targeting edits made through &#x60;PUT /v1/ads/{adId}&#x60; arrive as &#x60;ad.updated&#x60;. 

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
        WebhookPayloadAdSetUpdated webhookPayloadAdSetUpdated = new WebhookPayloadAdSetUpdated(); // WebhookPayloadAdSetUpdated | 
        try {
            apiInstance.onAdSetUpdated(webhookPayloadAdSetUpdated);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAdSetUpdated");
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
| **webhookPayloadAdSetUpdated** | [**WebhookPayloadAdSetUpdated**](WebhookPayloadAdSetUpdated.md)|  | |

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

## onAdSetUpdatedWithHttpInfo

> ApiResponse<Void> onAdSetUpdated onAdSetUpdatedWithHttpInfo(webhookPayloadAdSetUpdated)

Ad set updated event

An ad set was edited through Zernio (&#x60;source: \&quot;zernio\&quot;&#x60;), or outside Zernio and detected by the sync (&#x60;source: \&quot;platform\&quot;&#x60;).  ### When it fires  Fires after the platform and Zernio both accepted the edit. Outside edits arrive up to one sync interval late, and only to the user whose sync saw them.  ### Deduplication  Events are not deduplicated, so every edit is announced. Use the event &#x60;id&#x60; to drop repeats.  ### Payload notes  &#x60;changes&#x60; lists the edited fields: &#x60;name&#x60;, &#x60;status&#x60; (the ad set&#39;s own on/off switch), &#x60;budget&#x60;, &#x60;bid&#x60;, &#x60;schedule&#x60;, &#x60;targeting&#x60; or &#x60;settings&#x60;. Ignore unknown values. It never carries old or new values, so read the ad set.  ### What the sync detects  From the sync, &#x60;changes&#x60; covers only &#x60;name&#x60; and &#x60;status&#x60;. Status is not detected on Reddit.  ### When it does not fire  History loaded when an account connects is never announced. Budget and targeting edits made through &#x60;PUT /v1/ads/{adId}&#x60; arrive as &#x60;ad.updated&#x60;. 

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
        WebhookPayloadAdSetUpdated webhookPayloadAdSetUpdated = new WebhookPayloadAdSetUpdated(); // WebhookPayloadAdSetUpdated | 
        try {
            ApiResponse<Void> response = apiInstance.onAdSetUpdatedWithHttpInfo(webhookPayloadAdSetUpdated);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAdSetUpdated");
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
| **webhookPayloadAdSetUpdated** | [**WebhookPayloadAdSetUpdated**](WebhookPayloadAdSetUpdated.md)|  | |

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

A campaign, ad set or ad on a connected Meta ad account (&#x60;metaads&#x60;) changed status.  ### Sources  Two Meta &#x60;ad_account&#x60; fields feed it: &#x60;in_process_ad_objects&#x60; (finished processing, &#x60;status.raw&#x60; is Meta&#39;s &#x60;status_name&#x60;) and &#x60;with_issues_ad_objects&#x60; (&#x60;status.raw&#x60; is &#x60;WITH_ISSUES&#x60;, &#x60;error&#x60; filled from Meta).  ### Payload notes  &#x60;adObject.level&#x60; is &#x60;CAMPAIGN&#x60;, &#x60;AD_SET&#x60; or &#x60;AD&#x60;; creative-level events are not forwarded. Branch on &#x60;status.raw&#x60;. Use &#x60;error.code&#x60; as the stable discriminator, since &#x60;error.summary&#x60; and &#x60;error.message&#x60; are localized to the owner&#39;s Meta locale.  ### The error block  &#x60;error&#x60; is present on most &#x60;WITH_ISSUES&#x60; events but can be absent, and never appears on any other status. Null-check it before reading &#x60;error.code&#x60;.  ### Fan-out  Matching is keyed on &#x60;adObject.platformAdAccountId&#x60;. When several connected &#x60;metaads&#x60; accounts point at the same Meta ad account, each receives its own delivery. 

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

A campaign, ad set or ad on a connected Meta ad account (&#x60;metaads&#x60;) changed status.  ### Sources  Two Meta &#x60;ad_account&#x60; fields feed it: &#x60;in_process_ad_objects&#x60; (finished processing, &#x60;status.raw&#x60; is Meta&#39;s &#x60;status_name&#x60;) and &#x60;with_issues_ad_objects&#x60; (&#x60;status.raw&#x60; is &#x60;WITH_ISSUES&#x60;, &#x60;error&#x60; filled from Meta).  ### Payload notes  &#x60;adObject.level&#x60; is &#x60;CAMPAIGN&#x60;, &#x60;AD_SET&#x60; or &#x60;AD&#x60;; creative-level events are not forwarded. Branch on &#x60;status.raw&#x60;. Use &#x60;error.code&#x60; as the stable discriminator, since &#x60;error.summary&#x60; and &#x60;error.message&#x60; are localized to the owner&#39;s Meta locale.  ### The error block  &#x60;error&#x60; is present on most &#x60;WITH_ISSUES&#x60; events but can be absent, and never appears on any other status. Null-check it before reading &#x60;error.code&#x60;.  ### Fan-out  Matching is keyed on &#x60;adObject.platformAdAccountId&#x60;. When several connected &#x60;metaads&#x60; accounts point at the same Meta ad account, each receives its own delivery. 

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


## onAdUpdated

> void onAdUpdated(webhookPayloadAdUpdated)

Ad updated event

An ad was edited through Zernio (&#x60;source: \&quot;zernio\&quot;&#x60;), or outside Zernio and detected by the sync (&#x60;source: \&quot;platform\&quot;&#x60;).  ### When it fires  Fires once, to the owner of the edited ad. Outside edits arrive up to one sync interval late. Every edit is announced, so use the event &#x60;id&#x60; to drop repeats.  ### Payload notes  &#x60;changes&#x60; lists the edited fields: &#x60;name&#x60;, &#x60;status&#x60; (the ad&#39;s own on/off switch), &#x60;budget&#x60;, &#x60;targeting&#x60; or &#x60;creative&#x60;. Ignore unknown values; new ones can be added.  ### Reading the change  The event never carries old or new values, so read the ad. &#x60;platformId&#x60; can change when a LinkedIn creative is replaced, while &#x60;adId&#x60; stays stable.  ### When it does not fire  From the sync, &#x60;changes&#x60; covers only &#x60;name&#x60; and &#x60;status&#x60;. Budget, bid, schedule and targeting edits made outside Zernio, tracking tag edits and history loaded at connect are not announced. Ad rule changes arrive as &#x60;ad_rule.triggered&#x60;. 

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
        WebhookPayloadAdUpdated webhookPayloadAdUpdated = new WebhookPayloadAdUpdated(); // WebhookPayloadAdUpdated | 
        try {
            apiInstance.onAdUpdated(webhookPayloadAdUpdated);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAdUpdated");
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
| **webhookPayloadAdUpdated** | [**WebhookPayloadAdUpdated**](WebhookPayloadAdUpdated.md)|  | |

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

## onAdUpdatedWithHttpInfo

> ApiResponse<Void> onAdUpdated onAdUpdatedWithHttpInfo(webhookPayloadAdUpdated)

Ad updated event

An ad was edited through Zernio (&#x60;source: \&quot;zernio\&quot;&#x60;), or outside Zernio and detected by the sync (&#x60;source: \&quot;platform\&quot;&#x60;).  ### When it fires  Fires once, to the owner of the edited ad. Outside edits arrive up to one sync interval late. Every edit is announced, so use the event &#x60;id&#x60; to drop repeats.  ### Payload notes  &#x60;changes&#x60; lists the edited fields: &#x60;name&#x60;, &#x60;status&#x60; (the ad&#39;s own on/off switch), &#x60;budget&#x60;, &#x60;targeting&#x60; or &#x60;creative&#x60;. Ignore unknown values; new ones can be added.  ### Reading the change  The event never carries old or new values, so read the ad. &#x60;platformId&#x60; can change when a LinkedIn creative is replaced, while &#x60;adId&#x60; stays stable.  ### When it does not fire  From the sync, &#x60;changes&#x60; covers only &#x60;name&#x60; and &#x60;status&#x60;. Budget, bid, schedule and targeting edits made outside Zernio, tracking tag edits and history loaded at connect are not announced. Ad rule changes arrive as &#x60;ad_rule.triggered&#x60;. 

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
        WebhookPayloadAdUpdated webhookPayloadAdUpdated = new WebhookPayloadAdUpdated(); // WebhookPayloadAdUpdated | 
        try {
            ApiResponse<Void> response = apiInstance.onAdUpdatedWithHttpInfo(webhookPayloadAdUpdated);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAdUpdated");
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
| **webhookPayloadAdUpdated** | [**WebhookPayloadAdUpdated**](WebhookPayloadAdUpdated.md)|  | |

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

Meta finished processing a video uploaded with &#x60;async: true&#x60; on &#x60;POST /v1/ads/videos&#x60;.  ### Payload notes  &#x60;video.status&#x60; is &#x60;ready&#x60; (reference it as &#x60;video.id&#x60; on the create endpoints) or &#x60;error&#x60;, with &#x60;video.error&#x60; carrying the reason.  ### When it fires  Fires once per upload, when the video leaves &#x60;processing&#x60;. Zernio polls every 10 seconds for about 13 minutes; after that no event is sent, so read &#x60;GET /v1/ads/videos/{videoId}&#x60; for long videos. 

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

Meta finished processing a video uploaded with &#x60;async: true&#x60; on &#x60;POST /v1/ads/videos&#x60;.  ### Payload notes  &#x60;video.status&#x60; is &#x60;ready&#x60; (reference it as &#x60;video.id&#x60; on the create endpoints) or &#x60;error&#x60;, with &#x60;video.error&#x60; carrying the reason.  ### When it fires  Fires once per upload, when the video leaves &#x60;processing&#x60;. Zernio polls every 10 seconds for about 13 minutes; after that no event is sent, so read &#x60;GET /v1/ads/videos/{videoId}&#x60; for long videos. 

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

One connected account&#39;s analytics sync cycle completed successfully.  ### Payload notes  It is a trigger: no metrics and no cursor. On receipt, call &#x60;GET /v1/analytics/delta&#x60; with your own last &#x60;nextCursor&#x60; to read what changed across every account.  ### When it fires  Per account, per successful sync cycle, roughly hourly. It does not fire for a failed or skipped cycle, an inactive or disconnected account, or a platform without analytics sync.  ### Empty page  The feed is a materialized view, so an immediate read can return an empty &#x60;data&#x60; array. Re-poll with the same cursor. Advancing on an empty page can lose changes permanently.  ### Use a dedicated endpoint  Volume is about one event per account per hour. The consecutive-failure count is shared by every event on an endpoint, so an outage here can disable it and silence events like &#x60;post.published&#x60;. 

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

One connected account&#39;s analytics sync cycle completed successfully.  ### Payload notes  It is a trigger: no metrics and no cursor. On receipt, call &#x60;GET /v1/analytics/delta&#x60; with your own last &#x60;nextCursor&#x60; to read what changed across every account.  ### When it fires  Per account, per successful sync cycle, roughly hourly. It does not fire for a failed or skipped cycle, an inactive or disconnected account, or a platform without analytics sync.  ### Empty page  The feed is a materialized view, so an immediate read can return an empty &#x60;data&#x60; array. Re-poll with the same cursor. Advancing on an empty page can lose changes permanently.  ### Use a dedicated endpoint  Volume is about one event per account per hour. The consecutive-failure count is shared by every event on an endpoint, so an outage here can disable it and silence events like &#x60;post.published&#x60;. 

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

An entry was published to the API changelog when a change to the OpenAPI spec went live.  ### Who receives it  It belongs to no profile or account. Every active endpoint subscribed to it receives it; endpoints scoped with &#x60;profileIds&#x60; or &#x60;accountIds&#x60; do not. One subscription per integration is enough.  ### Payload notes  &#x60;entry.type&#x60;, &#x60;entry.message&#x60; (the announcement), &#x60;entry.url&#x60;, &#x60;entry.specVersion&#x60;, &#x60;entry.impact&#x60; (&#x60;action_required&#x60;, &#x60;additive&#x60; or &#x60;none&#x60;) and &#x60;entry.changes&#x60; (the spec diff as data).  ### How to act  Automate on &#x60;impact&#x60;, &#x60;changes&#x60; and &#x60;type&#x60;; read &#x60;message&#x60; for the reason. &#x60;GET /v1/changelog&#x60; lists entries newest first, to back-fill after downtime. 

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

An entry was published to the API changelog when a change to the OpenAPI spec went live.  ### Who receives it  It belongs to no profile or account. Every active endpoint subscribed to it receives it; endpoints scoped with &#x60;profileIds&#x60; or &#x60;accountIds&#x60; do not. One subscription per integration is enough.  ### Payload notes  &#x60;entry.type&#x60;, &#x60;entry.message&#x60; (the announcement), &#x60;entry.url&#x60;, &#x60;entry.specVersion&#x60;, &#x60;entry.impact&#x60; (&#x60;action_required&#x60;, &#x60;additive&#x60; or &#x60;none&#x60;) and &#x60;entry.changes&#x60; (the spec diff as data).  ### How to act  Automate on &#x60;impact&#x60;, &#x60;changes&#x60; and &#x60;type&#x60;; read &#x60;message&#x60; for the reason. &#x60;GET /v1/changelog&#x60; lists entries newest first, to back-fill after downtime. 

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


## onAutomationActionApplied

> void onAutomationActionApplied(webhookPayloadAutomationAction)

Automation action applied event

An automation changed something, such as an ad set paused or a budget raised.  ### Payload notes  &#x60;previous&#x60; and &#x60;target&#x60; carry the value before and the value set. Each action sends one event; dedupe on &#x60;id&#x60;, which stays the same if the event is sent again. 

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
        WebhookPayloadAutomationAction webhookPayloadAutomationAction = new WebhookPayloadAutomationAction(); // WebhookPayloadAutomationAction | 
        try {
            apiInstance.onAutomationActionApplied(webhookPayloadAutomationAction);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAutomationActionApplied");
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
| **webhookPayloadAutomationAction** | [**WebhookPayloadAutomationAction**](WebhookPayloadAutomationAction.md)|  | |

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
| **200** | Webhook received |  -  |

## onAutomationActionAppliedWithHttpInfo

> ApiResponse<Void> onAutomationActionApplied onAutomationActionAppliedWithHttpInfo(webhookPayloadAutomationAction)

Automation action applied event

An automation changed something, such as an ad set paused or a budget raised.  ### Payload notes  &#x60;previous&#x60; and &#x60;target&#x60; carry the value before and the value set. Each action sends one event; dedupe on &#x60;id&#x60;, which stays the same if the event is sent again. 

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
        WebhookPayloadAutomationAction webhookPayloadAutomationAction = new WebhookPayloadAutomationAction(); // WebhookPayloadAutomationAction | 
        try {
            ApiResponse<Void> response = apiInstance.onAutomationActionAppliedWithHttpInfo(webhookPayloadAutomationAction);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAutomationActionApplied");
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
| **webhookPayloadAutomationAction** | [**WebhookPayloadAutomationAction**](WebhookPayloadAutomationAction.md)|  | |

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
| **200** | Webhook received |  -  |


## onAutomationActionFailed

> void onAutomationActionFailed(webhookPayloadAutomationAction)

Automation action failed event

An automation change failed or was refused; &#x60;reason&#x60; says why.  ### Skipped changes  A change refused before any platform call has &#x60;status: skipped&#x60;, for example no live ads or a budget at its limit. 

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
        WebhookPayloadAutomationAction webhookPayloadAutomationAction = new WebhookPayloadAutomationAction(); // WebhookPayloadAutomationAction | 
        try {
            apiInstance.onAutomationActionFailed(webhookPayloadAutomationAction);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAutomationActionFailed");
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
| **webhookPayloadAutomationAction** | [**WebhookPayloadAutomationAction**](WebhookPayloadAutomationAction.md)|  | |

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
| **200** | Webhook received |  -  |

## onAutomationActionFailedWithHttpInfo

> ApiResponse<Void> onAutomationActionFailed onAutomationActionFailedWithHttpInfo(webhookPayloadAutomationAction)

Automation action failed event

An automation change failed or was refused; &#x60;reason&#x60; says why.  ### Skipped changes  A change refused before any platform call has &#x60;status: skipped&#x60;, for example no live ads or a budget at its limit. 

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
        WebhookPayloadAutomationAction webhookPayloadAutomationAction = new WebhookPayloadAutomationAction(); // WebhookPayloadAutomationAction | 
        try {
            ApiResponse<Void> response = apiInstance.onAutomationActionFailedWithHttpInfo(webhookPayloadAutomationAction);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAutomationActionFailed");
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
| **webhookPayloadAutomationAction** | [**WebhookPayloadAutomationAction**](WebhookPayloadAutomationAction.md)|  | |

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
| **200** | Webhook received |  -  |


## onAutomationActionUnknown

> void onAutomationActionUnknown(webhookPayloadAutomationAction)

Automation action unknown event

The platform did not answer, so it is unknown whether the automation&#39;s change happened.  ### What happens next  The next check reads the object back and sends &#x60;applied&#x60; or &#x60;failed&#x60;. 

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
        WebhookPayloadAutomationAction webhookPayloadAutomationAction = new WebhookPayloadAutomationAction(); // WebhookPayloadAutomationAction | 
        try {
            apiInstance.onAutomationActionUnknown(webhookPayloadAutomationAction);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAutomationActionUnknown");
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
| **webhookPayloadAutomationAction** | [**WebhookPayloadAutomationAction**](WebhookPayloadAutomationAction.md)|  | |

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
| **200** | Webhook received |  -  |

## onAutomationActionUnknownWithHttpInfo

> ApiResponse<Void> onAutomationActionUnknown onAutomationActionUnknownWithHttpInfo(webhookPayloadAutomationAction)

Automation action unknown event

The platform did not answer, so it is unknown whether the automation&#39;s change happened.  ### What happens next  The next check reads the object back and sends &#x60;applied&#x60; or &#x60;failed&#x60;. 

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
        WebhookPayloadAutomationAction webhookPayloadAutomationAction = new WebhookPayloadAutomationAction(); // WebhookPayloadAutomationAction | 
        try {
            ApiResponse<Void> response = apiInstance.onAutomationActionUnknownWithHttpInfo(webhookPayloadAutomationAction);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAutomationActionUnknown");
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
| **webhookPayloadAutomationAction** | [**WebhookPayloadAutomationAction**](WebhookPayloadAutomationAction.md)|  | |

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
| **200** | Webhook received |  -  |


## onAutomationAlertEscalated

> void onAutomationAlertEscalated(webhookPayloadAutomationAlert)

Automation alert escalated event

An open alert&#39;s &#x60;critical&#x60; conditions held.  ### When it fires  Sent once per episode. 

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
        WebhookPayloadAutomationAlert webhookPayloadAutomationAlert = new WebhookPayloadAutomationAlert(); // WebhookPayloadAutomationAlert | 
        try {
            apiInstance.onAutomationAlertEscalated(webhookPayloadAutomationAlert);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAutomationAlertEscalated");
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
| **webhookPayloadAutomationAlert** | [**WebhookPayloadAutomationAlert**](WebhookPayloadAutomationAlert.md)|  | |

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
| **200** | Webhook received |  -  |

## onAutomationAlertEscalatedWithHttpInfo

> ApiResponse<Void> onAutomationAlertEscalated onAutomationAlertEscalatedWithHttpInfo(webhookPayloadAutomationAlert)

Automation alert escalated event

An open alert&#39;s &#x60;critical&#x60; conditions held.  ### When it fires  Sent once per episode. 

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
        WebhookPayloadAutomationAlert webhookPayloadAutomationAlert = new WebhookPayloadAutomationAlert(); // WebhookPayloadAutomationAlert | 
        try {
            ApiResponse<Void> response = apiInstance.onAutomationAlertEscalatedWithHttpInfo(webhookPayloadAutomationAlert);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAutomationAlertEscalated");
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
| **webhookPayloadAutomationAlert** | [**WebhookPayloadAutomationAlert**](WebhookPayloadAutomationAlert.md)|  | |

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
| **200** | Webhook received |  -  |


## onAutomationAlertOpened

> void onAutomationAlertOpened(webhookPayloadAutomationAlert)

Automation alert opened event

An object matched the rule&#39;s conditions for &#x60;confirmChecks&#x60; runs in a row and its action was recorded.  ### When it fires  Sent once per episode. 

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
        WebhookPayloadAutomationAlert webhookPayloadAutomationAlert = new WebhookPayloadAutomationAlert(); // WebhookPayloadAutomationAlert | 
        try {
            apiInstance.onAutomationAlertOpened(webhookPayloadAutomationAlert);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAutomationAlertOpened");
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
| **webhookPayloadAutomationAlert** | [**WebhookPayloadAutomationAlert**](WebhookPayloadAutomationAlert.md)|  | |

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
| **200** | Webhook received |  -  |

## onAutomationAlertOpenedWithHttpInfo

> ApiResponse<Void> onAutomationAlertOpened onAutomationAlertOpenedWithHttpInfo(webhookPayloadAutomationAlert)

Automation alert opened event

An object matched the rule&#39;s conditions for &#x60;confirmChecks&#x60; runs in a row and its action was recorded.  ### When it fires  Sent once per episode. 

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
        WebhookPayloadAutomationAlert webhookPayloadAutomationAlert = new WebhookPayloadAutomationAlert(); // WebhookPayloadAutomationAlert | 
        try {
            ApiResponse<Void> response = apiInstance.onAutomationAlertOpenedWithHttpInfo(webhookPayloadAutomationAlert);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAutomationAlertOpened");
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
| **webhookPayloadAutomationAlert** | [**WebhookPayloadAutomationAlert**](WebhookPayloadAutomationAlert.md)|  | |

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
| **200** | Webhook received |  -  |


## onAutomationAlertResolved

> void onAutomationAlertResolved(webhookPayloadAutomationAlert)

Automation alert resolved event

An open alert ended; &#x60;reason&#x60; says which way.  ### Reasons  Its conditions cleared, a pause or reactivation applied, the rule changed, or nothing checked the object for 7 days. 

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
        WebhookPayloadAutomationAlert webhookPayloadAutomationAlert = new WebhookPayloadAutomationAlert(); // WebhookPayloadAutomationAlert | 
        try {
            apiInstance.onAutomationAlertResolved(webhookPayloadAutomationAlert);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAutomationAlertResolved");
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
| **webhookPayloadAutomationAlert** | [**WebhookPayloadAutomationAlert**](WebhookPayloadAutomationAlert.md)|  | |

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
| **200** | Webhook received |  -  |

## onAutomationAlertResolvedWithHttpInfo

> ApiResponse<Void> onAutomationAlertResolved onAutomationAlertResolvedWithHttpInfo(webhookPayloadAutomationAlert)

Automation alert resolved event

An open alert ended; &#x60;reason&#x60; says which way.  ### Reasons  Its conditions cleared, a pause or reactivation applied, the rule changed, or nothing checked the object for 7 days. 

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
        WebhookPayloadAutomationAlert webhookPayloadAutomationAlert = new WebhookPayloadAutomationAlert(); // WebhookPayloadAutomationAlert | 
        try {
            ApiResponse<Void> response = apiInstance.onAutomationAlertResolvedWithHttpInfo(webhookPayloadAutomationAlert);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAutomationAlertResolved");
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
| **webhookPayloadAutomationAlert** | [**WebhookPayloadAutomationAlert**](WebhookPayloadAutomationAlert.md)|  | |

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
| **200** | Webhook received |  -  |


## onAutomationCheckCompleted

> void onAutomationCheckCompleted(webhookPayloadAutomationCheckCompleted)

Automation check completed event

One scheduled check of an automation finished, including checks where nothing matched.  ### Payload notes  &#x60;automation.kind&#x60; names the product: &#x60;ad_rule&#x60; today, more as other automations move onto the same engine. 

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
        WebhookPayloadAutomationCheckCompleted webhookPayloadAutomationCheckCompleted = new WebhookPayloadAutomationCheckCompleted(); // WebhookPayloadAutomationCheckCompleted | 
        try {
            apiInstance.onAutomationCheckCompleted(webhookPayloadAutomationCheckCompleted);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAutomationCheckCompleted");
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
| **webhookPayloadAutomationCheckCompleted** | [**WebhookPayloadAutomationCheckCompleted**](WebhookPayloadAutomationCheckCompleted.md)|  | |

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
| **200** | Webhook received |  -  |

## onAutomationCheckCompletedWithHttpInfo

> ApiResponse<Void> onAutomationCheckCompleted onAutomationCheckCompletedWithHttpInfo(webhookPayloadAutomationCheckCompleted)

Automation check completed event

One scheduled check of an automation finished, including checks where nothing matched.  ### Payload notes  &#x60;automation.kind&#x60; names the product: &#x60;ad_rule&#x60; today, more as other automations move onto the same engine. 

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
        WebhookPayloadAutomationCheckCompleted webhookPayloadAutomationCheckCompleted = new WebhookPayloadAutomationCheckCompleted(); // WebhookPayloadAutomationCheckCompleted | 
        try {
            ApiResponse<Void> response = apiInstance.onAutomationCheckCompletedWithHttpInfo(webhookPayloadAutomationCheckCompleted);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onAutomationCheckCompleted");
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
| **webhookPayloadAutomationCheckCompleted** | [**WebhookPayloadAutomationCheckCompleted**](WebhookPayloadAutomationCheckCompleted.md)|  | |

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
| **200** | Webhook received |  -  |


## onBalanceCharged

> void onBalanceCharged(webhookPayloadBalanceCharged)

Balance charged event

Balance billing only. Funds were added to the balance by card: by someone (&#x60;trigger: manual&#x60;) or by the auto top-up rule (&#x60;trigger: auto_top_up&#x60;).  ### When it fires  Once per card payment into the balance, when it is credited. Stripe emails the billing owner its receipt for the charge.  ### Payload notes  &#x60;topup.amountCents&#x60; was added to the balance; the card was charged &#x60;topup.chargedCents&#x60;, which is that plus &#x60;topup.taxCents&#x60; (VAT, 0 when none applies). The invoice and receipt are at &#x60;GET /v1/balance/top-ups/{topupId}/invoice&#x60; and &#x60;/receipt&#x60;.  ### Who receives it  The billing owner&#39;s endpoints, like &#x60;balance.low&#x60;. Restricted keys need the &#x60;money&#x60; resource group. 

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
        WebhookPayloadBalanceCharged webhookPayloadBalanceCharged = new WebhookPayloadBalanceCharged(); // WebhookPayloadBalanceCharged | 
        try {
            apiInstance.onBalanceCharged(webhookPayloadBalanceCharged);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onBalanceCharged");
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
| **webhookPayloadBalanceCharged** | [**WebhookPayloadBalanceCharged**](WebhookPayloadBalanceCharged.md)|  | |

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

## onBalanceChargedWithHttpInfo

> ApiResponse<Void> onBalanceCharged onBalanceChargedWithHttpInfo(webhookPayloadBalanceCharged)

Balance charged event

Balance billing only. Funds were added to the balance by card: by someone (&#x60;trigger: manual&#x60;) or by the auto top-up rule (&#x60;trigger: auto_top_up&#x60;).  ### When it fires  Once per card payment into the balance, when it is credited. Stripe emails the billing owner its receipt for the charge.  ### Payload notes  &#x60;topup.amountCents&#x60; was added to the balance; the card was charged &#x60;topup.chargedCents&#x60;, which is that plus &#x60;topup.taxCents&#x60; (VAT, 0 when none applies). The invoice and receipt are at &#x60;GET /v1/balance/top-ups/{topupId}/invoice&#x60; and &#x60;/receipt&#x60;.  ### Who receives it  The billing owner&#39;s endpoints, like &#x60;balance.low&#x60;. Restricted keys need the &#x60;money&#x60; resource group. 

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
        WebhookPayloadBalanceCharged webhookPayloadBalanceCharged = new WebhookPayloadBalanceCharged(); // WebhookPayloadBalanceCharged | 
        try {
            ApiResponse<Void> response = apiInstance.onBalanceChargedWithHttpInfo(webhookPayloadBalanceCharged);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onBalanceCharged");
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
| **webhookPayloadBalanceCharged** | [**WebhookPayloadBalanceCharged**](WebhookPayloadBalanceCharged.md)|  | |

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


## onBalanceEmpty

> void onBalanceEmpty(webhookPayloadBalanceEmpty)

Balance empty event

Balance billing only. The balance reached $0 and no auto top-up covered it (auto top-up off, the card declined, or the monthly limit reached), so new pay-per-use (SMS, calls, numbers, X and the rest) answers 402 with &#x60;code&#x60; until the balance is funded.  ### When it fires  Once per time the balance runs out, within about a minute of the usage that emptied it. Funding the balance and running out again fires it again.  ### Who receives it  The billing owner&#39;s endpoints, like &#x60;balance.low&#x60;. Restricted keys need the &#x60;money&#x60; resource group.  ### How to act  Send the user to &#x60;fundingUrl&#x60;, or, for &#x60;usage_limit_reached&#x60;, raise &#x60;monthlyLimitCents&#x60; with &#x60;PATCH /v1/balance/auto-recharge&#x60;. 

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
        WebhookPayloadBalanceEmpty webhookPayloadBalanceEmpty = new WebhookPayloadBalanceEmpty(); // WebhookPayloadBalanceEmpty | 
        try {
            apiInstance.onBalanceEmpty(webhookPayloadBalanceEmpty);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onBalanceEmpty");
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
| **webhookPayloadBalanceEmpty** | [**WebhookPayloadBalanceEmpty**](WebhookPayloadBalanceEmpty.md)|  | |

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

## onBalanceEmptyWithHttpInfo

> ApiResponse<Void> onBalanceEmpty onBalanceEmptyWithHttpInfo(webhookPayloadBalanceEmpty)

Balance empty event

Balance billing only. The balance reached $0 and no auto top-up covered it (auto top-up off, the card declined, or the monthly limit reached), so new pay-per-use (SMS, calls, numbers, X and the rest) answers 402 with &#x60;code&#x60; until the balance is funded.  ### When it fires  Once per time the balance runs out, within about a minute of the usage that emptied it. Funding the balance and running out again fires it again.  ### Who receives it  The billing owner&#39;s endpoints, like &#x60;balance.low&#x60;. Restricted keys need the &#x60;money&#x60; resource group.  ### How to act  Send the user to &#x60;fundingUrl&#x60;, or, for &#x60;usage_limit_reached&#x60;, raise &#x60;monthlyLimitCents&#x60; with &#x60;PATCH /v1/balance/auto-recharge&#x60;. 

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
        WebhookPayloadBalanceEmpty webhookPayloadBalanceEmpty = new WebhookPayloadBalanceEmpty(); // WebhookPayloadBalanceEmpty | 
        try {
            ApiResponse<Void> response = apiInstance.onBalanceEmptyWithHttpInfo(webhookPayloadBalanceEmpty);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onBalanceEmpty");
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
| **webhookPayloadBalanceEmpty** | [**WebhookPayloadBalanceEmpty**](WebhookPayloadBalanceEmpty.md)|  | |

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


## onBalanceLow

> void onBalanceLow(webhookPayloadBalanceLow)

Balance low event

Balance billing only. The balance dropped below the low-balance alert set on auto top-up (&#x60;alertBelowCents&#x60; on &#x60;GET /v1/balance/auto-recharge&#x60;).  ### When it fires  Once per drop below the threshold; a balance back at or above it re-arms the next one. It does not fire when an auto top-up is already covering the drop, and never when no alert is set.  ### Who receives it  It belongs to the billing owner, not to a profile or account: endpoints scoped with &#x60;profileIds&#x60; or &#x60;accountIds&#x60; do not receive it. Restricted keys need the &#x60;money&#x60; resource group.  ### How to act  Send the user to &#x60;fundingUrl&#x60; (Billing with the Add funds drawer open), or add funds through the API. 

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
        WebhookPayloadBalanceLow webhookPayloadBalanceLow = new WebhookPayloadBalanceLow(); // WebhookPayloadBalanceLow | 
        try {
            apiInstance.onBalanceLow(webhookPayloadBalanceLow);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onBalanceLow");
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
| **webhookPayloadBalanceLow** | [**WebhookPayloadBalanceLow**](WebhookPayloadBalanceLow.md)|  | |

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

## onBalanceLowWithHttpInfo

> ApiResponse<Void> onBalanceLow onBalanceLowWithHttpInfo(webhookPayloadBalanceLow)

Balance low event

Balance billing only. The balance dropped below the low-balance alert set on auto top-up (&#x60;alertBelowCents&#x60; on &#x60;GET /v1/balance/auto-recharge&#x60;).  ### When it fires  Once per drop below the threshold; a balance back at or above it re-arms the next one. It does not fire when an auto top-up is already covering the drop, and never when no alert is set.  ### Who receives it  It belongs to the billing owner, not to a profile or account: endpoints scoped with &#x60;profileIds&#x60; or &#x60;accountIds&#x60; do not receive it. Restricted keys need the &#x60;money&#x60; resource group.  ### How to act  Send the user to &#x60;fundingUrl&#x60; (Billing with the Add funds drawer open), or add funds through the API. 

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
        WebhookPayloadBalanceLow webhookPayloadBalanceLow = new WebhookPayloadBalanceLow(); // WebhookPayloadBalanceLow | 
        try {
            ApiResponse<Void> response = apiInstance.onBalanceLowWithHttpInfo(webhookPayloadBalanceLow);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onBalanceLow");
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
| **webhookPayloadBalanceLow** | [**WebhookPayloadBalanceLow**](WebhookPayloadBalanceLow.md)|  | |

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

A Branded Calling caller identity is waiting on you; &#x60;reason&#x60; says what.  ### When it fires  Every &#x60;action_required&#x60; is paired with a &#x60;status_updated&#x60;.  ### Reasons  - &#x60;changes_requested&#x60;: answer the review with &#x60;PATCH&#x60;. - &#x60;email_code&#x60;: confirm the code the carrier emailed the authorizer. - &#x60;rejected&#x60;: fix and &#x60;PATCH&#x60;. - &#x60;expired&#x60;: resubmit.  ### Infringement claim  &#x60;infringement_claim&#x60;: a third party filed a trademark or impersonation claim and the carrier suspended the identity. Calls show a plain number and the monthly fee pauses until it is resolved.  Reply to our email with evidence that the name and logo are yours. If the claim is upheld, the identity is rejected for good. 

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

A Branded Calling caller identity is waiting on you; &#x60;reason&#x60; says what.  ### When it fires  Every &#x60;action_required&#x60; is paired with a &#x60;status_updated&#x60;.  ### Reasons  - &#x60;changes_requested&#x60;: answer the review with &#x60;PATCH&#x60;. - &#x60;email_code&#x60;: confirm the code the carrier emailed the authorizer. - &#x60;rejected&#x60;: fix and &#x60;PATCH&#x60;. - &#x60;expired&#x60;: resubmit.  ### Infringement claim  &#x60;infringement_claim&#x60;: a third party filed a trademark or impersonation claim and the carrier suspended the identity. Calls show a plain number and the monthly fee pauses until it is resolved.  Reply to our email with evidence that the name and logo are yours. If the claim is upheld, the identity is rejected for good. 

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

A Branded Calling caller identity changed status.  ### When it fires  Fires once per transition of the identity&#39;s &#x60;status&#x60;, the value &#x60;GET /v1/branded-calling/identities/{id}&#x60; returns. Never on a re-check that found nothing new.  ### Statuses  &#x60;requested&#x60;, &#x60;changes_requested&#x60;, &#x60;rejected&#x60; (&#x60;reason&#x60; says why), &#x60;pending_email_verification&#x60;, &#x60;in_review&#x60;, &#x60;verified&#x60; (live for a year, attach numbers), &#x60;suspended&#x60; (infringement claim open), &#x60;expired&#x60;, &#x60;permanently_rejected&#x60;. 

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

A Branded Calling caller identity changed status.  ### When it fires  Fires once per transition of the identity&#39;s &#x60;status&#x60;, the value &#x60;GET /v1/branded-calling/identities/{id}&#x60; returns. Never on a re-check that found nothing new.  ### Statuses  &#x60;requested&#x60;, &#x60;changes_requested&#x60;, &#x60;rejected&#x60; (&#x60;reason&#x60; says why), &#x60;pending_email_verification&#x60;, &#x60;in_review&#x60;, &#x60;verified&#x60; (live for a year, attach numbers), &#x60;suspended&#x60; (infringement claim open), &#x60;expired&#x60;, &#x60;permanently_rejected&#x60;. 

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

A number attached to a Branded Calling identity changed vetting status.  ### When it fires  Only starts once the identity is &#x60;verified&#x60; and you attached numbers. A batch is vetted as a unit; each number reports its own status.  ### Statuses  &#x60;submitted&#x60;, &#x60;in_review&#x60;, &#x60;verified&#x60; (calls from it show the identity), &#x60;unsuccessful&#x60; (refused; detach and re-add to retry), &#x60;suspended&#x60;, &#x60;expired&#x60;, &#x60;permanently_rejected&#x60; (can never be branded again). 

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

A number attached to a Branded Calling identity changed vetting status.  ### When it fires  Only starts once the identity is &#x60;verified&#x60; and you attached numbers. A batch is vetted as a unit; each number reports its own status.  ### Statuses  &#x60;submitted&#x60;, &#x60;in_review&#x60;, &#x60;verified&#x60; (calls from it show the identity), &#x60;unsuccessful&#x60; (refused; detach and re-add to retry), &#x60;suspended&#x60;, &#x60;expired&#x60;, &#x60;permanently_rejected&#x60; (can never be branded again). 

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

An event was added to the primary calendar of a connected mailbox, by the user, an invitation or the API.  ### Platform notes  On Microsoft the change is pushed seconds after it happens. 

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

An event was added to the primary calendar of a connected mailbox, by the user, an invitation or the API.  ### Platform notes  On Microsoft the change is pushed seconds after it happens. 

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

An event was deleted from the primary calendar.  ### Platform notes  On Google, a cancelled event counts as deleted. 

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

An event was deleted from the primary calendar.  ### Platform notes  On Google, a cancelled event counts as deleted. 

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

An event on the primary calendar changed: its time, details or participants&#39; answers. 

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

An event on the primary calendar changed: its time, details or participants&#39; answers. 

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

A phone or WhatsApp call ended; carries duration, end reason and a zero-markup cost breakdown.  ### Payload notes  &#x60;durationSeconds&#x60;; &#x60;endReason&#x60; is &#x60;hangup&#x60;, &#x60;no_answer&#x60;, &#x60;rejected&#x60; or &#x60;error&#x60;; &#x60;call.billing&#x60; holds Meta cost, Telnyx cost, recording surcharge and total. Costs are pass-through, with no margin.  ### When it fires  Unanswered, busy and rejected calls end here too. Branch on &#x60;endReason&#x60;; &#x60;call.failed&#x60; is for hard errors.  ### Recordings  With recording enabled, the payload carries &#x60;recordingUrl&#x60;, a signed URL expiring at &#x60;recordingExpiresAt&#x60;. Fetch a fresh one with &#x60;GET /v1/calls/{id}/recording&#x60; and &#x60;call.id&#x60;.  ### Missed-call follow-up  Check for &#x60;endReason: \&quot;no_answer\&quot;&#x60;, then text the caller over the linked &#x60;conversationId&#x60;. 

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

A phone or WhatsApp call ended; carries duration, end reason and a zero-markup cost breakdown.  ### Payload notes  &#x60;durationSeconds&#x60;; &#x60;endReason&#x60; is &#x60;hangup&#x60;, &#x60;no_answer&#x60;, &#x60;rejected&#x60; or &#x60;error&#x60;; &#x60;call.billing&#x60; holds Meta cost, Telnyx cost, recording surcharge and total. Costs are pass-through, with no margin.  ### When it fires  Unanswered, busy and rejected calls end here too. Branch on &#x60;endReason&#x60;; &#x60;call.failed&#x60; is for hard errors.  ### Recordings  With recording enabled, the payload carries &#x60;recordingUrl&#x60;, a signed URL expiring at &#x60;recordingExpiresAt&#x60;. Fetch a fresh one with &#x60;GET /v1/calls/{id}/recording&#x60; and &#x60;call.id&#x60;.  ### Missed-call follow-up  Check for &#x60;endReason: \&quot;no_answer\&quot;&#x60;, then text the caller over the linked &#x60;conversationId&#x60;. 

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

A call failed with a hard error before or during bridging, for example the destination rejected the SIP INVITE.  ### Payload notes  Carries the upstream error &#x60;code&#x60; and &#x60;message&#x60;, for example when Meta rejected the connect or Telnyx returned an error. 

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

A call failed with a hard error before or during bridging, for example the destination rejected the SIP INVITE.  ### Payload notes  Carries the upstream error &#x60;code&#x60; and &#x60;message&#x60;, for example when Meta rejected the connect or Telnyx returned an error. 

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

A WhatsApp user accepted or rejected your call-permission request.  ### When it fires  Independent of any call: it reports a reply to a permission prompt. Meta permits a business-initiated call only after the consumer taps Allow, and the accept can land days before the call.  ### Payload notes  &#x60;response&#x60; is &#x60;accept&#x60; or &#x60;reject&#x60;. Also carries the user&#39;s number, whether the grant is permanent, and the expiry when it is not. 

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

A WhatsApp user accepted or rejected your call-permission request.  ### When it fires  Independent of any call: it reports a reply to a permission prompt. Meta permits a business-initiated call only after the consumer taps Allow, and the accept can land days before the call.  ### Payload notes  &#x60;response&#x60; is &#x60;accept&#x60; or &#x60;reject&#x60;. Also carries the user&#39;s number, whether the grant is permanent, and the expiry when it is not. 

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

An inbound phone or WhatsApp call reached your number, or an outbound WhatsApp call was placed.  ### When it fires  Fires at ring time, before anyone answers; an unanswered call still emits it, then &#x60;call.ended&#x60; with &#x60;endReason: \&quot;no_answer\&quot;&#x60;. Outbound WhatsApp calls fire at origination with &#x60;direction: \&quot;outbound\&quot;&#x60;. Outbound phone calls never emit it.  ### Payload notes  Carries the Zernio call id, the caller and business numbers, the destination snapshot (&#x60;forwardTo&#x60;), and &#x60;contactId&#x60; and &#x60;conversationId&#x60; to message the caller with the regular send endpoints. 

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

An inbound phone or WhatsApp call reached your number, or an outbound WhatsApp call was placed.  ### When it fires  Fires at ring time, before anyone answers; an unanswered call still emits it, then &#x60;call.ended&#x60; with &#x60;endReason: \&quot;no_answer\&quot;&#x60;. Outbound WhatsApp calls fire at origination with &#x60;direction: \&quot;outbound\&quot;&#x60;. Outbound phone calls never emit it.  ### Payload notes  Carries the Zernio call id, the caller and business numbers, the destination snapshot (&#x60;forwardTo&#x60;), and &#x60;contactId&#x60; and &#x60;conversationId&#x60; to message the caller with the regular send endpoints. 

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


## onCallRecordingReady

> void onCallRecordingReady(webhookPayloadCallRecordingReady)

Call recording ready event

A call recording is ready to download.  ### When it fires  Only for teams with zero content retention, on calls with recording on, and only while a webhook listens to it. Zernio keeps no recording for these teams, and the copy behind the link expires after about 3 days. Download the file before &#x60;recording.expiresAt&#x60;.  ### Payload notes  &#x60;call.isVoicemail&#x60; tells a voicemail from a recorded call. If the recording could not be copied, no event fires and &#x60;call.ended&#x60; lists it in &#x60;callErrors&#x60;. 

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
        WebhookPayloadCallRecordingReady webhookPayloadCallRecordingReady = new WebhookPayloadCallRecordingReady(); // WebhookPayloadCallRecordingReady | 
        try {
            apiInstance.onCallRecordingReady(webhookPayloadCallRecordingReady);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCallRecordingReady");
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
| **webhookPayloadCallRecordingReady** | [**WebhookPayloadCallRecordingReady**](WebhookPayloadCallRecordingReady.md)|  | |

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

## onCallRecordingReadyWithHttpInfo

> ApiResponse<Void> onCallRecordingReady onCallRecordingReadyWithHttpInfo(webhookPayloadCallRecordingReady)

Call recording ready event

A call recording is ready to download.  ### When it fires  Only for teams with zero content retention, on calls with recording on, and only while a webhook listens to it. Zernio keeps no recording for these teams, and the copy behind the link expires after about 3 days. Download the file before &#x60;recording.expiresAt&#x60;.  ### Payload notes  &#x60;call.isVoicemail&#x60; tells a voicemail from a recorded call. If the recording could not be copied, no event fires and &#x60;call.ended&#x60; lists it in &#x60;callErrors&#x60;. 

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
        WebhookPayloadCallRecordingReady webhookPayloadCallRecordingReady = new WebhookPayloadCallRecordingReady(); // WebhookPayloadCallRecordingReady | 
        try {
            ApiResponse<Void> response = apiInstance.onCallRecordingReadyWithHttpInfo(webhookPayloadCallRecordingReady);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCallRecordingReady");
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
| **webhookPayloadCallRecordingReady** | [**WebhookPayloadCallRecordingReady**](WebhookPayloadCallRecordingReady.md)|  | |

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


## onCallTranscriptSegment

> void onCallTranscriptSegment(webhookPayloadCallTranscriptSegment)

Call transcript segment event

One final segment of a live call transcript.  ### When it fires  Only for teams with zero content retention, on calls with transcription on: once per final segment, while the call is live. Zernio stores no transcript for these teams, so it cannot be fetched later. Store each segment when it arrives.  ### Payload notes  &#x60;segment.text&#x60; is the final text, &#x60;segment.confidence&#x60; the recognition confidence and &#x60;segment.at&#x60; when it was transcribed. 

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
        WebhookPayloadCallTranscriptSegment webhookPayloadCallTranscriptSegment = new WebhookPayloadCallTranscriptSegment(); // WebhookPayloadCallTranscriptSegment | 
        try {
            apiInstance.onCallTranscriptSegment(webhookPayloadCallTranscriptSegment);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCallTranscriptSegment");
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
| **webhookPayloadCallTranscriptSegment** | [**WebhookPayloadCallTranscriptSegment**](WebhookPayloadCallTranscriptSegment.md)|  | |

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

## onCallTranscriptSegmentWithHttpInfo

> ApiResponse<Void> onCallTranscriptSegment onCallTranscriptSegmentWithHttpInfo(webhookPayloadCallTranscriptSegment)

Call transcript segment event

One final segment of a live call transcript.  ### When it fires  Only for teams with zero content retention, on calls with transcription on: once per final segment, while the call is live. Zernio stores no transcript for these teams, so it cannot be fetched later. Store each segment when it arrives.  ### Payload notes  &#x60;segment.text&#x60; is the final text, &#x60;segment.confidence&#x60; the recognition confidence and &#x60;segment.at&#x60; when it was transcribed. 

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
        WebhookPayloadCallTranscriptSegment webhookPayloadCallTranscriptSegment = new WebhookPayloadCallTranscriptSegment(); // WebhookPayloadCallTranscriptSegment | 
        try {
            ApiResponse<Void> response = apiInstance.onCallTranscriptSegmentWithHttpInfo(webhookPayloadCallTranscriptSegment);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCallTranscriptSegment");
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
| **webhookPayloadCallTranscriptSegment** | [**WebhookPayloadCallTranscriptSegment**](WebhookPayloadCallTranscriptSegment.md)|  | |

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

A campaign Zernio already tracked ran out of budget. TikTok only.  ### When it fires  Fires once per campaign when its budget runs out, at most once per 6 hours, so a daily budget that runs out again the next day is announced again.  ### When it does not fire  Ads seen for the first time by a sync never fire it.  ### Platform notes  Only TikTok reports this on the ad. Meta and Google keep such ads &#x60;ACTIVE&#x60;, so they never fire it. 

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

A campaign Zernio already tracked ran out of budget. TikTok only.  ### When it fires  Fires once per campaign when its budget runs out, at most once per 6 hours, so a daily budget that runs out again the next day is announced again.  ### When it does not fire  Ads seen for the first time by a sync never fire it.  ### Platform notes  Only TikTok reports this on the ad. Meta and Google keep such ads &#x60;ACTIVE&#x60;, so they never fire it. 

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


## onCampaignCreated

> void onCampaignCreated(webhookPayloadCampaignCreated)

Campaign created event

A campaign was created through Zernio (&#x60;source: \&quot;zernio\&quot;&#x60;) or detected by the sync (&#x60;source: \&quot;platform\&quot;&#x60;).  ### When it fires  Fires once the campaign row is recorded. A detected campaign arrives up to one sync interval late.  ### When it does not fire  History loaded when an account connects, and campaigns created more than 7 days ago, are never announced. 

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
        WebhookPayloadCampaignCreated webhookPayloadCampaignCreated = new WebhookPayloadCampaignCreated(); // WebhookPayloadCampaignCreated | 
        try {
            apiInstance.onCampaignCreated(webhookPayloadCampaignCreated);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignCreated");
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
| **webhookPayloadCampaignCreated** | [**WebhookPayloadCampaignCreated**](WebhookPayloadCampaignCreated.md)|  | |

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

## onCampaignCreatedWithHttpInfo

> ApiResponse<Void> onCampaignCreated onCampaignCreatedWithHttpInfo(webhookPayloadCampaignCreated)

Campaign created event

A campaign was created through Zernio (&#x60;source: \&quot;zernio\&quot;&#x60;) or detected by the sync (&#x60;source: \&quot;platform\&quot;&#x60;).  ### When it fires  Fires once the campaign row is recorded. A detected campaign arrives up to one sync interval late.  ### When it does not fire  History loaded when an account connects, and campaigns created more than 7 days ago, are never announced. 

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
        WebhookPayloadCampaignCreated webhookPayloadCampaignCreated = new WebhookPayloadCampaignCreated(); // WebhookPayloadCampaignCreated | 
        try {
            ApiResponse<Void> response = apiInstance.onCampaignCreatedWithHttpInfo(webhookPayloadCampaignCreated);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignCreated");
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
| **webhookPayloadCampaignCreated** | [**WebhookPayloadCampaignCreated**](WebhookPayloadCampaignCreated.md)|  | |

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


## onCampaignDraftApproved

> void onCampaignDraftApproved(webhookPayloadCampaignDraft)

Campaign draft approved event

You approved a draft version.  ### Effect  The creator can now publish it and submit the post with its &#x60;draftId&#x60;. 

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
        WebhookPayloadCampaignDraft webhookPayloadCampaignDraft = new WebhookPayloadCampaignDraft(); // WebhookPayloadCampaignDraft | 
        try {
            apiInstance.onCampaignDraftApproved(webhookPayloadCampaignDraft);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignDraftApproved");
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
| **webhookPayloadCampaignDraft** | [**WebhookPayloadCampaignDraft**](WebhookPayloadCampaignDraft.md)|  | |

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

## onCampaignDraftApprovedWithHttpInfo

> ApiResponse<Void> onCampaignDraftApproved onCampaignDraftApprovedWithHttpInfo(webhookPayloadCampaignDraft)

Campaign draft approved event

You approved a draft version.  ### Effect  The creator can now publish it and submit the post with its &#x60;draftId&#x60;. 

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
        WebhookPayloadCampaignDraft webhookPayloadCampaignDraft = new WebhookPayloadCampaignDraft(); // WebhookPayloadCampaignDraft | 
        try {
            ApiResponse<Void> response = apiInstance.onCampaignDraftApprovedWithHttpInfo(webhookPayloadCampaignDraft);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignDraftApproved");
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
| **webhookPayloadCampaignDraft** | [**WebhookPayloadCampaignDraft**](WebhookPayloadCampaignDraft.md)|  | |

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


## onCampaignDraftRejected

> void onCampaignDraftRejected(webhookPayloadCampaignDraft)

Campaign draft rejected event

You rejected a draft version.  ### Effect  It can never back a post, and it gets no new version. 

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
        WebhookPayloadCampaignDraft webhookPayloadCampaignDraft = new WebhookPayloadCampaignDraft(); // WebhookPayloadCampaignDraft | 
        try {
            apiInstance.onCampaignDraftRejected(webhookPayloadCampaignDraft);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignDraftRejected");
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
| **webhookPayloadCampaignDraft** | [**WebhookPayloadCampaignDraft**](WebhookPayloadCampaignDraft.md)|  | |

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

## onCampaignDraftRejectedWithHttpInfo

> ApiResponse<Void> onCampaignDraftRejected onCampaignDraftRejectedWithHttpInfo(webhookPayloadCampaignDraft)

Campaign draft rejected event

You rejected a draft version.  ### Effect  It can never back a post, and it gets no new version. 

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
        WebhookPayloadCampaignDraft webhookPayloadCampaignDraft = new WebhookPayloadCampaignDraft(); // WebhookPayloadCampaignDraft | 
        try {
            ApiResponse<Void> response = apiInstance.onCampaignDraftRejectedWithHttpInfo(webhookPayloadCampaignDraft);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignDraftRejected");
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
| **webhookPayloadCampaignDraft** | [**WebhookPayloadCampaignDraft**](WebhookPayloadCampaignDraft.md)|  | |

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


## onCampaignDraftRevisionRequested

> void onCampaignDraftRevisionRequested(webhookPayloadCampaignDraft)

Campaign draft revision requested event

You asked for changes to a draft version.  ### Comments  &#x60;draft.comments&#x60; lists your notes, each with &#x60;atMs&#x60; for the moment of the video it points at, or null for a general note. The creator can upload one new version of it. 

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
        WebhookPayloadCampaignDraft webhookPayloadCampaignDraft = new WebhookPayloadCampaignDraft(); // WebhookPayloadCampaignDraft | 
        try {
            apiInstance.onCampaignDraftRevisionRequested(webhookPayloadCampaignDraft);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignDraftRevisionRequested");
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
| **webhookPayloadCampaignDraft** | [**WebhookPayloadCampaignDraft**](WebhookPayloadCampaignDraft.md)|  | |

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

## onCampaignDraftRevisionRequestedWithHttpInfo

> ApiResponse<Void> onCampaignDraftRevisionRequested onCampaignDraftRevisionRequestedWithHttpInfo(webhookPayloadCampaignDraft)

Campaign draft revision requested event

You asked for changes to a draft version.  ### Comments  &#x60;draft.comments&#x60; lists your notes, each with &#x60;atMs&#x60; for the moment of the video it points at, or null for a general note. The creator can upload one new version of it. 

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
        WebhookPayloadCampaignDraft webhookPayloadCampaignDraft = new WebhookPayloadCampaignDraft(); // WebhookPayloadCampaignDraft | 
        try {
            ApiResponse<Void> response = apiInstance.onCampaignDraftRevisionRequestedWithHttpInfo(webhookPayloadCampaignDraft);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignDraftRevisionRequested");
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
| **webhookPayloadCampaignDraft** | [**WebhookPayloadCampaignDraft**](WebhookPayloadCampaignDraft.md)|  | |

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


## onCampaignDraftSubmitted

> void onCampaignDraftSubmitted(webhookPayloadCampaignDraft)

Campaign draft submitted event

A creator uploaded a draft, or a new version of one, on a campaign with &#x60;requireDraftApproval&#x60;.  ### Versions  &#x60;draft.version&#x60; is 1 for a new draft, higher for a new version answering your requested changes, and &#x60;draft.revisionOf&#x60; names the version it answers. 

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
        WebhookPayloadCampaignDraft webhookPayloadCampaignDraft = new WebhookPayloadCampaignDraft(); // WebhookPayloadCampaignDraft | 
        try {
            apiInstance.onCampaignDraftSubmitted(webhookPayloadCampaignDraft);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignDraftSubmitted");
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
| **webhookPayloadCampaignDraft** | [**WebhookPayloadCampaignDraft**](WebhookPayloadCampaignDraft.md)|  | |

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

## onCampaignDraftSubmittedWithHttpInfo

> ApiResponse<Void> onCampaignDraftSubmitted onCampaignDraftSubmittedWithHttpInfo(webhookPayloadCampaignDraft)

Campaign draft submitted event

A creator uploaded a draft, or a new version of one, on a campaign with &#x60;requireDraftApproval&#x60;.  ### Versions  &#x60;draft.version&#x60; is 1 for a new draft, higher for a new version answering your requested changes, and &#x60;draft.revisionOf&#x60; names the version it answers. 

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
        WebhookPayloadCampaignDraft webhookPayloadCampaignDraft = new WebhookPayloadCampaignDraft(); // WebhookPayloadCampaignDraft | 
        try {
            ApiResponse<Void> response = apiInstance.onCampaignDraftSubmittedWithHttpInfo(webhookPayloadCampaignDraft);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignDraftSubmitted");
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
| **webhookPayloadCampaignDraft** | [**WebhookPayloadCampaignDraft**](WebhookPayloadCampaignDraft.md)|  | |

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


## onCampaignParticipantApproved

> void onCampaignParticipantApproved(webhookPayloadCampaignParticipant)

Campaign participant approved event

You accepted a creator who asked to join.  ### Effect  They are now &#x60;active&#x60; and &#x60;participant.joinedAt&#x60; is set. This event replaces &#x60;campaign_participant.joined&#x60; for them, so it fires instead of it, never with it. 

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
            apiInstance.onCampaignParticipantApproved(webhookPayloadCampaignParticipant);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignParticipantApproved");
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

## onCampaignParticipantApprovedWithHttpInfo

> ApiResponse<Void> onCampaignParticipantApproved onCampaignParticipantApprovedWithHttpInfo(webhookPayloadCampaignParticipant)

Campaign participant approved event

You accepted a creator who asked to join.  ### Effect  They are now &#x60;active&#x60; and &#x60;participant.joinedAt&#x60; is set. This event replaces &#x60;campaign_participant.joined&#x60; for them, so it fires instead of it, never with it. 

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
            ApiResponse<Void> response = apiInstance.onCampaignParticipantApprovedWithHttpInfo(webhookPayloadCampaignParticipant);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignParticipantApproved");
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


## onCampaignParticipantDenied

> void onCampaignParticipantDenied(webhookPayloadCampaignParticipant)

Campaign participant denied event

You turned down a creator who asked to join.  ### Effect  They cannot submit anything to this campaign. 

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
            apiInstance.onCampaignParticipantDenied(webhookPayloadCampaignParticipant);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignParticipantDenied");
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

## onCampaignParticipantDeniedWithHttpInfo

> ApiResponse<Void> onCampaignParticipantDenied onCampaignParticipantDeniedWithHttpInfo(webhookPayloadCampaignParticipant)

Campaign participant denied event

You turned down a creator who asked to join.  ### Effect  They cannot submit anything to this campaign. 

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
            ApiResponse<Void> response = apiInstance.onCampaignParticipantDeniedWithHttpInfo(webhookPayloadCampaignParticipant);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignParticipantDenied");
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


## onCampaignParticipantJoined

> void onCampaignParticipantJoined(webhookPayloadCampaignParticipant)

Campaign participant joined event

A creator joined a campaign from their invite link or the open link.  ### When it fires  It fires once per participant, and &#x60;participant.joinedAt&#x60; says when. 

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

A creator joined a campaign from their invite link or the open link.  ### When it fires  It fires once per participant, and &#x60;participant.joinedAt&#x60; says when. 

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


## onCampaignParticipantPending

> void onCampaignParticipantPending(webhookPayloadCampaignParticipant)

Campaign participant pending event

A creator asked to join a campaign that reviews creators.  ### When it fires  A creator joined from the open link of a campaign whose &#x60;joinApproval&#x60; is &#x60;manual&#x60;. They wait as &#x60;pending&#x60; until you approve or deny them, and they do not take a place under &#x60;maxParticipants&#x60; while they wait. 

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
            apiInstance.onCampaignParticipantPending(webhookPayloadCampaignParticipant);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignParticipantPending");
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

## onCampaignParticipantPendingWithHttpInfo

> ApiResponse<Void> onCampaignParticipantPending onCampaignParticipantPendingWithHttpInfo(webhookPayloadCampaignParticipant)

Campaign participant pending event

A creator asked to join a campaign that reviews creators.  ### When it fires  A creator joined from the open link of a campaign whose &#x60;joinApproval&#x60; is &#x60;manual&#x60;. They wait as &#x60;pending&#x60; until you approve or deny them, and they do not take a place under &#x60;maxParticipants&#x60; while they wait. 

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
            ApiResponse<Void> response = apiInstance.onCampaignParticipantPendingWithHttpInfo(webhookPayloadCampaignParticipant);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignParticipantPending");
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

You removed a participant from the campaign.  ### When it does not fire  Removing a participant twice fires the event once. 

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

You removed a participant from the campaign.  ### When it does not fire  Removing a participant twice fires the event once. 

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

You suspended a participant.  ### Effect  They can no longer connect accounts or submit posts to this campaign. Posts they already submitted keep earning until you reject them. 

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

You suspended a participant.  ### Effect  They can no longer connect accounts or submit posts to this campaign. Posts they already submitted keep earning until you reject them. 

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

A payout through Zernio did not reach the creator.  ### When it fires  Stripe refused it, it stayed unconfirmed for 24 hours, or it was reversed. The amount is payable again, minus anything a rejection claws back. 

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

A payout through Zernio did not reach the creator.  ### When it fires  Stripe refused it, it stayed unconfirmed for 24 hours, or it was reversed. The amount is payable again, minus anything a rejection claws back. 

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

A participant&#39;s held earnings matured and became payable.  ### Payload notes  &#x60;payout.payableCents&#x60; is the participant&#39;s whole payable balance, the amount to pay when you pay from your own rails. 

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

A participant&#39;s held earnings matured and became payable.  ### Payload notes  &#x60;payout.payableCents&#x60; is the participant&#39;s whole payable balance, the amount to pay when you pay from your own rails. 

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

A payout to a participant was recorded.  ### Payload notes  &#x60;payout.settlement&#x60; holds the amount and the reference. &#x60;recorded&#x60; is true when the money moved outside Zernio. 

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

A payout to a participant was recorded.  ### Payload notes  &#x60;payout.settlement&#x60; holds the amount and the reference. &#x60;recorded&#x60; is true when the money moved outside Zernio. 

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


## onCampaignSampleApproved

> void onCampaignSampleApproved(webhookPayloadCampaignSample)

Campaign sample approved event

You approved a sample request.  ### Discount code  &#x60;sample.discountCode&#x60; is the single-use, 100% off code created in your store for that product. 

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
        WebhookPayloadCampaignSample webhookPayloadCampaignSample = new WebhookPayloadCampaignSample(); // WebhookPayloadCampaignSample | 
        try {
            apiInstance.onCampaignSampleApproved(webhookPayloadCampaignSample);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignSampleApproved");
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
| **webhookPayloadCampaignSample** | [**WebhookPayloadCampaignSample**](WebhookPayloadCampaignSample.md)|  | |

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

## onCampaignSampleApprovedWithHttpInfo

> ApiResponse<Void> onCampaignSampleApproved onCampaignSampleApprovedWithHttpInfo(webhookPayloadCampaignSample)

Campaign sample approved event

You approved a sample request.  ### Discount code  &#x60;sample.discountCode&#x60; is the single-use, 100% off code created in your store for that product. 

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
        WebhookPayloadCampaignSample webhookPayloadCampaignSample = new WebhookPayloadCampaignSample(); // WebhookPayloadCampaignSample | 
        try {
            ApiResponse<Void> response = apiInstance.onCampaignSampleApprovedWithHttpInfo(webhookPayloadCampaignSample);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignSampleApproved");
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
| **webhookPayloadCampaignSample** | [**WebhookPayloadCampaignSample**](WebhookPayloadCampaignSample.md)|  | |

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


## onCampaignSampleDeclined

> void onCampaignSampleDeclined(webhookPayloadCampaignSample)

Campaign sample declined event

You declined a sample request.  ### Effect  &#x60;sample.declineReason&#x60; says why. The creator can ask for the same product again. 

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
        WebhookPayloadCampaignSample webhookPayloadCampaignSample = new WebhookPayloadCampaignSample(); // WebhookPayloadCampaignSample | 
        try {
            apiInstance.onCampaignSampleDeclined(webhookPayloadCampaignSample);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignSampleDeclined");
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
| **webhookPayloadCampaignSample** | [**WebhookPayloadCampaignSample**](WebhookPayloadCampaignSample.md)|  | |

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

## onCampaignSampleDeclinedWithHttpInfo

> ApiResponse<Void> onCampaignSampleDeclined onCampaignSampleDeclinedWithHttpInfo(webhookPayloadCampaignSample)

Campaign sample declined event

You declined a sample request.  ### Effect  &#x60;sample.declineReason&#x60; says why. The creator can ask for the same product again. 

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
        WebhookPayloadCampaignSample webhookPayloadCampaignSample = new WebhookPayloadCampaignSample(); // WebhookPayloadCampaignSample | 
        try {
            ApiResponse<Void> response = apiInstance.onCampaignSampleDeclinedWithHttpInfo(webhookPayloadCampaignSample);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignSampleDeclined");
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
| **webhookPayloadCampaignSample** | [**WebhookPayloadCampaignSample**](WebhookPayloadCampaignSample.md)|  | |

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


## onCampaignSampleRequested

> void onCampaignSampleRequested(webhookPayloadCampaignSample)

Campaign sample requested event

A creator asked for one of the campaign&#39;s &#x60;sampleProducts&#x60;, with a shipping address. 

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
        WebhookPayloadCampaignSample webhookPayloadCampaignSample = new WebhookPayloadCampaignSample(); // WebhookPayloadCampaignSample | 
        try {
            apiInstance.onCampaignSampleRequested(webhookPayloadCampaignSample);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignSampleRequested");
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
| **webhookPayloadCampaignSample** | [**WebhookPayloadCampaignSample**](WebhookPayloadCampaignSample.md)|  | |

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

## onCampaignSampleRequestedWithHttpInfo

> ApiResponse<Void> onCampaignSampleRequested onCampaignSampleRequestedWithHttpInfo(webhookPayloadCampaignSample)

Campaign sample requested event

A creator asked for one of the campaign&#39;s &#x60;sampleProducts&#x60;, with a shipping address. 

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
        WebhookPayloadCampaignSample webhookPayloadCampaignSample = new WebhookPayloadCampaignSample(); // WebhookPayloadCampaignSample | 
        try {
            ApiResponse<Void> response = apiInstance.onCampaignSampleRequestedWithHttpInfo(webhookPayloadCampaignSample);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignSampleRequested");
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
| **webhookPayloadCampaignSample** | [**WebhookPayloadCampaignSample**](WebhookPayloadCampaignSample.md)|  | |

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


## onCampaignSampleShipped

> void onCampaignSampleShipped(webhookPayloadCampaignSample)

Campaign sample shipped event

You marked an approved sample as shipped.  ### Tracking  &#x60;sample.trackingUrl&#x60; is set when you gave one. 

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
        WebhookPayloadCampaignSample webhookPayloadCampaignSample = new WebhookPayloadCampaignSample(); // WebhookPayloadCampaignSample | 
        try {
            apiInstance.onCampaignSampleShipped(webhookPayloadCampaignSample);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignSampleShipped");
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
| **webhookPayloadCampaignSample** | [**WebhookPayloadCampaignSample**](WebhookPayloadCampaignSample.md)|  | |

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

## onCampaignSampleShippedWithHttpInfo

> ApiResponse<Void> onCampaignSampleShipped onCampaignSampleShippedWithHttpInfo(webhookPayloadCampaignSample)

Campaign sample shipped event

You marked an approved sample as shipped.  ### Tracking  &#x60;sample.trackingUrl&#x60; is set when you gave one. 

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
        WebhookPayloadCampaignSample webhookPayloadCampaignSample = new WebhookPayloadCampaignSample(); // WebhookPayloadCampaignSample | 
        try {
            ApiResponse<Void> response = apiInstance.onCampaignSampleShippedWithHttpInfo(webhookPayloadCampaignSample);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignSampleShipped");
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
| **webhookPayloadCampaignSample** | [**WebhookPayloadCampaignSample**](WebhookPayloadCampaignSample.md)|  | |

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

You approved a submission.  ### Earnings  What the submission earned so far moves to owed with the campaign hold. Later earnings post straight to owed. 

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

You approved a submission.  ### Earnings  What the submission earned so far moves to owed with the campaign hold. Later earnings post straight to owed. 

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

A submission gained a fraud flag it did not carry before, at submission or on a later sync.  ### Flags  Flags include &#x60;duplicate_post&#x60;, &#x60;view_spike&#x60;, &#x60;low_authenticity&#x60; and &#x60;x_read_cap&#x60; (the campaign&#39;s X read budget is spent). &#x60;submission.flags&#x60; lists every flag it carries. Zernio never rejects on its own; the decision is yours. 

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

A submission gained a fraud flag it did not carry before, at submission or on a later sync.  ### Flags  Flags include &#x60;duplicate_post&#x60;, &#x60;view_spike&#x60;, &#x60;low_authenticity&#x60; and &#x60;x_read_cap&#x60; (the campaign&#39;s X read budget is spent). &#x60;submission.flags&#x60; lists every flag it carries. Zernio never rejects on its own; the decision is yours. 

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

A submission is ready for your review.  ### When it fires  A CPM submission reached &#x60;minViewsToEarn&#x60;, a pool submission reached &#x60;minViewsToQualify&#x60;, and per post submissions arrive here after their first accrual. 

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

A submission is ready for your review.  ### When it fires  A CPM submission reached &#x60;minViewsToEarn&#x60;, a pool submission reached &#x60;minViewsToQualify&#x60;, and per post submissions arrive here after their first accrual. 

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

A creator submitted a post to a campaign, Zernio opened its tracking window and took the first view sample. 

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

A creator submitted a post to a campaign, Zernio opened its tracking window and took the first view sample. 

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

You rejected a submission and its tracking window was cancelled.  ### Earnings  Its unsettled earnings go back to the campaign budget. 

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

You rejected a submission and its tracking window was cancelled.  ### Earnings  Its unsettled earnings go back to the campaign budget. 

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


## onCampaignUpdated

> void onCampaignUpdated(webhookPayloadCampaignUpdated)

Campaign updated event

A campaign was edited through Zernio (&#x60;source: \&quot;zernio\&quot;&#x60;), or outside Zernio and detected by the sync (&#x60;source: \&quot;platform\&quot;&#x60;).  ### When it fires  Fires after the platform and Zernio both accepted the edit. Outside edits arrive up to one sync interval late, and only to the user whose sync saw them.  ### Deduplication  Events are not deduplicated, so every edit is announced. Use the event &#x60;id&#x60; to drop repeats.  ### Payload notes  &#x60;changes&#x60; lists the edited fields: &#x60;name&#x60;, &#x60;status&#x60; (the campaign&#39;s own on/off switch), &#x60;budget&#x60;, &#x60;bid&#x60; or &#x60;settings&#x60;. Ignore unknown values. It never carries old or new values, so read the campaign.  ### What the sync detects  From the sync, &#x60;changes&#x60; covers only &#x60;name&#x60;, &#x60;status&#x60; and &#x60;schedule&#x60;. Schedule is detected only on Google, LinkedIn, Pinterest and OpenAI Ads.  ### When it does not fire  Budget edits made outside Zernio and history loaded at connect are not announced. Ad set edits arrive as &#x60;ad_set.updated&#x60;. Ad rule changes arrive as &#x60;ad_rule.triggered&#x60;.  ### Google sub-resources  Edits to ad schedule, targeting, negative keywords, conversion goals, assets, asset groups and listing group filters are not announced. 

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
        WebhookPayloadCampaignUpdated webhookPayloadCampaignUpdated = new WebhookPayloadCampaignUpdated(); // WebhookPayloadCampaignUpdated | 
        try {
            apiInstance.onCampaignUpdated(webhookPayloadCampaignUpdated);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignUpdated");
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
| **webhookPayloadCampaignUpdated** | [**WebhookPayloadCampaignUpdated**](WebhookPayloadCampaignUpdated.md)|  | |

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

## onCampaignUpdatedWithHttpInfo

> ApiResponse<Void> onCampaignUpdated onCampaignUpdatedWithHttpInfo(webhookPayloadCampaignUpdated)

Campaign updated event

A campaign was edited through Zernio (&#x60;source: \&quot;zernio\&quot;&#x60;), or outside Zernio and detected by the sync (&#x60;source: \&quot;platform\&quot;&#x60;).  ### When it fires  Fires after the platform and Zernio both accepted the edit. Outside edits arrive up to one sync interval late, and only to the user whose sync saw them.  ### Deduplication  Events are not deduplicated, so every edit is announced. Use the event &#x60;id&#x60; to drop repeats.  ### Payload notes  &#x60;changes&#x60; lists the edited fields: &#x60;name&#x60;, &#x60;status&#x60; (the campaign&#39;s own on/off switch), &#x60;budget&#x60;, &#x60;bid&#x60; or &#x60;settings&#x60;. Ignore unknown values. It never carries old or new values, so read the campaign.  ### What the sync detects  From the sync, &#x60;changes&#x60; covers only &#x60;name&#x60;, &#x60;status&#x60; and &#x60;schedule&#x60;. Schedule is detected only on Google, LinkedIn, Pinterest and OpenAI Ads.  ### When it does not fire  Budget edits made outside Zernio and history loaded at connect are not announced. Ad set edits arrive as &#x60;ad_set.updated&#x60;. Ad rule changes arrive as &#x60;ad_rule.triggered&#x60;.  ### Google sub-resources  Edits to ad schedule, targeting, negative keywords, conversion goals, assets, asset groups and listing group filters are not announced. 

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
        WebhookPayloadCampaignUpdated webhookPayloadCampaignUpdated = new WebhookPayloadCampaignUpdated(); // WebhookPayloadCampaignUpdated | 
        try {
            ApiResponse<Void> response = apiInstance.onCampaignUpdatedWithHttpInfo(webhookPayloadCampaignUpdated);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onCampaignUpdated");
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
| **webhookPayloadCampaignUpdated** | [**WebhookPayloadCampaignUpdated**](WebhookPayloadCampaignUpdated.md)|  | |

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

A new comment arrived on a tracked post.  ### Platform notes  Delivered for Instagram, Facebook, Threads, YouTube, LinkedIn, Bluesky, Reddit and TikTok. X/Twitter does not fire it. TikTok needs an account connected through the TikTok for Business app.  ### Delivery timing  Instagram, Facebook, Threads and TikTok arrive in real time from the platform&#39;s webhook. The rest are poll-driven, so delivery is not instant.  ### Live comments  On Instagram, &#x60;comment.isLive: true&#x60; marks a comment made during a live broadcast. The key is absent on every other comment.  ### Ads  &#x60;comment.ad&#x60; is present only on comments made on paid content, so &#x60;if (comment.ad)&#x60; filters ad-driven comments.  ### Ad fields  Instagram carries &#x60;ad.id&#x60; and &#x60;ad.title&#x60;. Facebook carries &#x60;ad.promotionStatus&#x60;: &#x60;active&#x60; for boosted organic posts, &#x60;ineligible&#x60; for dark post creatives.  ### Instagram author profile  Comments may carry &#x60;comment.author.instagramProfile&#x60; (&#x60;isFollower&#x60;, &#x60;isFollowing&#x60;, &#x60;followerCount&#x60;, &#x60;isVerified&#x60;). An absent object means unknown, never \&quot;not a follower\&quot;.  ### Why the profile is often absent  Meta reveals the follow relationship only for people who have messaged the account, and commenting does not grant that consent. The object is absent for most first-time commenters. 

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

A new comment arrived on a tracked post.  ### Platform notes  Delivered for Instagram, Facebook, Threads, YouTube, LinkedIn, Bluesky, Reddit and TikTok. X/Twitter does not fire it. TikTok needs an account connected through the TikTok for Business app.  ### Delivery timing  Instagram, Facebook, Threads and TikTok arrive in real time from the platform&#39;s webhook. The rest are poll-driven, so delivery is not instant.  ### Live comments  On Instagram, &#x60;comment.isLive: true&#x60; marks a comment made during a live broadcast. The key is absent on every other comment.  ### Ads  &#x60;comment.ad&#x60; is present only on comments made on paid content, so &#x60;if (comment.ad)&#x60; filters ad-driven comments.  ### Ad fields  Instagram carries &#x60;ad.id&#x60; and &#x60;ad.title&#x60;. Facebook carries &#x60;ad.promotionStatus&#x60;: &#x60;active&#x60; for boosted organic posts, &#x60;ineligible&#x60; for dark post creatives.  ### Instagram author profile  Comments may carry &#x60;comment.author.instagramProfile&#x60; (&#x60;isFollower&#x60;, &#x60;isFollowing&#x60;, &#x60;followerCount&#x60;, &#x60;isVerified&#x60;). An absent object means unknown, never \&quot;not a follower\&quot;.  ### Why the profile is often absent  Meta reveals the follow relationship only for people who have messaged the account, and commenting does not grant that consent. The object is absent for most first-time commenters. 

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

An order was placed in the store.  ### Payload notes  &#x60;resource.status&#x60; is its normalized state at that moment. Read the order with &#x60;GET /v1/commerce/orders/{orderId}?accountId&#x3D;...&#x60;. Fires once per Zernio account. 

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

An order was placed in the store.  ### Payload notes  &#x60;resource.status&#x60; is its normalized state at that moment. Read the order with &#x60;GET /v1/commerce/orders/{orderId}?accountId&#x3D;...&#x60;. Fires once per Zernio account. 

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

A refund was issued on an order.  ### Payload notes  &#x60;resource.id&#x60; is the order id, not the refund id. &#x60;resource.status&#x60; and &#x60;resource.platformStatus&#x60; are &#x60;null&#x60;. A &#x60;commerce.order.updated&#x60; usually follows for the same change. 

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

A refund was issued on an order.  ### Payload notes  &#x60;resource.id&#x60; is the order id, not the refund id. &#x60;resource.status&#x60; and &#x60;resource.platformStatus&#x60; are &#x60;null&#x60;. A &#x60;commerce.order.updated&#x60; usually follows for the same change. 

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

An order changed in the store, such as payment, fulfilment, cancellation or edits.  ### Payload notes  &#x60;resource.status&#x60; is the new state. Refunds also fire it. Fires once per Zernio account connected to the store. 

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

An order changed in the store, such as payment, fulfilment, cancellation or edits.  ### Payload notes  &#x60;resource.status&#x60; is the new state. Refunds also fire it. Fires once per Zernio account connected to the store. 

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

A product was created in a connected Shopify store or WooCommerce site.  ### Payload notes  &#x60;resource.id&#x60; is the store&#39;s product id. Read the product with &#x60;GET /v1/commerce/products/{productId}?accountId&#x3D;...&#x60;. Fires once per Zernio account connected to the store. 

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

A product was created in a connected Shopify store or WooCommerce site.  ### Payload notes  &#x60;resource.id&#x60; is the store&#39;s product id. Read the product with &#x60;GET /v1/commerce/products/{productId}?accountId&#x3D;...&#x60;. Fires once per Zernio account connected to the store. 

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

A product was deleted in the store.  ### Payload notes  &#x60;resource.status&#x60; and &#x60;resource.platformStatus&#x60; are &#x60;null&#x60;. Fires once per Zernio account connected to the store. 

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

A product was deleted in the store.  ### Payload notes  &#x60;resource.status&#x60; and &#x60;resource.platformStatus&#x60; are &#x60;null&#x60;. Fires once per Zernio account connected to the store. 

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

A product changed in the store, or WooCommerce restored it from the trash.  ### Payload notes  Fields, status, variants or prices changed; read the product for what. There is no restored event. Fires once per Zernio account connected to the store. 

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

A product changed in the store, or WooCommerce restored it from the trash.  ### Payload notes  Fields, status, variants or prices changed; read the product for what. There is no restored event. Fires once per Zernio account connected to the store. 

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

A contact was deleted in Google Contacts or Outlook.  ### Effect  Zernio removes its email channels for that account; the contact stays when other channels remain. It arrives up to 15 minutes after the change, from the sync. 

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

A contact was deleted in Google Contacts or Outlook.  ### Effect  Zernio removes its email channels for that account; the contact stays when other channels remain. It arrives up to 15 minutes after the change, from the sync. 

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

A contact custom field changed value; &#x60;field&#x60; is the field slug.  ### When it fires  Once per custom field whose value a write changed. Writing the current value fires nothing.  ### Payload notes  &#x60;previousValue&#x60; is &#x60;null&#x60; when the field was not set. &#x60;value&#x60; is &#x60;null&#x60; when it was removed. 

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

A contact custom field changed value; &#x60;field&#x60; is the field slug.  ### When it fires  Once per custom field whose value a write changed. Writing the current value fires nothing.  ### Payload notes  &#x60;previousValue&#x60; is &#x60;null&#x60; when the field was not set. &#x60;value&#x60; is &#x60;null&#x60; when it was removed. 

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

A tag was added to a contact by the API, a workflow &#x60;add_tag&#x60; node or a comment-automation click.  ### When it fires  Once per tag a write actually added. Re-adding a tag the contact already has fires nothing.  ### When it does not fire  Creating a contact with tags fires nothing. Only changes to an existing contact do. 

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

A tag was added to a contact by the API, a workflow &#x60;add_tag&#x60; node or a comment-automation click.  ### When it fires  Once per tag a write actually added. Re-adding a tag the contact already has fires nothing.  ### When it does not fire  Creating a contact with tags fires nothing. Only changes to an existing contact do. 

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

A tag was removed from a contact.  ### When it fires  Once per tag a write actually removed. 

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

A tag was removed from a contact.  ### When it fires  Once per tag a write actually removed. 

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

A contact sync added or changed a contact; &#x60;contact.id&#x60; is the Zernio contact id.  ### When it fires  It fires from the sync of a Google Contacts or Outlook account, which runs every 15 minutes, so up to 15 minutes after the change. It also fires when a WhatsApp coexistence address book adds or renames a contact. 

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

A contact sync added or changed a contact; &#x60;contact.id&#x60; is the Zernio contact id.  ### When it fires  It fires from the sync of a Google Contacts or Outlook account, which runs every 15 minutes, so up to 15 minutes after the change. It also fires when a WhatsApp coexistence address book adds or renames a contact. 

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

Control of a conversation moved: Meta Business Agent on WhatsApp, or Meta&#39;s conversation routing on Facebook and Instagram (&#x60;messaging_handovers&#x60;). On Instagram, Conversation Routing replaced the Handover Protocol in October 2025 and kept its thread-control events.  ### Owner values  &#x60;control.owner&#x60; is &#x60;ai_agent&#x60; (Meta Business Agent, WhatsApp), &#x60;app&#x60; (you) or &#x60;other&#x60; (a WhatsApp partner app, or a receiver such as Page Inbox on Messenger and Instagram).  ### Control fields  &#x60;control.previousOwner&#x60; is &#x60;null&#x60; when no handover touched the thread. &#x60;control.ownerAppId&#x60; is the new owner&#39;s Meta app id when named (Page Inbox is &#x60;263902037430900&#x60;). &#x60;control.metadata&#x60; is the transferring app&#39;s note, verbatim.  ### WhatsApp  Meta Business Agent took the conversation, handed it to you, or another partner app took it. While &#x60;ai_agent&#x60; owns it, its replies arrive on &#x60;message.sent&#x60; with &#x60;source: \&quot;meta_business_agent\&quot;&#x60;.  ### Taking control on WhatsApp  Sending any message through the inbox takes control back. To hand it to the agent without sending, call &#x60;POST /v1/inbox/conversations/{conversationId}/thread-control&#x60; with &#x60;action: \&quot;release\&quot;&#x60;.  ### Facebook and Instagram  Meta sent Zernio a &#x60;pass_thread_control&#x60; (another app passed the thread to you) or &#x60;take_thread_control&#x60; (another app took it from you) event. It fires once per change of the stored owner.  It does not fire on &#x60;release&#x60; or when two other apps move a thread between them (Meta sends nothing), nor for your own thread-control calls (their response carries the new owner).  While you are not the owner, sends answer &#x60;409&#x60; &#x60;not_thread_owner&#x60;.  ### Taking control on Facebook and Instagram  Call &#x60;POST /v1/inbox/conversations/{conversationId}/thread-control&#x60; with &#x60;action: \&quot;take\&quot;&#x60;, or &#x60;\&quot;request\&quot;&#x60; to ask the owner to pass it. Both answer 400 &#x60;platform_not_supported&#x60; on Instagram Login connections.  Meta accepts &#x60;take&#x60; only when the account has a default app set in conversation routing and the business has allowed Zernio to take control of conversations; otherwise it answers code 27.  ### When it does not fire  A repeat report of the same owner fires nothing. A &#x60;request&#x60; changes nothing until the owner passes the thread.  ### Standby messages  While another app owns the conversation, inbound messages arrive on &#x60;message.received&#x60; with &#x60;metadata.standby: true&#x60;. 

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

Control of a conversation moved: Meta Business Agent on WhatsApp, or Meta&#39;s conversation routing on Facebook and Instagram (&#x60;messaging_handovers&#x60;). On Instagram, Conversation Routing replaced the Handover Protocol in October 2025 and kept its thread-control events.  ### Owner values  &#x60;control.owner&#x60; is &#x60;ai_agent&#x60; (Meta Business Agent, WhatsApp), &#x60;app&#x60; (you) or &#x60;other&#x60; (a WhatsApp partner app, or a receiver such as Page Inbox on Messenger and Instagram).  ### Control fields  &#x60;control.previousOwner&#x60; is &#x60;null&#x60; when no handover touched the thread. &#x60;control.ownerAppId&#x60; is the new owner&#39;s Meta app id when named (Page Inbox is &#x60;263902037430900&#x60;). &#x60;control.metadata&#x60; is the transferring app&#39;s note, verbatim.  ### WhatsApp  Meta Business Agent took the conversation, handed it to you, or another partner app took it. While &#x60;ai_agent&#x60; owns it, its replies arrive on &#x60;message.sent&#x60; with &#x60;source: \&quot;meta_business_agent\&quot;&#x60;.  ### Taking control on WhatsApp  Sending any message through the inbox takes control back. To hand it to the agent without sending, call &#x60;POST /v1/inbox/conversations/{conversationId}/thread-control&#x60; with &#x60;action: \&quot;release\&quot;&#x60;.  ### Facebook and Instagram  Meta sent Zernio a &#x60;pass_thread_control&#x60; (another app passed the thread to you) or &#x60;take_thread_control&#x60; (another app took it from you) event. It fires once per change of the stored owner.  It does not fire on &#x60;release&#x60; or when two other apps move a thread between them (Meta sends nothing), nor for your own thread-control calls (their response carries the new owner).  While you are not the owner, sends answer &#x60;409&#x60; &#x60;not_thread_owner&#x60;.  ### Taking control on Facebook and Instagram  Call &#x60;POST /v1/inbox/conversations/{conversationId}/thread-control&#x60; with &#x60;action: \&quot;take\&quot;&#x60;, or &#x60;\&quot;request\&quot;&#x60; to ask the owner to pass it. Both answer 400 &#x60;platform_not_supported&#x60; on Instagram Login connections.  Meta accepts &#x60;take&#x60; only when the account has a default app set in conversation routing and the business has allowed Zernio to take control of conversations; otherwise it answers code 27.  ### When it does not fire  A repeat report of the same owner fires nothing. A &#x60;request&#x60; changes nothing until the owner passes the thread.  ### Standby messages  While another app owns the conversation, inbound messages arrive on &#x60;message.received&#x60; with &#x60;metadata.standby: true&#x60;. 

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

A new conversation began between a connected account and a contact, in either direction, on any DM platform.  ### When it fires  Once per conversation, the first time it appears. Covers Instagram, Messenger, WhatsApp, Telegram, X, Reddit, Bluesky, TikTok, SMS, RCS, iMessage, Slack and email.  ### When it does not fire  DM history replayed when an Instagram or Facebook account connects never fires it. 

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

A new conversation began between a connected account and a contact, in either direction, on any DM platform.  ### When it fires  Once per conversation, the first time it appears. Covers Instagram, Messenger, WhatsApp, Telegram, X, Reddit, Bluesky, TikTok, SMS, RCS, iMessage, Slack and email.  ### When it does not fire  DM history replayed when an Instagram or Facebook account connects never fires it. 

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

A campaign&#39;s earnings reached its budget.  ### When it fires  Nothing more accrues until budget is freed. It fires once per campaign. 

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

A campaign&#39;s earnings reached its budget.  ### When it fires  Nothing more accrues until budget is freed. It fires once per campaign. 

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

A campaign closed, either because you closed it or because &#x60;endsAt&#x60; passed.  ### When it fires  After &#x60;endsAt&#x60;, the campaign closes once every tracking window had its final read. A pool campaign is split among participants at this moment. 

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

A campaign closed, either because you closed it or because &#x60;endsAt&#x60; passed.  ### When it fires  After &#x60;endsAt&#x60;, the campaign closes once every tracking window had its final read. A pool campaign is split among participants at this moment. 

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


## onEmailBounced

> void onEmailBounced(webhookPayloadEmailBounced)

Email bounced

A delivery failure report for mail the mailbox sent arrived: the receiving server refused it for a recipient. Fires for every send from the mailbox, once per failed recipient. Delayed-delivery warnings and out-of-office replies do not fire it.  Act on &#x60;recommendedAction&#x60;: &#x60;remove&#x60; means the address does not take mail. Refusals on the sending side (&#x60;auth_failure&#x60;, &#x60;blocklisted&#x60;, &#x60;spam_blocked&#x60;, &#x60;policy_blocked&#x60;) never say &#x60;remove&#x60;. The report also arrives as &#x60;message.received&#x60;, and it does not count as a reply for &#x60;email.thread_replied&#x60;. 

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
        WebhookPayloadEmailBounced webhookPayloadEmailBounced = new WebhookPayloadEmailBounced(); // WebhookPayloadEmailBounced | 
        try {
            apiInstance.onEmailBounced(webhookPayloadEmailBounced);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onEmailBounced");
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
| **webhookPayloadEmailBounced** | [**WebhookPayloadEmailBounced**](WebhookPayloadEmailBounced.md)|  | |

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

## onEmailBouncedWithHttpInfo

> ApiResponse<Void> onEmailBounced onEmailBouncedWithHttpInfo(webhookPayloadEmailBounced)

Email bounced

A delivery failure report for mail the mailbox sent arrived: the receiving server refused it for a recipient. Fires for every send from the mailbox, once per failed recipient. Delayed-delivery warnings and out-of-office replies do not fire it.  Act on &#x60;recommendedAction&#x60;: &#x60;remove&#x60; means the address does not take mail. Refusals on the sending side (&#x60;auth_failure&#x60;, &#x60;blocklisted&#x60;, &#x60;spam_blocked&#x60;, &#x60;policy_blocked&#x60;) never say &#x60;remove&#x60;. The report also arrives as &#x60;message.received&#x60;, and it does not count as a reply for &#x60;email.thread_replied&#x60;. 

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
        WebhookPayloadEmailBounced webhookPayloadEmailBounced = new WebhookPayloadEmailBounced(); // WebhookPayloadEmailBounced | 
        try {
            ApiResponse<Void> response = apiInstance.onEmailBouncedWithHttpInfo(webhookPayloadEmailBounced);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onEmailBounced");
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
| **webhookPayloadEmailBounced** | [**WebhookPayloadEmailBounced**](WebhookPayloadEmailBounced.md)|  | |

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


## onEmailLinkClicked

> void onEmailLinkClicked(webhookPayloadEmailLinkClicked)

Email link clicked

A recipient followed a link of a message sent with &#x60;trackLinks: true&#x60;. Every http(s) link in the html was rewritten to a Zernio redirect that records the click and sends the reader on to &#x60;click.url&#x60;.  Security scanners in corporate mail gateways sometimes follow links on delivery, which reports as a click. 

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
        WebhookPayloadEmailLinkClicked webhookPayloadEmailLinkClicked = new WebhookPayloadEmailLinkClicked(); // WebhookPayloadEmailLinkClicked | 
        try {
            apiInstance.onEmailLinkClicked(webhookPayloadEmailLinkClicked);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onEmailLinkClicked");
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
| **webhookPayloadEmailLinkClicked** | [**WebhookPayloadEmailLinkClicked**](WebhookPayloadEmailLinkClicked.md)|  | |

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

## onEmailLinkClickedWithHttpInfo

> ApiResponse<Void> onEmailLinkClicked onEmailLinkClickedWithHttpInfo(webhookPayloadEmailLinkClicked)

Email link clicked

A recipient followed a link of a message sent with &#x60;trackLinks: true&#x60;. Every http(s) link in the html was rewritten to a Zernio redirect that records the click and sends the reader on to &#x60;click.url&#x60;.  Security scanners in corporate mail gateways sometimes follow links on delivery, which reports as a click. 

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
        WebhookPayloadEmailLinkClicked webhookPayloadEmailLinkClicked = new WebhookPayloadEmailLinkClicked(); // WebhookPayloadEmailLinkClicked | 
        try {
            ApiResponse<Void> response = apiInstance.onEmailLinkClickedWithHttpInfo(webhookPayloadEmailLinkClicked);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onEmailLinkClicked");
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
| **webhookPayloadEmailLinkClicked** | [**WebhookPayloadEmailLinkClicked**](WebhookPayloadEmailLinkClicked.md)|  | |

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


## onEmailOpened

> void onEmailOpened(webhookPayloadEmailOpened)

Email opened

A mail client loaded the open pixel of a message sent with &#x60;trackOpens: true&#x60;.  Opens are a signal, not proof of reading:  - Gmail and Apple Mail fetch images through their own proxies, some as soon as the mail arrives. - Clients that block images never report an open. - The sender viewing the message in their own Sent folder counts too.  Repeat fetches within 10 seconds raise &#x60;count&#x60; without firing again. 

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
        WebhookPayloadEmailOpened webhookPayloadEmailOpened = new WebhookPayloadEmailOpened(); // WebhookPayloadEmailOpened | 
        try {
            apiInstance.onEmailOpened(webhookPayloadEmailOpened);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onEmailOpened");
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
| **webhookPayloadEmailOpened** | [**WebhookPayloadEmailOpened**](WebhookPayloadEmailOpened.md)|  | |

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

## onEmailOpenedWithHttpInfo

> ApiResponse<Void> onEmailOpened onEmailOpenedWithHttpInfo(webhookPayloadEmailOpened)

Email opened

A mail client loaded the open pixel of a message sent with &#x60;trackOpens: true&#x60;.  Opens are a signal, not proof of reading:  - Gmail and Apple Mail fetch images through their own proxies, some as soon as the mail arrives. - Clients that block images never report an open. - The sender viewing the message in their own Sent folder counts too.  Repeat fetches within 10 seconds raise &#x60;count&#x60; without firing again. 

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
        WebhookPayloadEmailOpened webhookPayloadEmailOpened = new WebhookPayloadEmailOpened(); // WebhookPayloadEmailOpened | 
        try {
            ApiResponse<Void> response = apiInstance.onEmailOpenedWithHttpInfo(webhookPayloadEmailOpened);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onEmailOpened");
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
| **webhookPayloadEmailOpened** | [**WebhookPayloadEmailOpened**](WebhookPayloadEmailOpened.md)|  | |

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


## onEmailSendFailed

> void onEmailSendFailed(webhookPayloadEmailSendFailed)

Scheduled email failed

A send scheduled with &#x60;scheduledFor&#x60; could not leave at its time. Nothing reached the recipients. &#x60;error&#x60; says why, for example the mailbox was disconnected, the daily send cap was reached or the provider refused the mail. The send stays listed with &#x60;status: failed&#x60;; schedule it again to retry. 

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
        WebhookPayloadEmailSendFailed webhookPayloadEmailSendFailed = new WebhookPayloadEmailSendFailed(); // WebhookPayloadEmailSendFailed | 
        try {
            apiInstance.onEmailSendFailed(webhookPayloadEmailSendFailed);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onEmailSendFailed");
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
| **webhookPayloadEmailSendFailed** | [**WebhookPayloadEmailSendFailed**](WebhookPayloadEmailSendFailed.md)|  | |

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

## onEmailSendFailedWithHttpInfo

> ApiResponse<Void> onEmailSendFailed onEmailSendFailedWithHttpInfo(webhookPayloadEmailSendFailed)

Scheduled email failed

A send scheduled with &#x60;scheduledFor&#x60; could not leave at its time. Nothing reached the recipients. &#x60;error&#x60; says why, for example the mailbox was disconnected, the daily send cap was reached or the provider refused the mail. The send stays listed with &#x60;status: failed&#x60;; schedule it again to retry. 

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
        WebhookPayloadEmailSendFailed webhookPayloadEmailSendFailed = new WebhookPayloadEmailSendFailed(); // WebhookPayloadEmailSendFailed | 
        try {
            ApiResponse<Void> response = apiInstance.onEmailSendFailedWithHttpInfo(webhookPayloadEmailSendFailed);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onEmailSendFailed");
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
| **webhookPayloadEmailSendFailed** | [**WebhookPayloadEmailSendFailed**](WebhookPayloadEmailSendFailed.md)|  | |

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


## onEmailSent

> void onEmailSent(webhookPayloadEmailSent)

Email sent

A mail left through the email API. Exactly one event per mail, whichever path sent it: &#x60;source&#x60; is &#x60;send&#x60;, &#x60;reply&#x60;, &#x60;forward&#x60;, &#x60;draft&#x60; or &#x60;scheduled&#x60;. A scheduled draft carries both &#x60;scheduleId&#x60; and &#x60;draftId&#x60;.  Use it to record sends in your own system with the &#x60;metadata&#x60; you passed. The sent copy also arrives as &#x60;message.sent&#x60; in the inbox. 

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
        WebhookPayloadEmailSent webhookPayloadEmailSent = new WebhookPayloadEmailSent(); // WebhookPayloadEmailSent | 
        try {
            apiInstance.onEmailSent(webhookPayloadEmailSent);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onEmailSent");
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
| **webhookPayloadEmailSent** | [**WebhookPayloadEmailSent**](WebhookPayloadEmailSent.md)|  | |

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

## onEmailSentWithHttpInfo

> ApiResponse<Void> onEmailSent onEmailSentWithHttpInfo(webhookPayloadEmailSent)

Email sent

A mail left through the email API. Exactly one event per mail, whichever path sent it: &#x60;source&#x60; is &#x60;send&#x60;, &#x60;reply&#x60;, &#x60;forward&#x60;, &#x60;draft&#x60; or &#x60;scheduled&#x60;. A scheduled draft carries both &#x60;scheduleId&#x60; and &#x60;draftId&#x60;.  Use it to record sends in your own system with the &#x60;metadata&#x60; you passed. The sent copy also arrives as &#x60;message.sent&#x60; in the inbox. 

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
        WebhookPayloadEmailSent webhookPayloadEmailSent = new WebhookPayloadEmailSent(); // WebhookPayloadEmailSent | 
        try {
            ApiResponse<Void> response = apiInstance.onEmailSentWithHttpInfo(webhookPayloadEmailSent);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onEmailSent");
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
| **webhookPayloadEmailSent** | [**WebhookPayloadEmailSent**](WebhookPayloadEmailSent.md)|  | |

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


## onEmailThreadReplied

> void onEmailThreadReplied(webhookPayloadEmailThreadReplied)

Email thread replied

Mail from someone other than the mailbox arrived in the thread of a message sent with &#x60;trackReplies: true&#x60;. Works on text and html sends. Auto-replies count as replies; bounce reports do not and fire &#x60;email.bounced&#x60; instead.  &#x60;reply.clean.text&#x60; is the reply without the quoted history, so an agent can act on it without reading the message. The reply also arrives as &#x60;message.received&#x60; with its full content. 

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
        WebhookPayloadEmailThreadReplied webhookPayloadEmailThreadReplied = new WebhookPayloadEmailThreadReplied(); // WebhookPayloadEmailThreadReplied | 
        try {
            apiInstance.onEmailThreadReplied(webhookPayloadEmailThreadReplied);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onEmailThreadReplied");
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
| **webhookPayloadEmailThreadReplied** | [**WebhookPayloadEmailThreadReplied**](WebhookPayloadEmailThreadReplied.md)|  | |

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

## onEmailThreadRepliedWithHttpInfo

> ApiResponse<Void> onEmailThreadReplied onEmailThreadRepliedWithHttpInfo(webhookPayloadEmailThreadReplied)

Email thread replied

Mail from someone other than the mailbox arrived in the thread of a message sent with &#x60;trackReplies: true&#x60;. Works on text and html sends. Auto-replies count as replies; bounce reports do not and fire &#x60;email.bounced&#x60; instead.  &#x60;reply.clean.text&#x60; is the reply without the quoted history, so an agent can act on it without reading the message. The reply also arrives as &#x60;message.received&#x60; with its full content. 

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
        WebhookPayloadEmailThreadReplied webhookPayloadEmailThreadReplied = new WebhookPayloadEmailThreadReplied(); // WebhookPayloadEmailThreadReplied | 
        try {
            ApiResponse<Void> response = apiInstance.onEmailThreadRepliedWithHttpInfo(webhookPayloadEmailThreadReplied);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onEmailThreadReplied");
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
| **webhookPayloadEmailThreadReplied** | [**WebhookPayloadEmailThreadReplied**](WebhookPayloadEmailThreadReplied.md)|  | |

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

A file the account can reach was created in Google Drive or OneDrive.  ### Platform notes  A folder counts as a file. The event is pushed seconds after the change. 

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

A file the account can reach was created in Google Drive or OneDrive.  ### Platform notes  A folder counts as a file. The event is pushed seconds after the change. 

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

A file the account could reach was deleted or moved to the trash. 

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

A file the account could reach was deleted or moved to the trash. 

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

The user picked files in a picker session; &#x60;picker.files&#x60; lists each one&#39;s &#x60;id&#x60;, &#x60;name&#x60;, &#x60;mimeType&#x60; and &#x60;kind&#x60;.  ### When it fires  It fires when the user finishes a hosted picker session (&#x60;POST /v1/files/picker-sessions&#x60;) and picks at least one file. Not sent on cancel. The files are readable from then on. 

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

The user picked files in a picker session; &#x60;picker.files&#x60; lists each one&#39;s &#x60;id&#x60;, &#x60;name&#x60;, &#x60;mimeType&#x60; and &#x60;kind&#x60;.  ### When it fires  It fires when the user finishes a hosted picker session (&#x60;POST /v1/files/picker-sessions&#x60;) and picks at least one file. Not sent on cancel. The files are readable from then on. 

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

A file the account can reach was changed, renamed or moved. 

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

A file the account can reach was changed, renamed or moved. 

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

A new lead was submitted against a Meta Lead Gen (Instant) form or a TikTok Instant Form (both pushed by the network), or a Google Ads or LinkedIn lead form (read every 15 minutes). &#x60;lead.platform&#x60; names the network.  Leads older than 7 days when Zernio first reads them are stored without this event.  ### Payload notes  &#x60;lead.fields&#x60; maps question key to answer; multiple-choice values are the option key (for example &#x60;k1&#x60;), not the display label.  ### Provenance  &#x60;lead.formId&#x60;, &#x60;lead.adId&#x60; and &#x60;lead.campaignId&#x60; give provenance. &#x60;lead.adId&#x60; is null for organic or test leads.  ### Consents  &#x60;lead.consents&#x60; lists the answer to every custom disclaimer checkbox, for example &#x60;{ \&quot;checkboxKey\&quot;: \&quot;call_consent\&quot;, \&quot;isChecked\&quot;: true }&#x60;. Route call and SMS consent into your CRM from it. Empty when the form has no checkboxes.  ### Checkbox keys  When no key was set on the checkbox, Meta derives &#x60;checkboxKey&#x60; from its text, so match on the full key. &#x60;GET /v1/ads/leads&#x60; and &#x60;GET /v1/ads/lead-forms/{formId}/leads&#x60; return the same array.  ### Deduplication  Deduplicate on &#x60;lead.leadgenId&#x60; (Meta&#39;s lead id) or the event &#x60;id&#x60;.  ### Routing  &#x60;account.profileId&#x60; names the Zernio profile of the Facebook account that received the lead, for multi-tenant routing. Always present, &#x60;null&#x60; only when no profile is on record.  ### Requires ads enabled  Needs ads enabled on the team. Zernio asks for &#x60;leads_retrieval&#x60; at Facebook consent only then; without it Meta refuses the Page&#39;s &#x60;leadgen&#x60; subscription. Accounts connected earlier need a reconnect.  ### Lost subscription  A Page can lose its &#x60;leadgen&#x60; subscription while other events keep arriving. &#x60;leadgen: false&#x60; (with a &#x60;warning&#x60;) on the Page&#39;s webhook subscription means leads are not reaching Zernio; re-subscribe the Page. 

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

A new lead was submitted against a Meta Lead Gen (Instant) form or a TikTok Instant Form (both pushed by the network), or a Google Ads or LinkedIn lead form (read every 15 minutes). &#x60;lead.platform&#x60; names the network.  Leads older than 7 days when Zernio first reads them are stored without this event.  ### Payload notes  &#x60;lead.fields&#x60; maps question key to answer; multiple-choice values are the option key (for example &#x60;k1&#x60;), not the display label.  ### Provenance  &#x60;lead.formId&#x60;, &#x60;lead.adId&#x60; and &#x60;lead.campaignId&#x60; give provenance. &#x60;lead.adId&#x60; is null for organic or test leads.  ### Consents  &#x60;lead.consents&#x60; lists the answer to every custom disclaimer checkbox, for example &#x60;{ \&quot;checkboxKey\&quot;: \&quot;call_consent\&quot;, \&quot;isChecked\&quot;: true }&#x60;. Route call and SMS consent into your CRM from it. Empty when the form has no checkboxes.  ### Checkbox keys  When no key was set on the checkbox, Meta derives &#x60;checkboxKey&#x60; from its text, so match on the full key. &#x60;GET /v1/ads/leads&#x60; and &#x60;GET /v1/ads/lead-forms/{formId}/leads&#x60; return the same array.  ### Deduplication  Deduplicate on &#x60;lead.leadgenId&#x60; (Meta&#39;s lead id) or the event &#x60;id&#x60;.  ### Routing  &#x60;account.profileId&#x60; names the Zernio profile of the Facebook account that received the lead, for multi-tenant routing. Always present, &#x60;null&#x60; only when no profile is on record.  ### Requires ads enabled  Needs ads enabled on the team. Zernio asks for &#x60;leads_retrieval&#x60; at Facebook consent only then; without it Meta refuses the Page&#39;s &#x60;leadgen&#x60; subscription. Accounts connected earlier need a reconnect.  ### Lost subscription  A Page can lose its &#x60;leadgen&#x60; subscription while other events keep arriving. &#x60;leadgen: false&#x60; (with a &#x60;warning&#x60;) on the Page&#39;s webhook subscription means leads are not reaching Zernio; re-subscribe the Page. 

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


## onMentionReceived

> void onMentionReceived(webhookPayloadMention)

Mention received event

A connected Instagram, Facebook or LinkedIn account was mentioned in a post, caption or comment.  ### When it fires  Once per mention, the first time Zernio sees it. Delivery is at most once: reconcile with &#x60;GET /v1/inbox/mentions&#x60;.  - Instagram and Facebook arrive in real time from the platform&#39;s webhook. - LinkedIn arrives from its webhook or from polling, so delivery can take minutes. A newly connected account can receive mentions from the last 48 hours once.  ### Payload notes  Carries the same fields as &#x60;GET /v1/inbox/mentions&#x60;. Fields a platform does not provide are null. A LinkedIn mention found by polling for a team that does not retain content has no author, and an Instagram mention has no content if the live read fails. 

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
        WebhookPayloadMention webhookPayloadMention = new WebhookPayloadMention(); // WebhookPayloadMention | 
        try {
            apiInstance.onMentionReceived(webhookPayloadMention);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMentionReceived");
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
| **webhookPayloadMention** | [**WebhookPayloadMention**](WebhookPayloadMention.md)|  | |

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

## onMentionReceivedWithHttpInfo

> ApiResponse<Void> onMentionReceived onMentionReceivedWithHttpInfo(webhookPayloadMention)

Mention received event

A connected Instagram, Facebook or LinkedIn account was mentioned in a post, caption or comment.  ### When it fires  Once per mention, the first time Zernio sees it. Delivery is at most once: reconcile with &#x60;GET /v1/inbox/mentions&#x60;.  - Instagram and Facebook arrive in real time from the platform&#39;s webhook. - LinkedIn arrives from its webhook or from polling, so delivery can take minutes. A newly connected account can receive mentions from the last 48 hours once.  ### Payload notes  Carries the same fields as &#x60;GET /v1/inbox/mentions&#x60;. Fields a platform does not provide are null. A LinkedIn mention found by polling for a team that does not retain content has no author, and an Instagram mention has no content if the live read fails. 

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
        WebhookPayloadMention webhookPayloadMention = new WebhookPayloadMention(); // WebhookPayloadMention | 
        try {
            ApiResponse<Void> response = apiInstance.onMentionReceivedWithHttpInfo(webhookPayloadMention);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onMentionReceived");
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
| **webhookPayloadMention** | [**WebhookPayloadMention**](WebhookPayloadMention.md)|  | |

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

A sender deleted (unsent) a message on Instagram or WhatsApp.  ### Platform notes  Instagram reports incoming unsends. WhatsApp reports both directions, including business deletions through the Cloud API or a Coexistence app. &#x60;message.direction&#x60; tells them apart.  ### Payload notes  The payload keeps the pre-delete &#x60;text&#x60; and &#x60;attachments&#x60; for moderation, compliance or archival. The Zernio dashboard does not show this content. 

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

A sender deleted (unsent) a message on Instagram or WhatsApp.  ### Platform notes  Instagram reports incoming unsends. WhatsApp reports both directions, including business deletions through the Cloud API or a Coexistence app. &#x60;message.direction&#x60; tells them apart.  ### Payload notes  The payload keeps the pre-delete &#x60;text&#x60; and &#x60;attachments&#x60; for moderation, compliance or archival. The Zernio dashboard does not show this content. 

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

An outgoing message was delivered to the recipient on WhatsApp, Facebook Messenger, SMS, RCS or iMessage.  ### Platform notes  On WhatsApp, &#x60;pricing&#x60; and &#x60;billingConversation&#x60; carry Meta&#39;s billing context for the message. 

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

An outgoing message was delivered to the recipient on WhatsApp, Facebook Messenger, SMS, RCS or iMessage.  ### Platform notes  On WhatsApp, &#x60;pricing&#x60; and &#x60;billingConversation&#x60; carry Meta&#39;s billing context for the message. 

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

A sender edited a previously sent message on Instagram, Facebook Messenger, Telegram or WhatsApp.  ### Payload notes  &#x60;editHistory&#x60; holds every prior version, oldest first. &#x60;message.text&#x60; is the latest version. 

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

A sender edited a previously sent message on Instagram, Facebook Messenger, Telegram or WhatsApp.  ### Payload notes  &#x60;editHistory&#x60; holds every prior version, oldest first. &#x60;message.text&#x60; is the latest version. 

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

An outgoing message failed to deliver on WhatsApp, SMS, RCS or iMessage.  ### Payload notes  &#x60;error&#x60; carries &#x60;code&#x60;, &#x60;title&#x60; and &#x60;message&#x60; from the platform, for example &#x60;131026&#x60; for an unreachable WhatsApp recipient. On SMS it carries the carrier&#39;s error code. 

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

An outgoing message failed to deliver on WhatsApp, SMS, RCS or iMessage.  ### Payload notes  &#x60;error&#x60; carries &#x60;code&#x60;, &#x60;title&#x60; and &#x60;message&#x60; from the platform, for example &#x60;131026&#x60; for an unreachable WhatsApp recipient. On SMS it carries the carrier&#39;s error code. 

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

A WhatsApp recipient played a voice message you sent, reported the first time they play it. 

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

A WhatsApp recipient played a voice message you sent, reported the first time they play it. 

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

An outgoing message was read by the recipient on WhatsApp, Facebook Messenger, Instagram or RCS. 

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

An outgoing message was read by the recipient on WhatsApp, Facebook Messenger, Instagram or RCS. 

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

A new message arrived in the inbox; &#x60;message.text&#x60;, &#x60;message.attachments[]&#x60; and &#x60;message.sender&#x60; describe it.  ### Standby  While another app owns the conversation it carries &#x60;metadata.standby: true&#x60;. Zernio runs no workflow or keyword automation on it. A bot must skip standby messages, or on WhatsApp it takes the conversation from the agent.  ### Interactive replies  Button and list taps, flow responses and orders arrive under &#x60;metadata&#x60; (&#x60;interactiveType&#x60;, &#x60;interactiveId&#x60;, &#x60;flowResponseData&#x60;, &#x60;order&#x60;). Only a referral that arrives without a message becomes &#x60;referral.received&#x60;.  ### Platform notes  New email from Google, Microsoft and IMAP mailboxes arrives as this event. 

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

A new message arrived in the inbox; &#x60;message.text&#x60;, &#x60;message.attachments[]&#x60; and &#x60;message.sender&#x60; describe it.  ### Standby  While another app owns the conversation it carries &#x60;metadata.standby: true&#x60;. Zernio runs no workflow or keyword automation on it. A bot must skip standby messages, or on WhatsApp it takes the conversation from the agent.  ### Interactive replies  Button and list taps, flow responses and orders arrive under &#x60;metadata&#x60; (&#x60;interactiveType&#x60;, &#x60;interactiveId&#x60;, &#x60;flowResponseData&#x60;, &#x60;order&#x60;). Only a referral that arrives without a message becomes &#x60;referral.received&#x60;.  ### Platform notes  New email from Google, Microsoft and IMAP mailboxes arrives as this event. 

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

A message was sent through the API, the dashboard, or the WhatsApp Business app on Coexistence numbers.  ### Sender  &#x60;message.sentVia&#x60; is one of &#x60;human&#x60;, &#x60;api&#x60;, &#x60;broadcast&#x60;, &#x60;sequence&#x60;, &#x60;workflow&#x60;, &#x60;comment_automation&#x60; or &#x60;bulk-api&#x60;. It is &#x60;null&#x60; for sends from the platform&#39;s own app and for older messages; treat &#x60;null&#x60; as unknown, never as human.  ### Attribution keys  &#x60;automationId&#x60;, &#x60;workflowId&#x60;, &#x60;executionId&#x60;, &#x60;broadcastId&#x60; and &#x60;sequenceId&#x60; are always present. Each is &#x60;null&#x60; unless that kind of sender produced the message.  ### Quote replies  A quote-reply sent through the API carries &#x60;metadata.quotedMessageId&#x60;. One sent from the WhatsApp Business or Instagram app does not.  ### Platform notes  On Instagram and Facebook the attribution can be missing when Meta&#39;s echo of a send reaches Zernio before the send is recorded. On WhatsApp, Meta Business Agent replies carry &#x60;source: \&quot;meta_business_agent\&quot;&#x60;. 

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

A message was sent through the API, the dashboard, or the WhatsApp Business app on Coexistence numbers.  ### Sender  &#x60;message.sentVia&#x60; is one of &#x60;human&#x60;, &#x60;api&#x60;, &#x60;broadcast&#x60;, &#x60;sequence&#x60;, &#x60;workflow&#x60;, &#x60;comment_automation&#x60; or &#x60;bulk-api&#x60;. It is &#x60;null&#x60; for sends from the platform&#39;s own app and for older messages; treat &#x60;null&#x60; as unknown, never as human.  ### Attribution keys  &#x60;automationId&#x60;, &#x60;workflowId&#x60;, &#x60;executionId&#x60;, &#x60;broadcastId&#x60; and &#x60;sequenceId&#x60; are always present. Each is &#x60;null&#x60; unless that kind of sender produced the message.  ### Quote replies  A quote-reply sent through the API carries &#x60;metadata.quotedMessageId&#x60;. One sent from the WhatsApp Business or Instagram app does not.  ### Platform notes  On Instagram and Facebook the attribution can be missing when Meta&#39;s echo of a send reaches Zernio before the send is recorded. On WhatsApp, Meta Business Agent replies carry &#x60;source: \&quot;meta_business_agent\&quot;&#x60;. 

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

A country you watch has deliverable phone numbers again; fires once per watch.  ### When it fires  Fired by the 6-hourly stock sweep, before you own a number in that country. The watch (&#x60;POST /v1/phone-numbers/stock-watches&#x60;) is then consumed.  ### Payload notes  &#x60;stock.country&#x60; is the watched country. &#x60;stock.types[]&#x60; lists each number type in stock with its &#x60;availableCount&#x60; at sweep time. Numbers are first come, first served; buy with &#x60;POST /v1/phone-numbers/purchase&#x60;. 

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

A country you watch has deliverable phone numbers again; fires once per watch.  ### When it fires  Fired by the 6-hourly stock sweep, before you own a number in that country. The watch (&#x60;POST /v1/phone-numbers/stock-watches&#x60;) is then consumed.  ### Payload notes  &#x60;stock.country&#x60; is the watched country. &#x60;stock.types[]&#x60; lists each number type in stock with its &#x60;availableCount&#x60; at sweep time. Numbers are first come, first served; buy with &#x60;POST /v1/phone-numbers/purchase&#x60;. 

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

A tracked post&#39;s authenticity score crossed 40, in either direction.  ### When it fires  Only while the tracking window is open. A post&#39;s first score never fires it.  ### Payload notes  Carries &#x60;score&#x60;, &#x60;previousScore&#x60;, &#x60;confidence&#x60; and &#x60;reasons&#x60;. 

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

A tracked post&#39;s authenticity score crossed 40, in either direction.  ### When it fires  Only while the tracking window is open. A post&#39;s first score never fires it.  ### Payload notes  Carries &#x60;score&#x60;, &#x60;previousScore&#x60;, &#x60;confidence&#x60; and &#x60;reasons&#x60;. 

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

A scheduled post was cancelled because its account was disconnected, and nothing published.  ### When it fires  A multi-platform post fires it only once every platform entry is cancelled. If a platform already published, the rollup is &#x60;post.partial&#x60; instead.  ### When it does not fire  &#x60;DELETE /v1/posts/{postId}&#x60; removes the post without sending this event. 

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

A scheduled post was cancelled because its account was disconnected, and nothing published.  ### When it fires  A multi-platform post fires it only once every platform entry is cancelled. If a platform already published, the rollup is &#x60;post.partial&#x60; instead.  ### When it does not fire  &#x60;DELETE /v1/posts/{postId}&#x60; removes the post without sending this event. 

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

A post authored natively on the platform, outside Zernio, was detected for the first time.  ### When it fires  Detected by a background sync roughly hourly, not in real time. Example: a Google Business Profile post created in the Google interface.  ### Payload notes  &#x60;post.source&#x60; is always &#x60;\&quot;external\&quot;&#x60; and &#x60;post.id&#x60; is the platform-native post id.  ### First sync backfill  On a freshly connected account, every existing native post fires it once. Treat it as an idempotent upsert keyed on &#x60;post.id&#x60;. 

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

A post authored natively on the platform, outside Zernio, was detected for the first time.  ### When it fires  Detected by a background sync roughly hourly, not in real time. Example: a Google Business Profile post created in the Google interface.  ### Payload notes  &#x60;post.source&#x60; is always &#x60;\&quot;external\&quot;&#x60; and &#x60;post.id&#x60; is the platform-native post id.  ### First sync backfill  On a freshly connected account, every existing native post fires it once. Treat it as an idempotent upsert keyed on &#x60;post.id&#x60;. 

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

A tracked native post was removed from the platform.  ### Payload notes  &#x60;post.deletedAt&#x60; is the detection time.  ### Detection limits  Coverage is bounded to the most recent posts the platform listing returns, so very old deletions may go undetected.  ### When it does not fire  Detection diffs against posts a prior sync already indexed. An account with no indexed post never emits it. 

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

A tracked native post was removed from the platform.  ### Payload notes  &#x60;post.deletedAt&#x60; is the detection time.  ### Detection limits  Coverage is bounded to the most recent posts the platform listing returns, so very old deletions may go undetected.  ### When it does not fire  Detection diffs against posts a prior sync already indexed. An account with no indexed post never emits it. 

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

A tracked native post&#39;s text or media changed on the platform.  ### How edits are detected  Zernio compares text and media structure and, where available, the platform&#39;s own edit timestamp. A media-URL-only refresh (rotated CDN URLs) does not fire it. 

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

A tracked native post&#39;s text or media changed on the platform.  ### How edits are detected  Zernio compares text and media structure and, where available, the platform&#39;s own edit timestamp. A media-URL-only refresh (rotated CDN URLs) does not fire it. 

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

A post failed on every target platform.  ### When it fires  Once per publishing job, after every platform target ends. Exactly one of &#x60;post.published&#x60;, &#x60;post.partial&#x60; or &#x60;post.failed&#x60; fires.  A TikTok target TikTok is still processing (status &#x60;uploading&#x60;) holds it for up to 48 hours. Meanwhile &#x60;post.platform.published&#x60; and &#x60;post.platform.failed&#x60; report the other targets.  ### Payload notes  Each &#x60;platforms[]&#x60; entry carries &#x60;error&#x60;, &#x60;errorCategory&#x60; and &#x60;errorSource&#x60;, the same taxonomy as &#x60;platforms[]&#x60; on Get post. Branch on &#x60;errorCategory&#x60;, not on the message text. 

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

A post failed on every target platform.  ### When it fires  Once per publishing job, after every platform target ends. Exactly one of &#x60;post.published&#x60;, &#x60;post.partial&#x60; or &#x60;post.failed&#x60; fires.  A TikTok target TikTok is still processing (status &#x60;uploading&#x60;) holds it for up to 48 hours. Meanwhile &#x60;post.platform.published&#x60; and &#x60;post.platform.failed&#x60; report the other targets.  ### Payload notes  Each &#x60;platforms[]&#x60; entry carries &#x60;error&#x60;, &#x60;errorCategory&#x60; and &#x60;errorSource&#x60;, the same taxonomy as &#x60;platforms[]&#x60; on Get post. Branch on &#x60;errorCategory&#x60;, not on the message text. 

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

A post published on some platforms and failed on others.  ### When it fires  Once per publishing job, after every platform target ends. Exactly one of &#x60;post.published&#x60;, &#x60;post.partial&#x60; or &#x60;post.failed&#x60; fires.  A TikTok target TikTok is still processing (status &#x60;uploading&#x60;) holds it for up to 48 hours. Meanwhile &#x60;post.platform.published&#x60; and &#x60;post.platform.failed&#x60; report the other targets.  It can follow a &#x60;post.failed&#x60; for the same post when TikTok later reports a failed TikTok target as published.  ### Payload notes  Read &#x60;platforms[].status&#x60; to tell them apart. Failed entries carry &#x60;error&#x60;, &#x60;errorCategory&#x60; and &#x60;errorSource&#x60;. 

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

A post published on some platforms and failed on others.  ### When it fires  Once per publishing job, after every platform target ends. Exactly one of &#x60;post.published&#x60;, &#x60;post.partial&#x60; or &#x60;post.failed&#x60; fires.  A TikTok target TikTok is still processing (status &#x60;uploading&#x60;) holds it for up to 48 hours. Meanwhile &#x60;post.platform.published&#x60; and &#x60;post.platform.failed&#x60; report the other targets.  It can follow a &#x60;post.failed&#x60; for the same post when TikTok later reports a failed TikTok target as published.  ### Payload notes  Read &#x60;platforms[].status&#x60; to tell them apart. Failed entries carry &#x60;error&#x60;, &#x60;errorCategory&#x60; and &#x60;errorSource&#x60;. 

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

A published platform target was deleted on the platform.  ### When it fires  Detected by a background sync roughly hourly, once per platform target. Platforms push no deletion notice, so it can trail the rollup by days.  ### Payload notes  &#x60;platform.status&#x60; is &#x60;deleted&#x60;. &#x60;platform.deletedAt&#x60; is the detection time, not the moment of deletion.  ### Detection limits  Detection is listing-based: coverage is bounded to the posts the listing returns, and rare false positives happen. The event is not retracted when the post reappears. Re-check before deleting.  ### When it does not fire  Detection diffs against posts a prior sync already indexed. An account with no indexed post never emits it. 

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

A published platform target was deleted on the platform.  ### When it fires  Detected by a background sync roughly hourly, once per platform target. Platforms push no deletion notice, so it can trail the rollup by days.  ### Payload notes  &#x60;platform.status&#x60; is &#x60;deleted&#x60;. &#x60;platform.deletedAt&#x60; is the detection time, not the moment of deletion.  ### Detection limits  Detection is listing-based: coverage is bounded to the posts the listing returns, and rare false positives happen. The event is not retracted when the post reappears. Re-check before deleting.  ### When it does not fire  Detection diffs against posts a prior sync already indexed. An account with no indexed post never emits it. 

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

One platform target failed permanently.  ### When it fires  Only on permanent failure; retryable errors stay silent. The rollup (&#x60;post.failed&#x60; or &#x60;post.partial&#x60;) fires separately once every platform ends.  ### After a publish  It can fire for a target that already emitted &#x60;post.platform.published&#x60;, if background reconciliation finds the publish never completed.  ### Payload notes  &#x60;platform.error&#x60; carries the platform&#39;s message. &#x60;platform.errorCategory&#x60; and &#x60;platform.errorSource&#x60; classify it, so a reconnect (&#x60;auth_expired&#x60;) separates from a content fix (&#x60;user_content&#x60;). 

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

One platform target failed permanently.  ### When it fires  Only on permanent failure; retryable errors stay silent. The rollup (&#x60;post.failed&#x60; or &#x60;post.partial&#x60;) fires separately once every platform ends.  ### After a publish  It can fire for a target that already emitted &#x60;post.platform.published&#x60;, if background reconciliation finds the publish never completed.  ### Payload notes  &#x60;platform.error&#x60; carries the platform&#39;s message. &#x60;platform.errorCategory&#x60; and &#x60;platform.errorSource&#x60; classify it, so a reconnect (&#x60;auth_expired&#x60;) separates from a content fix (&#x60;user_content&#x60;). 

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

One platform target finished publishing, without waiting for the other targets.  ### When it fires  Once per platform target, as soon as it finishes. A cross-post to 2 accounts on the same platform produces 2 events. Use &#x60;post.published&#x60; for the post-level rollup.  ### Payload notes  &#x60;platform&#x60; carries the platform post id and URL. &#x60;account&#x60; identifies the connected account.  ### TikTok targets still processing  TikTok can keep processing a post for up to 48 hours (entry status &#x60;uploading&#x60;). That target fires when TikTok finishes. The other targets fire as they finish, and the post rollup waits for TikTok.  ### Later reconciliation  If a target later fails background reconciliation, &#x60;post.platform.failed&#x60; fires for the same target afterward.  A failed TikTok target that TikTok later reports as published fires &#x60;post.platform.published&#x60; afterward, and the rollup fires again. 

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

One platform target finished publishing, without waiting for the other targets.  ### When it fires  Once per platform target, as soon as it finishes. A cross-post to 2 accounts on the same platform produces 2 events. Use &#x60;post.published&#x60; for the post-level rollup.  ### Payload notes  &#x60;platform&#x60; carries the platform post id and URL. &#x60;account&#x60; identifies the connected account.  ### TikTok targets still processing  TikTok can keep processing a post for up to 48 hours (entry status &#x60;uploading&#x60;). That target fires when TikTok finishes. The other targets fire as they finish, and the post rollup waits for TikTok.  ### Later reconciliation  If a target later fails background reconciliation, &#x60;post.platform.failed&#x60; fires for the same target afterward.  A failed TikTok target that TikTok later reports as published fires &#x60;post.platform.published&#x60; afterward, and the rollup fires again. 

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

Every platform target of a post published.  ### When it fires  Once per publishing job, after every platform target ends. Exactly one of &#x60;post.published&#x60;, &#x60;post.partial&#x60; or &#x60;post.failed&#x60; fires.  A TikTok target TikTok is still processing (status &#x60;uploading&#x60;) holds it for up to 48 hours. Meanwhile &#x60;post.platform.published&#x60; and &#x60;post.platform.failed&#x60; report the other targets.  It can follow a &#x60;post.partial&#x60; or &#x60;post.failed&#x60; for the same post when TikTok later reports a failed TikTok target as published.  ### Payload notes  Each &#x60;platforms[]&#x60; entry carries the &#x60;platformPostId&#x60; and &#x60;publishedUrl&#x60;. 

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

Every platform target of a post published.  ### When it fires  Once per publishing job, after every platform target ends. Exactly one of &#x60;post.published&#x60;, &#x60;post.partial&#x60; or &#x60;post.failed&#x60; fires.  A TikTok target TikTok is still processing (status &#x60;uploading&#x60;) holds it for up to 48 hours. Meanwhile &#x60;post.platform.published&#x60; and &#x60;post.platform.failed&#x60; report the other targets.  It can follow a &#x60;post.partial&#x60; or &#x60;post.failed&#x60; for the same post when TikTok later reports a failed TikTok target as published.  ### Payload notes  Each &#x60;platforms[]&#x60; entry carries the &#x60;platformPostId&#x60; and &#x60;publishedUrl&#x60;. 

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

A recycling schedule cloned a published post for republishing.  ### Payload notes  &#x60;post.id&#x60; is the new clone&#39;s id. The clone emits its own &#x60;post.scheduled&#x60;. 

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

A recycling schedule cloned a published post for republishing.  ### Payload notes  &#x60;post.id&#x60; is the new clone&#39;s id. The clone emits its own &#x60;post.scheduled&#x60;. 

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

A post entered the scheduled state.  ### When it fires  Created with a schedule (with &#x60;publishNow&#x60;, accepted and queued), promoted from draft, added to a queue, retried after failing, or created as a recycled clone.  ### Approval and repeats  A post saved with &#x60;requiresApproval: true&#x60; fires it on approval, not at creation. One post can emit it more than once.  ### When it does not fire  Editing or moving an already-scheduled post to another time does not fire it. 

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

A post entered the scheduled state.  ### When it fires  Created with a schedule (with &#x60;publishNow&#x60;, accepted and queued), promoted from draft, added to a queue, retried after failing, or created as a recycled clone.  ### Approval and repeats  A post saved with &#x60;requiresApproval: true&#x60; fires it on approval, not at creation. One post can emit it more than once.  ### When it does not fire  Editing or moving an already-scheduled post to another time does not fire it. 

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

A published TikTok post&#39;s public URL became available.  ### When it fires  TikTok exposes the video id asynchronously, often minutes after upload, so &#x60;post.published&#x60; can carry an empty &#x60;publishedUrl&#x60;. Fires at most once per platform target. For a draft, it fires when the creator posts the draft publicly from the TikTok app.  ### Payload notes  Delivers &#x60;platform.publishedUrl&#x60; and the resolved &#x60;platform.platformPostId&#x60;. Same shape as &#x60;post.platform.published&#x60;.  ### When it does not fire  Private posts, which have no public URL, and drafts the creator never posts. 

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

A published TikTok post&#39;s public URL became available.  ### When it fires  TikTok exposes the video id asynchronously, often minutes after upload, so &#x60;post.published&#x60; can carry an empty &#x60;publishedUrl&#x60;. Fires at most once per platform target. For a draft, it fires when the creator posts the draft publicly from the TikTok app.  ### Payload notes  Delivers &#x60;platform.publishedUrl&#x60; and the resolved &#x60;platform.platformPostId&#x60;. Same shape as &#x60;post.platform.published&#x60;.  ### When it does not fire  Private posts, which have no public URL, and drafts the creator never posts. 

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

A post&#39;s tracking window ended and its final analytics read finished.  ### When it fires  Once per window. A cancelled window never fires it.  ### Payload notes  &#x60;final&#x60; holds the closing metrics, or is null when no sample could be read. When the post was deleted, it is the last sample held, if any.  ### Completion reasons  &#x60;window.completionReason&#x60; is &#x60;final_read&#x60; (the read succeeded), &#x60;unreachable&#x60; (the sync failed or no sample exists) or &#x60;post_deleted&#x60; (the post is gone). 

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

A post&#39;s tracking window ended and its final analytics read finished.  ### When it fires  Once per window. A cancelled window never fires it.  ### Payload notes  &#x60;final&#x60; holds the closing metrics, or is null when no sample could be read. When the post was deleted, it is the last sample held, if any.  ### Completion reasons  &#x60;window.completionReason&#x60; is &#x60;final_read&#x60; (the read succeeded), &#x60;unreachable&#x60; (the sync failed or no sample exists) or &#x60;post_deleted&#x60; (the post is gone). 

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

An RCS agent moved into a new customer-visible status; &#x60;status&#x60; is the new one.  ### Statuses  &#x60;changes_requested&#x60; (note in &#x60;reason&#x60;), &#x60;brand_vetting&#x60;, &#x60;agent_review&#x60;, &#x60;testing&#x60;, &#x60;launch_review&#x60;, &#x60;launching&#x60;, &#x60;live&#x60;, &#x60;rejected&#x60; (&#x60;reason&#x60; says why), &#x60;deactivated&#x60;. In &#x60;testing&#x60;, add test phones, then file the launch; a &#x60;reason&#x60; means it bounced.  ### When it fires  Fires once per move into a status. &#x60;requested&#x60; sends nothing. Overlapping status checks never send the same status twice in a row.  ### Payload notes  &#x60;agent.profileId&#x60; is the owning profile. &#x60;agent.accountId&#x60; is &#x60;null&#x60; when the agent has no linked account. 

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

An RCS agent moved into a new customer-visible status; &#x60;status&#x60; is the new one.  ### Statuses  &#x60;changes_requested&#x60; (note in &#x60;reason&#x60;), &#x60;brand_vetting&#x60;, &#x60;agent_review&#x60;, &#x60;testing&#x60;, &#x60;launch_review&#x60;, &#x60;launching&#x60;, &#x60;live&#x60;, &#x60;rejected&#x60; (&#x60;reason&#x60; says why), &#x60;deactivated&#x60;. In &#x60;testing&#x60;, add test phones, then file the launch; a &#x60;reason&#x60; means it bounced.  ### When it fires  Fires once per move into a status. &#x60;requested&#x60; sends nothing. Overlapping status checks never send the same status twice in a row.  ### Payload notes  &#x60;agent.profileId&#x60; is the owning profile. &#x60;agent.accountId&#x60; is &#x60;null&#x60; when the agent has no linked account. 

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

A participant added or removed an emoji reaction on a message on Instagram, Facebook, WhatsApp, Telegram, Slack or TikTok.  ### Payload notes  Sent as its own event, never as &#x60;message.received&#x60;. &#x60;reaction.action&#x60; is &#x60;added&#x60; or &#x60;removed&#x60;. &#x60;reaction.platformMessageId&#x60; is always present; &#x60;reaction.messageId&#x60; is the Zernio id when resolvable.  ### Removals  On WhatsApp, Instagram and Facebook removals, &#x60;reaction.emoji&#x60; is an empty string because the platform does not say which emoji went away. Match on &#x60;platformMessageId&#x60; to clear a mirrored reaction.  ### TikTok  A like or emoji reaction on a DM arrives only as this event, never as an empty &#x60;message.received&#x60;. &#x60;platformMessageId&#x60; is the TikTok id of the liked message. AI emoji reactions can have an empty &#x60;emoji&#x60;.  ### Telegram  The bot must be an administrator in the chat. Telegram does not send reactions in private chats to bots.  ### Accounts connected before August 2026  Instagram and Facebook accounts connected before August 2026 do not receive this event until their webhook subscription is refreshed. Reconnect them, or re-subscribe a Facebook Page without a reconnect. 

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

A participant added or removed an emoji reaction on a message on Instagram, Facebook, WhatsApp, Telegram, Slack or TikTok.  ### Payload notes  Sent as its own event, never as &#x60;message.received&#x60;. &#x60;reaction.action&#x60; is &#x60;added&#x60; or &#x60;removed&#x60;. &#x60;reaction.platformMessageId&#x60; is always present; &#x60;reaction.messageId&#x60; is the Zernio id when resolvable.  ### Removals  On WhatsApp, Instagram and Facebook removals, &#x60;reaction.emoji&#x60; is an empty string because the platform does not say which emoji went away. Match on &#x60;platformMessageId&#x60; to clear a mirrored reaction.  ### TikTok  A like or emoji reaction on a DM arrives only as this event, never as an empty &#x60;message.received&#x60;. &#x60;platformMessageId&#x60; is the TikTok id of the liked message. AI emoji reactions can have an empty &#x60;emoji&#x60;.  ### Telegram  The bot must be an administrator in the chat. Telegram does not send reactions in private chats to bots.  ### Accounts connected before August 2026  Instagram and Facebook accounts connected before August 2026 do not receive this event until their webhook subscription is refreshed. Reconnect them, or re-subscribe a Facebook Page without a reconnect. 

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

Someone opened an existing Instagram or Messenger thread through an ig.me or m.me &#x60;ref&#x60; link or returning ad click.  ### Payload notes  Meta&#39;s referral object is forwarded verbatim: &#x60;ref&#x60; and &#x60;source&#x60; for links, &#x60;ad_id&#x60; and &#x60;ads_context_data&#x60; for ad clicks.  ### When it does not fire  A referral that rides an inbound message arrives on &#x60;message.received&#x60; under &#x60;metadata.referral&#x60; instead. The two never fire for the same click.  ### Stored referral  The first referral captured on a conversation is also persisted on it (&#x60;metadata&#x60; on &#x60;GET /v1/inbox/conversations&#x60;). 

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

Someone opened an existing Instagram or Messenger thread through an ig.me or m.me &#x60;ref&#x60; link or returning ad click.  ### Payload notes  Meta&#39;s referral object is forwarded verbatim: &#x60;ref&#x60; and &#x60;source&#x60; for links, &#x60;ad_id&#x60; and &#x60;ads_context_data&#x60; for ad clicks.  ### When it does not fire  A referral that rides an inbound message arrives on &#x60;message.received&#x60; under &#x60;metadata.referral&#x60; instead. The two never fire for the same click.  ### Stored referral  The first referral captured on a conversation is also persisted on it (&#x60;metadata&#x60; on &#x60;GET /v1/inbox/conversations&#x60;). 

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


## onReviewDeleted

> void onReviewDeleted(webhookPayloadReviewDeleted)

Review deleted event

Google Business Profile stopped returning a review, for example after its spam filter removed it.  ### When it fires  Zernio detects it by polling, so it usually fires 6 to 12 hours after the review disappears. Only locations covered by a webhook subscribed to &#x60;review.deleted&#x60; or &#x60;review.restored&#x60; are checked.  ### Restores  If the review comes back, &#x60;review.restored&#x60; fires, so a hidden then restored review produces &#x60;review.deleted&#x60; then &#x60;review.restored&#x60;. A &#x60;review.updated&#x60; can arrive for a deleted review; the next check restores it.  ### Payload notes  &#x60;review.id&#x60; is the full review name, the same value &#x60;review.new&#x60; sent. It may arrive for a review id you never received &#x60;review.new&#x60; for, so ignore ids you do not know. 

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
        WebhookPayloadReviewDeleted webhookPayloadReviewDeleted = new WebhookPayloadReviewDeleted(); // WebhookPayloadReviewDeleted | 
        try {
            apiInstance.onReviewDeleted(webhookPayloadReviewDeleted);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onReviewDeleted");
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
| **webhookPayloadReviewDeleted** | [**WebhookPayloadReviewDeleted**](WebhookPayloadReviewDeleted.md)|  | |

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

## onReviewDeletedWithHttpInfo

> ApiResponse<Void> onReviewDeleted onReviewDeletedWithHttpInfo(webhookPayloadReviewDeleted)

Review deleted event

Google Business Profile stopped returning a review, for example after its spam filter removed it.  ### When it fires  Zernio detects it by polling, so it usually fires 6 to 12 hours after the review disappears. Only locations covered by a webhook subscribed to &#x60;review.deleted&#x60; or &#x60;review.restored&#x60; are checked.  ### Restores  If the review comes back, &#x60;review.restored&#x60; fires, so a hidden then restored review produces &#x60;review.deleted&#x60; then &#x60;review.restored&#x60;. A &#x60;review.updated&#x60; can arrive for a deleted review; the next check restores it.  ### Payload notes  &#x60;review.id&#x60; is the full review name, the same value &#x60;review.new&#x60; sent. It may arrive for a review id you never received &#x60;review.new&#x60; for, so ignore ids you do not know. 

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
        WebhookPayloadReviewDeleted webhookPayloadReviewDeleted = new WebhookPayloadReviewDeleted(); // WebhookPayloadReviewDeleted | 
        try {
            ApiResponse<Void> response = apiInstance.onReviewDeletedWithHttpInfo(webhookPayloadReviewDeleted);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onReviewDeleted");
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
| **webhookPayloadReviewDeleted** | [**WebhookPayloadReviewDeleted**](WebhookPayloadReviewDeleted.md)|  | |

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

A new review was posted on a connected Google Business Profile account, in real time through Pub/Sub. 

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

A new review was posted on a connected Google Business Profile account, in real time through Pub/Sub. 

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


## onReviewRestored

> void onReviewRestored(webhookPayloadReviewRestored)

Review restored event

Google returned a review previously reported by &#x60;review.deleted&#x60;; the payload has the same shape as &#x60;review.new&#x60;.  ### When it fires  It may reach a webhook that subscribed after the deletion, so ignore ids you do not know. 

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
        WebhookPayloadReviewRestored webhookPayloadReviewRestored = new WebhookPayloadReviewRestored(); // WebhookPayloadReviewRestored | 
        try {
            apiInstance.onReviewRestored(webhookPayloadReviewRestored);
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onReviewRestored");
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
| **webhookPayloadReviewRestored** | [**WebhookPayloadReviewRestored**](WebhookPayloadReviewRestored.md)|  | |

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

## onReviewRestoredWithHttpInfo

> ApiResponse<Void> onReviewRestored onReviewRestoredWithHttpInfo(webhookPayloadReviewRestored)

Review restored event

Google returned a review previously reported by &#x60;review.deleted&#x60;; the payload has the same shape as &#x60;review.new&#x60;.  ### When it fires  It may reach a webhook that subscribed after the deletion, so ignore ids you do not know. 

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
        WebhookPayloadReviewRestored webhookPayloadReviewRestored = new WebhookPayloadReviewRestored(); // WebhookPayloadReviewRestored | 
        try {
            ApiResponse<Void> response = apiInstance.onReviewRestoredWithHttpInfo(webhookPayloadReviewRestored);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling WebhookEventsApi#onReviewRestored");
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
| **webhookPayloadReviewRestored** | [**WebhookPayloadReviewRestored**](WebhookPayloadReviewRestored.md)|  | |

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

A Google Business Profile review changed: the reviewer edited it, or its reply was added, edited or removed.  ### Reply through the API  A reply sent through the Zernio API fires the event immediately. The periodic check then reports it again with the full review payload, so expect a second delivery.  ### Replies written in Google  Google sends no notification for replies written in its interface. The periodic check detects them, usually within 6 hours for reviews updated in the last 30 days, about 7 days for older.  ### Checks  Only teams with a webhook subscribed to &#x60;review.updated&#x60; are checked. A removed reply, through the API or in Google, fires from the periodic check with &#x60;review.hasReply&#x60; set to &#x60;false&#x60;.  ### Payload notes  Same shape as &#x60;review.new&#x60;. When a reply is present, &#x60;review.hasReply&#x60; is &#x60;true&#x60; and &#x60;review.reply&#x60; is populated. 

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

A Google Business Profile review changed: the reviewer edited it, or its reply was added, edited or removed.  ### Reply through the API  A reply sent through the Zernio API fires the event immediately. The periodic check then reports it again with the full review payload, so expect a second delivery.  ### Replies written in Google  Google sends no notification for replies written in its interface. The periodic check detects them, usually within 6 hours for reviews updated in the last 30 days, about 7 days for older.  ### Checks  Only teams with a webhook subscribed to &#x60;review.updated&#x60; are checked. A removed reply, through the API or in Google, fires from the periodic check with &#x60;review.hasReply&#x60; set to &#x60;false&#x60;.  ### Payload notes  Same shape as &#x60;review.new&#x60;. When a reply is present, &#x60;review.hasReply&#x60; is &#x60;true&#x60; and &#x60;review.reply&#x60; is populated. 

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

A contact was enrolled in a sequence, through the API or a workflow &#x60;enroll_sequence&#x60; node. 

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

A contact was enrolled in a sequence, through the API or a workflow &#x60;enroll_sequence&#x60; node. 

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

A contact left a sequence; &#x60;exitReason&#x60; says why.  ### Exit reasons  - &#x60;completed&#x60;: the last step was sent. - &#x60;replied&#x60; - &#x60;manual&#x60;: unenrolled through the API. - &#x60;failed&#x60;: the step kept failing to send. - &#x60;unsubscribed&#x60; 

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

A contact left a sequence; &#x60;exitReason&#x60; says why.  ### Exit reasons  - &#x60;completed&#x60;: the last step was sent. - &#x60;replied&#x60; - &#x60;manual&#x60;: unenrolled through the API. - &#x60;failed&#x60;: the step kept failing to send. - &#x60;unsubscribed&#x60; 

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

An SMS registration is waiting on its owner; &#x60;reason&#x60; says why.  ### Reasons  - &#x60;changes_requested&#x60;: answer &#x60;message&#x60; via &#x60;POST /v1/sms/registrations/{id}/respond&#x60;. - &#x60;otp_required&#x60;: submit the texted code via &#x60;POST /v1/sms/registrations/{id}/verify-otp&#x60;; no &#x60;message&#x60;. - &#x60;carrier_info_required&#x60;: expires after 7 days.  ### When it fires  Fires once per new request and once per OTP or carrier request, not on follow-up messages. A carrier rejection alone does not fire it. 

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

An SMS registration is waiting on its owner; &#x60;reason&#x60; says why.  ### Reasons  - &#x60;changes_requested&#x60;: answer &#x60;message&#x60; via &#x60;POST /v1/sms/registrations/{id}/respond&#x60;. - &#x60;otp_required&#x60;: submit the texted code via &#x60;POST /v1/sms/registrations/{id}/verify-otp&#x60;; no &#x60;message&#x60;. - &#x60;carrier_info_required&#x60;: expires after 7 days.  ### When it fires  Fires once per new request and once per OTP or carrier request, not on follow-up messages. A carrier rejection alone does not fire it. 

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

An SMS registration changed status; &#x60;status&#x60; is the new one.  ### Statuses  - &#x60;changes_requested&#x60;: answers needed. - &#x60;requested&#x60;: submitted, resubmitted, or your answers are back in review. - &#x60;pending&#x60;: with the carriers. - &#x60;approved&#x60;: live, attach numbers. - &#x60;rejected&#x60;: &#x60;reason&#x60; is the carriers&#39; words. - &#x60;deactivated&#x60;  ### Rejections  A carrier rejection needs nothing from you. Zernio handles the fix and resends it, so the status returns to &#x60;pending&#x60;. 

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

An SMS registration changed status; &#x60;status&#x60; is the new one.  ### Statuses  - &#x60;changes_requested&#x60;: answers needed. - &#x60;requested&#x60;: submitted, resubmitted, or your answers are back in review. - &#x60;pending&#x60;: with the carriers. - &#x60;approved&#x60;: live, attach numbers. - &#x60;rejected&#x60;: &#x60;reason&#x60; is the carriers&#39; words. - &#x60;deactivated&#x60;  ### Rejections  A carrier rejection needs nothing from you. Zernio handles the fix and resends it, so the status returns to &#x60;pending&#x60;. 

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

A support run finished with an answer, or handed the question to a person.  ### Payload notes  &#x60;run.status&#x60; is &#x60;completed&#x60;, or &#x60;needs_human&#x60; when Ana handed the question to a person. &#x60;run.answer&#x60; holds the answer; &#x60;run.stopReason&#x60; says why it stopped (&#x60;answered&#x60; or &#x60;human_review&#x60;, among others). 

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

A support run finished with an answer, or handed the question to a person.  ### Payload notes  &#x60;run.status&#x60; is &#x60;completed&#x60;, or &#x60;needs_human&#x60; when Ana handed the question to a person. &#x60;run.answer&#x60; holds the answer; &#x60;run.stopReason&#x60; says why it stopped (&#x60;answered&#x60; or &#x60;human_review&#x60;, among others). 

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

A support run failed or expired, and is not billed.  ### Payload notes  &#x60;run.status&#x60; is &#x60;failed&#x60; and &#x60;run.answer&#x60; is &#x60;null&#x60;. &#x60;run.stopReason&#x60; is &#x60;expired&#x60; when the run never finished. &#x60;run.costUsd&#x60; is 0. 

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

A support run failed or expired, and is not billed.  ### Payload notes  &#x60;run.status&#x60; is &#x60;failed&#x60; and &#x60;run.answer&#x60; is &#x60;null&#x60;. &#x60;run.stopReason&#x60; is &#x60;expired&#x60; when the run never finished. &#x60;run.costUsd&#x60; is 0. 

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

The recipient submitted the right verification code.  ### Payload notes  Carries &#x60;verification.verificationId&#x60;, &#x60;verification.channel&#x60; (&#x60;sms&#x60;) and &#x60;verification.to&#x60;. 

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

The recipient submitted the right verification code.  ### Payload notes  Carries &#x60;verification.verificationId&#x60;, &#x60;verification.channel&#x60; (&#x60;sms&#x60;) and &#x60;verification.to&#x60;. 

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

A verification ran out of attempts without a correct code.  ### Payload notes  &#x60;reason&#x60; is &#x60;max_attempts_reached&#x60;. Carries the same &#x60;verification&#x60; fields as &#x60;verification.approved&#x60;. 

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

A verification ran out of attempts without a correct code.  ### Payload notes  &#x60;reason&#x60; is &#x60;max_attempts_reached&#x60;. Carries the same &#x60;verification&#x60; fields as &#x60;verification.approved&#x60;. 

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

Zernio sent a test event to an endpoint.  ### When it fires  Sent when you call Test webhook or press test in the dashboard, whatever events the endpoint subscribes to. Sent once, synchronously, and never retried. 

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

Zernio sent a test event to an endpoint.  ### When it fires  Sent when you call Test webhook or press test in the dashboard, whatever events the endpoint subscribes to. Sent once, synchronously, and never retried. 

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

Meta sent an account alert for a connected WhatsApp Business Account.  ### Payload notes  Forwards Meta&#39;s &#x60;account_alerts&#x60; as is. &#x60;alert.severity&#x60; is &#x60;CRITICAL&#x60;, &#x60;WARNING&#x60; or &#x60;INFORMATIONAL&#x60;; &#x60;alert.type&#x60; is Meta&#39;s alert type; &#x60;alert.description&#x60; is the text.  ### Who receives it  An alert about one number goes to that number&#39;s account. A business-level alert goes to every connected number on the WABA. 

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

Meta sent an account alert for a connected WhatsApp Business Account.  ### Payload notes  Forwards Meta&#39;s &#x60;account_alerts&#x60; as is. &#x60;alert.severity&#x60; is &#x60;CRITICAL&#x60;, &#x60;WARNING&#x60; or &#x60;INFORMATIONAL&#x60;; &#x60;alert.type&#x60; is Meta&#39;s alert type; &#x60;alert.description&#x60; is the text.  ### Who receives it  An alert about one number goes to that number&#39;s account. A business-level alert goes to every connected number on the WABA. 

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

Meta finished reviewing a WhatsApp display-name change on a connected number.  ### When it fires  Fires only on a review outcome, forwarded from Meta&#39;s &#x60;phone_number_name_update&#x60; field. A name applied without review (&#x60;AVAILABLE_WITHOUT_REVIEW&#x60;) produces no event.  ### Payload notes  Branch on &#x60;name.status&#x60; (&#x60;APPROVED&#x60;, &#x60;DECLINED&#x60;, &#x60;PENDING_REVIEW&#x60;). Meta&#39;s &#x60;REJECTED&#x60; maps to &#x60;DECLINED&#x60; and &#x60;DEFERRED&#x60; to &#x60;PENDING_REVIEW&#x60;, because the review is still open. &#x60;name.requestedName&#x60; and &#x60;name.rejectionReason&#x60; are Meta&#39;s values or null.  ### Delivery  Delivery is at-least-once; dedupe on &#x60;(account.accountId, name.status, name.requestedName)&#x60;. 

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

Meta finished reviewing a WhatsApp display-name change on a connected number.  ### When it fires  Fires only on a review outcome, forwarded from Meta&#39;s &#x60;phone_number_name_update&#x60; field. A name applied without review (&#x60;AVAILABLE_WITHOUT_REVIEW&#x60;) produces no event.  ### Payload notes  Branch on &#x60;name.status&#x60; (&#x60;APPROVED&#x60;, &#x60;DECLINED&#x60;, &#x60;PENDING_REVIEW&#x60;). Meta&#39;s &#x60;REJECTED&#x60; maps to &#x60;DECLINED&#x60; and &#x60;DEFERRED&#x60; to &#x60;PENDING_REVIEW&#x60;, because the review is still open. &#x60;name.requestedName&#x60; and &#x60;name.rejectionReason&#x60; are Meta&#39;s values or null.  ### Delivery  Delivery is at-least-once; dedupe on &#x60;(account.accountId, name.status, name.requestedName)&#x60;. 

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

A connected number&#39;s quality rating or messaging limit tier changed.  ### When it fires  Fires only when the rating or tier differs from the value Zernio held. A tier change Meta applies to the whole business portfolio fires once per connected number.  ### Payload notes  &#x60;quality.source&#x60; says which Meta signal reported it. Compare &#x60;quality.previousQualityRating&#x60; with &#x60;quality.qualityRating&#x60;, and the previous and current messaging limit tier. &#x60;quality.qualityRating&#x60; is Meta&#39;s live value (&#x60;GREEN&#x60;, &#x60;YELLOW&#x60;, &#x60;RED&#x60;).  ### Delivery  Delivery is at-least-once; dedupe on the event &#x60;id&#x60;. 

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

A connected number&#39;s quality rating or messaging limit tier changed.  ### When it fires  Fires only when the rating or tier differs from the value Zernio held. A tier change Meta applies to the whole business portfolio fires once per connected number.  ### Payload notes  &#x60;quality.source&#x60; says which Meta signal reported it. Compare &#x60;quality.previousQualityRating&#x60; with &#x60;quality.qualityRating&#x60;, and the previous and current messaging limit tier. &#x60;quality.qualityRating&#x60; is Meta&#39;s live value (&#x60;GREEN&#x60;, &#x60;YELLOW&#x60;, &#x60;RED&#x60;).  ### Delivery  Delivery is at-least-once; dedupe on the event &#x60;id&#x60;. 

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

Meta restricted, disabled, deleted or reinstated a connected WhatsApp Business Account, or flagged a violation on it.  ### When it fires  Mirrors Meta&#39;s &#x60;account_update&#x60; events. They apply to the whole WhatsApp Business Account, so every connected number on it receives one event.  ### Payload notes  Branch on &#x60;status.status&#x60; (&#x60;restricted&#x60; or &#x60;active&#x60;) and &#x60;status.metaEvent&#x60;. &#x60;status.restrictions&#x60; lists what Meta restricted (for example &#x60;RESTRICTED_BIZ_INITIATED_MESSAGING&#x60;) and when each lifts. The same status is on the account as &#x60;platformStatus&#x60;. 

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

Meta restricted, disabled, deleted or reinstated a connected WhatsApp Business Account, or flagged a violation on it.  ### When it fires  Mirrors Meta&#39;s &#x60;account_update&#x60; events. They apply to the whole WhatsApp Business Account, so every connected number on it receives one event.  ### Payload notes  Branch on &#x60;status.status&#x60; (&#x60;restricted&#x60; or &#x60;active&#x60;) and &#x60;status.metaEvent&#x60;. &#x60;status.restrictions&#x60; lists what Meta restricted (for example &#x60;RESTRICTED_BIZ_INITIATED_MESSAGING&#x60;) and when each lifts. The same status is on the account as &#x60;platformStatus&#x60;. 

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

Meta&#39;s automatic event identification detected a lead or purchase in a Click-to-WhatsApp conversation.  ### Payload notes  Branch on &#x60;eventName&#x60; (&#x60;LeadSubmitted&#x60; or &#x60;Purchase&#x60;). &#x60;Purchase&#x60; may carry the detected amount in &#x60;customData&#x60; (&#x60;currency&#x60;, &#x60;value&#x60;). It carries the &#x60;ctwaClid&#x60;.  ### Conversions API match key  Meta omits the clid on a minority of referrals, most often WhatsApp Status placements; this event can supply it. Zernio writes it onto the conversation, so &#x60;POST /v1/whatsapp/conversions&#x60; becomes usable for it.  ### Availability  Detection is not available for EU, UK and JP businesses. Elsewhere the owner opts in during Embedded Signup. An endpoint subscribed on a number whose owner did not opt in receives nothing. 

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

Meta&#39;s automatic event identification detected a lead or purchase in a Click-to-WhatsApp conversation.  ### Payload notes  Branch on &#x60;eventName&#x60; (&#x60;LeadSubmitted&#x60; or &#x60;Purchase&#x60;). &#x60;Purchase&#x60; may carry the detected amount in &#x60;customData&#x60; (&#x60;currency&#x60;, &#x60;value&#x60;). It carries the &#x60;ctwaClid&#x60;.  ### Conversions API match key  Meta omits the clid on a minority of referrals, most often WhatsApp Status placements; this event can supply it. Zernio writes it onto the conversation, so &#x60;POST /v1/whatsapp/conversions&#x60; becomes usable for it.  ### Availability  Detection is not available for EU, UK and JP businesses. Elsewhere the owner opts in during Embedded Signup. An endpoint subscribed on a number whose owner did not opt in receives nothing. 

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

A WhatsApp user changed phone number or Meta regenerated their business-scoped user id (BSUID).  ### When it fires  Fires when Meta reports the user under a new phone number (&#x60;reason: \&quot;user_changed_number\&quot;&#x60;) or a new BSUID (&#x60;user_changed_user_id&#x60;, &#x60;user_identity_changed&#x60; or &#x60;user_id_update&#x60;).  ### Payload notes  &#x60;previous&#x60; and &#x60;current&#x60; carry the phone number, BSUID, parent BSUID and username. Use them to re-key records stored against the old value.  ### Already applied  Zernio has already moved the inbox conversation and the contact when the event arrives. &#x60;conversationId&#x60; and &#x60;contactId&#x60; point at them, or are null when there was none.  ### Delivery  Delivery is at-least-once; dedupe on the event &#x60;id&#x60;. 

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

A WhatsApp user changed phone number or Meta regenerated their business-scoped user id (BSUID).  ### When it fires  Fires when Meta reports the user under a new phone number (&#x60;reason: \&quot;user_changed_number\&quot;&#x60;) or a new BSUID (&#x60;user_changed_user_id&#x60;, &#x60;user_identity_changed&#x60; or &#x60;user_id_update&#x60;).  ### Payload notes  &#x60;previous&#x60; and &#x60;current&#x60; carry the phone number, BSUID, parent BSUID and username. Use them to re-key records stored against the old value.  ### Already applied  Zernio has already moved the inbox conversation and the contact when the event arrives. &#x60;conversationId&#x60; and &#x60;contactId&#x60; point at them, or are null when there was none.  ### Delivery  Delivery is at-least-once; dedupe on the event &#x60;id&#x60;. 

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

The regulator asked for more information on a placed number order; nothing was rejected.  ### When it fires  The order stays pending, and the number stays &#x60;pending_regulatory&#x60;, until you provide the information. The status does not change.  ### Payload notes  &#x60;reason&#x60; carries the regulator&#39;s request verbatim when available. &#x60;requirements&#x60; lists every requirement with the reviewer&#39;s current verdict; the &#x60;declined&#x60; ones are what to fix, keyed by &#x60;requirementId&#x60;. Verdicts describe the review at &#x60;reviewedAt&#x60;.  ### How to resolve  Provide the missing details from the dashboard&#39;s phone-numbers page, or re-submit the fields through the remediation endpoint. The review resumes automatically. 

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

The regulator asked for more information on a placed number order; nothing was rejected.  ### When it fires  The order stays pending, and the number stays &#x60;pending_regulatory&#x60;, until you provide the information. The status does not change.  ### Payload notes  &#x60;reason&#x60; carries the regulator&#39;s request verbatim when available. &#x60;requirements&#x60; lists every requirement with the reviewer&#39;s current verdict; the &#x60;declined&#x60; ones are what to fix, keyed by &#x60;requirementId&#x60;. Verdicts describe the review at &#x60;reviewedAt&#x60;.  ### How to resolve  Provide the missing details from the dashboard&#39;s phone-numbers page, or re-submit the fields through the remediation endpoint. The review resumes automatically. 

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

A number you provisioned through Zernio finished setup and is ready to connect.  ### When it fires  Regulated (non-US) numbers can take 1 to 3 business days after the order is approved. In instant-provisioning countries this is the first event, with no review states before it. 

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

A number you provisioned through Zernio finished setup and is ready to connect.  ### When it fires  Regulated (non-US) numbers can take 1 to 3 business days after the order is approved. In instant-provisioning countries this is the first event, with no review states before it. 

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

A regulated number order was declined in regulatory review and no number was activated.  ### Payload notes  &#x60;reason&#x60; carries the reviewer&#39;s rejection reason when available. You are never billed for a declined number.  ### Remediation  Resubmit corrected details and the number returns to &#x60;pending_regulatory&#x60;. It is the same number, with no new billing. 

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

A regulated number order was declined in regulatory review and no number was activated.  ### Payload notes  &#x60;reason&#x60; carries the reviewer&#39;s rejection reason when available. You are never billed for a declined number.  ### Remediation  Resubmit corrected details and the number returns to &#x60;pending_regulatory&#x60;. It is the same number, with no new billing. 

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

An end customer completed a hosted KYC share link and the number entered regulatory review.  ### When it fires  Fires only for hosted share links (&#x60;POST /v1/phone-numbers/kyc/share&#x60;). When you submit KYC over the API, no event fires.  ### What follows  The number is &#x60;pending_regulatory&#x60; under your account. &#x60;whatsapp.number.activated&#x60; or &#x60;whatsapp.number.declined&#x60; follows once the provider rules on it. Update your own UI from this event instead of polling. 

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

An end customer completed a hosted KYC share link and the number entered regulatory review.  ### When it fires  Fires only for hosted share links (&#x60;POST /v1/phone-numbers/kyc/share&#x60;). When you submit KYC over the API, no event fires.  ### What follows  The number is &#x60;pending_regulatory&#x60; under your account. &#x60;whatsapp.number.activated&#x60; or &#x60;whatsapp.number.declined&#x60; follows once the provider rules on it. Update your own UI from this event instead of polling. 

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

A suspended number was reactivated, for example after the payment recovered, and is usable again. 

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

A suspended number was reactivated, for example after the payment recovered, and is usable again. 

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

A number was released and is no longer usable.  ### Payload notes  Released by you, a billing cleanup or an admin. &#x60;reason&#x60; is a value such as &#x60;user_requested&#x60; or &#x60;cleanup_suspended&#x60;. This is the only terminal status. 

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

A number was released and is no longer usable.  ### Payload notes  Released by you, a billing cleanup or an admin. &#x60;reason&#x60; is a value such as &#x60;user_requested&#x60; or &#x60;cleanup_suspended&#x60;. This is the only terminal status. 

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

An active number was suspended, for example after a failed payment.  ### Payload notes  &#x60;reason&#x60; is a value such as &#x60;payment_failed&#x60; or &#x60;subscription_ended&#x60;. The number stops working until the issue is resolved, then &#x60;whatsapp.number.reactivated&#x60; follows.  ### When it does not recover  A suspension left unresolved ends in release. 

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

An active number was suspended, for example after a failed payment.  ### Payload notes  &#x60;reason&#x60; is a value such as &#x60;payment_failed&#x60; or &#x60;subscription_ended&#x60;. The number stops working until the issue is resolved, then &#x60;whatsapp.number.reactivated&#x60; follows.  ### When it does not recover  A suspension left unresolved ends in release. 

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

A regulated number requires the end user to complete an identity check.  ### Payload notes  &#x60;verificationUrl&#x60; is a one-time link to forward to the person whose ID is on file, for example for Australian mobile numbers. The order completes once they pass. The number stays &#x60;pending_regulatory&#x60;. 

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

A regulated number requires the end user to complete an identity check.  ### Payload notes  &#x60;verificationUrl&#x60; is a one-time link to forward to the person whose ID is on file, for example for Australian mobile numbers. The order completes once they pass. The number stays &#x60;pending_regulatory&#x60;. 

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

Meta reclassified a WhatsApp template&#39;s category, first as a 24-hour advance notice and again when applied.  ### When it fires  Sent with &#x60;template.changeType: \&quot;scheduled\&quot;&#x60; for Meta&#39;s 24-hour advance notice, and again with &#x60;\&quot;applied\&quot;&#x60; when the change takes effect.  ### Payload notes  &#x60;template.category&#x60; is always the category right now. Meta clears a custom delivery window when it recategorises a template, so read &#x60;message_send_ttl_seconds&#x60; back after an &#x60;applied&#x60; change.  ### Platform notes  Forwarded from Meta&#39;s &#x60;template_category_update&#x60; field. The category decides Meta&#39;s per-delivery rate and the delivery window the template can carry. 

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

Meta reclassified a WhatsApp template&#39;s category, first as a 24-hour advance notice and again when applied.  ### When it fires  Sent with &#x60;template.changeType: \&quot;scheduled\&quot;&#x60; for Meta&#39;s 24-hour advance notice, and again with &#x60;\&quot;applied\&quot;&#x60; when the change takes effect.  ### Payload notes  &#x60;template.category&#x60; is always the category right now. Meta clears a custom delivery window when it recategorises a template, so read &#x60;message_send_ttl_seconds&#x60; back after an &#x60;applied&#x60; change.  ### Platform notes  Forwarded from Meta&#39;s &#x60;template_category_update&#x60; field. The category decides Meta&#39;s per-delivery rate and the delivery window the template can carry. 

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

Meta finished reviewing or re-reviewing a WhatsApp Business template on a connected WABA.  ### Payload notes  Branch on &#x60;template.status&#x60; (&#x60;APPROVED&#x60;, &#x60;REJECTED&#x60;, &#x60;PENDING&#x60;, &#x60;PAUSED&#x60;, &#x60;DISABLED&#x60;, &#x60;IN_APPEAL&#x60;, &#x60;PENDING_DELETION&#x60;). &#x60;template.reason&#x60; is Meta&#39;s free-form reason or &#x60;\&quot;NONE\&quot;&#x60;.  ### Platform notes  Forwarded from Meta&#39;s &#x60;message_template_status_update&#x60; field. Meta includes neither the previous status nor the template&#39;s category. 

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

Meta finished reviewing or re-reviewing a WhatsApp Business template on a connected WABA.  ### Payload notes  Branch on &#x60;template.status&#x60; (&#x60;APPROVED&#x60;, &#x60;REJECTED&#x60;, &#x60;PENDING&#x60;, &#x60;PAUSED&#x60;, &#x60;DISABLED&#x60;, &#x60;IN_APPEAL&#x60;, &#x60;PENDING_DELETION&#x60;). &#x60;template.reason&#x60; is Meta&#39;s free-form reason or &#x60;\&quot;NONE\&quot;&#x60;.  ### Platform notes  Forwarded from Meta&#39;s &#x60;message_template_status_update&#x60; field. Meta includes neither the previous status nor the template&#39;s category. 

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

A workflow run ended, with &#x60;execution.status&#x60; &#x60;completed&#x60;, or &#x60;exited&#x60; when it ended on purpose before its last node.  ### Exits  An exit is a handoff, or a button that switched the contact to another workflow. 

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

A workflow run ended, with &#x60;execution.status&#x60; &#x60;completed&#x60;, or &#x60;exited&#x60; when it ended on purpose before its last node.  ### Exits  An exit is a handoff, or a button that switched the contact to another workflow. 

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

A workflow run failed; &#x60;error&#x60; names the node that failed and why. 

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

A workflow run failed; &#x60;error&#x60; names the node that failed and why. 

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

A workflow run started for a conversation; &#x60;trigger.type&#x60; is the trigger node&#39;s type.  ### Payload notes  &#x60;trigger.text&#x60; is the inbound message that started the run, when there was one. 

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

A workflow run started for a conversation; &#x60;trigger.type&#x60; is the trigger node&#39;s type.  ### Payload notes  &#x60;trigger.text&#x60; is the inbound message that started the run, when there was one. 

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

