

# StagedAdChangeRequest

Only with type `operation`: the write that was staged as its request. Confirm sends this request through its own route.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**operation** | [**OperationEnum**](#OperationEnum) | The operationId of the staged write. Every write in this list accepts &#x60;stage: true&#x60; in its body, or &#x60;?stage&#x3D;true&#x60; when it has no body. |  |
|**method** | [**MethodEnum**](#MethodEnum) |  |  |
|**path** | **String** | The path of the write, for example /v1/ads/keywords. |  |
|**params** | **Map&lt;String, String&gt;** | The path values of the staged request, by the names in &#x60;path&#x60;. |  [optional] |
|**query** | **Map&lt;String, String&gt;** | The query values of the staged request, without &#x60;stage&#x60;. |  [optional] |



## Enum: OperationEnum

| Name | Value |
|---- | -----|
| ADD_ACCOUNT_CALLOUTS | &quot;addAccountCallouts&quot; |
| ADD_ACCOUNT_SITELINKS | &quot;addAccountSitelinks&quot; |
| ADD_ACCOUNT_STRUCTURED_SNIPPETS | &quot;addAccountStructuredSnippets&quot; |
| ADD_AD_KEYWORDS | &quot;addAdKeywords&quot; |
| APPLY_GOOGLE_RECOMMENDATIONS | &quot;applyGoogleRecommendations&quot; |
| ARCHIVE_LEAD_FORM | &quot;archiveLeadForm&quot; |
| ASSIGN_AD_ACCOUNT_USER | &quot;assignAdAccountUser&quot; |
| ASSIGN_PAGE_USER | &quot;assignPageUser&quot; |
| ATTACH_AD_GROUP_ASSETS | &quot;attachAdGroupAssets&quot; |
| ATTACH_AD_LABEL | &quot;attachAdLabel&quot; |
| ATTACH_CAMPAIGN_ASSETS | &quot;attachCampaignAssets&quot; |
| BOOST_POST | &quot;boostPost&quot; |
| BULK_UPDATE_AD_CAMPAIGN_STATUS | &quot;bulkUpdateAdCampaignStatus&quot; |
| CREATE_AD_AUDIENCE | &quot;createAdAudience&quot; |
| CREATE_AD_CREATIVE | &quot;createAdCreative&quot; |
| CREATE_AD_LABEL | &quot;createAdLabel&quot; |
| CREATE_AD_NEGATIVE_KEYWORD_LIST | &quot;createAdNegativeKeywordList&quot; |
| CREATE_BID_STRATEGY | &quot;createBidStrategy&quot; |
| CREATE_CALL_AD | &quot;createCallAd&quot; |
| CREATE_CONVERSION_ACTION | &quot;createConversionAction&quot; |
| CREATE_CTWA_AD | &quot;createCtwaAd&quot; |
| CREATE_CUSTOM_CONVERSION_GOAL | &quot;createCustomConversionGoal&quot; |
| CREATE_GOOGLE_ASSET_GROUP | &quot;createGoogleAssetGroup&quot; |
| CREATE_HIGH_DEMAND_PERIOD | &quot;createHighDemandPeriod&quot; |
| CREATE_LEAD_FORM | &quot;createLeadForm&quot; |
| CREATE_MESSAGING_AD | &quot;createMessagingAd&quot; |
| CREATE_SHARED_BUDGET | &quot;createSharedBudget&quot; |
| CREATE_VALUE_RULE_SET | &quot;createValueRuleSet&quot; |
| DELETE_AD | &quot;deleteAd&quot; |
| DELETE_AD_AUDIENCE | &quot;deleteAdAudience&quot; |
| DELETE_AD_CAMPAIGN | &quot;deleteAdCampaign&quot; |
| DELETE_AD_CREATIVE | &quot;deleteAdCreative&quot; |
| DELETE_AD_NEGATIVE_KEYWORD_LIST | &quot;deleteAdNegativeKeywordList&quot; |
| DELETE_AD_SET | &quot;deleteAdSet&quot; |
| DELETE_AD_VIDEO | &quot;deleteAdVideo&quot; |
| DELETE_VALUE_RULE_SET | &quot;deleteValueRuleSet&quot; |
| DETACH_AD_LABEL | &quot;detachAdLabel&quot; |
| DISMISS_GOOGLE_RECOMMENDATIONS | &quot;dismissGoogleRecommendations&quot; |
| DUPLICATE_AD | &quot;duplicateAd&quot; |
| DUPLICATE_AD_CAMPAIGN | &quot;duplicateAdCampaign&quot; |
| DUPLICATE_AD_SET | &quot;duplicateAdSet&quot; |
| EDIT_AD_NEGATIVE_KEYWORD_LIST_KEYWORDS | &quot;editAdNegativeKeywordListKeywords&quot; |
| EDIT_CAMPAIGN_NEGATIVE_KEYWORD_LISTS | &quot;editCampaignNegativeKeywordLists&quot; |
| EDIT_CAMPAIGN_NEGATIVE_KEYWORDS | &quot;editCampaignNegativeKeywords&quot; |
| EDIT_GOOGLE_ASSET_GROUP_ASSETS | &quot;editGoogleAssetGroupAssets&quot; |
| INVITE_AD_ACCOUNT_TO_MANAGER | &quot;inviteAdAccountToManager&quot; |
| INVITE_AD_ACCOUNT_USER | &quot;inviteAdAccountUser&quot; |
| REMOVE_ACCOUNT_CALLOUT | &quot;removeAccountCallout&quot; |
| REMOVE_ACCOUNT_SITELINK | &quot;removeAccountSitelink&quot; |
| REMOVE_ACCOUNT_STRUCTURED_SNIPPET | &quot;removeAccountStructuredSnippet&quot; |
| REMOVE_AD_ACCOUNT_USER | &quot;removeAdAccountUser&quot; |
| REMOVE_AD_GROUP_ASSETS | &quot;removeAdGroupAssets&quot; |
| REMOVE_AD_KEYWORD | &quot;removeAdKeyword&quot; |
| REMOVE_AD_LABEL | &quot;removeAdLabel&quot; |
| REMOVE_CAMPAIGN_ASSETS | &quot;removeCampaignAssets&quot; |
| REMOVE_CUSTOM_CONVERSION_GOAL | &quot;removeCustomConversionGoal&quot; |
| REMOVE_GOOGLE_ASSET_GROUP | &quot;removeGoogleAssetGroup&quot; |
| REMOVE_PAGE_USER | &quot;removePageUser&quot; |
| REPLACE_AD_AUDIENCE_COMPANIES | &quot;replaceAdAudienceCompanies&quot; |
| REPLACE_AD_NEGATIVE_KEYWORD_LIST_KEYWORDS | &quot;replaceAdNegativeKeywordListKeywords&quot; |
| REPLACE_CAMPAIGN_NEGATIVE_KEYWORD_LISTS | &quot;replaceCampaignNegativeKeywordLists&quot; |
| REPLACE_CAMPAIGN_NEGATIVE_KEYWORDS | &quot;replaceCampaignNegativeKeywords&quot; |
| REPLACE_GOOGLE_LISTING_GROUP_FILTERS | &quot;replaceGoogleListingGroupFilters&quot; |
| REVOKE_AD_ACCOUNT_USER_INVITATION | &quot;revokeAdAccountUserInvitation&quot; |
| SET_PARTNERSHIP_AD_PERMISSION | &quot;setPartnershipAdPermission&quot; |
| SET_UP_AD_ACCOUNT_BILLING | &quot;setUpAdAccountBilling&quot; |
| UPDATE_ACCOUNT_CALLOUTS | &quot;updateAccountCallouts&quot; |
| UPDATE_ACCOUNT_SITELINKS | &quot;updateAccountSitelinks&quot; |
| UPDATE_ACCOUNT_STRUCTURED_SNIPPETS | &quot;updateAccountStructuredSnippets&quot; |
| UPDATE_AD_ACCOUNT | &quot;updateAdAccount&quot; |
| UPDATE_AD_ACCOUNT_MANAGER_LINK | &quot;updateAdAccountManagerLink&quot; |
| UPDATE_AD_AUDIENCE | &quot;updateAdAudience&quot; |
| UPDATE_AD_CONVERSION_GOALS | &quot;updateAdConversionGoals&quot; |
| UPDATE_AD_CREATIVE | &quot;updateAdCreative&quot; |
| UPDATE_AD_GROUP_ASSETS | &quot;updateAdGroupAssets&quot; |
| UPDATE_AD_KEYWORD | &quot;updateAdKeyword&quot; |
| UPDATE_AD_LABEL | &quot;updateAdLabel&quot; |
| UPDATE_AD_NEGATIVE_KEYWORD_LIST | &quot;updateAdNegativeKeywordList&quot; |
| UPDATE_AD_TRACKING_TAGS | &quot;updateAdTrackingTags&quot; |
| UPDATE_BID_STRATEGY | &quot;updateBidStrategy&quot; |
| UPDATE_CAMPAIGN_AD_SCHEDULE | &quot;updateCampaignAdSchedule&quot; |
| UPDATE_CAMPAIGN_ASSETS | &quot;updateCampaignAssets&quot; |
| UPDATE_CAMPAIGN_CONVERSION_GOALS | &quot;updateCampaignConversionGoals&quot; |
| UPDATE_CONVERSION_ACTION | &quot;updateConversionAction&quot; |
| UPDATE_CUSTOM_CONVERSION_GOAL | &quot;updateCustomConversionGoal&quot; |
| UPDATE_GOOGLE_ASSET_GROUP | &quot;updateGoogleAssetGroup&quot; |
| UPDATE_VALUE_RULE_SET | &quot;updateValueRuleSet&quot; |
| WITHDRAW_AD_ACCOUNT_USER_INVITATION_APPROVAL | &quot;withdrawAdAccountUserInvitationApproval&quot; |



## Enum: MethodEnum

| Name | Value |
|---- | -----|
| POST | &quot;POST&quot; |
| PUT | &quot;PUT&quot; |
| PATCH | &quot;PATCH&quot; |
| DELETE | &quot;DELETE&quot; |



