# AdCampaignsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addAdKeywords**](AdCampaignsApi.md#addAdKeywords) | **POST** /v1/ads/keywords | Add Search ad-group keywords |
| [**addAdKeywordsWithHttpInfo**](AdCampaignsApi.md#addAdKeywordsWithHttpInfo) | **POST** /v1/ads/keywords | Add Search ad-group keywords |
| [**applyGoogleRecommendations**](AdCampaignsApi.md#applyGoogleRecommendations) | **POST** /v1/ads/recommendations/apply | Apply Google Ads recommendations |
| [**applyGoogleRecommendationsWithHttpInfo**](AdCampaignsApi.md#applyGoogleRecommendationsWithHttpInfo) | **POST** /v1/ads/recommendations/apply | Apply Google Ads recommendations |
| [**attachAdGroupAssets**](AdCampaignsApi.md#attachAdGroupAssets) | **POST** /v1/ads/ad-sets/{adSetId}/assets | Attach ad-group assets |
| [**attachAdGroupAssetsWithHttpInfo**](AdCampaignsApi.md#attachAdGroupAssetsWithHttpInfo) | **POST** /v1/ads/ad-sets/{adSetId}/assets | Attach ad-group assets |
| [**attachCampaignAssets**](AdCampaignsApi.md#attachCampaignAssets) | **POST** /v1/ads/campaigns/{campaignId}/assets | Attach campaign assets |
| [**attachCampaignAssetsWithHttpInfo**](AdCampaignsApi.md#attachCampaignAssetsWithHttpInfo) | **POST** /v1/ads/campaigns/{campaignId}/assets | Attach campaign assets |
| [**boostPost**](AdCampaignsApi.md#boostPost) | **POST** /v1/ads/boost | Boost post as ad |
| [**boostPostWithHttpInfo**](AdCampaignsApi.md#boostPostWithHttpInfo) | **POST** /v1/ads/boost | Boost post as ad |
| [**bulkUpdateAdCampaignStatus**](AdCampaignsApi.md#bulkUpdateAdCampaignStatus) | **POST** /v1/ads/campaigns/bulk-status | Pause or resume many campaigns |
| [**bulkUpdateAdCampaignStatusWithHttpInfo**](AdCampaignsApi.md#bulkUpdateAdCampaignStatusWithHttpInfo) | **POST** /v1/ads/campaigns/bulk-status | Pause or resume many campaigns |
| [**createAdCampaign**](AdCampaignsApi.md#createAdCampaign) | **POST** /v1/ads/campaigns | Create a standalone campaign |
| [**createAdCampaignWithHttpInfo**](AdCampaignsApi.md#createAdCampaignWithHttpInfo) | **POST** /v1/ads/campaigns | Create a standalone campaign |
| [**createAdSet**](AdCampaignsApi.md#createAdSet) | **POST** /v1/ads/ad-sets | Create a standalone ad group |
| [**createAdSetWithHttpInfo**](AdCampaignsApi.md#createAdSetWithHttpInfo) | **POST** /v1/ads/ad-sets | Create a standalone ad group |
| [**createBidStrategy**](AdCampaignsApi.md#createBidStrategy) | **POST** /v1/ads/bid-strategies | Create portfolio bid strategy |
| [**createBidStrategyWithHttpInfo**](AdCampaignsApi.md#createBidStrategyWithHttpInfo) | **POST** /v1/ads/bid-strategies | Create portfolio bid strategy |
| [**createGoogleAssetGroup**](AdCampaignsApi.md#createGoogleAssetGroup) | **POST** /v1/ads/campaigns/{campaignId}/asset-groups | Create a Performance Max asset group |
| [**createGoogleAssetGroupWithHttpInfo**](AdCampaignsApi.md#createGoogleAssetGroupWithHttpInfo) | **POST** /v1/ads/campaigns/{campaignId}/asset-groups | Create a Performance Max asset group |
| [**createSharedBudget**](AdCampaignsApi.md#createSharedBudget) | **POST** /v1/ads/shared-budgets | Create a shared budget |
| [**createSharedBudgetWithHttpInfo**](AdCampaignsApi.md#createSharedBudgetWithHttpInfo) | **POST** /v1/ads/shared-budgets | Create a shared budget |
| [**createStandaloneAd**](AdCampaignsApi.md#createStandaloneAd) | **POST** /v1/ads/create | Create standalone ad |
| [**createStandaloneAdWithHttpInfo**](AdCampaignsApi.md#createStandaloneAdWithHttpInfo) | **POST** /v1/ads/create | Create standalone ad |
| [**deleteAd**](AdCampaignsApi.md#deleteAd) | **DELETE** /v1/ads/{adId} | Cancel an ad |
| [**deleteAdWithHttpInfo**](AdCampaignsApi.md#deleteAdWithHttpInfo) | **DELETE** /v1/ads/{adId} | Cancel an ad |
| [**deleteAdCampaign**](AdCampaignsApi.md#deleteAdCampaign) | **DELETE** /v1/ads/campaigns/{campaignId} | Delete a campaign |
| [**deleteAdCampaignWithHttpInfo**](AdCampaignsApi.md#deleteAdCampaignWithHttpInfo) | **DELETE** /v1/ads/campaigns/{campaignId} | Delete a campaign |
| [**deleteAdSet**](AdCampaignsApi.md#deleteAdSet) | **DELETE** /v1/ads/ad-sets/{adSetId} | Delete an ad set |
| [**deleteAdSetWithHttpInfo**](AdCampaignsApi.md#deleteAdSetWithHttpInfo) | **DELETE** /v1/ads/ad-sets/{adSetId} | Delete an ad set |
| [**dismissAdsAlert**](AdCampaignsApi.md#dismissAdsAlert) | **POST** /v1/ads/alerts/{alertId}/dismiss | Dismiss an ads alert |
| [**dismissAdsAlertWithHttpInfo**](AdCampaignsApi.md#dismissAdsAlertWithHttpInfo) | **POST** /v1/ads/alerts/{alertId}/dismiss | Dismiss an ads alert |
| [**dismissGoogleRecommendations**](AdCampaignsApi.md#dismissGoogleRecommendations) | **POST** /v1/ads/recommendations/dismiss | Dismiss Google Ads recommendations |
| [**dismissGoogleRecommendationsWithHttpInfo**](AdCampaignsApi.md#dismissGoogleRecommendationsWithHttpInfo) | **POST** /v1/ads/recommendations/dismiss | Dismiss Google Ads recommendations |
| [**duplicateAd**](AdCampaignsApi.md#duplicateAd) | **POST** /v1/ads/{adId}/duplicate | Duplicate an ad |
| [**duplicateAdWithHttpInfo**](AdCampaignsApi.md#duplicateAdWithHttpInfo) | **POST** /v1/ads/{adId}/duplicate | Duplicate an ad |
| [**duplicateAdCampaign**](AdCampaignsApi.md#duplicateAdCampaign) | **POST** /v1/ads/campaigns/{campaignId}/duplicate | Duplicate a campaign |
| [**duplicateAdCampaignWithHttpInfo**](AdCampaignsApi.md#duplicateAdCampaignWithHttpInfo) | **POST** /v1/ads/campaigns/{campaignId}/duplicate | Duplicate a campaign |
| [**duplicateAdSet**](AdCampaignsApi.md#duplicateAdSet) | **POST** /v1/ads/ad-sets/{adSetId}/duplicate | Duplicate an ad set |
| [**duplicateAdSetWithHttpInfo**](AdCampaignsApi.md#duplicateAdSetWithHttpInfo) | **POST** /v1/ads/ad-sets/{adSetId}/duplicate | Duplicate an ad set |
| [**editGoogleAssetGroupAssets**](AdCampaignsApi.md#editGoogleAssetGroupAssets) | **POST** /v1/ads/campaigns/{campaignId}/asset-groups/{assetGroupId}/assets | Link or unlink asset group assets |
| [**editGoogleAssetGroupAssetsWithHttpInfo**](AdCampaignsApi.md#editGoogleAssetGroupAssetsWithHttpInfo) | **POST** /v1/ads/campaigns/{campaignId}/asset-groups/{assetGroupId}/assets | Link or unlink asset group assets |
| [**getAd**](AdCampaignsApi.md#getAd) | **GET** /v1/ads/{adId} | Get ad details |
| [**getAdWithHttpInfo**](AdCampaignsApi.md#getAdWithHttpInfo) | **GET** /v1/ads/{adId} | Get ad details |
| [**getAdCampaignDetails**](AdCampaignsApi.md#getAdCampaignDetails) | **GET** /v1/ads/campaigns/{campaignId} | Get live campaign details |
| [**getAdCampaignDetailsWithHttpInfo**](AdCampaignsApi.md#getAdCampaignDetailsWithHttpInfo) | **GET** /v1/ads/campaigns/{campaignId} | Get live campaign details |
| [**getAdReview**](AdCampaignsApi.md#getAdReview) | **GET** /v1/ads/{adId}/review | Read the platform&#39;s review verdict for an ad |
| [**getAdReviewWithHttpInfo**](AdCampaignsApi.md#getAdReviewWithHttpInfo) | **GET** /v1/ads/{adId}/review | Read the platform&#39;s review verdict for an ad |
| [**getAdSetDetails**](AdCampaignsApi.md#getAdSetDetails) | **GET** /v1/ads/ad-sets/{adSetId} | Get live ad-set details |
| [**getAdSetDetailsWithHttpInfo**](AdCampaignsApi.md#getAdSetDetailsWithHttpInfo) | **GET** /v1/ads/ad-sets/{adSetId} | Get live ad-set details |
| [**getAdSetTargeting**](AdCampaignsApi.md#getAdSetTargeting) | **GET** /v1/ads/ad-sets/{adSetId}/targeting | Read a Reddit ad group&#39;s targeting and schedule |
| [**getAdSetTargetingWithHttpInfo**](AdCampaignsApi.md#getAdSetTargetingWithHttpInfo) | **GET** /v1/ads/ad-sets/{adSetId}/targeting | Read a Reddit ad group&#39;s targeting and schedule |
| [**getAdTree**](AdCampaignsApi.md#getAdTree) | **GET** /v1/ads/tree | Get campaign tree |
| [**getAdTreeWithHttpInfo**](AdCampaignsApi.md#getAdTreeWithHttpInfo) | **GET** /v1/ads/tree | Get campaign tree |
| [**getAdsTimeline**](AdCampaignsApi.md#getAdsTimeline) | **GET** /v1/ads/timeline | Get daily account metrics |
| [**getAdsTimelineWithHttpInfo**](AdCampaignsApi.md#getAdsTimelineWithHttpInfo) | **GET** /v1/ads/timeline | Get daily account metrics |
| [**getCampaignAdSchedule**](AdCampaignsApi.md#getCampaignAdSchedule) | **GET** /v1/ads/campaigns/{campaignId}/ad-schedule | Read a campaign&#39;s ad schedule (dayparting) |
| [**getCampaignAdScheduleWithHttpInfo**](AdCampaignsApi.md#getCampaignAdScheduleWithHttpInfo) | **GET** /v1/ads/campaigns/{campaignId}/ad-schedule | Read a campaign&#39;s ad schedule (dayparting) |
| [**getCampaignBidding**](AdCampaignsApi.md#getCampaignBidding) | **GET** /v1/ads/campaigns/{campaignId}/bidding | Read a campaign&#39;s current bidding |
| [**getCampaignBiddingWithHttpInfo**](AdCampaignsApi.md#getCampaignBiddingWithHttpInfo) | **GET** /v1/ads/campaigns/{campaignId}/bidding | Read a campaign&#39;s current bidding |
| [**getCampaignConversionGoals**](AdCampaignsApi.md#getCampaignConversionGoals) | **GET** /v1/ads/campaigns/{campaignId}/conversion-goals | Get campaign conversion goals |
| [**getCampaignConversionGoalsWithHttpInfo**](AdCampaignsApi.md#getCampaignConversionGoalsWithHttpInfo) | **GET** /v1/ads/campaigns/{campaignId}/conversion-goals | Get campaign conversion goals |
| [**getCampaignTargeting**](AdCampaignsApi.md#getCampaignTargeting) | **GET** /v1/ads/campaigns/{campaignId}/targeting | Read a Google campaign&#39;s device, location, excluded location, and language targeting |
| [**getCampaignTargetingWithHttpInfo**](AdCampaignsApi.md#getCampaignTargetingWithHttpInfo) | **GET** /v1/ads/campaigns/{campaignId}/targeting | Read a Google campaign&#39;s device, location, excluded location, and language targeting |
| [**getGoogleAssetGroup**](AdCampaignsApi.md#getGoogleAssetGroup) | **GET** /v1/ads/campaigns/{campaignId}/asset-groups/{assetGroupId} | Get a Performance Max asset group |
| [**getGoogleAssetGroupWithHttpInfo**](AdCampaignsApi.md#getGoogleAssetGroupWithHttpInfo) | **GET** /v1/ads/campaigns/{campaignId}/asset-groups/{assetGroupId} | Get a Performance Max asset group |
| [**getTikTokSmartPlusAdReview**](AdCampaignsApi.md#getTikTokSmartPlusAdReview) | **GET** /v1/ads/{adId}/tiktok-smart-plus-review | Review status of each creative in a TikTok Smart+ ad |
| [**getTikTokSmartPlusAdReviewWithHttpInfo**](AdCampaignsApi.md#getTikTokSmartPlusAdReviewWithHttpInfo) | **GET** /v1/ads/{adId}/tiktok-smart-plus-review | Review status of each creative in a TikTok Smart+ ad |
| [**listAdCampaigns**](AdCampaignsApi.md#listAdCampaigns) | **GET** /v1/ads/campaigns | List campaigns |
| [**listAdCampaignsWithHttpInfo**](AdCampaignsApi.md#listAdCampaignsWithHttpInfo) | **GET** /v1/ads/campaigns | List campaigns |
| [**listAdGroupAssets**](AdCampaignsApi.md#listAdGroupAssets) | **GET** /v1/ads/ad-sets/{adSetId}/assets | List ad-group assets |
| [**listAdGroupAssetsWithHttpInfo**](AdCampaignsApi.md#listAdGroupAssetsWithHttpInfo) | **GET** /v1/ads/ad-sets/{adSetId}/assets | List ad-group assets |
| [**listAdKeywords**](AdCampaignsApi.md#listAdKeywords) | **GET** /v1/ads/keywords | List Search keywords |
| [**listAdKeywordsWithHttpInfo**](AdCampaignsApi.md#listAdKeywordsWithHttpInfo) | **GET** /v1/ads/keywords | List Search keywords |
| [**listAdSets**](AdCampaignsApi.md#listAdSets) | **GET** /v1/ads/ad-sets | List ad sets |
| [**listAdSetsWithHttpInfo**](AdCampaignsApi.md#listAdSetsWithHttpInfo) | **GET** /v1/ads/ad-sets | List ad sets |
| [**listAds**](AdCampaignsApi.md#listAds) | **GET** /v1/ads | List ads |
| [**listAdsWithHttpInfo**](AdCampaignsApi.md#listAdsWithHttpInfo) | **GET** /v1/ads | List ads |
| [**listAdsAlerts**](AdCampaignsApi.md#listAdsAlerts) | **GET** /v1/ads/alerts | List ads that need attention |
| [**listAdsAlertsWithHttpInfo**](AdCampaignsApi.md#listAdsAlertsWithHttpInfo) | **GET** /v1/ads/alerts | List ads that need attention |
| [**listBidStrategies**](AdCampaignsApi.md#listBidStrategies) | **GET** /v1/ads/bid-strategies | List portfolio bid strategies |
| [**listBidStrategiesWithHttpInfo**](AdCampaignsApi.md#listBidStrategiesWithHttpInfo) | **GET** /v1/ads/bid-strategies | List portfolio bid strategies |
| [**listCampaignAssets**](AdCampaignsApi.md#listCampaignAssets) | **GET** /v1/ads/campaigns/{campaignId}/assets | List campaign assets |
| [**listCampaignAssetsWithHttpInfo**](AdCampaignsApi.md#listCampaignAssetsWithHttpInfo) | **GET** /v1/ads/campaigns/{campaignId}/assets | List campaign assets |
| [**listCampaignNegativeKeywordLists**](AdCampaignsApi.md#listCampaignNegativeKeywordLists) | **GET** /v1/ads/campaigns/{campaignId}/negative-keyword-lists | List campaign negative lists |
| [**listCampaignNegativeKeywordListsWithHttpInfo**](AdCampaignsApi.md#listCampaignNegativeKeywordListsWithHttpInfo) | **GET** /v1/ads/campaigns/{campaignId}/negative-keyword-lists | List campaign negative lists |
| [**listCampaignNegativeKeywords**](AdCampaignsApi.md#listCampaignNegativeKeywords) | **GET** /v1/ads/campaigns/{campaignId}/negative-keywords | List campaign-level negative keywords |
| [**listCampaignNegativeKeywordsWithHttpInfo**](AdCampaignsApi.md#listCampaignNegativeKeywordsWithHttpInfo) | **GET** /v1/ads/campaigns/{campaignId}/negative-keywords | List campaign-level negative keywords |
| [**listGoogleAssetGroups**](AdCampaignsApi.md#listGoogleAssetGroups) | **GET** /v1/ads/campaigns/{campaignId}/asset-groups | List Performance Max asset groups |
| [**listGoogleAssetGroupsWithHttpInfo**](AdCampaignsApi.md#listGoogleAssetGroupsWithHttpInfo) | **GET** /v1/ads/campaigns/{campaignId}/asset-groups | List Performance Max asset groups |
| [**listGoogleRecommendations**](AdCampaignsApi.md#listGoogleRecommendations) | **GET** /v1/ads/recommendations | List Google Ads recommendations |
| [**listGoogleRecommendationsWithHttpInfo**](AdCampaignsApi.md#listGoogleRecommendationsWithHttpInfo) | **GET** /v1/ads/recommendations | List Google Ads recommendations |
| [**listSharedBudgets**](AdCampaignsApi.md#listSharedBudgets) | **GET** /v1/ads/shared-budgets | List shared budgets |
| [**listSharedBudgetsWithHttpInfo**](AdCampaignsApi.md#listSharedBudgetsWithHttpInfo) | **GET** /v1/ads/shared-budgets | List shared budgets |
| [**listTikTokSmartPlusReviews**](AdCampaignsApi.md#listTikTokSmartPlusReviews) | **GET** /v1/ads/tiktok-smart-plus-reviews | Review status of every TikTok Smart+ ad of an advertiser |
| [**listTikTokSmartPlusReviewsWithHttpInfo**](AdCampaignsApi.md#listTikTokSmartPlusReviewsWithHttpInfo) | **GET** /v1/ads/tiktok-smart-plus-reviews | Review status of every TikTok Smart+ ad of an advertiser |
| [**removeAdGroupAssets**](AdCampaignsApi.md#removeAdGroupAssets) | **DELETE** /v1/ads/ad-sets/{adSetId}/assets | Remove ad-group assets |
| [**removeAdGroupAssetsWithHttpInfo**](AdCampaignsApi.md#removeAdGroupAssetsWithHttpInfo) | **DELETE** /v1/ads/ad-sets/{adSetId}/assets | Remove ad-group assets |
| [**removeAdKeyword**](AdCampaignsApi.md#removeAdKeyword) | **DELETE** /v1/ads/keywords/{keywordId} | Remove a Search keyword |
| [**removeAdKeywordWithHttpInfo**](AdCampaignsApi.md#removeAdKeywordWithHttpInfo) | **DELETE** /v1/ads/keywords/{keywordId} | Remove a Search keyword |
| [**removeCampaignAssets**](AdCampaignsApi.md#removeCampaignAssets) | **DELETE** /v1/ads/campaigns/{campaignId}/assets | Remove campaign assets |
| [**removeCampaignAssetsWithHttpInfo**](AdCampaignsApi.md#removeCampaignAssetsWithHttpInfo) | **DELETE** /v1/ads/campaigns/{campaignId}/assets | Remove campaign assets |
| [**removeGoogleAssetGroup**](AdCampaignsApi.md#removeGoogleAssetGroup) | **DELETE** /v1/ads/campaigns/{campaignId}/asset-groups/{assetGroupId} | Remove a Performance Max asset group |
| [**removeGoogleAssetGroupWithHttpInfo**](AdCampaignsApi.md#removeGoogleAssetGroupWithHttpInfo) | **DELETE** /v1/ads/campaigns/{campaignId}/asset-groups/{assetGroupId} | Remove a Performance Max asset group |
| [**replaceCampaignNegativeKeywordLists**](AdCampaignsApi.md#replaceCampaignNegativeKeywordLists) | **PUT** /v1/ads/campaigns/{campaignId}/negative-keyword-lists | Replace campaign negative lists |
| [**replaceCampaignNegativeKeywordListsWithHttpInfo**](AdCampaignsApi.md#replaceCampaignNegativeKeywordListsWithHttpInfo) | **PUT** /v1/ads/campaigns/{campaignId}/negative-keyword-lists | Replace campaign negative lists |
| [**replaceCampaignNegativeKeywords**](AdCampaignsApi.md#replaceCampaignNegativeKeywords) | **PUT** /v1/ads/campaigns/{campaignId}/negative-keywords | Replace campaign-level negative keywords |
| [**replaceCampaignNegativeKeywordsWithHttpInfo**](AdCampaignsApi.md#replaceCampaignNegativeKeywordsWithHttpInfo) | **PUT** /v1/ads/campaigns/{campaignId}/negative-keywords | Replace campaign-level negative keywords |
| [**replaceGoogleListingGroupFilters**](AdCampaignsApi.md#replaceGoogleListingGroupFilters) | **PUT** /v1/ads/campaigns/{campaignId}/asset-groups/{assetGroupId}/listing-group-filters | Replace an asset group&#39;s listing-group tree |
| [**replaceGoogleListingGroupFiltersWithHttpInfo**](AdCampaignsApi.md#replaceGoogleListingGroupFiltersWithHttpInfo) | **PUT** /v1/ads/campaigns/{campaignId}/asset-groups/{assetGroupId}/listing-group-filters | Replace an asset group&#39;s listing-group tree |
| [**updateAd**](AdCampaignsApi.md#updateAd) | **PUT** /v1/ads/{adId} | Update ad |
| [**updateAdWithHttpInfo**](AdCampaignsApi.md#updateAdWithHttpInfo) | **PUT** /v1/ads/{adId} | Update ad |
| [**updateAdCampaign**](AdCampaignsApi.md#updateAdCampaign) | **PUT** /v1/ads/campaigns/{campaignId} | Update a campaign |
| [**updateAdCampaignWithHttpInfo**](AdCampaignsApi.md#updateAdCampaignWithHttpInfo) | **PUT** /v1/ads/campaigns/{campaignId} | Update a campaign |
| [**updateAdCampaignStatus**](AdCampaignsApi.md#updateAdCampaignStatus) | **PUT** /v1/ads/campaigns/{campaignId}/status | Pause or resume a campaign |
| [**updateAdCampaignStatusWithHttpInfo**](AdCampaignsApi.md#updateAdCampaignStatusWithHttpInfo) | **PUT** /v1/ads/campaigns/{campaignId}/status | Pause or resume a campaign |
| [**updateAdGroupAssets**](AdCampaignsApi.md#updateAdGroupAssets) | **PUT** /v1/ads/ad-sets/{adSetId}/assets | Update ad-group assets |
| [**updateAdGroupAssetsWithHttpInfo**](AdCampaignsApi.md#updateAdGroupAssetsWithHttpInfo) | **PUT** /v1/ads/ad-sets/{adSetId}/assets | Update ad-group assets |
| [**updateAdKeyword**](AdCampaignsApi.md#updateAdKeyword) | **PATCH** /v1/ads/keywords/{keywordId} | Pause or enable a Search keyword |
| [**updateAdKeywordWithHttpInfo**](AdCampaignsApi.md#updateAdKeywordWithHttpInfo) | **PATCH** /v1/ads/keywords/{keywordId} | Pause or enable a Search keyword |
| [**updateAdSet**](AdCampaignsApi.md#updateAdSet) | **PUT** /v1/ads/ad-sets/{adSetId} | Update an ad set |
| [**updateAdSetWithHttpInfo**](AdCampaignsApi.md#updateAdSetWithHttpInfo) | **PUT** /v1/ads/ad-sets/{adSetId} | Update an ad set |
| [**updateAdSetStatus**](AdCampaignsApi.md#updateAdSetStatus) | **PUT** /v1/ads/ad-sets/{adSetId}/status | Pause or resume a single ad set |
| [**updateAdSetStatusWithHttpInfo**](AdCampaignsApi.md#updateAdSetStatusWithHttpInfo) | **PUT** /v1/ads/ad-sets/{adSetId}/status | Pause or resume a single ad set |
| [**updateAdStatus**](AdCampaignsApi.md#updateAdStatus) | **PUT** /v1/ads/{adId}/status | Pause or resume a single ad |
| [**updateAdStatusWithHttpInfo**](AdCampaignsApi.md#updateAdStatusWithHttpInfo) | **PUT** /v1/ads/{adId}/status | Pause or resume a single ad |
| [**updateBidStrategy**](AdCampaignsApi.md#updateBidStrategy) | **PATCH** /v1/ads/bid-strategies/{strategyId} | Update portfolio bid strategy |
| [**updateBidStrategyWithHttpInfo**](AdCampaignsApi.md#updateBidStrategyWithHttpInfo) | **PATCH** /v1/ads/bid-strategies/{strategyId} | Update portfolio bid strategy |
| [**updateCampaignAdSchedule**](AdCampaignsApi.md#updateCampaignAdSchedule) | **PUT** /v1/ads/campaigns/{campaignId}/ad-schedule | Replace a campaign&#39;s ad schedule (dayparting) |
| [**updateCampaignAdScheduleWithHttpInfo**](AdCampaignsApi.md#updateCampaignAdScheduleWithHttpInfo) | **PUT** /v1/ads/campaigns/{campaignId}/ad-schedule | Replace a campaign&#39;s ad schedule (dayparting) |
| [**updateCampaignAssets**](AdCampaignsApi.md#updateCampaignAssets) | **PUT** /v1/ads/campaigns/{campaignId}/assets | Update campaign assets |
| [**updateCampaignAssetsWithHttpInfo**](AdCampaignsApi.md#updateCampaignAssetsWithHttpInfo) | **PUT** /v1/ads/campaigns/{campaignId}/assets | Update campaign assets |
| [**updateCampaignConversionGoals**](AdCampaignsApi.md#updateCampaignConversionGoals) | **PATCH** /v1/ads/campaigns/{campaignId}/conversion-goals | Update campaign conversion goals |
| [**updateCampaignConversionGoalsWithHttpInfo**](AdCampaignsApi.md#updateCampaignConversionGoalsWithHttpInfo) | **PATCH** /v1/ads/campaigns/{campaignId}/conversion-goals | Update campaign conversion goals |
| [**updateCampaignTargeting**](AdCampaignsApi.md#updateCampaignTargeting) | **PUT** /v1/ads/campaigns/{campaignId}/targeting | Edit a Google campaign&#39;s device, location, excluded location, or language targeting |
| [**updateCampaignTargetingWithHttpInfo**](AdCampaignsApi.md#updateCampaignTargetingWithHttpInfo) | **PUT** /v1/ads/campaigns/{campaignId}/targeting | Edit a Google campaign&#39;s device, location, excluded location, or language targeting |
| [**updateGoogleAssetGroup**](AdCampaignsApi.md#updateGoogleAssetGroup) | **PATCH** /v1/ads/campaigns/{campaignId}/asset-groups/{assetGroupId} | Update a Performance Max asset group |
| [**updateGoogleAssetGroupWithHttpInfo**](AdCampaignsApi.md#updateGoogleAssetGroupWithHttpInfo) | **PATCH** /v1/ads/campaigns/{campaignId}/asset-groups/{assetGroupId} | Update a Performance Max asset group |



## addAdKeywords

> AddAdKeywords201Response addAdKeywords(addAdKeywordsRequest)

Add Search ad-group keywords

Adds keywords, or negative keywords, to a Google Search ad group without replacing the ones already there.  Adds one or more keyword criteria to an existing Google Search ad group, without touching the keywords already there (unlike the whole-set diff on &#x60;PUT /v1/ads/{adId}&#x60;, &#x60;keywords&#x60;/&#x60;negativeKeywords&#x60; in &#x60;platformSpecificData&#x60;, which replaces the set). Set &#x60;negative: true&#x60; to add ad-group-level negatives instead of positive keywords. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        AddAdKeywordsRequest addAdKeywordsRequest = new AddAdKeywordsRequest(); // AddAdKeywordsRequest | 
        try {
            AddAdKeywords201Response result = apiInstance.addAdKeywords(addAdKeywordsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#addAdKeywords");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **addAdKeywordsRequest** | [**AddAdKeywordsRequest**](AddAdKeywordsRequest.md)|  | |

### Return type

[**AddAdKeywords201Response**](AddAdKeywords201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **201** | Keywords added |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | Only available on Google Ads accounts |  -  |

## addAdKeywordsWithHttpInfo

> ApiResponse<AddAdKeywords201Response> addAdKeywords addAdKeywordsWithHttpInfo(addAdKeywordsRequest)

Add Search ad-group keywords

Adds keywords, or negative keywords, to a Google Search ad group without replacing the ones already there.  Adds one or more keyword criteria to an existing Google Search ad group, without touching the keywords already there (unlike the whole-set diff on &#x60;PUT /v1/ads/{adId}&#x60;, &#x60;keywords&#x60;/&#x60;negativeKeywords&#x60; in &#x60;platformSpecificData&#x60;, which replaces the set). Set &#x60;negative: true&#x60; to add ad-group-level negatives instead of positive keywords. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        AddAdKeywordsRequest addAdKeywordsRequest = new AddAdKeywordsRequest(); // AddAdKeywordsRequest | 
        try {
            ApiResponse<AddAdKeywords201Response> response = apiInstance.addAdKeywordsWithHttpInfo(addAdKeywordsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#addAdKeywords");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **addAdKeywordsRequest** | [**AddAdKeywordsRequest**](AddAdKeywordsRequest.md)|  | |

### Return type

ApiResponse<[**AddAdKeywords201Response**](AddAdKeywords201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **201** | Keywords added |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | Only available on Google Ads accounts |  -  |


## applyGoogleRecommendations

> ApplyGoogleRecommendations200Response applyGoogleRecommendations(applyGoogleRecommendationsRequest)

Apply Google Ads recommendations

Applies Google&#39;s optimization suggestions to an ad account, using Google&#39;s values or your own; the changes cannot be undone.  Apply up to 100 recommendations. This changes the account (budgets, bidding, keywords, assets) and is not reversible or idempotent. Google offers no validate-only mode for it.  Items run in partial-failure mode, so one stale recommendation does not block the rest.  ### &#x60;parameters&#x60;  Optional. It takes exactly one key named for the recommendation type, in Google&#39;s ApplyRecommendationOperation shape. For example:  - &#x60;campaignBudget: { newBudgetAmountMicros }&#x60; - &#x60;keyword: { matchType, cpcBidMicros }&#x60;  Omit it to apply Google&#39;s suggested values. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        ApplyGoogleRecommendationsRequest applyGoogleRecommendationsRequest = new ApplyGoogleRecommendationsRequest(); // ApplyGoogleRecommendationsRequest | 
        try {
            ApplyGoogleRecommendations200Response result = apiInstance.applyGoogleRecommendations(applyGoogleRecommendationsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#applyGoogleRecommendations");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **applyGoogleRecommendationsRequest** | [**ApplyGoogleRecommendationsRequest**](ApplyGoogleRecommendationsRequest.md)|  | |

### Return type

[**ApplyGoogleRecommendations200Response**](ApplyGoogleRecommendations200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-recommendation outcome. A failed item does not stop the others. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **404** | Resource not found |  -  |
| **422** | No Google Ads customer on this connection, or it needs reconnecting. |  -  |
| **429** | Google quota or the Zernio Google operations burst limit is exhausted. |  -  |
| **501** | accountId is not a Google Ads connection. |  -  |

## applyGoogleRecommendationsWithHttpInfo

> ApiResponse<ApplyGoogleRecommendations200Response> applyGoogleRecommendations applyGoogleRecommendationsWithHttpInfo(applyGoogleRecommendationsRequest)

Apply Google Ads recommendations

Applies Google&#39;s optimization suggestions to an ad account, using Google&#39;s values or your own; the changes cannot be undone.  Apply up to 100 recommendations. This changes the account (budgets, bidding, keywords, assets) and is not reversible or idempotent. Google offers no validate-only mode for it.  Items run in partial-failure mode, so one stale recommendation does not block the rest.  ### &#x60;parameters&#x60;  Optional. It takes exactly one key named for the recommendation type, in Google&#39;s ApplyRecommendationOperation shape. For example:  - &#x60;campaignBudget: { newBudgetAmountMicros }&#x60; - &#x60;keyword: { matchType, cpcBidMicros }&#x60;  Omit it to apply Google&#39;s suggested values. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        ApplyGoogleRecommendationsRequest applyGoogleRecommendationsRequest = new ApplyGoogleRecommendationsRequest(); // ApplyGoogleRecommendationsRequest | 
        try {
            ApiResponse<ApplyGoogleRecommendations200Response> response = apiInstance.applyGoogleRecommendationsWithHttpInfo(applyGoogleRecommendationsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#applyGoogleRecommendations");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **applyGoogleRecommendationsRequest** | [**ApplyGoogleRecommendationsRequest**](ApplyGoogleRecommendationsRequest.md)|  | |

### Return type

ApiResponse<[**ApplyGoogleRecommendations200Response**](ApplyGoogleRecommendations200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-recommendation outcome. A failed item does not stop the others. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **404** | Resource not found |  -  |
| **422** | No Google Ads customer on this connection, or it needs reconnecting. |  -  |
| **429** | Google quota or the Zernio Google operations burst limit is exhausted. |  -  |
| **501** | accountId is not a Google Ads connection. |  -  |


## attachAdGroupAssets

> AttachAdGroupAssets201Response attachAdGroupAssets(adSetId, attachCampaignAssetsRequest)

Attach ad-group assets

Creates sitelinks, callouts, structured snippets or image assets and attaches them to a Google ad group in one step.  Creates and attaches sitelinks, callouts, structured snippets and image assets in one Google mutation. Google shows images only on accounts it deems eligible (account age, policy history, vertical). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Numeric Google platform id.
        AttachCampaignAssetsRequest attachCampaignAssetsRequest = new AttachCampaignAssetsRequest(); // AttachCampaignAssetsRequest | 
        try {
            AttachAdGroupAssets201Response result = apiInstance.attachAdGroupAssets(adSetId, attachCampaignAssetsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#attachAdGroupAssets");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adSetId** | **String**| Numeric Google platform id. | |
| **attachCampaignAssetsRequest** | [**AttachCampaignAssetsRequest**](AttachCampaignAssetsRequest.md)|  | |

### Return type

[**AttachAdGroupAssets201Response**](AttachAdGroupAssets201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **201** | Assets created and attached. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access is required.  Also returned with code &#x60;ad_account_not_selected&#x60; when the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |

## attachAdGroupAssetsWithHttpInfo

> ApiResponse<AttachAdGroupAssets201Response> attachAdGroupAssets attachAdGroupAssetsWithHttpInfo(adSetId, attachCampaignAssetsRequest)

Attach ad-group assets

Creates sitelinks, callouts, structured snippets or image assets and attaches them to a Google ad group in one step.  Creates and attaches sitelinks, callouts, structured snippets and image assets in one Google mutation. Google shows images only on accounts it deems eligible (account age, policy history, vertical). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Numeric Google platform id.
        AttachCampaignAssetsRequest attachCampaignAssetsRequest = new AttachCampaignAssetsRequest(); // AttachCampaignAssetsRequest | 
        try {
            ApiResponse<AttachAdGroupAssets201Response> response = apiInstance.attachAdGroupAssetsWithHttpInfo(adSetId, attachCampaignAssetsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#attachAdGroupAssets");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adSetId** | **String**| Numeric Google platform id. | |
| **attachCampaignAssetsRequest** | [**AttachCampaignAssetsRequest**](AttachCampaignAssetsRequest.md)|  | |

### Return type

ApiResponse<[**AttachAdGroupAssets201Response**](AttachAdGroupAssets201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **201** | Assets created and attached. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access is required.  Also returned with code &#x60;ad_account_not_selected&#x60; when the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |


## attachCampaignAssets

> AttachCampaignAssets201Response attachCampaignAssets(campaignId, attachCampaignAssetsRequest)

Attach campaign assets

Adds sitelinks, callouts, structured snippets and images to a Google campaign in one step.  Creates and attaches sitelinks, callouts, structured snippets and image assets in one Google mutation. Google shows images only on accounts it deems eligible (account age, policy history, vertical). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Numeric Google platform id.
        AttachCampaignAssetsRequest attachCampaignAssetsRequest = new AttachCampaignAssetsRequest(); // AttachCampaignAssetsRequest | 
        try {
            AttachCampaignAssets201Response result = apiInstance.attachCampaignAssets(campaignId, attachCampaignAssetsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#attachCampaignAssets");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Numeric Google platform id. | |
| **attachCampaignAssetsRequest** | [**AttachCampaignAssetsRequest**](AttachCampaignAssetsRequest.md)|  | |

### Return type

[**AttachCampaignAssets201Response**](AttachCampaignAssets201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **201** | Assets created and attached. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access is required.  Also returned with code &#x60;ad_account_not_selected&#x60; when the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix it, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |

## attachCampaignAssetsWithHttpInfo

> ApiResponse<AttachCampaignAssets201Response> attachCampaignAssets attachCampaignAssetsWithHttpInfo(campaignId, attachCampaignAssetsRequest)

Attach campaign assets

Adds sitelinks, callouts, structured snippets and images to a Google campaign in one step.  Creates and attaches sitelinks, callouts, structured snippets and image assets in one Google mutation. Google shows images only on accounts it deems eligible (account age, policy history, vertical). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Numeric Google platform id.
        AttachCampaignAssetsRequest attachCampaignAssetsRequest = new AttachCampaignAssetsRequest(); // AttachCampaignAssetsRequest | 
        try {
            ApiResponse<AttachCampaignAssets201Response> response = apiInstance.attachCampaignAssetsWithHttpInfo(campaignId, attachCampaignAssetsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#attachCampaignAssets");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Numeric Google platform id. | |
| **attachCampaignAssetsRequest** | [**AttachCampaignAssetsRequest**](AttachCampaignAssetsRequest.md)|  | |

### Return type

ApiResponse<[**AttachCampaignAssets201Response**](AttachCampaignAssets201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **201** | Assets created and attached. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access is required.  Also returned with code &#x60;ad_account_not_selected&#x60; when the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix it, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |


## boostPost

> BoostPost200Response boostPost(boostPostRequest, idempotencyKey)

Boost post as ad

Turns an already published post into a paid ad that keeps the post&#39;s likes and comments, creating the campaign around it.  By default it provisions the whole hierarchy (campaign, ad set, ad).  ### Attach shape (Meta)  Send &#x60;adSetId&#x60; to put the ad under an EXISTING ad set instead, so that ad set keeps its learning phase.  That ad set then owns &#x60;budget&#x60;, &#x60;schedule&#x60; and &#x60;targeting&#x60;. Sending any of those alongside &#x60;adSetId&#x60; is a 400 rather than a silent drop. &#x60;budget&#x60; is required only without &#x60;adSetId&#x60;.  &#x60;instagramAccountId&#x60;, &#x60;destinationType&#x60;, &#x60;whatsappPhoneNumber&#x60; and &#x60;adSetId&#x60; are Meta-only and return 400 on other platforms.  ### Meta accounts  &#x60;accountId&#x60; may be a Facebook, Instagram or Meta ads (business login) connection.  A business-login connection has no posting account, so pass the post as &#x60;platformPostId&#x60; (Facebook &#x60;pageId_postId&#x60; or an Instagram media id). A Zernio &#x60;postId&#x60; is a 400 there.  ### X  &#x60;accountId&#x60; may be the posting X account or its X Ads connection: either resolves the other on the same profile.  A Zernio &#x60;postId&#x60; on an X Ads connection resolves through its X account, and is a 400 when the profile has none (pass &#x60;platformPostId&#x60; instead).  ### Reddit  &#x60;accountId&#x60; is the Reddit Ads connection (platform &#x60;redditads&#x60;). Pass the Reddit post as either:  - &#x60;platformPostId&#x60; (&#x60;t3_abc123&#x60; or the bare id) - a Zernio &#x60;postId&#x60;, which resolves through the Reddit account connected on the same profile (400 when there is none)  Reddit promotes only posts made by a profile of the ad account: a post by any other author returns 422.  Goals:  - traffic - awareness - conversions - video_views (the post must be a video, 422 otherwise) - lead_generation  conversions and lead_generation need a pixel that already received the event (see &#x60;promotedObject&#x60;).  &#x60;leadGenFormId&#x60; returns 400: Reddit retired its native lead forms, so &#x60;lead_generation&#x60; sends people to &#x60;linkUrl&#x60; and optimizes toward the pixel&#39;s Lead event.  Each boost creates a campaign, an ad group carrying the budget, the targeting and the bid, and the ad. &#x60;bidStrategy&#x60; sets the ad group&#39;s bid:  - LOWEST_COST_WITHOUT_CAP (or omitted): automatic bidding (BIDLESS) - LOWEST_COST_WITH_BID_CAP: MANUAL_BIDDING with &#x60;bidAmount&#x60; as the bid - COST_CAP: MAXIMIZE_VOLUME with &#x60;bidAmount&#x60; as the cap - Any other strategy returns 422 before anything is created.  ### Messaging boosts (Meta)  Use &#x60;goal: engagement&#x60; with one of these CTAs:  - &#x60;callToAction: WHATSAPP_MESSAGE&#x60;: implies WHATSAPP - &#x60;MESSAGE_PAGE&#x60;: implies MESSENGER - &#x60;INSTAGRAM_MESSAGE&#x60;: implies INSTAGRAM_DIRECT  &#x60;destinationType&#x60; alone does not select a messaging CTA. Omit &#x60;linkUrl&#x60; only for messaging CTAs. Plain link CTAs keep their goal and link behavior when combined with an independent &#x60;destinationType&#x60;.  The campaign uses OUTCOME_ENGAGEMENT and the ad set uses CONVERSATIONS with the promoted Page. Optional &#x60;whatsappPhoneNumber&#x60; selects a number already paired with that Page.  Conflicting CTA/destination, instant form, goal, or optimizationGoal inputs return 400. Attach requires the target ad set destination to match.  Existing post references preserve social proof. An Instagram reel rejected by Meta is not re-uploaded as a new post for a messaging boost.  ### Retries  Boosts are NOT idempotent and can take minutes when Meta requires re-hosting an Instagram video, so do not retry on client timeout.  Send an Idempotency-Key header to make retries safe: same key and body replays the original 201, and distinct keys always create distinct ads.  Without the header, an identical request is treated as a retry:  - While one is in flight it returns 409. - Within 10 minutes of a completed boost it returns the already-created ad instead of creating another.  To intentionally duplicate an ad, send distinct Idempotency-Keys (or vary the body, e.g. the name). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        BoostPostRequest boostPostRequest = new BoostPostRequest(); // BoostPostRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. 
        try {
            BoostPost200Response result = apiInstance.boostPost(boostPostRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#boostPost");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **boostPostRequest** | [**BoostPostRequest**](BoostPostRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  | [optional] |

### Return type

[**BoostPost200Response**](BoostPost200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | validateOnly dry-run passed (Meta), nothing was created |  -  |
| **201** | Ad created |  -  |
| **400** | Missing required fields or invalid values, &#x60;validateOnly: true&#x60; outside Meta, &#x60;dryRun&#x60; sent, or a Meta validateOnly validation failure (verbatim) |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **429** | Meta only (code &#x60;rate_limited&#x60;). Meta puts a security hold lasting days (code 31, subcode 3858385, \&quot;Please authenticate your account\&quot;) on ad accounts that receive bursts of ad writes, and it counts &#x60;validateOnly&#x60; checks as writes.  To keep integrations out of that hold, Zernio:  - runs creates for one Meta ad account one at a time (a parallel request waits up to 60 seconds for its turn); - allows at most 30 creates per ad account in any rolling 5 minutes, &#x60;validateOnly&#x60; included.  A 429 here means one of the two was hit: wait &#x60;Retry-After&#x60; seconds and send creates for that ad account sequentially. Other ad accounts are not affected.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |
| **403** | Ads access required. Legacy plans need the Ads add-on; it is included by default on usage-based plans. Also returned with these codes:  - &#x60;ads_allowance_exceeded&#x60;: the team has no payment method on file and has reached the 500 free live ads. Add a card to resume. - &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;. - &#x60;ad_account_not_selected&#x60; fix: add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection), or use a connection that has it selected. - &#x60;insufficient_permissions&#x60;: the Facebook user behind the token lacks the Advertise permission on the Meta ad account, or the token lacks &#x60;ads_management&#x60; (Meta subcode 2490585, 2490591 or 4841020; see &#x60;ErrorResponse.details&#x60;).  |  -  |
| **409** | The account may also be inactive or need reconnection (code ads_connection_required). Reconnect it and read GET /v1/accounts for its current ID before retrying. An identical boost request is already in progress (with or without an Idempotency-Key). Wait for it to finish instead of retrying.  |  -  |
| **422** | Returned with one of these codes:  - &#x60;ads_connection_required&#x60;: platform ads connection required (TikTok Ads, X Ads), missing linked account, or (for TikTok) the connected TikTok user is not authorized as an Identity on the target advertiser. The message includes the actionable \&quot;TikTok Ads Manager → Assets → Identity\&quot; remediation step. - &#x60;idempotency_key_reused&#x60;: an Idempotency-Key was reused with a different request body. - &#x60;ad_account_unusable&#x60;: Meta refuses writes on the ad account because its status is ineligible to manage ads (see &#x60;ErrorResponse.details&#x60;).  |  -  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |

## boostPostWithHttpInfo

> ApiResponse<BoostPost200Response> boostPost boostPostWithHttpInfo(boostPostRequest, idempotencyKey)

Boost post as ad

Turns an already published post into a paid ad that keeps the post&#39;s likes and comments, creating the campaign around it.  By default it provisions the whole hierarchy (campaign, ad set, ad).  ### Attach shape (Meta)  Send &#x60;adSetId&#x60; to put the ad under an EXISTING ad set instead, so that ad set keeps its learning phase.  That ad set then owns &#x60;budget&#x60;, &#x60;schedule&#x60; and &#x60;targeting&#x60;. Sending any of those alongside &#x60;adSetId&#x60; is a 400 rather than a silent drop. &#x60;budget&#x60; is required only without &#x60;adSetId&#x60;.  &#x60;instagramAccountId&#x60;, &#x60;destinationType&#x60;, &#x60;whatsappPhoneNumber&#x60; and &#x60;adSetId&#x60; are Meta-only and return 400 on other platforms.  ### Meta accounts  &#x60;accountId&#x60; may be a Facebook, Instagram or Meta ads (business login) connection.  A business-login connection has no posting account, so pass the post as &#x60;platformPostId&#x60; (Facebook &#x60;pageId_postId&#x60; or an Instagram media id). A Zernio &#x60;postId&#x60; is a 400 there.  ### X  &#x60;accountId&#x60; may be the posting X account or its X Ads connection: either resolves the other on the same profile.  A Zernio &#x60;postId&#x60; on an X Ads connection resolves through its X account, and is a 400 when the profile has none (pass &#x60;platformPostId&#x60; instead).  ### Reddit  &#x60;accountId&#x60; is the Reddit Ads connection (platform &#x60;redditads&#x60;). Pass the Reddit post as either:  - &#x60;platformPostId&#x60; (&#x60;t3_abc123&#x60; or the bare id) - a Zernio &#x60;postId&#x60;, which resolves through the Reddit account connected on the same profile (400 when there is none)  Reddit promotes only posts made by a profile of the ad account: a post by any other author returns 422.  Goals:  - traffic - awareness - conversions - video_views (the post must be a video, 422 otherwise) - lead_generation  conversions and lead_generation need a pixel that already received the event (see &#x60;promotedObject&#x60;).  &#x60;leadGenFormId&#x60; returns 400: Reddit retired its native lead forms, so &#x60;lead_generation&#x60; sends people to &#x60;linkUrl&#x60; and optimizes toward the pixel&#39;s Lead event.  Each boost creates a campaign, an ad group carrying the budget, the targeting and the bid, and the ad. &#x60;bidStrategy&#x60; sets the ad group&#39;s bid:  - LOWEST_COST_WITHOUT_CAP (or omitted): automatic bidding (BIDLESS) - LOWEST_COST_WITH_BID_CAP: MANUAL_BIDDING with &#x60;bidAmount&#x60; as the bid - COST_CAP: MAXIMIZE_VOLUME with &#x60;bidAmount&#x60; as the cap - Any other strategy returns 422 before anything is created.  ### Messaging boosts (Meta)  Use &#x60;goal: engagement&#x60; with one of these CTAs:  - &#x60;callToAction: WHATSAPP_MESSAGE&#x60;: implies WHATSAPP - &#x60;MESSAGE_PAGE&#x60;: implies MESSENGER - &#x60;INSTAGRAM_MESSAGE&#x60;: implies INSTAGRAM_DIRECT  &#x60;destinationType&#x60; alone does not select a messaging CTA. Omit &#x60;linkUrl&#x60; only for messaging CTAs. Plain link CTAs keep their goal and link behavior when combined with an independent &#x60;destinationType&#x60;.  The campaign uses OUTCOME_ENGAGEMENT and the ad set uses CONVERSATIONS with the promoted Page. Optional &#x60;whatsappPhoneNumber&#x60; selects a number already paired with that Page.  Conflicting CTA/destination, instant form, goal, or optimizationGoal inputs return 400. Attach requires the target ad set destination to match.  Existing post references preserve social proof. An Instagram reel rejected by Meta is not re-uploaded as a new post for a messaging boost.  ### Retries  Boosts are NOT idempotent and can take minutes when Meta requires re-hosting an Instagram video, so do not retry on client timeout.  Send an Idempotency-Key header to make retries safe: same key and body replays the original 201, and distinct keys always create distinct ads.  Without the header, an identical request is treated as a retry:  - While one is in flight it returns 409. - Within 10 minutes of a completed boost it returns the already-created ad instead of creating another.  To intentionally duplicate an ad, send distinct Idempotency-Keys (or vary the body, e.g. the name). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        BoostPostRequest boostPostRequest = new BoostPostRequest(); // BoostPostRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. 
        try {
            ApiResponse<BoostPost200Response> response = apiInstance.boostPostWithHttpInfo(boostPostRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#boostPost");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **boostPostRequest** | [**BoostPostRequest**](BoostPostRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  | [optional] |

### Return type

ApiResponse<[**BoostPost200Response**](BoostPost200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | validateOnly dry-run passed (Meta), nothing was created |  -  |
| **201** | Ad created |  -  |
| **400** | Missing required fields or invalid values, &#x60;validateOnly: true&#x60; outside Meta, &#x60;dryRun&#x60; sent, or a Meta validateOnly validation failure (verbatim) |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **429** | Meta only (code &#x60;rate_limited&#x60;). Meta puts a security hold lasting days (code 31, subcode 3858385, \&quot;Please authenticate your account\&quot;) on ad accounts that receive bursts of ad writes, and it counts &#x60;validateOnly&#x60; checks as writes.  To keep integrations out of that hold, Zernio:  - runs creates for one Meta ad account one at a time (a parallel request waits up to 60 seconds for its turn); - allows at most 30 creates per ad account in any rolling 5 minutes, &#x60;validateOnly&#x60; included.  A 429 here means one of the two was hit: wait &#x60;Retry-After&#x60; seconds and send creates for that ad account sequentially. Other ad accounts are not affected.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |
| **403** | Ads access required. Legacy plans need the Ads add-on; it is included by default on usage-based plans. Also returned with these codes:  - &#x60;ads_allowance_exceeded&#x60;: the team has no payment method on file and has reached the 500 free live ads. Add a card to resume. - &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;. - &#x60;ad_account_not_selected&#x60; fix: add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection), or use a connection that has it selected. - &#x60;insufficient_permissions&#x60;: the Facebook user behind the token lacks the Advertise permission on the Meta ad account, or the token lacks &#x60;ads_management&#x60; (Meta subcode 2490585, 2490591 or 4841020; see &#x60;ErrorResponse.details&#x60;).  |  -  |
| **409** | The account may also be inactive or need reconnection (code ads_connection_required). Reconnect it and read GET /v1/accounts for its current ID before retrying. An identical boost request is already in progress (with or without an Idempotency-Key). Wait for it to finish instead of retrying.  |  -  |
| **422** | Returned with one of these codes:  - &#x60;ads_connection_required&#x60;: platform ads connection required (TikTok Ads, X Ads), missing linked account, or (for TikTok) the connected TikTok user is not authorized as an Identity on the target advertiser. The message includes the actionable \&quot;TikTok Ads Manager → Assets → Identity\&quot; remediation step. - &#x60;idempotency_key_reused&#x60;: an Idempotency-Key was reused with a different request body. - &#x60;ad_account_unusable&#x60;: Meta refuses writes on the ad account because its status is ineligible to manage ads (see &#x60;ErrorResponse.details&#x60;).  |  -  |
| **503** | An upstream service or database is temporarily unavailable. Retry after the indicated delay. A timed-out write may have completed upstream; check its outcome before resubmitting. |  * Retry-After - Minimum delay in seconds before retrying. <br>  |


## bulkUpdateAdCampaignStatus

> BulkUpdateAdCampaignStatus200Response bulkUpdateAdCampaignStatus(bulkUpdateAdCampaignStatusRequest)

Pause or resume many campaigns

Pauses or resumes up to 50 campaigns in one call, with a separate result per campaign so one failure does not block the rest.  Each campaign is updated concurrently, and the response contains a per-campaign result so a single bad row does not fail the whole batch.  Each campaign is read, written and re-read exactly as PUT /v1/ads/campaigns/{campaignId}/status describes: only the campaign&#39;s own switch is written, never its ad sets&#39; or ads&#39;.  &#x60;updated&#x60; / &#x60;skipped&#x60; count campaigns. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        BulkUpdateAdCampaignStatusRequest bulkUpdateAdCampaignStatusRequest = new BulkUpdateAdCampaignStatusRequest(); // BulkUpdateAdCampaignStatusRequest | 
        try {
            BulkUpdateAdCampaignStatus200Response result = apiInstance.bulkUpdateAdCampaignStatus(bulkUpdateAdCampaignStatusRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#bulkUpdateAdCampaignStatus");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **bulkUpdateAdCampaignStatusRequest** | [**BulkUpdateAdCampaignStatusRequest**](BulkUpdateAdCampaignStatusRequest.md)|  | |

### Return type

[**BulkUpdateAdCampaignStatus200Response**](BulkUpdateAdCampaignStatus200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-campaign results |  -  |
| **400** | Invalid input |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |

## bulkUpdateAdCampaignStatusWithHttpInfo

> ApiResponse<BulkUpdateAdCampaignStatus200Response> bulkUpdateAdCampaignStatus bulkUpdateAdCampaignStatusWithHttpInfo(bulkUpdateAdCampaignStatusRequest)

Pause or resume many campaigns

Pauses or resumes up to 50 campaigns in one call, with a separate result per campaign so one failure does not block the rest.  Each campaign is updated concurrently, and the response contains a per-campaign result so a single bad row does not fail the whole batch.  Each campaign is read, written and re-read exactly as PUT /v1/ads/campaigns/{campaignId}/status describes: only the campaign&#39;s own switch is written, never its ad sets&#39; or ads&#39;.  &#x60;updated&#x60; / &#x60;skipped&#x60; count campaigns. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        BulkUpdateAdCampaignStatusRequest bulkUpdateAdCampaignStatusRequest = new BulkUpdateAdCampaignStatusRequest(); // BulkUpdateAdCampaignStatusRequest | 
        try {
            ApiResponse<BulkUpdateAdCampaignStatus200Response> response = apiInstance.bulkUpdateAdCampaignStatusWithHttpInfo(bulkUpdateAdCampaignStatusRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#bulkUpdateAdCampaignStatus");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **bulkUpdateAdCampaignStatusRequest** | [**BulkUpdateAdCampaignStatusRequest**](BulkUpdateAdCampaignStatusRequest.md)|  | |

### Return type

ApiResponse<[**BulkUpdateAdCampaignStatus200Response**](BulkUpdateAdCampaignStatus200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-campaign results |  -  |
| **400** | Invalid input |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Returned with code &#x60;ads_allowance_exceeded&#x60; when the team has no payment method on file and has reached the 500 free live ads: add a card to resume. |  -  |


## createAdCampaign

> CreateAdCampaign200Response createAdCampaign(createAdCampaignRequest, idempotencyKey)

Create a standalone campaign

Creates an empty campaign, paused, so you can add ad sets and ads to it afterwards.  Creates a campaign WITHOUT its first ad set / ad, on the platform of the given &#x60;accountId&#x60;. Ad sets join it later via &#x60;existingCampaignId&#x60; on the create endpoints.  Created &#x60;PAUSED&#x60; (TikTok &#x60;DISABLE&#x60;) unless &#x60;status: ACTIVE&#x60; where the platform supports it.  **Idempotency:** send an &#x60;Idempotency-Key&#x60; header to make retries safe.  ### Field support  - &#x60;specialAdCategories&#x60;: Meta-only (400 elsewhere). - &#x60;bidStrategy&#x60;: Meta and Google (400 elsewhere). Google also accepts &#x60;portfolioBidStrategyId&#x60; instead. - Budget: Google, X and OpenAI require one (422 without one). OpenAI accepts daily or lifetime, Google only &#x60;budgetType: daily&#x60;.  ### Platform notes  - Meta: a budget here is campaign-level (CBO) by definition. Omit it for ABO (each ad set carries its own budget). - OpenAI: &#x60;goal&#x60; sets the campaign objective, and &#x60;conversions&#x60; needs an active standard conversion event on the account. - Reddit: see below. - LinkedIn: creates the campaign GROUP (our campaign level) and rejects a budget, which lives on the campaign (ad set) level there. It comes back &#x60;status: DRAFT&#x60;.  ### Reddit  &#x60;goal&#x60; is one of traffic, awareness, conversions, video_views or lead_generation (422 otherwise). The budget is optional.  - With a budget, the campaign uses Reddit&#39;s campaign budget optimization and carries the pixel (see &#x60;promotedObject&#x60;, which then needs &#x60;customEventType&#x60; for &#x60;conversions&#x60;). The budget is daily or lifetime; a lifetime budget needs &#x60;endDate&#x60; (400 otherwise). - &#x60;startDate&#x60; / &#x60;endDate&#x60; set the campaign&#39;s schedule and need that campaign budget (400 without one). - Without a budget, each ad set carries its own budget and dates. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        CreateAdCampaignRequest createAdCampaignRequest = new CreateAdCampaignRequest(); // CreateAdCampaignRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key. 
        try {
            CreateAdCampaign200Response result = apiInstance.createAdCampaign(createAdCampaignRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#createAdCampaign");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createAdCampaignRequest** | [**CreateAdCampaignRequest**](CreateAdCampaignRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key.  | [optional] |

### Return type

[**CreateAdCampaign200Response**](CreateAdCampaign200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | Campaign validation passed without creating a campaign. |  -  |
| **201** | Campaign created |  -  |
| **400** | Invalid input, or Meta rejected the create |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **501** | &#x60;validateOnly: true&#x60; outside Meta, or campaign-only creation on a platform that does not support it. Carries code &#x60;feature_not_available&#x60;. |  -  |

## createAdCampaignWithHttpInfo

> ApiResponse<CreateAdCampaign200Response> createAdCampaign createAdCampaignWithHttpInfo(createAdCampaignRequest, idempotencyKey)

Create a standalone campaign

Creates an empty campaign, paused, so you can add ad sets and ads to it afterwards.  Creates a campaign WITHOUT its first ad set / ad, on the platform of the given &#x60;accountId&#x60;. Ad sets join it later via &#x60;existingCampaignId&#x60; on the create endpoints.  Created &#x60;PAUSED&#x60; (TikTok &#x60;DISABLE&#x60;) unless &#x60;status: ACTIVE&#x60; where the platform supports it.  **Idempotency:** send an &#x60;Idempotency-Key&#x60; header to make retries safe.  ### Field support  - &#x60;specialAdCategories&#x60;: Meta-only (400 elsewhere). - &#x60;bidStrategy&#x60;: Meta and Google (400 elsewhere). Google also accepts &#x60;portfolioBidStrategyId&#x60; instead. - Budget: Google, X and OpenAI require one (422 without one). OpenAI accepts daily or lifetime, Google only &#x60;budgetType: daily&#x60;.  ### Platform notes  - Meta: a budget here is campaign-level (CBO) by definition. Omit it for ABO (each ad set carries its own budget). - OpenAI: &#x60;goal&#x60; sets the campaign objective, and &#x60;conversions&#x60; needs an active standard conversion event on the account. - Reddit: see below. - LinkedIn: creates the campaign GROUP (our campaign level) and rejects a budget, which lives on the campaign (ad set) level there. It comes back &#x60;status: DRAFT&#x60;.  ### Reddit  &#x60;goal&#x60; is one of traffic, awareness, conversions, video_views or lead_generation (422 otherwise). The budget is optional.  - With a budget, the campaign uses Reddit&#39;s campaign budget optimization and carries the pixel (see &#x60;promotedObject&#x60;, which then needs &#x60;customEventType&#x60; for &#x60;conversions&#x60;). The budget is daily or lifetime; a lifetime budget needs &#x60;endDate&#x60; (400 otherwise). - &#x60;startDate&#x60; / &#x60;endDate&#x60; set the campaign&#39;s schedule and need that campaign budget (400 without one). - Without a budget, each ad set carries its own budget and dates. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        CreateAdCampaignRequest createAdCampaignRequest = new CreateAdCampaignRequest(); // CreateAdCampaignRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key. 
        try {
            ApiResponse<CreateAdCampaign200Response> response = apiInstance.createAdCampaignWithHttpInfo(createAdCampaignRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#createAdCampaign");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createAdCampaignRequest** | [**CreateAdCampaignRequest**](CreateAdCampaignRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key.  | [optional] |

### Return type

ApiResponse<[**CreateAdCampaign200Response**](CreateAdCampaign200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | Campaign validation passed without creating a campaign. |  -  |
| **201** | Campaign created |  -  |
| **400** | Invalid input, or Meta rejected the create |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **501** | &#x60;validateOnly: true&#x60; outside Meta, or campaign-only creation on a platform that does not support it. Carries code &#x60;feature_not_available&#x60;. |  -  |


## createAdSet

> CreateAdSet201Response createAdSet(createAdSetRequest, idempotencyKey)

Create a standalone ad group

Creates an empty ad group under an existing campaign, ready for ads to be added later.  The ad group is created WITHOUT an ad (Google Ads compliance row C.190). Ads join it later via &#x60;adSetId&#x60; on POST /v1/ads/create. Supports Google Ads and Reddit Ads; every other platform returns 501.  **Reddit Ads** (&#x60;platform: reddit&#x60;)  - &#x60;adAccountId&#x60; (the Reddit ad account id) is required and must be a selected ad account of the connection (403 otherwise). - When the campaign has no campaign budget, send &#x60;budgetAmount&#x60; + &#x60;budgetType&#x60; (a lifetime budget needs &#x60;endDate&#x60;). - The ad group is optimized for the campaign&#39;s objective. &#x60;promotedObject.customEventType&#x60; is required on a conversions campaign, and the pixel must have received that event, else 422. - It bids with &#x60;bidStrategy&#x60;/&#x60;bidAmount&#x60; like POST /v1/ads/create. - Under campaign budget optimization the ad group takes the campaign&#39;s bid, goal type, optimization event and pixel, and bid fields return 400. - The ad group must start no earlier than a future campaign start and end no later than the campaign end (400 otherwise). - &#x60;targeting&#x60; takes the same targeting object as the other ad endpoints (no geo defaults to the US). - A campaign of another ad account returns 404, a Reddit Max campaign 422. - &#x60;maxCpc&#x60; and &#x60;customerId&#x60; are Google only (400 on Reddit), and the Reddit fields return 400 on Google.  ### After creation  Created &#x60;PAUSED&#x60; unless &#x60;status: ACTIVE&#x60;. The new ad group has no ad yet, so it will not appear in GET /v1/ads/tree (built purely from &#x60;ads&#x60; rows) until one is added. Use GET /v1/ads/ad-sets to see it in the meantime.  It can be read, edited and deleted through &#x60;/v1/ads/ad-sets/{adSetId}&#x60; right away (targeting, schedule, name, &#x60;status&#x60;, &#x60;budget&#x60; and bid fields). A budget on an ad group that spends its campaign budget returns 422.  **Idempotency:** send an &#x60;Idempotency-Key&#x60; header to make retries safe. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        CreateAdSetRequest createAdSetRequest = new CreateAdSetRequest(); // CreateAdSetRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key. 
        try {
            CreateAdSet201Response result = apiInstance.createAdSet(createAdSetRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#createAdSet");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createAdSetRequest** | [**CreateAdSetRequest**](CreateAdSetRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key.  | [optional] |

### Return type

[**CreateAdSet201Response**](CreateAdSet201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **201** | Ad group created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Forbidden. The code says why:  - &#x60;ads_allowance_exceeded&#x60;: the team has no payment method on file and has reached the 500 free live ads. Add a card to resume. - &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the ad account this request targets is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix &#x60;ad_account_not_selected&#x60;, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **422** | Reddit: the campaign is a Reddit Max campaign, the ad account has no pixel, or the pixel never received the conversion event |  -  |
| **501** | Only supported on Google Ads and Reddit Ads |  -  |

## createAdSetWithHttpInfo

> ApiResponse<CreateAdSet201Response> createAdSet createAdSetWithHttpInfo(createAdSetRequest, idempotencyKey)

Create a standalone ad group

Creates an empty ad group under an existing campaign, ready for ads to be added later.  The ad group is created WITHOUT an ad (Google Ads compliance row C.190). Ads join it later via &#x60;adSetId&#x60; on POST /v1/ads/create. Supports Google Ads and Reddit Ads; every other platform returns 501.  **Reddit Ads** (&#x60;platform: reddit&#x60;)  - &#x60;adAccountId&#x60; (the Reddit ad account id) is required and must be a selected ad account of the connection (403 otherwise). - When the campaign has no campaign budget, send &#x60;budgetAmount&#x60; + &#x60;budgetType&#x60; (a lifetime budget needs &#x60;endDate&#x60;). - The ad group is optimized for the campaign&#39;s objective. &#x60;promotedObject.customEventType&#x60; is required on a conversions campaign, and the pixel must have received that event, else 422. - It bids with &#x60;bidStrategy&#x60;/&#x60;bidAmount&#x60; like POST /v1/ads/create. - Under campaign budget optimization the ad group takes the campaign&#39;s bid, goal type, optimization event and pixel, and bid fields return 400. - The ad group must start no earlier than a future campaign start and end no later than the campaign end (400 otherwise). - &#x60;targeting&#x60; takes the same targeting object as the other ad endpoints (no geo defaults to the US). - A campaign of another ad account returns 404, a Reddit Max campaign 422. - &#x60;maxCpc&#x60; and &#x60;customerId&#x60; are Google only (400 on Reddit), and the Reddit fields return 400 on Google.  ### After creation  Created &#x60;PAUSED&#x60; unless &#x60;status: ACTIVE&#x60;. The new ad group has no ad yet, so it will not appear in GET /v1/ads/tree (built purely from &#x60;ads&#x60; rows) until one is added. Use GET /v1/ads/ad-sets to see it in the meantime.  It can be read, edited and deleted through &#x60;/v1/ads/ad-sets/{adSetId}&#x60; right away (targeting, schedule, name, &#x60;status&#x60;, &#x60;budget&#x60; and bid fields). A budget on an ad group that spends its campaign budget returns 422.  **Idempotency:** send an &#x60;Idempotency-Key&#x60; header to make retries safe. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        CreateAdSetRequest createAdSetRequest = new CreateAdSetRequest(); // CreateAdSetRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key. 
        try {
            ApiResponse<CreateAdSet201Response> response = apiInstance.createAdSetWithHttpInfo(createAdSetRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#createAdSet");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createAdSetRequest** | [**CreateAdSetRequest**](CreateAdSetRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key.  | [optional] |

### Return type

ApiResponse<[**CreateAdSet201Response**](CreateAdSet201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **201** | Ad group created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Forbidden. The code says why:  - &#x60;ads_allowance_exceeded&#x60;: the team has no payment method on file and has reached the 500 free live ads. Add a card to resume. - &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the ad account this request targets is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix &#x60;ad_account_not_selected&#x60;, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **422** | Reddit: the campaign is a Reddit Max campaign, the ad account has no pixel, or the pixel never received the conversion event |  -  |
| **501** | Only supported on Google Ads and Reddit Ads |  -  |


## createBidStrategy

> CreateBidStrategy201Response createBidStrategy(createBidStrategyRequest)

Create portfolio bid strategy

Creates a Google Ads bid strategy that several campaigns can share, such as one target CPA or ROAS.  Attach it to a campaign with &#x60;portfolioBidStrategyId&#x60; on POST /v1/ads/create, PUT /v1/ads/campaigns/{campaignId}, or PUT /v1/ads/ad-sets/{adSetId}. Attaching a strategy aligned to a shared budget fails there with a 400 (Google&#39;s &#x60;BIDDING_STRATEGY_AND_BUDGET_MUST_BE_ALIGNED&#x60;); this is not retryable. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        CreateBidStrategyRequest createBidStrategyRequest = new CreateBidStrategyRequest(); // CreateBidStrategyRequest | 
        try {
            CreateBidStrategy201Response result = apiInstance.createBidStrategy(createBidStrategyRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#createBidStrategy");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createBidStrategyRequest** | [**CreateBidStrategyRequest**](CreateBidStrategyRequest.md)|  | |

### Return type

[**CreateBidStrategy201Response**](CreateBidStrategy201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **201** | Bid strategy created |  -  |
| **400** | Invalid input, or Google rejected the strategy (e.g. shared-budget alignment). The message carries Google&#39;s error. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **422** | No Google Ads customer accounts on this connection. Reconnect Google Ads. |  -  |
| **429** | Google Ads operations budget exhausted; retry later. |  -  |
| **501** | Only available on Google Ads accounts |  -  |

## createBidStrategyWithHttpInfo

> ApiResponse<CreateBidStrategy201Response> createBidStrategy createBidStrategyWithHttpInfo(createBidStrategyRequest)

Create portfolio bid strategy

Creates a Google Ads bid strategy that several campaigns can share, such as one target CPA or ROAS.  Attach it to a campaign with &#x60;portfolioBidStrategyId&#x60; on POST /v1/ads/create, PUT /v1/ads/campaigns/{campaignId}, or PUT /v1/ads/ad-sets/{adSetId}. Attaching a strategy aligned to a shared budget fails there with a 400 (Google&#39;s &#x60;BIDDING_STRATEGY_AND_BUDGET_MUST_BE_ALIGNED&#x60;); this is not retryable. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        CreateBidStrategyRequest createBidStrategyRequest = new CreateBidStrategyRequest(); // CreateBidStrategyRequest | 
        try {
            ApiResponse<CreateBidStrategy201Response> response = apiInstance.createBidStrategyWithHttpInfo(createBidStrategyRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#createBidStrategy");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createBidStrategyRequest** | [**CreateBidStrategyRequest**](CreateBidStrategyRequest.md)|  | |

### Return type

ApiResponse<[**CreateBidStrategy201Response**](CreateBidStrategy201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **201** | Bid strategy created |  -  |
| **400** | Invalid input, or Google rejected the strategy (e.g. shared-budget alignment). The message carries Google&#39;s error. |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **422** | No Google Ads customer accounts on this connection. Reconnect Google Ads. |  -  |
| **429** | Google Ads operations budget exhausted; retry later. |  -  |
| **501** | Only available on Google Ads accounts |  -  |


## createGoogleAssetGroup

> CreateGoogleAssetGroup200Response createGoogleAssetGroup(campaignId, createGoogleAssetGroupRequest)

Create a Performance Max asset group

Adds an asset group with its assets and optional product targeting to a Performance Max campaign, or just validates it without creating anything.  The group, any new assets, their links and an optional listing-group tree are created in one atomic request, so Google checks the asset minimums (for non-retail campaigns) against the whole set. Created PAUSED unless status is ENABLED. validateOnly: true runs Google&#39;s validation without creating anything. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Google Ads campaign id.
        CreateGoogleAssetGroupRequest createGoogleAssetGroupRequest = new CreateGoogleAssetGroupRequest(); // CreateGoogleAssetGroupRequest | 
        try {
            CreateGoogleAssetGroup200Response result = apiInstance.createGoogleAssetGroup(campaignId, createGoogleAssetGroupRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#createGoogleAssetGroup");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Google Ads campaign id. | |
| **createGoogleAssetGroupRequest** | [**CreateGoogleAssetGroupRequest**](CreateGoogleAssetGroupRequest.md)|  | |

### Return type

[**CreateGoogleAssetGroup200Response**](CreateGoogleAssetGroup200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Asset group created. |  -  |
| **200** | validateOnly request accepted by Google. Nothing was created. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **404** | Resource not found |  -  |
| **422** | Google Ads connection needs reconnecting. |  -  |
| **429** | Google quota or the Zernio Google operations burst limit is exhausted. |  -  |
| **501** | Campaign is not on Google Ads. |  -  |

## createGoogleAssetGroupWithHttpInfo

> ApiResponse<CreateGoogleAssetGroup200Response> createGoogleAssetGroup createGoogleAssetGroupWithHttpInfo(campaignId, createGoogleAssetGroupRequest)

Create a Performance Max asset group

Adds an asset group with its assets and optional product targeting to a Performance Max campaign, or just validates it without creating anything.  The group, any new assets, their links and an optional listing-group tree are created in one atomic request, so Google checks the asset minimums (for non-retail campaigns) against the whole set. Created PAUSED unless status is ENABLED. validateOnly: true runs Google&#39;s validation without creating anything. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Google Ads campaign id.
        CreateGoogleAssetGroupRequest createGoogleAssetGroupRequest = new CreateGoogleAssetGroupRequest(); // CreateGoogleAssetGroupRequest | 
        try {
            ApiResponse<CreateGoogleAssetGroup200Response> response = apiInstance.createGoogleAssetGroupWithHttpInfo(campaignId, createGoogleAssetGroupRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#createGoogleAssetGroup");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Google Ads campaign id. | |
| **createGoogleAssetGroupRequest** | [**CreateGoogleAssetGroupRequest**](CreateGoogleAssetGroupRequest.md)|  | |

### Return type

ApiResponse<[**CreateGoogleAssetGroup200Response**](CreateGoogleAssetGroup200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Asset group created. |  -  |
| **200** | validateOnly request accepted by Google. Nothing was created. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **404** | Resource not found |  -  |
| **422** | Google Ads connection needs reconnecting. |  -  |
| **429** | Google quota or the Zernio Google operations burst limit is exhausted. |  -  |
| **501** | Campaign is not on Google Ads. |  -  |


## createSharedBudget

> CreateSharedBudget201Response createSharedBudget(createSharedBudgetRequest)

Create a shared budget

Creates a daily Google Ads budget that several campaigns can share.  Creates a daily shared campaign budget (&#x60;explicitly_shared: true&#x60;, standard delivery) that several campaigns can draw from. A lifetime budget returns 422, like every Google budget. Google refuses some bidding strategies on a shared budget; that error surfaces when a campaign is moved onto it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        CreateSharedBudgetRequest createSharedBudgetRequest = new CreateSharedBudgetRequest(); // CreateSharedBudgetRequest | 
        try {
            CreateSharedBudget201Response result = apiInstance.createSharedBudget(createSharedBudgetRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#createSharedBudget");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createSharedBudgetRequest** | [**CreateSharedBudgetRequest**](CreateSharedBudgetRequest.md)|  | |

### Return type

[**CreateSharedBudget201Response**](CreateSharedBudget201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Shared budget created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **422** | Lifetime budget requested. |  -  |
| **501** | Only available on Google Ads accounts |  -  |

## createSharedBudgetWithHttpInfo

> ApiResponse<CreateSharedBudget201Response> createSharedBudget createSharedBudgetWithHttpInfo(createSharedBudgetRequest)

Create a shared budget

Creates a daily Google Ads budget that several campaigns can share.  Creates a daily shared campaign budget (&#x60;explicitly_shared: true&#x60;, standard delivery) that several campaigns can draw from. A lifetime budget returns 422, like every Google budget. Google refuses some bidding strategies on a shared budget; that error surfaces when a campaign is moved onto it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        CreateSharedBudgetRequest createSharedBudgetRequest = new CreateSharedBudgetRequest(); // CreateSharedBudgetRequest | 
        try {
            ApiResponse<CreateSharedBudget201Response> response = apiInstance.createSharedBudgetWithHttpInfo(createSharedBudgetRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#createSharedBudget");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createSharedBudgetRequest** | [**CreateSharedBudgetRequest**](CreateSharedBudgetRequest.md)|  | |

### Return type

ApiResponse<[**CreateSharedBudget201Response**](CreateSharedBudget201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Shared budget created |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **422** | Lifetime budget requested. |  -  |
| **501** | Only available on Google Ads accounts |  -  |


## createStandaloneAd

> CreateStandaloneAd200Response createStandaloneAd(createStandaloneAdRequest, idempotencyKey)

Create standalone ad

Creates a paid ad with your own creative, building the campaign and ad set it needs or adding it to existing ones.  Works across Meta, Google Ads, Pinterest, TikTok, X, LinkedIn, OpenAI Ads (ChatGPT Ads) and Reddit Ads. Per-platform required fields, budget minimums, and video-ad rules are documented on each property below.  ### Request shapes  The body selects one of these mutually exclusive shapes:  - Legacy single-creative shape (all platforms, the default). - Meta-only multi-creative shape via the creatives array: one ad set with N ads sharing budget and targeting. - Attach shape via adSetId: adds one new ad to an existing ad set, inheriting its budget, targeting, and schedule (Meta, Google Ads, TikTok, and LinkedIn).  On LinkedIn, adSetId in the attach shape is the existing Campaign id, and the budget, schedule, targeting and bidding fields must be omitted. &#x60;goal&#x60; may be omitted too (taken from the Campaign&#39;s objective), and the created ad&#39;s &#x60;targeting&#x60; echoes the Campaign&#39;s audience.  ### Google Performance Max  Set &#x60;campaignType: \&quot;pmax\&quot;&#x60; and supply &#x60;assetGroup&#x60; with text, images by role, business name and finalUrl. This creates a daily budget, PAUSED campaign and asset group atomically.  - &#x60;validateOnly: true&#x60; validates the complete request with Google without creating or persisting resources. - Read assets with &#x60;GET /v1/ads/campaigns/{campaignId}/asset-groups&#x60;. - The logo is required; video is optional via &#x60;assetGroup.youtubeVideoId&#x60;. - Brand guidelines are disabled at creation. - All supplied asset links are validated together against Google&#39;s minimum asset requirements. - PMax rejects ACTIVE creation, portfolio bidding, bid caps, legacy creative fields and attach shapes. - Geo and language targeting are supported; omitted geo targets all locations. - PMax does not require top-level goal, headline, body or linkUrl.  Supported bidding:  - Omitted or LOWEST_COST_WITHOUT_CAP: Maximize Conversions. - COST_CAP plus bidAmount: target CPA. - LOWEST_COST_WITH_MIN_ROAS plus roasAverageFloor: Maximize Conversion Value with target ROAS.  ### Google Demand Gen  Set &#x60;campaignType: \&quot;demand_gen\&quot;&#x60; and supply &#x60;demandGen&#x60;. One atomic request creates a daily budget, PAUSED campaign, one ad group and one ad. The ad is:  - a multi-asset image ad by default; - a video responsive ad when &#x60;demandGen.youtubeVideoIds&#x60; is sent; - a carousel ad (2 to 10 cards) when &#x60;demandGen.carouselCards&#x60; is sent.  Targeting and validation:  - Geo (countries, regions, cities, zips, metros) and languages go on the ad group, as Demand Gen requires. - &#x60;demandGen.channels&#x60; sets the ad group&#39;s channel controls. - &#x60;demandGen.audience&#x60; builds a Google Audience (user lists, interests, custom audiences, age ranges, genders) attached to the ad group, or &#x60;demandGen.audienceId&#x60; attaches an existing one. - &#x60;validateOnly: true&#x60; validates everything with Google without creating resources.  Supported bidding:  - Omitted or LOWEST_COST_WITHOUT_CAP: Maximize Conversions. - COST_CAP plus bidAmount: target CPA. - LOWEST_COST_WITH_MIN_ROAS plus roasAverageFloor: target ROAS. - LOWEST_COST_WITH_BID_CAP plus bidAmount: target CPC.  The created ad carries the native &#x60;platformCampaignId&#x60;, &#x60;platformAdSetId&#x60; (ad group) and &#x60;platformAdId&#x60;. After creation:  - Activate with PUT /v1/ads/campaigns/{campaignId}/status. - Edit budget, bidding and name with the regular campaign endpoints. - Edit creative, channels, audience and ad group targeting with PUT /v1/ads/{adId} (&#x60;demandGen&#x60;, &#x60;targeting&#x60;).  To grow an existing Demand Gen campaign, send one of these (neither takes budget, bidding or schedule fields; both support &#x60;validateOnly&#x60;):  - &#x60;existingCampaignId&#x60;: adds a PAUSED ad group, with its own geo, languages, channels and audience, plus its ad. - &#x60;adSetId&#x60;: adds a PAUSED ad to that ad group.  ### Meta creative options  Meta accepts &#x60;creativeFeatures&#x60; on the single and attach shapes and as defaults for &#x60;creatives[]&#x60;; an item replaces the whole feature map.  &#x60;promotion&#x60; is not supported on any shape, and any object is rejected with 400.  Reusing &#x60;existingCreativeId&#x60; uses the existing creative settings instead of new settings. Requested settings are persisted for lists, exports, and default ad-detail reads.  ### Meta required fields per shape  A missing field is a 400 naming it in &#x60;param&#x60;.  - Every shape that builds a new ad set (no &#x60;adSetId&#x60;, &#x60;existingCampaignId&#x60; or &#x60;buyingType: \&quot;RESERVED\&quot;&#x60;): &#x60;budgetAmount&#x60;. &#x60;budgetType&#x60; defaults to daily, and a lifetime budget without &#x60;endDate&#x60; ends 7 days after it starts (see &#x60;appliedDefaults&#x60;). - Single image or video (the default), also with &#x60;adSetId&#x60;: &#x60;headline&#x60; (max 255), &#x60;body&#x60;, &#x60;callToAction&#x60;, and exactly one of &#x60;imageUrl&#x60; / &#x60;video&#x60;. A catalog template creative takes none, and ignores and does not upload any sent. - Single image or video also needs &#x60;linkUrl&#x60;, unless the goal is &#x60;lead_generation&#x60; or &#x60;page_visits&#x60; or &#x60;leadGenFormId&#x60; is set. - &#x60;bodies[]&#x60; / &#x60;headlines[]&#x60; text variations: &#x60;body&#x60;, one list with 2+ items, &#x60;callToAction&#x60;, &#x60;imageUrl&#x60; or &#x60;video&#x60;, and &#x60;linkUrl&#x60; unless the goal is &#x60;lead_generation&#x60; or &#x60;leadGenFormId&#x60; is set. &#x60;headline&#x60; is not required. - &#x60;placementAssets&#x60;: &#x60;headline&#x60;, &#x60;body&#x60;, &#x60;callToAction&#x60;, and &#x60;linkUrl&#x60; with the same exemptions as the single shape; the media comes from &#x60;placementAssets&#x60;. - &#x60;carouselCards&#x60;: &#x60;body&#x60;, &#x60;callToAction&#x60;, and &#x60;linkUrl&#x60; unless the goal is &#x60;lead_generation&#x60; or &#x60;leadGenFormId&#x60; is set. &#x60;headline&#x60; is not required. - &#x60;creatives[]&#x60;: per entry &#x60;headline&#x60;, &#x60;body&#x60;, &#x60;callToAction&#x60;, &#x60;imageUrl&#x60; or &#x60;video&#x60;, and &#x60;linkUrl&#x60; unless the goal is &#x60;lead_generation&#x60;. Top-level &#x60;body&#x60; is not required. - &#x60;dynamicCreative&#x60;: &#x60;imageUrls&#x60; or &#x60;videoUrls&#x60;, &#x60;callToActionTypes&#x60;, and &#x60;linkUrls&#x60; unless the goal is &#x60;lead_generation&#x60;. Top-level &#x60;body&#x60; is not required. - &#x60;existingCreativeId&#x60;: no creative fields. - Goal &#x60;page_likes&#x60;: &#x60;body&#x60; only. - Goal &#x60;lead_generation&#x60; always needs &#x60;leadGenFormId&#x60;, except with &#x60;existingCreativeId&#x60;.  ### Meta activation  Meta builds the campaign, ad set and ads PAUSED and switches the requested levels to ACTIVE as the last step.  When Meta refuses that switch, or the connection drops, after Zernio&#39;s retries, the request still answers 201 and nothing is deleted:  - The refused level and every level below it stay PAUSED. - Levels above it that already went ACTIVE stay ACTIVE. - The ad comes back with &#x60;status: paused&#x60; and its &#x60;configuredStatus&#x60; as read back from Meta. - A switch Meta applied although its answer was lost counts as ACTIVE, since Zernio reads the status back first.  &#x60;message&#x60; says not everything is ACTIVE. &#x60;warnings&#x60; carries one entry starting with &#x60;activation_failed:&#x60; that quotes Meta&#39;s code, subcode and message, and names what was kept PAUSED and what was switched ACTIVE.  That warning also lists the calls that switch the PAUSED ones on later, in this order, with status &#x60;active&#x60;:  1. PUT /v1/ads/campaigns/{campaignId}/status 2. PUT /v1/ads/ad-sets/{adSetId}/status 3. PUT /v1/ads/{adId}/status  On the &#x60;creatives[]&#x60; shape, only the ads Meta refused stay PAUSED when the campaign and ad set went through. A Reach and Frequency ad is created ACTIVE and is never listed as kept PAUSED. With an &#x60;Idempotency-Key&#x60;, a retry replays this 201.  ### LinkedIn  LinkedIn creates a Single Image or Single Video Ad backed by a Direct Sponsored Content \&quot;dark post\&quot; authored by a Company Page (see &#x60;organizationId&#x60;).  - Supported goals: engagement, traffic, awareness, and video_views. - Video ads use the &#x60;video&#x60; field; video_views requires a video. - Traffic ads require &#x60;linkUrl&#x60;.  ### Reddit Ads  Use the &#x60;accountId&#x60; of a &#x60;redditads&#x60; connection and an &#x60;adAccountId&#x60; like &#x60;a2_abc123&#x60;. Zernio creates a campaign, an ad group carrying the budget, schedule, targeting and pixel, and an ad running a new promoted post. The post is authored by the ad account&#39;s first profile (422 when it has none).  The creative format follows the body:  - &#x60;carouselCards&#x60;: a carousel. - &#x60;video&#x60;: a video ad. - &#x60;imageUrl&#x60;: an image ad. - None of them: a text ad, which cannot link out (&#x60;linkUrl&#x60; is a 400 there; &#x60;body&#x60; is required).  Only the legacy single-creative shape is available: &#x60;creatives[]&#x60;, &#x60;adSetId&#x60;, &#x60;existingCampaignId&#x60; and &#x60;validateOnly&#x60; are refused.  Reddit throttling surfaces as 429 &#x60;rate_limited&#x60; with &#x60;platform: reddit&#x60;; retry after a delay. To promote an existing Reddit post, use POST /v1/ads/boost.  ### Idempotency  This endpoint is not idempotent at the platform level: a blind retry creates a second campaign/ad set/ad. Send an &#x60;Idempotency-Key&#x60; header to make retries safe.  - The first request with a given key creates the ad and we store the response. - A retry with the same key replays that exact response (with &#x60;Idempotent-Replayed: true&#x60;) instead of creating duplicates. - Reusing a key with a different body returns 422. - A key whose first request is still in flight returns 409 (retry after a short backoff). - If the first request is cut off mid-create (for example by a function timeout), its key can stay in progress and keep returning 409 until it expires. Use a new key to retry sooner, after checking whether the ad was created. - Keys are scoped to your credential and expire after 24h. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        CreateStandaloneAdRequest createStandaloneAdRequest = new CreateStandaloneAdRequest(); // CreateStandaloneAdRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. 
        try {
            CreateStandaloneAd200Response result = apiInstance.createStandaloneAd(createStandaloneAdRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#createStandaloneAd");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createStandaloneAdRequest** | [**CreateStandaloneAdRequest**](CreateStandaloneAdRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  | [optional] |

### Return type

[**CreateStandaloneAd200Response**](CreateStandaloneAd200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | validateOnly dry-run passed, nothing was created |  -  |
| **201** | Ad(s) created |  -  |
| **400** | Missing required fields, invalid values, non-Meta platform used with creatives[] / adSetId, or a Meta validateOnly validation failure (verbatim) |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **429** | Meta only (code &#x60;rate_limited&#x60;). Meta puts a security hold lasting days (code 31, subcode 3858385, \&quot;Please authenticate your account\&quot;) on ad accounts that receive bursts of ad writes, and it counts &#x60;validateOnly&#x60; checks as writes.  To keep integrations out of that hold, Zernio:  - runs creates for one Meta ad account one at a time (a parallel request waits up to 60 seconds for its turn); - allows at most 30 creates per ad account in any rolling 5 minutes, &#x60;validateOnly&#x60; included.  A 429 here means one of the two was hit: wait &#x60;Retry-After&#x60; seconds and send creates for that ad account sequentially. Other ad accounts are not affected.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |
| **403** | Ads access required. Legacy plans need the Ads add-on; it is included by default on usage-based plans. Also returned with these codes:  - &#x60;ads_allowance_exceeded&#x60;: the team has no payment method on file and has reached the 500 free live ads. Add a card to resume. - &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;. - &#x60;ad_account_not_selected&#x60;, fix: add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected. - &#x60;insufficient_permissions&#x60;: the Facebook user behind the connection&#39;s token lacks the Advertise permission on the Meta ad account, or the token lacks &#x60;ads_management&#x60; (Meta subcode 2490585, 2490591 or 4841020; see &#x60;ErrorResponse.details&#x60;).  |  -  |
| **422** | Platform ads connection required (TikTok Ads, X Ads) or missing linked account. Also returned:  - With code &#x60;ad_account_unusable&#x60;: Meta refuses writes on the ad account because its status is ineligible to manage ads (see &#x60;ErrorResponse.details&#x60;). - On Reddit: &#x60;video_views&#x60; without a video, or an ad account with no pixel or no profile. - On Reddit, with code &#x60;invalid_resource_state&#x60;: a pixel that never received the event the ad group optimizes toward.  |  -  |
| **501** | The requested option is not supported on this platform: &#x60;validateOnly&#x60; outside Meta and Google Performance Max, or a shape the adapter does not implement. Carries code &#x60;feature_not_available&#x60;.  |  -  |
| **502** | The platform rejected the request, or failed to produce media the ad needs (e.g. Meta generated no poster for an uploaded video when no &#x60;video.thumbnailUrl&#x60; was supplied). An upstream 4xx status is forwarded instead of 502.  - Inspect &#x60;platformError&#x60; for the upstream payload. - Failures we raise carry a &#x60;reason&#x60;; a payload forwarded verbatim from Meta may not. - On the &#x60;creatives[]&#x60; shape, a missing poster also carries &#x60;creativeIndex&#x60; and &#x60;videoUrl&#x60; to identify the entry. - On Meta, &#x60;details&#x60; names the failing &#x60;stage&#x60;, the &#x60;adAccountId&#x60; and every created object with its cleanup result (see &#x60;ErrorResponse.details&#x60;). An &#x60;unconfirmedWrite&#x60; there means Meta did not confirm a create and Zernio did not retry it.  |  -  |
| **503** | An upstream service is temporarily unavailable (most often the connection to Meta dropped mid-request). Retry after the indicated delay.  On Meta, &#x60;details&#x60; carries the same &#x60;stage&#x60;, &#x60;adAccountId&#x60; and &#x60;createdObjects&#x60; as a 502, and the message names every &#x60;left_behind&#x60; object. In &#x60;createdObjects&#x60;:  - &#x60;deleted&#x60;: Zernio deleted the object. - &#x60;left_behind&#x60;: still exists on the ad account because cleanup could not delete it (Meta refused the delete, or the delete hit a network error). Delete a left-behind video with &#x60;DELETE /v1/ads/videos/{id}&#x60; and the other objects in Meta Ads Manager. - &#x60;kept&#x60;: images are never deleted, because an image hash is shared by every upload of the same file.  An empty &#x60;left_behind&#x60; list is not a guarantee: when Meta created media but its answer never arrived (a dropped connection or a 5xx on the first step of a video upload), Zernio never learned the id and cannot list or delete it.  |  * Retry-After - Minimum delay in seconds before retrying. <br>  |

## createStandaloneAdWithHttpInfo

> ApiResponse<CreateStandaloneAd200Response> createStandaloneAd createStandaloneAdWithHttpInfo(createStandaloneAdRequest, idempotencyKey)

Create standalone ad

Creates a paid ad with your own creative, building the campaign and ad set it needs or adding it to existing ones.  Works across Meta, Google Ads, Pinterest, TikTok, X, LinkedIn, OpenAI Ads (ChatGPT Ads) and Reddit Ads. Per-platform required fields, budget minimums, and video-ad rules are documented on each property below.  ### Request shapes  The body selects one of these mutually exclusive shapes:  - Legacy single-creative shape (all platforms, the default). - Meta-only multi-creative shape via the creatives array: one ad set with N ads sharing budget and targeting. - Attach shape via adSetId: adds one new ad to an existing ad set, inheriting its budget, targeting, and schedule (Meta, Google Ads, TikTok, and LinkedIn).  On LinkedIn, adSetId in the attach shape is the existing Campaign id, and the budget, schedule, targeting and bidding fields must be omitted. &#x60;goal&#x60; may be omitted too (taken from the Campaign&#39;s objective), and the created ad&#39;s &#x60;targeting&#x60; echoes the Campaign&#39;s audience.  ### Google Performance Max  Set &#x60;campaignType: \&quot;pmax\&quot;&#x60; and supply &#x60;assetGroup&#x60; with text, images by role, business name and finalUrl. This creates a daily budget, PAUSED campaign and asset group atomically.  - &#x60;validateOnly: true&#x60; validates the complete request with Google without creating or persisting resources. - Read assets with &#x60;GET /v1/ads/campaigns/{campaignId}/asset-groups&#x60;. - The logo is required; video is optional via &#x60;assetGroup.youtubeVideoId&#x60;. - Brand guidelines are disabled at creation. - All supplied asset links are validated together against Google&#39;s minimum asset requirements. - PMax rejects ACTIVE creation, portfolio bidding, bid caps, legacy creative fields and attach shapes. - Geo and language targeting are supported; omitted geo targets all locations. - PMax does not require top-level goal, headline, body or linkUrl.  Supported bidding:  - Omitted or LOWEST_COST_WITHOUT_CAP: Maximize Conversions. - COST_CAP plus bidAmount: target CPA. - LOWEST_COST_WITH_MIN_ROAS plus roasAverageFloor: Maximize Conversion Value with target ROAS.  ### Google Demand Gen  Set &#x60;campaignType: \&quot;demand_gen\&quot;&#x60; and supply &#x60;demandGen&#x60;. One atomic request creates a daily budget, PAUSED campaign, one ad group and one ad. The ad is:  - a multi-asset image ad by default; - a video responsive ad when &#x60;demandGen.youtubeVideoIds&#x60; is sent; - a carousel ad (2 to 10 cards) when &#x60;demandGen.carouselCards&#x60; is sent.  Targeting and validation:  - Geo (countries, regions, cities, zips, metros) and languages go on the ad group, as Demand Gen requires. - &#x60;demandGen.channels&#x60; sets the ad group&#39;s channel controls. - &#x60;demandGen.audience&#x60; builds a Google Audience (user lists, interests, custom audiences, age ranges, genders) attached to the ad group, or &#x60;demandGen.audienceId&#x60; attaches an existing one. - &#x60;validateOnly: true&#x60; validates everything with Google without creating resources.  Supported bidding:  - Omitted or LOWEST_COST_WITHOUT_CAP: Maximize Conversions. - COST_CAP plus bidAmount: target CPA. - LOWEST_COST_WITH_MIN_ROAS plus roasAverageFloor: target ROAS. - LOWEST_COST_WITH_BID_CAP plus bidAmount: target CPC.  The created ad carries the native &#x60;platformCampaignId&#x60;, &#x60;platformAdSetId&#x60; (ad group) and &#x60;platformAdId&#x60;. After creation:  - Activate with PUT /v1/ads/campaigns/{campaignId}/status. - Edit budget, bidding and name with the regular campaign endpoints. - Edit creative, channels, audience and ad group targeting with PUT /v1/ads/{adId} (&#x60;demandGen&#x60;, &#x60;targeting&#x60;).  To grow an existing Demand Gen campaign, send one of these (neither takes budget, bidding or schedule fields; both support &#x60;validateOnly&#x60;):  - &#x60;existingCampaignId&#x60;: adds a PAUSED ad group, with its own geo, languages, channels and audience, plus its ad. - &#x60;adSetId&#x60;: adds a PAUSED ad to that ad group.  ### Meta creative options  Meta accepts &#x60;creativeFeatures&#x60; on the single and attach shapes and as defaults for &#x60;creatives[]&#x60;; an item replaces the whole feature map.  &#x60;promotion&#x60; is not supported on any shape, and any object is rejected with 400.  Reusing &#x60;existingCreativeId&#x60; uses the existing creative settings instead of new settings. Requested settings are persisted for lists, exports, and default ad-detail reads.  ### Meta required fields per shape  A missing field is a 400 naming it in &#x60;param&#x60;.  - Every shape that builds a new ad set (no &#x60;adSetId&#x60;, &#x60;existingCampaignId&#x60; or &#x60;buyingType: \&quot;RESERVED\&quot;&#x60;): &#x60;budgetAmount&#x60;. &#x60;budgetType&#x60; defaults to daily, and a lifetime budget without &#x60;endDate&#x60; ends 7 days after it starts (see &#x60;appliedDefaults&#x60;). - Single image or video (the default), also with &#x60;adSetId&#x60;: &#x60;headline&#x60; (max 255), &#x60;body&#x60;, &#x60;callToAction&#x60;, and exactly one of &#x60;imageUrl&#x60; / &#x60;video&#x60;. A catalog template creative takes none, and ignores and does not upload any sent. - Single image or video also needs &#x60;linkUrl&#x60;, unless the goal is &#x60;lead_generation&#x60; or &#x60;page_visits&#x60; or &#x60;leadGenFormId&#x60; is set. - &#x60;bodies[]&#x60; / &#x60;headlines[]&#x60; text variations: &#x60;body&#x60;, one list with 2+ items, &#x60;callToAction&#x60;, &#x60;imageUrl&#x60; or &#x60;video&#x60;, and &#x60;linkUrl&#x60; unless the goal is &#x60;lead_generation&#x60; or &#x60;leadGenFormId&#x60; is set. &#x60;headline&#x60; is not required. - &#x60;placementAssets&#x60;: &#x60;headline&#x60;, &#x60;body&#x60;, &#x60;callToAction&#x60;, and &#x60;linkUrl&#x60; with the same exemptions as the single shape; the media comes from &#x60;placementAssets&#x60;. - &#x60;carouselCards&#x60;: &#x60;body&#x60;, &#x60;callToAction&#x60;, and &#x60;linkUrl&#x60; unless the goal is &#x60;lead_generation&#x60; or &#x60;leadGenFormId&#x60; is set. &#x60;headline&#x60; is not required. - &#x60;creatives[]&#x60;: per entry &#x60;headline&#x60;, &#x60;body&#x60;, &#x60;callToAction&#x60;, &#x60;imageUrl&#x60; or &#x60;video&#x60;, and &#x60;linkUrl&#x60; unless the goal is &#x60;lead_generation&#x60;. Top-level &#x60;body&#x60; is not required. - &#x60;dynamicCreative&#x60;: &#x60;imageUrls&#x60; or &#x60;videoUrls&#x60;, &#x60;callToActionTypes&#x60;, and &#x60;linkUrls&#x60; unless the goal is &#x60;lead_generation&#x60;. Top-level &#x60;body&#x60; is not required. - &#x60;existingCreativeId&#x60;: no creative fields. - Goal &#x60;page_likes&#x60;: &#x60;body&#x60; only. - Goal &#x60;lead_generation&#x60; always needs &#x60;leadGenFormId&#x60;, except with &#x60;existingCreativeId&#x60;.  ### Meta activation  Meta builds the campaign, ad set and ads PAUSED and switches the requested levels to ACTIVE as the last step.  When Meta refuses that switch, or the connection drops, after Zernio&#39;s retries, the request still answers 201 and nothing is deleted:  - The refused level and every level below it stay PAUSED. - Levels above it that already went ACTIVE stay ACTIVE. - The ad comes back with &#x60;status: paused&#x60; and its &#x60;configuredStatus&#x60; as read back from Meta. - A switch Meta applied although its answer was lost counts as ACTIVE, since Zernio reads the status back first.  &#x60;message&#x60; says not everything is ACTIVE. &#x60;warnings&#x60; carries one entry starting with &#x60;activation_failed:&#x60; that quotes Meta&#39;s code, subcode and message, and names what was kept PAUSED and what was switched ACTIVE.  That warning also lists the calls that switch the PAUSED ones on later, in this order, with status &#x60;active&#x60;:  1. PUT /v1/ads/campaigns/{campaignId}/status 2. PUT /v1/ads/ad-sets/{adSetId}/status 3. PUT /v1/ads/{adId}/status  On the &#x60;creatives[]&#x60; shape, only the ads Meta refused stay PAUSED when the campaign and ad set went through. A Reach and Frequency ad is created ACTIVE and is never listed as kept PAUSED. With an &#x60;Idempotency-Key&#x60;, a retry replays this 201.  ### LinkedIn  LinkedIn creates a Single Image or Single Video Ad backed by a Direct Sponsored Content \&quot;dark post\&quot; authored by a Company Page (see &#x60;organizationId&#x60;).  - Supported goals: engagement, traffic, awareness, and video_views. - Video ads use the &#x60;video&#x60; field; video_views requires a video. - Traffic ads require &#x60;linkUrl&#x60;.  ### Reddit Ads  Use the &#x60;accountId&#x60; of a &#x60;redditads&#x60; connection and an &#x60;adAccountId&#x60; like &#x60;a2_abc123&#x60;. Zernio creates a campaign, an ad group carrying the budget, schedule, targeting and pixel, and an ad running a new promoted post. The post is authored by the ad account&#39;s first profile (422 when it has none).  The creative format follows the body:  - &#x60;carouselCards&#x60;: a carousel. - &#x60;video&#x60;: a video ad. - &#x60;imageUrl&#x60;: an image ad. - None of them: a text ad, which cannot link out (&#x60;linkUrl&#x60; is a 400 there; &#x60;body&#x60; is required).  Only the legacy single-creative shape is available: &#x60;creatives[]&#x60;, &#x60;adSetId&#x60;, &#x60;existingCampaignId&#x60; and &#x60;validateOnly&#x60; are refused.  Reddit throttling surfaces as 429 &#x60;rate_limited&#x60; with &#x60;platform: reddit&#x60;; retry after a delay. To promote an existing Reddit post, use POST /v1/ads/boost.  ### Idempotency  This endpoint is not idempotent at the platform level: a blind retry creates a second campaign/ad set/ad. Send an &#x60;Idempotency-Key&#x60; header to make retries safe.  - The first request with a given key creates the ad and we store the response. - A retry with the same key replays that exact response (with &#x60;Idempotent-Replayed: true&#x60;) instead of creating duplicates. - Reusing a key with a different body returns 422. - A key whose first request is still in flight returns 409 (retry after a short backoff). - If the first request is cut off mid-create (for example by a function timeout), its key can stay in progress and keep returning 409 until it expires. Use a new key to retry sooner, after checking whether the ad was created. - Keys are scoped to your credential and expire after 24h. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        CreateStandaloneAdRequest createStandaloneAdRequest = new CreateStandaloneAdRequest(); // CreateStandaloneAdRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours. 
        try {
            ApiResponse<CreateStandaloneAd200Response> response = apiInstance.createStandaloneAdWithHttpInfo(createStandaloneAdRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#createStandaloneAd");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createStandaloneAdRequest** | [**CreateStandaloneAdRequest**](CreateStandaloneAdRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  A request cut off mid-handler (e.g. by a function timeout) can leave its key in progress, answering 409 until the key expires after 24 hours.  | [optional] |

### Return type

ApiResponse<[**CreateStandaloneAd200Response**](CreateStandaloneAd200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | validateOnly dry-run passed, nothing was created |  -  |
| **201** | Ad(s) created |  -  |
| **400** | Missing required fields, invalid values, non-Meta platform used with creatives[] / adSetId, or a Meta validateOnly validation failure (verbatim) |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **429** | Meta only (code &#x60;rate_limited&#x60;). Meta puts a security hold lasting days (code 31, subcode 3858385, \&quot;Please authenticate your account\&quot;) on ad accounts that receive bursts of ad writes, and it counts &#x60;validateOnly&#x60; checks as writes.  To keep integrations out of that hold, Zernio:  - runs creates for one Meta ad account one at a time (a parallel request waits up to 60 seconds for its turn); - allows at most 30 creates per ad account in any rolling 5 minutes, &#x60;validateOnly&#x60; included.  A 429 here means one of the two was hit: wait &#x60;Retry-After&#x60; seconds and send creates for that ad account sequentially. Other ad accounts are not affected.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |
| **403** | Ads access required. Legacy plans need the Ads add-on; it is included by default on usage-based plans. Also returned with these codes:  - &#x60;ads_allowance_exceeded&#x60;: the team has no payment method on file and has reached the 500 free live ads. Add a card to resume. - &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;. - &#x60;ad_account_not_selected&#x60;, fix: add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected. - &#x60;insufficient_permissions&#x60;: the Facebook user behind the connection&#39;s token lacks the Advertise permission on the Meta ad account, or the token lacks &#x60;ads_management&#x60; (Meta subcode 2490585, 2490591 or 4841020; see &#x60;ErrorResponse.details&#x60;).  |  -  |
| **422** | Platform ads connection required (TikTok Ads, X Ads) or missing linked account. Also returned:  - With code &#x60;ad_account_unusable&#x60;: Meta refuses writes on the ad account because its status is ineligible to manage ads (see &#x60;ErrorResponse.details&#x60;). - On Reddit: &#x60;video_views&#x60; without a video, or an ad account with no pixel or no profile. - On Reddit, with code &#x60;invalid_resource_state&#x60;: a pixel that never received the event the ad group optimizes toward.  |  -  |
| **501** | The requested option is not supported on this platform: &#x60;validateOnly&#x60; outside Meta and Google Performance Max, or a shape the adapter does not implement. Carries code &#x60;feature_not_available&#x60;.  |  -  |
| **502** | The platform rejected the request, or failed to produce media the ad needs (e.g. Meta generated no poster for an uploaded video when no &#x60;video.thumbnailUrl&#x60; was supplied). An upstream 4xx status is forwarded instead of 502.  - Inspect &#x60;platformError&#x60; for the upstream payload. - Failures we raise carry a &#x60;reason&#x60;; a payload forwarded verbatim from Meta may not. - On the &#x60;creatives[]&#x60; shape, a missing poster also carries &#x60;creativeIndex&#x60; and &#x60;videoUrl&#x60; to identify the entry. - On Meta, &#x60;details&#x60; names the failing &#x60;stage&#x60;, the &#x60;adAccountId&#x60; and every created object with its cleanup result (see &#x60;ErrorResponse.details&#x60;). An &#x60;unconfirmedWrite&#x60; there means Meta did not confirm a create and Zernio did not retry it.  |  -  |
| **503** | An upstream service is temporarily unavailable (most often the connection to Meta dropped mid-request). Retry after the indicated delay.  On Meta, &#x60;details&#x60; carries the same &#x60;stage&#x60;, &#x60;adAccountId&#x60; and &#x60;createdObjects&#x60; as a 502, and the message names every &#x60;left_behind&#x60; object. In &#x60;createdObjects&#x60;:  - &#x60;deleted&#x60;: Zernio deleted the object. - &#x60;left_behind&#x60;: still exists on the ad account because cleanup could not delete it (Meta refused the delete, or the delete hit a network error). Delete a left-behind video with &#x60;DELETE /v1/ads/videos/{id}&#x60; and the other objects in Meta Ads Manager. - &#x60;kept&#x60;: images are never deleted, because an image hash is shared by every upload of the same file.  An empty &#x60;left_behind&#x60; list is not a guarantee: when Meta created media but its answer never arrived (a dropped connection or a 5xx on the first step of a video upload), Zernio never learned the id and cannot list or delete it.  |  * Retry-After - Minimum delay in seconds before retrying. <br>  |


## deleteAd

> DeleteAccountGroup200Response deleteAd(adId)

Cancel an ad

Deletes an ad on the platform while keeping its history, and removes empty parents only when they were created through this API.  The ad is deleted on the platform and marked as cancelled in the database. It is preserved for history.  - OpenAI Ads has no delete API: the ad is archived instead (a terminal state, the closest equivalent). - Reddit Ads has no delete either: the ad is archived (&#x60;configured_status&#x60; ARCHIVED).  To delete a whole campaign on purpose use &#x60;DELETE /v1/ads/campaigns/{campaignId}&#x60;.  ### Parents  Only the ad is deleted; a campaign or ad set is never deleted while it still holds another ad. Parents created outside Zernio, and the parents of an ad imported from the platform, are always kept.  ### Meta  When the ad set and campaign were created by Zernio (by &#x60;POST /v1/ads/create&#x60; or &#x60;POST /v1/ads/boost&#x60;) and Meta lists no other ad in the ad set (archived ads count), the emptied ad set is deleted too. The campaign follows once it holds no other ad set.  ### LinkedIn  The ad is a creative inside a campaign inside a campaign group.  - The creative is always removed. - The campaign is removed only when Zernio created it and LinkedIn lists no other creative in it that is not archived, canceled or deleted. - The campaign group is removed only when Zernio created it and LinkedIn lists no other campaign in it that is not canceled or deleted (archived campaigns count).  If the creative itself cannot be removed the request fails and no parent is touched.  ### X  The ad is a promoted post inside a line item inside a campaign.  - The promoted post is always removed. - The line item is removed only when Zernio created it (by &#x60;POST /v1/ads/create&#x60; or &#x60;POST /v1/ads/boost&#x60;) and X lists no other undeleted promoted post in it. - The campaign is removed only when Zernio created it and X lists no other undeleted line item in it.  If X refuses the promoted post delete the request fails and no parent is touched. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adId = "adId_example"; // String | 
        try {
            DeleteAccountGroup200Response result = apiInstance.deleteAd(adId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#deleteAd");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adId** | **String**|  | |

### Return type

[**DeleteAccountGroup200Response**](DeleteAccountGroup200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad cancelled |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **404** | Resource not found |  -  |

## deleteAdWithHttpInfo

> ApiResponse<DeleteAccountGroup200Response> deleteAd deleteAdWithHttpInfo(adId)

Cancel an ad

Deletes an ad on the platform while keeping its history, and removes empty parents only when they were created through this API.  The ad is deleted on the platform and marked as cancelled in the database. It is preserved for history.  - OpenAI Ads has no delete API: the ad is archived instead (a terminal state, the closest equivalent). - Reddit Ads has no delete either: the ad is archived (&#x60;configured_status&#x60; ARCHIVED).  To delete a whole campaign on purpose use &#x60;DELETE /v1/ads/campaigns/{campaignId}&#x60;.  ### Parents  Only the ad is deleted; a campaign or ad set is never deleted while it still holds another ad. Parents created outside Zernio, and the parents of an ad imported from the platform, are always kept.  ### Meta  When the ad set and campaign were created by Zernio (by &#x60;POST /v1/ads/create&#x60; or &#x60;POST /v1/ads/boost&#x60;) and Meta lists no other ad in the ad set (archived ads count), the emptied ad set is deleted too. The campaign follows once it holds no other ad set.  ### LinkedIn  The ad is a creative inside a campaign inside a campaign group.  - The creative is always removed. - The campaign is removed only when Zernio created it and LinkedIn lists no other creative in it that is not archived, canceled or deleted. - The campaign group is removed only when Zernio created it and LinkedIn lists no other campaign in it that is not canceled or deleted (archived campaigns count).  If the creative itself cannot be removed the request fails and no parent is touched.  ### X  The ad is a promoted post inside a line item inside a campaign.  - The promoted post is always removed. - The line item is removed only when Zernio created it (by &#x60;POST /v1/ads/create&#x60; or &#x60;POST /v1/ads/boost&#x60;) and X lists no other undeleted promoted post in it. - The campaign is removed only when Zernio created it and X lists no other undeleted line item in it.  If X refuses the promoted post delete the request fails and no parent is touched. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adId = "adId_example"; // String | 
        try {
            ApiResponse<DeleteAccountGroup200Response> response = apiInstance.deleteAdWithHttpInfo(adId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#deleteAd");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adId** | **String**|  | |

### Return type

ApiResponse<[**DeleteAccountGroup200Response**](DeleteAccountGroup200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad cancelled |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **404** | Resource not found |  -  |


## deleteAdCampaign

> DeleteAdCampaign200Response deleteAdCampaign(campaignId, deleteAdCampaignRequest)

Delete a campaign

Deletes a campaign on its platform, including a campaign that never got any ads.  Only the campaign itself is sent to the platform:  - Meta, Google, TikTok, LinkedIn and X delete it. - OpenAI, Reddit and Pinterest have no campaign delete and archive it instead (see below).  Locally, all Ad documents for this campaign are marked &#x60;status: cancelled&#x60;.  ### Empty campaigns  A campaign with zero ads has no local Ad documents to resolve, so it is invisible to &#x60;/v1/ads/tree&#x60; and this endpoint would 404. That state comes from the two-step create flow (campaign, then ads via &#x60;existingCampaignId&#x60;) whenever Meta rejects the ad step.  To delete such a shell, send &#x60;accountId&#x60; in the body or the query string. We skip the local lookup entirely and forward the delete to the platform of that connection. &#x60;accountId&#x60; is ignored when the campaign does have ads.  ### Google, TikTok, LinkedIn, Pinterest, Reddit and OpenAI  Google, TikTok, LinkedIn, Pinterest and Reddit take the ad account from the synced campaign (OpenAI needs none). When the campaign was never synced (or is synced under several ad accounts), the answer is 409 &#x60;invalid_resource_state&#x60; on &#x60;campaignId&#x60; and nothing is deleted: sync the ad account and retry.  Before deleting on Google, TikTok, LinkedIn, Pinterest, OpenAI or Reddit, Zernio asks the platform whether the campaign still holds ad groups or ads. Google asset groups count; on LinkedIn, campaigns inside the campaign group count.  If it does, or the platform cannot confirm it has none (a TikTok Smart+ campaign), the answer is 409 &#x60;invalid_resource_state&#x60; on &#x60;campaignId&#x60; and nothing is deleted. Either:  - sync the ad account and delete the campaign again so its ads are cancelled with it, or - delete them on the platform first.  ### X  On X the ad account comes from the synced campaign, which wins over &#x60;adAccountId&#x60;. When the campaign was never synced, send &#x60;adAccountId&#x60; too.  Before deleting, Zernio asks X whether the campaign still holds undeleted line items (ads not synced yet). If it does, the answer is 409 &#x60;invalid_field_value&#x60; on &#x60;campaignId&#x60; and nothing is deleted.  - Line items that hold promoted posts: sync the ad account and retry. - Line items without promoted posts never sync, so delete them in X Ads Manager first.  ### Reddit Ads  Reddit Ads has no delete: the campaign is archived instead (&#x60;configured_status&#x60; ARCHIVED), which stops delivery for good. Its ad groups and ads keep their own switches but cannot deliver under an archived campaign.  ### OpenAI Ads  OpenAI Ads has no delete either: the campaign is archived (state &#x60;archive&#x60;). Its ad groups and ads are not touched on OpenAI. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        DeleteAdCampaignRequest deleteAdCampaignRequest = new DeleteAdCampaignRequest(); // DeleteAdCampaignRequest | 
        try {
            DeleteAdCampaign200Response result = apiInstance.deleteAdCampaign(campaignId, deleteAdCampaignRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#deleteAdCampaign");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Platform campaign ID | |
| **deleteAdCampaignRequest** | [**DeleteAdCampaignRequest**](DeleteAdCampaignRequest.md)|  | |

### Return type

[**DeleteAdCampaign200Response**](DeleteAdCampaign200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **409** | One of three conflicts:  - The ads connection is inactive or needs reconnection (code &#x60;ads_connection_required&#x60;, param &#x60;accountId&#x60;). Reconnect it, then read GET /v1/accounts for its current account ID before retrying. - X only: the empty campaign still holds line items on X (code &#x60;invalid_field_value&#x60;, param &#x60;campaignId&#x60;) and nothing was deleted. Sync the ad account when they hold promoted posts, otherwise delete them in X Ads Manager, then retry. - Google, TikTok, LinkedIn, Pinterest, OpenAI or Reddit: the empty campaign has no synced record naming its ad account, or the platform still lists ad groups or ads under it (code &#x60;invalid_resource_state&#x60;, param &#x60;campaignId&#x60;). Nothing was deleted: sync the ad account, then retry.  |  -  |
| **400** | Invalid request |  -  |
| **200** | Campaign deleted |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | Operation not supported on this platform |  -  |

## deleteAdCampaignWithHttpInfo

> ApiResponse<DeleteAdCampaign200Response> deleteAdCampaign deleteAdCampaignWithHttpInfo(campaignId, deleteAdCampaignRequest)

Delete a campaign

Deletes a campaign on its platform, including a campaign that never got any ads.  Only the campaign itself is sent to the platform:  - Meta, Google, TikTok, LinkedIn and X delete it. - OpenAI, Reddit and Pinterest have no campaign delete and archive it instead (see below).  Locally, all Ad documents for this campaign are marked &#x60;status: cancelled&#x60;.  ### Empty campaigns  A campaign with zero ads has no local Ad documents to resolve, so it is invisible to &#x60;/v1/ads/tree&#x60; and this endpoint would 404. That state comes from the two-step create flow (campaign, then ads via &#x60;existingCampaignId&#x60;) whenever Meta rejects the ad step.  To delete such a shell, send &#x60;accountId&#x60; in the body or the query string. We skip the local lookup entirely and forward the delete to the platform of that connection. &#x60;accountId&#x60; is ignored when the campaign does have ads.  ### Google, TikTok, LinkedIn, Pinterest, Reddit and OpenAI  Google, TikTok, LinkedIn, Pinterest and Reddit take the ad account from the synced campaign (OpenAI needs none). When the campaign was never synced (or is synced under several ad accounts), the answer is 409 &#x60;invalid_resource_state&#x60; on &#x60;campaignId&#x60; and nothing is deleted: sync the ad account and retry.  Before deleting on Google, TikTok, LinkedIn, Pinterest, OpenAI or Reddit, Zernio asks the platform whether the campaign still holds ad groups or ads. Google asset groups count; on LinkedIn, campaigns inside the campaign group count.  If it does, or the platform cannot confirm it has none (a TikTok Smart+ campaign), the answer is 409 &#x60;invalid_resource_state&#x60; on &#x60;campaignId&#x60; and nothing is deleted. Either:  - sync the ad account and delete the campaign again so its ads are cancelled with it, or - delete them on the platform first.  ### X  On X the ad account comes from the synced campaign, which wins over &#x60;adAccountId&#x60;. When the campaign was never synced, send &#x60;adAccountId&#x60; too.  Before deleting, Zernio asks X whether the campaign still holds undeleted line items (ads not synced yet). If it does, the answer is 409 &#x60;invalid_field_value&#x60; on &#x60;campaignId&#x60; and nothing is deleted.  - Line items that hold promoted posts: sync the ad account and retry. - Line items without promoted posts never sync, so delete them in X Ads Manager first.  ### Reddit Ads  Reddit Ads has no delete: the campaign is archived instead (&#x60;configured_status&#x60; ARCHIVED), which stops delivery for good. Its ad groups and ads keep their own switches but cannot deliver under an archived campaign.  ### OpenAI Ads  OpenAI Ads has no delete either: the campaign is archived (state &#x60;archive&#x60;). Its ad groups and ads are not touched on OpenAI. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        DeleteAdCampaignRequest deleteAdCampaignRequest = new DeleteAdCampaignRequest(); // DeleteAdCampaignRequest | 
        try {
            ApiResponse<DeleteAdCampaign200Response> response = apiInstance.deleteAdCampaignWithHttpInfo(campaignId, deleteAdCampaignRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#deleteAdCampaign");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Platform campaign ID | |
| **deleteAdCampaignRequest** | [**DeleteAdCampaignRequest**](DeleteAdCampaignRequest.md)|  | |

### Return type

ApiResponse<[**DeleteAdCampaign200Response**](DeleteAdCampaign200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **409** | One of three conflicts:  - The ads connection is inactive or needs reconnection (code &#x60;ads_connection_required&#x60;, param &#x60;accountId&#x60;). Reconnect it, then read GET /v1/accounts for its current account ID before retrying. - X only: the empty campaign still holds line items on X (code &#x60;invalid_field_value&#x60;, param &#x60;campaignId&#x60;) and nothing was deleted. Sync the ad account when they hold promoted posts, otherwise delete them in X Ads Manager, then retry. - Google, TikTok, LinkedIn, Pinterest, OpenAI or Reddit: the empty campaign has no synced record naming its ad account, or the platform still lists ad groups or ads under it (code &#x60;invalid_resource_state&#x60;, param &#x60;campaignId&#x60;). Nothing was deleted: sync the ad account, then retry.  |  -  |
| **400** | Invalid request |  -  |
| **200** | Campaign deleted |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | Operation not supported on this platform |  -  |


## deleteAdSet

> DeleteAdSet200Response deleteAdSet(adSetId)

Delete an ad set

Deletes an ad set and its ads while keeping the campaign, archiving it instead on platforms without a hard delete.  Locally, every Ad document under the ad set is marked &#x60;status: cancelled&#x60;.  Delete is soft on platforms that have no hard delete: LinkedIn moves the campaign to &#x60;PENDING_DELETION&#x60;, Pinterest and Reddit archive the ad group, and X soft-flags the line item. Google removes the ad group. All remain readable for reporting. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Platform ad set ID
        try {
            DeleteAdSet200Response result = apiInstance.deleteAdSet(adSetId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#deleteAdSet");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adSetId** | **String**| Platform ad set ID | |

### Return type

[**DeleteAdSet200Response**](DeleteAdSet200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad set deleted |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **404** | Ad set not found |  -  |
| **501** | Operation not supported on this platform |  -  |

## deleteAdSetWithHttpInfo

> ApiResponse<DeleteAdSet200Response> deleteAdSet deleteAdSetWithHttpInfo(adSetId)

Delete an ad set

Deletes an ad set and its ads while keeping the campaign, archiving it instead on platforms without a hard delete.  Locally, every Ad document under the ad set is marked &#x60;status: cancelled&#x60;.  Delete is soft on platforms that have no hard delete: LinkedIn moves the campaign to &#x60;PENDING_DELETION&#x60;, Pinterest and Reddit archive the ad group, and X soft-flags the line item. Google removes the ad group. All remain readable for reporting. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Platform ad set ID
        try {
            ApiResponse<DeleteAdSet200Response> response = apiInstance.deleteAdSetWithHttpInfo(adSetId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#deleteAdSet");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adSetId** | **String**| Platform ad set ID | |

### Return type

ApiResponse<[**DeleteAdSet200Response**](DeleteAdSet200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad set deleted |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **404** | Ad set not found |  -  |
| **501** | Operation not supported on this platform |  -  |


## dismissAdsAlert

> DismissAdsAlert200Response dismissAdsAlert(alertId)

Dismiss an ads alert

Hides an alert from &#x60;GET /v1/ads/alerts&#x60; for 30 days for the calling user. If the problem is still there after that, the alert comes back. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String alertId = "alertId_example"; // String | The `id` of an alert from GET /v1/ads/alerts.
        try {
            DismissAdsAlert200Response result = apiInstance.dismissAdsAlert(alertId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#dismissAdsAlert");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **alertId** | **String**| The &#x60;id&#x60; of an alert from GET /v1/ads/alerts. | |

### Return type

[**DismissAdsAlert200Response**](DismissAdsAlert200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Dismissed. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **503** | Dismissing is temporarily unavailable (code &#x60;feature_not_available&#x60;). |  -  |

## dismissAdsAlertWithHttpInfo

> ApiResponse<DismissAdsAlert200Response> dismissAdsAlert dismissAdsAlertWithHttpInfo(alertId)

Dismiss an ads alert

Hides an alert from &#x60;GET /v1/ads/alerts&#x60; for 30 days for the calling user. If the problem is still there after that, the alert comes back. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String alertId = "alertId_example"; // String | The `id` of an alert from GET /v1/ads/alerts.
        try {
            ApiResponse<DismissAdsAlert200Response> response = apiInstance.dismissAdsAlertWithHttpInfo(alertId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#dismissAdsAlert");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **alertId** | **String**| The &#x60;id&#x60; of an alert from GET /v1/ads/alerts. | |

### Return type

ApiResponse<[**DismissAdsAlert200Response**](DismissAdsAlert200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Dismissed. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **503** | Dismissing is temporarily unavailable (code &#x60;feature_not_available&#x60;). |  -  |


## dismissGoogleRecommendations

> ApplyGoogleRecommendations200Response dismissGoogleRecommendations(dismissGoogleRecommendationsRequest)

Dismiss Google Ads recommendations

Dismisses Google optimization suggestions so Google stops showing them.  Dismiss up to 100 recommendations so Google stops suggesting them. Items run in partial-failure mode. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        DismissGoogleRecommendationsRequest dismissGoogleRecommendationsRequest = new DismissGoogleRecommendationsRequest(); // DismissGoogleRecommendationsRequest | 
        try {
            ApplyGoogleRecommendations200Response result = apiInstance.dismissGoogleRecommendations(dismissGoogleRecommendationsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#dismissGoogleRecommendations");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **dismissGoogleRecommendationsRequest** | [**DismissGoogleRecommendationsRequest**](DismissGoogleRecommendationsRequest.md)|  | |

### Return type

[**ApplyGoogleRecommendations200Response**](ApplyGoogleRecommendations200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-recommendation outcome. A failed item does not stop the others. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **404** | Resource not found |  -  |
| **422** | No Google Ads customer on this connection, or it needs reconnecting. |  -  |
| **429** | Google quota or the Zernio Google operations burst limit is exhausted. |  -  |
| **501** | accountId is not a Google Ads connection. |  -  |

## dismissGoogleRecommendationsWithHttpInfo

> ApiResponse<ApplyGoogleRecommendations200Response> dismissGoogleRecommendations dismissGoogleRecommendationsWithHttpInfo(dismissGoogleRecommendationsRequest)

Dismiss Google Ads recommendations

Dismisses Google optimization suggestions so Google stops showing them.  Dismiss up to 100 recommendations so Google stops suggesting them. Items run in partial-failure mode. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        DismissGoogleRecommendationsRequest dismissGoogleRecommendationsRequest = new DismissGoogleRecommendationsRequest(); // DismissGoogleRecommendationsRequest | 
        try {
            ApiResponse<ApplyGoogleRecommendations200Response> response = apiInstance.dismissGoogleRecommendationsWithHttpInfo(dismissGoogleRecommendationsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#dismissGoogleRecommendations");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **dismissGoogleRecommendationsRequest** | [**DismissGoogleRecommendationsRequest**](DismissGoogleRecommendationsRequest.md)|  | |

### Return type

ApiResponse<[**ApplyGoogleRecommendations200Response**](ApplyGoogleRecommendations200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-recommendation outcome. A failed item does not stop the others. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **404** | Resource not found |  -  |
| **422** | No Google Ads customer on this connection, or it needs reconnecting. |  -  |
| **429** | Google quota or the Zernio Google operations burst limit is exhausted. |  -  |
| **501** | accountId is not a Google Ads connection. |  -  |


## duplicateAd

> DuplicateAd200Response duplicateAd(adId, idempotencyKey, duplicateAdRequest)

Duplicate an ad

Copies a single Meta ad, optionally into another ad set, created paused so you can review it before launch.  It duplicates the ad via Meta&#39;s native &#x60;POST /{ad-id}/copies&#x60;. The copy is created paused.  - &#x60;adSetId&#x60; retargets the copy into another ad set; omitted &#x3D; the source&#39;s own ad set. - Accepts the Zernio ad id or the platform ad id. - Sync discovery is triggered automatically (&#x60;syncAfter: false&#x60; to skip).  ### Creative settings  Creative settings returned by Meta, including explicit promotion metadata and creativeFeatures, are preserved when the native copy requires a creative rebuild. Metadata Meta does not return cannot be recovered.  ### Fallback rebuild  When Meta refuses the native copy with its capability error (code 3), which happens for some creatives built by other tools, the ad is rebuilt instead:  1. A new creative from the source&#39;s returned spec. 2. A new ad in the target ad set, carrying the source name, status option, rename options and tracking specs. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adId = "adId_example"; // String | Zernio ad ID or platform ad ID
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key. 
        DuplicateAdRequest duplicateAdRequest = new DuplicateAdRequest(); // DuplicateAdRequest | 
        try {
            DuplicateAd200Response result = apiInstance.duplicateAd(adId, idempotencyKey, duplicateAdRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#duplicateAd");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adId** | **String**| Zernio ad ID or platform ad ID | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key.  | [optional] |
| **duplicateAdRequest** | [**DuplicateAdRequest**](DuplicateAdRequest.md)|  | [optional] |

### Return type

[**DuplicateAd200Response**](DuplicateAd200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | Several active connections on the API key&#39;s profiles reach the ad account of this ad (code &#x60;ambiguous_account&#x60;), so the connection to act with is ambiguous. Keep one of them connected or move the others to a profile this key cannot access. |  -  |
| **200** | Ad duplicated |  -  |
| **400** | Invalid input |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Forbidden. Two codes:  - &#x60;ads_allowance_exceeded&#x60;: the team has no payment method on file and has reached the 500 free live ads. Add a card to resume. - &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix &#x60;ad_account_not_selected&#x60;, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | Ad not found |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## duplicateAdWithHttpInfo

> ApiResponse<DuplicateAd200Response> duplicateAd duplicateAdWithHttpInfo(adId, idempotencyKey, duplicateAdRequest)

Duplicate an ad

Copies a single Meta ad, optionally into another ad set, created paused so you can review it before launch.  It duplicates the ad via Meta&#39;s native &#x60;POST /{ad-id}/copies&#x60;. The copy is created paused.  - &#x60;adSetId&#x60; retargets the copy into another ad set; omitted &#x3D; the source&#39;s own ad set. - Accepts the Zernio ad id or the platform ad id. - Sync discovery is triggered automatically (&#x60;syncAfter: false&#x60; to skip).  ### Creative settings  Creative settings returned by Meta, including explicit promotion metadata and creativeFeatures, are preserved when the native copy requires a creative rebuild. Metadata Meta does not return cannot be recovered.  ### Fallback rebuild  When Meta refuses the native copy with its capability error (code 3), which happens for some creatives built by other tools, the ad is rebuilt instead:  1. A new creative from the source&#39;s returned spec. 2. A new ad in the target ad set, carrying the source name, status option, rename options and tracking specs. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adId = "adId_example"; // String | Zernio ad ID or platform ad ID
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key. 
        DuplicateAdRequest duplicateAdRequest = new DuplicateAdRequest(); // DuplicateAdRequest | 
        try {
            ApiResponse<DuplicateAd200Response> response = apiInstance.duplicateAdWithHttpInfo(adId, idempotencyKey, duplicateAdRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#duplicateAd");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adId** | **String**| Zernio ad ID or platform ad ID | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key.  | [optional] |
| **duplicateAdRequest** | [**DuplicateAdRequest**](DuplicateAdRequest.md)|  | [optional] |

### Return type

ApiResponse<[**DuplicateAd200Response**](DuplicateAd200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | Several active connections on the API key&#39;s profiles reach the ad account of this ad (code &#x60;ambiguous_account&#x60;), so the connection to act with is ambiguous. Keep one of them connected or move the others to a profile this key cannot access. |  -  |
| **200** | Ad duplicated |  -  |
| **400** | Invalid input |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Forbidden. Two codes:  - &#x60;ads_allowance_exceeded&#x60;: the team has no payment method on file and has reached the 500 free live ads. Add a card to resume. - &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix &#x60;ad_account_not_selected&#x60;, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | Ad not found |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## duplicateAdCampaign

> DuplicateAdCampaign200Response duplicateAdCampaign(campaignId, duplicateAdCampaignRequest, idempotencyKey)

Duplicate a campaign

Copies a campaign with its ad sets, ads, creatives and targeting, created paused so you can review it before launch.  Ad sets, ads, creatives, and targeting are copied by default (&#x60;deepCopy: true&#x60;). The copy is created paused so callers can review before launching.  ### Per-platform implementation  - **Meta** copies one level at a time with Meta&#39;s &#x60;/copies&#x60; endpoint. See below. - **TikTok** has no native copy primitive. See below. - **LinkedIn** has no native copy primitive. See below. - Other platforms return 501 Not Implemented.  ### Meta  Zernio copies the campaign, then each of its ad sets (DELETED and ARCHIVED ones are skipped), then each ad of every ad set. So a campaign of any size copies: Meta refuses a single deep copy of 3 or more objects.  - &#x60;statusOption&#x60; applies at every level. - If any child copy fails, the partial copy is deleted and the request fails with Meta&#39;s error, so a retry starts clean. - Each copied object takes a few seconds, so a large campaign takes minutes to answer.  ### TikTok  Zernio walks the source graph (&#x60;/v2/campaign/get/&#x60;, &#x60;/v2/adgroup/get/&#x60;, &#x60;/v2/ad/get/&#x60;) and recreates each entity via the corresponding &#x60;/create/&#x60; endpoints. It carries over budget / targeting / bid_type / bid_price / deep_bid_type / creative fields. Spark Ad linkage (&#x60;tiktok_item_id&#x60;) is preserved.  ### LinkedIn  Zernio walks the source CampaignGroup → Campaigns → Creatives and recreates each entity. It carries over these fields, plus every Creative&#39;s &#x60;content&#x60; object verbatim:  - &#x60;type&#x60; / &#x60;costType&#x60; / &#x60;unitCost&#x60; / &#x60;optimizationTargetType&#x60; - &#x60;creativeSelection&#x60; / &#x60;objectiveType&#x60; / &#x60;format&#x60; - &#x60;dailyBudget&#x60; / &#x60;totalBudget&#x60; / &#x60;targetingCriteria&#x60; / &#x60;runSchedule&#x60;  &#x60;statusOption: INHERITED_FROM_SOURCE&#x60; is evaluated **per entity**: any Group / Campaign / Creative whose source is &#x60;ACTIVE&#x60; gets its clone activated too.  Duplicating an ACTIVE campaign with &#x60;INHERITED_FROM_SOURCE&#x60; starts a second front of spend the moment the clone activates. The safe default is &#x60;PAUSED&#x60;.  ### Sync  The new hierarchy is asynchronous to materialize in our DB, and we trigger sync discovery automatically. Set &#x60;syncAfter: false&#x60; to skip and poll &#x60;/v1/ads/tree&#x60; on your own cadence. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Source platform campaign ID
        DuplicateAdCampaignRequest duplicateAdCampaignRequest = new DuplicateAdCampaignRequest(); // DuplicateAdCampaignRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key. 
        try {
            DuplicateAdCampaign200Response result = apiInstance.duplicateAdCampaign(campaignId, duplicateAdCampaignRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#duplicateAdCampaign");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Source platform campaign ID | |
| **duplicateAdCampaignRequest** | [**DuplicateAdCampaignRequest**](DuplicateAdCampaignRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key.  | [optional] |

### Return type

[**DuplicateAdCampaign200Response**](DuplicateAdCampaign200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign duplicated |  -  |
| **400** | Invalid input |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | One of two refusals:  - &#x60;ads_allowance_exceeded&#x60;: the team has no payment method on file and has reached the 500 free live ads. Add a card to resume. - &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the ad account this request targets is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix &#x60;ad_account_not_selected&#x60;, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | Source campaign not found |  -  |
| **501** | Operation not supported on this platform |  -  |

## duplicateAdCampaignWithHttpInfo

> ApiResponse<DuplicateAdCampaign200Response> duplicateAdCampaign duplicateAdCampaignWithHttpInfo(campaignId, duplicateAdCampaignRequest, idempotencyKey)

Duplicate a campaign

Copies a campaign with its ad sets, ads, creatives and targeting, created paused so you can review it before launch.  Ad sets, ads, creatives, and targeting are copied by default (&#x60;deepCopy: true&#x60;). The copy is created paused so callers can review before launching.  ### Per-platform implementation  - **Meta** copies one level at a time with Meta&#39;s &#x60;/copies&#x60; endpoint. See below. - **TikTok** has no native copy primitive. See below. - **LinkedIn** has no native copy primitive. See below. - Other platforms return 501 Not Implemented.  ### Meta  Zernio copies the campaign, then each of its ad sets (DELETED and ARCHIVED ones are skipped), then each ad of every ad set. So a campaign of any size copies: Meta refuses a single deep copy of 3 or more objects.  - &#x60;statusOption&#x60; applies at every level. - If any child copy fails, the partial copy is deleted and the request fails with Meta&#39;s error, so a retry starts clean. - Each copied object takes a few seconds, so a large campaign takes minutes to answer.  ### TikTok  Zernio walks the source graph (&#x60;/v2/campaign/get/&#x60;, &#x60;/v2/adgroup/get/&#x60;, &#x60;/v2/ad/get/&#x60;) and recreates each entity via the corresponding &#x60;/create/&#x60; endpoints. It carries over budget / targeting / bid_type / bid_price / deep_bid_type / creative fields. Spark Ad linkage (&#x60;tiktok_item_id&#x60;) is preserved.  ### LinkedIn  Zernio walks the source CampaignGroup → Campaigns → Creatives and recreates each entity. It carries over these fields, plus every Creative&#39;s &#x60;content&#x60; object verbatim:  - &#x60;type&#x60; / &#x60;costType&#x60; / &#x60;unitCost&#x60; / &#x60;optimizationTargetType&#x60; - &#x60;creativeSelection&#x60; / &#x60;objectiveType&#x60; / &#x60;format&#x60; - &#x60;dailyBudget&#x60; / &#x60;totalBudget&#x60; / &#x60;targetingCriteria&#x60; / &#x60;runSchedule&#x60;  &#x60;statusOption: INHERITED_FROM_SOURCE&#x60; is evaluated **per entity**: any Group / Campaign / Creative whose source is &#x60;ACTIVE&#x60; gets its clone activated too.  Duplicating an ACTIVE campaign with &#x60;INHERITED_FROM_SOURCE&#x60; starts a second front of spend the moment the clone activates. The safe default is &#x60;PAUSED&#x60;.  ### Sync  The new hierarchy is asynchronous to materialize in our DB, and we trigger sync discovery automatically. Set &#x60;syncAfter: false&#x60; to skip and poll &#x60;/v1/ads/tree&#x60; on your own cadence. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Source platform campaign ID
        DuplicateAdCampaignRequest duplicateAdCampaignRequest = new DuplicateAdCampaignRequest(); // DuplicateAdCampaignRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key. 
        try {
            ApiResponse<DuplicateAdCampaign200Response> response = apiInstance.duplicateAdCampaignWithHttpInfo(campaignId, duplicateAdCampaignRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#duplicateAdCampaign");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Source platform campaign ID | |
| **duplicateAdCampaignRequest** | [**DuplicateAdCampaignRequest**](DuplicateAdCampaignRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key.  | [optional] |

### Return type

ApiResponse<[**DuplicateAdCampaign200Response**](DuplicateAdCampaign200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign duplicated |  -  |
| **400** | Invalid input |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | One of two refusals:  - &#x60;ads_allowance_exceeded&#x60;: the team has no payment method on file and has reached the 500 free live ads. Add a card to resume. - &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the ad account this request targets is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix &#x60;ad_account_not_selected&#x60;, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | Source campaign not found |  -  |
| **501** | Operation not supported on this platform |  -  |


## duplicateAdSet

> DuplicateAdSet200Response duplicateAdSet(adSetId, duplicateAdSetRequest, idempotencyKey)

Duplicate an ad set

Copies an ad set, optionally with its ads and into another campaign, created paused so you can review it before launch.  The copy is created paused so callers can review before launching. &#x60;campaignId&#x60; retargets the copy into another campaign; omitted &#x3D; the source&#39;s own campaign.  **Meta:** ads and creatives are included by default (&#x60;deepCopy: true&#x60;).  - The ad set is copied with Meta&#39;s &#x60;/copies&#x60; endpoint, then each of its ads (DELETED and ARCHIVED ones are skipped) into the new ad set. - So an ad set with any number of ads copies: Meta refuses a single deep copy of 3 or more objects. - &#x60;statusOption&#x60; applies to the ad set and every ad. - If an ad copy fails, the partial ad set copy is deleted and the request fails with Meta&#39;s error. - Sync discovery is triggered automatically (&#x60;syncAfter: false&#x60; to skip).  TikTok: the ad group is read and recreated under the campaign with its targeting, bidding, budget and schedule (start reset to now); &#x60;deepCopy: true&#x60; recreates its ads too (default false). &#x60;startTime&#x60;, &#x60;endTime&#x60; and &#x60;renameStrategy&#x60; are ignored and &#x60;statusOption&#x60; must be PAUSED or absent. The copy appears on the next discovery sync. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Source platform ad set ID
        DuplicateAdSetRequest duplicateAdSetRequest = new DuplicateAdSetRequest(); // DuplicateAdSetRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key. 
        try {
            DuplicateAdSet200Response result = apiInstance.duplicateAdSet(adSetId, duplicateAdSetRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#duplicateAdSet");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adSetId** | **String**| Source platform ad set ID | |
| **duplicateAdSetRequest** | [**DuplicateAdSetRequest**](DuplicateAdSetRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key.  | [optional] |

### Return type

[**DuplicateAdSet200Response**](DuplicateAdSet200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad set duplicated |  -  |
| **400** | Invalid input |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Forbidden. Codes:  - &#x60;ads_allowance_exceeded&#x60;: the team has no payment method on file and has reached the 500 free live ads. Add a card to resume. - &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix &#x60;ad_account_not_selected&#x60;, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | Source ad set not found |  -  |
| **501** | Only supported on Meta (facebook/instagram) and TikTok |  -  |

## duplicateAdSetWithHttpInfo

> ApiResponse<DuplicateAdSet200Response> duplicateAdSet duplicateAdSetWithHttpInfo(adSetId, duplicateAdSetRequest, idempotencyKey)

Duplicate an ad set

Copies an ad set, optionally with its ads and into another campaign, created paused so you can review it before launch.  The copy is created paused so callers can review before launching. &#x60;campaignId&#x60; retargets the copy into another campaign; omitted &#x3D; the source&#39;s own campaign.  **Meta:** ads and creatives are included by default (&#x60;deepCopy: true&#x60;).  - The ad set is copied with Meta&#39;s &#x60;/copies&#x60; endpoint, then each of its ads (DELETED and ARCHIVED ones are skipped) into the new ad set. - So an ad set with any number of ads copies: Meta refuses a single deep copy of 3 or more objects. - &#x60;statusOption&#x60; applies to the ad set and every ad. - If an ad copy fails, the partial ad set copy is deleted and the request fails with Meta&#39;s error. - Sync discovery is triggered automatically (&#x60;syncAfter: false&#x60; to skip).  TikTok: the ad group is read and recreated under the campaign with its targeting, bidding, budget and schedule (start reset to now); &#x60;deepCopy: true&#x60; recreates its ads too (default false). &#x60;startTime&#x60;, &#x60;endTime&#x60; and &#x60;renameStrategy&#x60; are ignored and &#x60;statusOption&#x60; must be PAUSED or absent. The copy appears on the next discovery sync. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Source platform ad set ID
        DuplicateAdSetRequest duplicateAdSetRequest = new DuplicateAdSetRequest(); // DuplicateAdSetRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key. 
        try {
            ApiResponse<DuplicateAdSet200Response> response = apiInstance.duplicateAdSetWithHttpInfo(adSetId, duplicateAdSetRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#duplicateAdSet");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adSetId** | **String**| Source platform ad set ID | |
| **duplicateAdSetRequest** | [**DuplicateAdSetRequest**](DuplicateAdSetRequest.md)|  | |
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes retries safe.  - Same key + same body: replays the original response. - Same key + different body: 422. - Key still processing: 409.  Only 2xx responses are stored, so a request that failed with a 4xx can be retried with a corrected body under the SAME key.  | [optional] |

### Return type

ApiResponse<[**DuplicateAdSet200Response**](DuplicateAdSet200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad set duplicated |  -  |
| **400** | Invalid input |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Forbidden. Codes:  - &#x60;ads_allowance_exceeded&#x60;: the team has no payment method on file and has reached the 500 free live ads. Add a card to resume. - &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix &#x60;ad_account_not_selected&#x60;, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | Source ad set not found |  -  |
| **501** | Only supported on Meta (facebook/instagram) and TikTok |  -  |


## editGoogleAssetGroupAssets

> EditGoogleAssetGroupAssets200Response editGoogleAssetGroupAssets(campaignId, assetGroupId, editGoogleAssetGroupAssetsRequest)

Link or unlink asset group assets

Links new or existing assets to a Performance Max asset group and unlinks others in one change, keeping unlinked assets in the account library.  Link existing assets or new content to the asset group, and unlink assets, in one atomic request.  - Links are applied before unlinks, so swapping the last asset of a role does not trip Google&#39;s per-role minimum. - Unlinking removes the link only; the asset stays in the account library. - validateOnly: true validates without writing. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Google Ads campaign id.
        String assetGroupId = "assetGroupId_example"; // String | Google asset group id.
        EditGoogleAssetGroupAssetsRequest editGoogleAssetGroupAssetsRequest = new EditGoogleAssetGroupAssetsRequest(); // EditGoogleAssetGroupAssetsRequest | 
        try {
            EditGoogleAssetGroupAssets200Response result = apiInstance.editGoogleAssetGroupAssets(campaignId, assetGroupId, editGoogleAssetGroupAssetsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#editGoogleAssetGroupAssets");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Google Ads campaign id. | |
| **assetGroupId** | **String**| Google asset group id. | |
| **editGoogleAssetGroupAssetsRequest** | [**EditGoogleAssetGroupAssetsRequest**](EditGoogleAssetGroupAssetsRequest.md)|  | |

### Return type

[**EditGoogleAssetGroupAssets200Response**](EditGoogleAssetGroupAssets200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Links applied (or validated). |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **404** | Resource not found |  -  |
| **422** | Google Ads connection needs reconnecting. |  -  |
| **429** | Google quota or the Zernio Google operations burst limit is exhausted. |  -  |
| **501** | Campaign is not on Google Ads. |  -  |

## editGoogleAssetGroupAssetsWithHttpInfo

> ApiResponse<EditGoogleAssetGroupAssets200Response> editGoogleAssetGroupAssets editGoogleAssetGroupAssetsWithHttpInfo(campaignId, assetGroupId, editGoogleAssetGroupAssetsRequest)

Link or unlink asset group assets

Links new or existing assets to a Performance Max asset group and unlinks others in one change, keeping unlinked assets in the account library.  Link existing assets or new content to the asset group, and unlink assets, in one atomic request.  - Links are applied before unlinks, so swapping the last asset of a role does not trip Google&#39;s per-role minimum. - Unlinking removes the link only; the asset stays in the account library. - validateOnly: true validates without writing. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Google Ads campaign id.
        String assetGroupId = "assetGroupId_example"; // String | Google asset group id.
        EditGoogleAssetGroupAssetsRequest editGoogleAssetGroupAssetsRequest = new EditGoogleAssetGroupAssetsRequest(); // EditGoogleAssetGroupAssetsRequest | 
        try {
            ApiResponse<EditGoogleAssetGroupAssets200Response> response = apiInstance.editGoogleAssetGroupAssetsWithHttpInfo(campaignId, assetGroupId, editGoogleAssetGroupAssetsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#editGoogleAssetGroupAssets");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Google Ads campaign id. | |
| **assetGroupId** | **String**| Google asset group id. | |
| **editGoogleAssetGroupAssetsRequest** | [**EditGoogleAssetGroupAssetsRequest**](EditGoogleAssetGroupAssetsRequest.md)|  | |

### Return type

ApiResponse<[**EditGoogleAssetGroupAssets200Response**](EditGoogleAssetGroupAssets200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Links applied (or validated). |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **404** | Resource not found |  -  |
| **422** | Google Ads connection needs reconnecting. |  -  |
| **429** | Google quota or the Zernio Google operations burst limit is exhausted. |  -  |
| **501** | Campaign is not on Google Ads. |  -  |


## getAd

> GetAd200Response getAd(adId, live, accountId)

Get ad details

Shows one ad with its creative, targeting, status and performance metrics.  ### Google Search ads  Google Search ads include current creative.headlines, creative.descriptions and creative.finalUrls, preserving pinnedField. Top-level cachedAt and stale report cache freshness. Google mutations invalidate this read.  RSA enrichment requires a stored advertisingChannelType of SEARCH. Ads with an unknown or other channel return their stored details without a Google read. If RSA enrichment fails, the stored ad is returned with HTTP 200 and without cache metadata.  ### Accepted ad ids  The &#x60;{adId}&#x60; path segment accepts any identifier dialect Zernio indexes for the ad:  - the Zernio internal &#x60;_id&#x60; (24-char hex) - Meta&#39;s numeric &#x60;platformAdId&#x60; (the value shipped in &#x60;comment.received&#x60; webhooks as &#x60;comment.ad.id&#x60;) - the creative&#39;s &#x60;effective_object_story_id&#x60; (&#x60;{pageId}_{postId}&#x60; shape, Facebook side) - the creative&#39;s &#x60;effective_instagram_media_id&#x60; (Instagram side) - an Instagram media id an ad comment arrived on (&#x60;comment.platformPostId&#x60; of a &#x60;comment.received&#x60; carrying &#x60;comment.ad.id&#x60;), including the extra media Meta creates for placement variants  Any of these resolve to the same ad, so the caller doesn&#39;t need a translation step.  &#x60;creative.creativeFeatures&#x60; holds the stored requested settings, which do not confirm platform application.  ### Facebook ad dark posts  Meta gives an ad with per-placement assets one extra unpublished post per placement, and comments land on it. Meta exposes no link from that post to its ad.  - When exactly one ad on the Page, created before the dark post, carries the same copy as the post, the dark post id resolves to that ad. - Otherwise, when the id is a dark post Zernio has seen comments on and its Page is connected, the response is &#x60;ad: null&#x60; plus &#x60;darkPost&#x60;. It carries the Meta Ads account and the ad accounts running ads for that Page.  Read its comments with GET /v1/ads/{adId}/comments using the same id.  ### Status freshness  &#x60;status&#x60;, &#x60;configuredStatus&#x60;, &#x60;platformStatus&#x60;, &#x60;platformAdSetStatus&#x60; and &#x60;platformCampaignStatus&#x60; are the values Zernio last stored.  Background sync refreshes them, typically within 15 to 60 minutes (Google up to about 3 hours), and ended or long-paused objects may be refreshed less often.  Zernio&#39;s own status writes re-read the switches they change. A change made in the platform&#39;s own ads manager therefore shows up here only after the next sync.  Controllers that act on a switch should pass &#x60;live&#x3D;true&#x60;. It reads the switches from the platform now, stores them, and returns &#x60;statusReadAt&#x60; (null when the read failed and the stored values were returned).  With &#x60;live&#x3D;true&#x60; these are read live:  - the ad&#39;s own switch (&#x60;configuredStatus&#x60;) - its delivery status (&#x60;status&#x60;, &#x60;platformStatus&#x60;) - its ad set and campaign switches (&#x60;platformAdSetStatus&#x60;, &#x60;platformCampaignStatus&#x60;)  ### Meta ads that are not synced yet  Pass &#x60;accountId&#x60; with a Meta &#x60;platformAdId&#x60; to read an ad Zernio has not synced (for example one created in Ads Manager on an ad account reached only through a Facebook connection).  The ad is read live from Meta and mapped exactly like a synced row: name, &#x60;status&#x60;, &#x60;platformStatus&#x60;, &#x60;configuredStatus&#x60;, &#x60;platformAdSetId&#x60;, &#x60;platformCampaignId&#x60;, campaign and ad set names, budgets, and &#x60;creative&#x60; with its &#x60;id&#x60;, body, link, image and video.  It comes back with &#x60;synced: false&#x60;, no &#x60;id&#x60; (it has no Zernio row) and &#x60;statusReadAt&#x60; set to the time of the read. Synced ads answer &#x60;synced: true&#x60;.  Only a numeric id takes this path, so dark post ids (&#x60;{pageId}_{postId}&#x60;) keep the dark post lookup above. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adId = "adId_example"; // String | Zernio `_id` (hex), Meta `platformAdId` (numeric), or one of the creative's effective story/media IDs. See description for details. 
        Boolean live = false; // Boolean | Read the on/off switches live from the platform instead of returning synced values. See \"Status freshness\" in the operation description.  - The fresh values are stored (later reads return them too), and the response carries `statusReadAt`, the time of the read. - At most 20 platform objects are read per request. - Where a read fails (credentials, platform error, no reader on that platform), stored values come back with `statusReadAt: null`.  **On X** the budget is read live too:  - GET /v1/ads/{adId}: `budget`, `adSetBudget`, `campaignBudget` and `budgetLevel` are the line item and campaign budgets X holds now (stored like the switches). - Ad set and campaign listings: `budget` is what that line item or campaign holds now (returned, not stored). A row whose budget the other level holds keeps its synced `budget`. 
        String accountId = "accountId_example"; // String | Meta only. A Zernio connection id (Meta Ads or Facebook connection) used when `{adId}` is a Meta ad not in Zernio's synced store, e.g. an Ads Manager ad on an ad account reached only through a Facebook connection.  The ad is then read live from Meta through that connection, and the response carries `synced: false`. Ads Meta reports as DELETED are returned too, with their status.  Same rules as GET /v1/ads/campaigns/{campaignId}:  - Connection on a profile the API key cannot access: 404. - Ad on an ad account outside the connection's selected ad accounts: 403 `ad_account_not_selected`. - Id Meta cannot read through the connection, or not an ad (e.g. a campaign or ad set id): 404 `ad_not_found`. - Connection that is not Meta: 501.  Ignored when the ad is in the store (its own connection is used). Without it, an unsynced ad answers 404 `ad_not_found`. Writes (PUT, DELETE, status) still need the ad in the store. 
        try {
            GetAd200Response result = apiInstance.getAd(adId, live, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getAd");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adId** | **String**| Zernio &#x60;_id&#x60; (hex), Meta &#x60;platformAdId&#x60; (numeric), or one of the creative&#39;s effective story/media IDs. See description for details.  | |
| **live** | **Boolean**| Read the on/off switches live from the platform instead of returning synced values. See \&quot;Status freshness\&quot; in the operation description.  - The fresh values are stored (later reads return them too), and the response carries &#x60;statusReadAt&#x60;, the time of the read. - At most 20 platform objects are read per request. - Where a read fails (credentials, platform error, no reader on that platform), stored values come back with &#x60;statusReadAt: null&#x60;.  **On X** the budget is read live too:  - GET /v1/ads/{adId}: &#x60;budget&#x60;, &#x60;adSetBudget&#x60;, &#x60;campaignBudget&#x60; and &#x60;budgetLevel&#x60; are the line item and campaign budgets X holds now (stored like the switches). - Ad set and campaign listings: &#x60;budget&#x60; is what that line item or campaign holds now (returned, not stored). A row whose budget the other level holds keeps its synced &#x60;budget&#x60;.  | [optional] [default to false] |
| **accountId** | **String**| Meta only. A Zernio connection id (Meta Ads or Facebook connection) used when &#x60;{adId}&#x60; is a Meta ad not in Zernio&#39;s synced store, e.g. an Ads Manager ad on an ad account reached only through a Facebook connection.  The ad is then read live from Meta through that connection, and the response carries &#x60;synced: false&#x60;. Ads Meta reports as DELETED are returned too, with their status.  Same rules as GET /v1/ads/campaigns/{campaignId}:  - Connection on a profile the API key cannot access: 404. - Ad on an ad account outside the connection&#39;s selected ad accounts: 403 &#x60;ad_account_not_selected&#x60;. - Id Meta cannot read through the connection, or not an ad (e.g. a campaign or ad set id): 404 &#x60;ad_not_found&#x60;. - Connection that is not Meta: 501.  Ignored when the ad is in the store (its own connection is used). Without it, an unsynced ad answers 404 &#x60;ad_not_found&#x60;. Writes (PUT, DELETE, status) still need the ad in the store.  | [optional] |

### Return type

[**GetAd200Response**](GetAd200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad details |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **404** | Resource not found |  -  |
| **501** | &#x60;accountId&#x60; names a connection that is not Meta (unsynced ad reads are Meta only). |  -  |

## getAdWithHttpInfo

> ApiResponse<GetAd200Response> getAd getAdWithHttpInfo(adId, live, accountId)

Get ad details

Shows one ad with its creative, targeting, status and performance metrics.  ### Google Search ads  Google Search ads include current creative.headlines, creative.descriptions and creative.finalUrls, preserving pinnedField. Top-level cachedAt and stale report cache freshness. Google mutations invalidate this read.  RSA enrichment requires a stored advertisingChannelType of SEARCH. Ads with an unknown or other channel return their stored details without a Google read. If RSA enrichment fails, the stored ad is returned with HTTP 200 and without cache metadata.  ### Accepted ad ids  The &#x60;{adId}&#x60; path segment accepts any identifier dialect Zernio indexes for the ad:  - the Zernio internal &#x60;_id&#x60; (24-char hex) - Meta&#39;s numeric &#x60;platformAdId&#x60; (the value shipped in &#x60;comment.received&#x60; webhooks as &#x60;comment.ad.id&#x60;) - the creative&#39;s &#x60;effective_object_story_id&#x60; (&#x60;{pageId}_{postId}&#x60; shape, Facebook side) - the creative&#39;s &#x60;effective_instagram_media_id&#x60; (Instagram side) - an Instagram media id an ad comment arrived on (&#x60;comment.platformPostId&#x60; of a &#x60;comment.received&#x60; carrying &#x60;comment.ad.id&#x60;), including the extra media Meta creates for placement variants  Any of these resolve to the same ad, so the caller doesn&#39;t need a translation step.  &#x60;creative.creativeFeatures&#x60; holds the stored requested settings, which do not confirm platform application.  ### Facebook ad dark posts  Meta gives an ad with per-placement assets one extra unpublished post per placement, and comments land on it. Meta exposes no link from that post to its ad.  - When exactly one ad on the Page, created before the dark post, carries the same copy as the post, the dark post id resolves to that ad. - Otherwise, when the id is a dark post Zernio has seen comments on and its Page is connected, the response is &#x60;ad: null&#x60; plus &#x60;darkPost&#x60;. It carries the Meta Ads account and the ad accounts running ads for that Page.  Read its comments with GET /v1/ads/{adId}/comments using the same id.  ### Status freshness  &#x60;status&#x60;, &#x60;configuredStatus&#x60;, &#x60;platformStatus&#x60;, &#x60;platformAdSetStatus&#x60; and &#x60;platformCampaignStatus&#x60; are the values Zernio last stored.  Background sync refreshes them, typically within 15 to 60 minutes (Google up to about 3 hours), and ended or long-paused objects may be refreshed less often.  Zernio&#39;s own status writes re-read the switches they change. A change made in the platform&#39;s own ads manager therefore shows up here only after the next sync.  Controllers that act on a switch should pass &#x60;live&#x3D;true&#x60;. It reads the switches from the platform now, stores them, and returns &#x60;statusReadAt&#x60; (null when the read failed and the stored values were returned).  With &#x60;live&#x3D;true&#x60; these are read live:  - the ad&#39;s own switch (&#x60;configuredStatus&#x60;) - its delivery status (&#x60;status&#x60;, &#x60;platformStatus&#x60;) - its ad set and campaign switches (&#x60;platformAdSetStatus&#x60;, &#x60;platformCampaignStatus&#x60;)  ### Meta ads that are not synced yet  Pass &#x60;accountId&#x60; with a Meta &#x60;platformAdId&#x60; to read an ad Zernio has not synced (for example one created in Ads Manager on an ad account reached only through a Facebook connection).  The ad is read live from Meta and mapped exactly like a synced row: name, &#x60;status&#x60;, &#x60;platformStatus&#x60;, &#x60;configuredStatus&#x60;, &#x60;platformAdSetId&#x60;, &#x60;platformCampaignId&#x60;, campaign and ad set names, budgets, and &#x60;creative&#x60; with its &#x60;id&#x60;, body, link, image and video.  It comes back with &#x60;synced: false&#x60;, no &#x60;id&#x60; (it has no Zernio row) and &#x60;statusReadAt&#x60; set to the time of the read. Synced ads answer &#x60;synced: true&#x60;.  Only a numeric id takes this path, so dark post ids (&#x60;{pageId}_{postId}&#x60;) keep the dark post lookup above. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adId = "adId_example"; // String | Zernio `_id` (hex), Meta `platformAdId` (numeric), or one of the creative's effective story/media IDs. See description for details. 
        Boolean live = false; // Boolean | Read the on/off switches live from the platform instead of returning synced values. See \"Status freshness\" in the operation description.  - The fresh values are stored (later reads return them too), and the response carries `statusReadAt`, the time of the read. - At most 20 platform objects are read per request. - Where a read fails (credentials, platform error, no reader on that platform), stored values come back with `statusReadAt: null`.  **On X** the budget is read live too:  - GET /v1/ads/{adId}: `budget`, `adSetBudget`, `campaignBudget` and `budgetLevel` are the line item and campaign budgets X holds now (stored like the switches). - Ad set and campaign listings: `budget` is what that line item or campaign holds now (returned, not stored). A row whose budget the other level holds keeps its synced `budget`. 
        String accountId = "accountId_example"; // String | Meta only. A Zernio connection id (Meta Ads or Facebook connection) used when `{adId}` is a Meta ad not in Zernio's synced store, e.g. an Ads Manager ad on an ad account reached only through a Facebook connection.  The ad is then read live from Meta through that connection, and the response carries `synced: false`. Ads Meta reports as DELETED are returned too, with their status.  Same rules as GET /v1/ads/campaigns/{campaignId}:  - Connection on a profile the API key cannot access: 404. - Ad on an ad account outside the connection's selected ad accounts: 403 `ad_account_not_selected`. - Id Meta cannot read through the connection, or not an ad (e.g. a campaign or ad set id): 404 `ad_not_found`. - Connection that is not Meta: 501.  Ignored when the ad is in the store (its own connection is used). Without it, an unsynced ad answers 404 `ad_not_found`. Writes (PUT, DELETE, status) still need the ad in the store. 
        try {
            ApiResponse<GetAd200Response> response = apiInstance.getAdWithHttpInfo(adId, live, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getAd");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adId** | **String**| Zernio &#x60;_id&#x60; (hex), Meta &#x60;platformAdId&#x60; (numeric), or one of the creative&#39;s effective story/media IDs. See description for details.  | |
| **live** | **Boolean**| Read the on/off switches live from the platform instead of returning synced values. See \&quot;Status freshness\&quot; in the operation description.  - The fresh values are stored (later reads return them too), and the response carries &#x60;statusReadAt&#x60;, the time of the read. - At most 20 platform objects are read per request. - Where a read fails (credentials, platform error, no reader on that platform), stored values come back with &#x60;statusReadAt: null&#x60;.  **On X** the budget is read live too:  - GET /v1/ads/{adId}: &#x60;budget&#x60;, &#x60;adSetBudget&#x60;, &#x60;campaignBudget&#x60; and &#x60;budgetLevel&#x60; are the line item and campaign budgets X holds now (stored like the switches). - Ad set and campaign listings: &#x60;budget&#x60; is what that line item or campaign holds now (returned, not stored). A row whose budget the other level holds keeps its synced &#x60;budget&#x60;.  | [optional] [default to false] |
| **accountId** | **String**| Meta only. A Zernio connection id (Meta Ads or Facebook connection) used when &#x60;{adId}&#x60; is a Meta ad not in Zernio&#39;s synced store, e.g. an Ads Manager ad on an ad account reached only through a Facebook connection.  The ad is then read live from Meta through that connection, and the response carries &#x60;synced: false&#x60;. Ads Meta reports as DELETED are returned too, with their status.  Same rules as GET /v1/ads/campaigns/{campaignId}:  - Connection on a profile the API key cannot access: 404. - Ad on an ad account outside the connection&#39;s selected ad accounts: 403 &#x60;ad_account_not_selected&#x60;. - Id Meta cannot read through the connection, or not an ad (e.g. a campaign or ad set id): 404 &#x60;ad_not_found&#x60;. - Connection that is not Meta: 501.  Ignored when the ad is in the store (its own connection is used). Without it, an unsynced ad answers 404 &#x60;ad_not_found&#x60;. Writes (PUT, DELETE, status) still need the ad in the store.  | [optional] |

### Return type

ApiResponse<[**GetAd200Response**](GetAd200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad details |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **404** | Resource not found |  -  |
| **501** | &#x60;accountId&#x60; names a connection that is not Meta (unsynced ad reads are Meta only). |  -  |


## getAdCampaignDetails

> GetAdCampaignDetails200Response getAdCampaignDetails(campaignId, accountId, fields)

Get live campaign details

Shows a Meta campaign&#39;s current settings straight from Meta, such as its objective, budget, bid strategy, schedule and delivery issues.  It reads one campaign live from Meta, returned verbatim, so a caller that knows a campaign id no longer has to page &#x60;GET /v1/ads/campaigns&#x60; to find it.  The default projection covers name, status, objective, buying type, bid strategy, budgets, spend cap, schedule and &#x60;issues_info&#x60;.  ### Fields and errors  - &#x60;fields&#x60; is a raw-passthrough override; unknown fields return Meta&#39;s 400 verbatim. - A campaign the resolved connection cannot see comes back as Meta&#39;s own 400, not a 404. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Meta campaign id (platformCampaignId).
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String fields = "id,name,status,daily_budget"; // String | Comma-separated Graph field override. Supports nested {} projections and Graph field modifiers.
        try {
            GetAdCampaignDetails200Response result = apiInstance.getAdCampaignDetails(campaignId, accountId, fields);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getAdCampaignDetails");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Meta campaign id (platformCampaignId). | |
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **fields** | **String**| Comma-separated Graph field override. Supports nested {} projections and Graph field modifiers. | [optional] |

### Return type

[**GetAdCampaignDetails200Response**](GetAdCampaignDetails200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | The campaign as returned by Meta |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## getAdCampaignDetailsWithHttpInfo

> ApiResponse<GetAdCampaignDetails200Response> getAdCampaignDetails getAdCampaignDetailsWithHttpInfo(campaignId, accountId, fields)

Get live campaign details

Shows a Meta campaign&#39;s current settings straight from Meta, such as its objective, budget, bid strategy, schedule and delivery issues.  It reads one campaign live from Meta, returned verbatim, so a caller that knows a campaign id no longer has to page &#x60;GET /v1/ads/campaigns&#x60; to find it.  The default projection covers name, status, objective, buying type, bid strategy, budgets, spend cap, schedule and &#x60;issues_info&#x60;.  ### Fields and errors  - &#x60;fields&#x60; is a raw-passthrough override; unknown fields return Meta&#39;s 400 verbatim. - A campaign the resolved connection cannot see comes back as Meta&#39;s own 400, not a 404. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Meta campaign id (platformCampaignId).
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String fields = "id,name,status,daily_budget"; // String | Comma-separated Graph field override. Supports nested {} projections and Graph field modifiers.
        try {
            ApiResponse<GetAdCampaignDetails200Response> response = apiInstance.getAdCampaignDetailsWithHttpInfo(campaignId, accountId, fields);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getAdCampaignDetails");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Meta campaign id (platformCampaignId). | |
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **fields** | **String**| Comma-separated Graph field override. Supports nested {} projections and Graph field modifiers. | [optional] |

### Return type

ApiResponse<[**GetAdCampaignDetails200Response**](GetAdCampaignDetails200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | The campaign as returned by Meta |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## getAdReview

> GetAdReview200Response getAdReview(adId, accountId)

Read the platform&#39;s review verdict for an ad

Shows whether the platform approved an ad, where it may not deliver, and every rejection reason, without re-enabling a paused ad.  It reads the ad&#39;s review verdict from the platform now, including every rejection reason with TikTok&#39;s suggestion and the piece of content it refers to. It is read-only, so it works on a paused ad without re-enabling it.  Supported on TikTok, Google and Meta. Other platforms return 501.  ### Google  Reads &#x60;ad_group_ad.policy_summary&#x60; live. &#x60;approvalStatus&#x60; and &#x60;reviewStatus&#x60; are Google&#39;s verbatim:  - &#x60;approvalStatus&#x60;: APPROVED, APPROVED_LIMITED, AREA_OF_INTEREST_ONLY, DISAPPROVED, UNKNOWN. - &#x60;reviewStatus&#x60;: REVIEW_IN_PROGRESS, REVIEWED, UNDER_APPEAL, ELIGIBLE_MAY_SERVE. - &#x60;approved&#x60;: true for the three approved statuses, false for DISAPPROVED, null otherwise.  &#x60;policyTopics&#x60; carries every policy topic entry with its &#x60;type&#x60; (PROHIBITED, LIMITED, ...) and Google&#39;s &#x60;evidences&#x60; and &#x60;constraints&#x60; verbatim. Each PROHIBITED topic is also listed in &#x60;rejections&#x60; (reason &#x3D; the topic).  The &#x60;forbidden*&#x60; arrays are TikTok-only and always empty on Google.  ### Meta (Facebook and Instagram ads)  Reads the Ad&#39;s &#x60;ad_review_feedback&#x60;, &#x60;effective_status&#x60; and &#x60;issues_info&#x60; live.  - &#x60;reviewStatus&#x60;: Meta&#39;s &#x60;effective_status&#x60; verbatim (ACTIVE, PAUSED, PENDING_REVIEW, DISAPPROVED, PREAPPROVED, WITH_ISSUES, IN_PROCESS, ...). - &#x60;approved&#x60;: true for ACTIVE and PREAPPROVED, false for DISAPPROVED, null otherwise. - &#x60;reviewFeedback&#x60;: Meta&#39;s feedback verbatim, as &#x60;global&#x60; (reason -&gt; explanation) and &#x60;placementSpecific&#x60; (placement -&gt; reason -&gt; explanation). - &#x60;issues&#x60;: Meta&#39;s &#x60;issues_info&#x60; verbatim.  Each global reason is listed in &#x60;rejections&#x60;, and so is each placement-specific reason, with that placement in its &#x60;forbiddenPlacements&#x60;. The review&#39;s &#x60;forbiddenPlacements&#x60; lists every placement with feedback.  &#x60;forbiddenAges&#x60;, &#x60;forbiddenLocations&#x60; and &#x60;forbiddenOperatingSystems&#x60; are always empty on Meta.  When Meta returns no feedback (usually an ad in review or approved everywhere), the status comes back with empty &#x60;rejections&#x60; and empty &#x60;reviewFeedback&#x60; maps. An ACTIVE ad rejected on one placement still carries that placement&#39;s feedback.  The &#x60;effective_status&#x60; read is also stored on the ad, so &#x60;GET /v1/ads/{adId}&#x60; returns it next. A deleted ad answers 404.  ### Meta ads that are not synced yet  Pass &#x60;accountId&#x60; with a Meta platform ad id that is not in Zernio&#39;s store to read its review live through that connection. The response then has &#x60;adId: null&#x60;, &#x60;synced: false&#x60;, and nothing is stored. Synced ads answer &#x60;synced: true&#x60;.  ### TikTok  TikTok uses &#x60;/ad/review_info/&#x60;. Use it alongside the ad&#39;s &#x60;platformStatus&#x60;:  - &#x60;AD_STATUS_AUDIT&#x60;: the ad is in review (maps to &#x60;status: pending_review&#x60;). - &#x60;AD_STATUS_AD_PRE_ONLINE&#x60;: it passed and is about to deliver (also maps to &#x60;status: pending_review&#x60;). - &#x60;AD_STATUS_AUDIT_DENY&#x60;: maps to &#x60;rejected&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adId = "adId_example"; // String | Zernio ad id (24-char hex) or the platform ad id.
        String accountId = "accountId_example"; // String | Meta only. A Zernio connection id (Meta Ads or Facebook connection) used when `{adId}` is a Meta ad not in Zernio's synced store, e.g. an Ads Manager ad on an ad account reached only through a Facebook connection.  The ad is then read live from Meta through that connection, and the response carries `synced: false`. Ads Meta reports as DELETED are returned too, with their status.  Same rules as GET /v1/ads/campaigns/{campaignId}:  - Connection on a profile the API key cannot access: 404. - Ad on an ad account outside the connection's selected ad accounts: 403 `ad_account_not_selected`. - Id Meta cannot read through the connection, or not an ad (e.g. a campaign or ad set id): 404 `ad_not_found`. - Connection that is not Meta: 501.  Ignored when the ad is in the store (its own connection is used). Without it, an unsynced ad answers 404 `ad_not_found`. Writes (PUT, DELETE, status) still need the ad in the store. 
        try {
            GetAdReview200Response result = apiInstance.getAdReview(adId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getAdReview");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adId** | **String**| Zernio ad id (24-char hex) or the platform ad id. | |
| **accountId** | **String**| Meta only. A Zernio connection id (Meta Ads or Facebook connection) used when &#x60;{adId}&#x60; is a Meta ad not in Zernio&#39;s synced store, e.g. an Ads Manager ad on an ad account reached only through a Facebook connection.  The ad is then read live from Meta through that connection, and the response carries &#x60;synced: false&#x60;. Ads Meta reports as DELETED are returned too, with their status.  Same rules as GET /v1/ads/campaigns/{campaignId}:  - Connection on a profile the API key cannot access: 404. - Ad on an ad account outside the connection&#39;s selected ad accounts: 403 &#x60;ad_account_not_selected&#x60;. - Id Meta cannot read through the connection, or not an ad (e.g. a campaign or ad set id): 404 &#x60;ad_not_found&#x60;. - Connection that is not Meta: 501.  Ignored when the ad is in the store (its own connection is used). Without it, an unsynced ad answers 404 &#x60;ad_not_found&#x60;. Writes (PUT, DELETE, status) still need the ad in the store.  | [optional] |

### Return type

[**GetAdReview200Response**](GetAdReview200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **200** | The review verdict |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Ad not found, it has no platform ad id yet, or the platform has no review record for it |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted. Behavior per platform:  - **Reddit:** rate-limits per connected Reddit user (1000 requests per 10-minute window), shared by every operation on that account. Retry after the window resets; repeated calls while exhausted do not succeed and keep the budget spent. - **Google Ads:** writes and reports run on one developer token shared by every Google Ads account on Zernio. It holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. - **Google Ads envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **YouTube Analytics:** reads (channel-insights, demographics, daily-views, video-retention) use the \&quot;Queries per day\&quot; quota of the Google Cloud project the account is connected through, shared with other Zernio customers, so a 429 is not your own volume. Resets at midnight Pacific Time. - **YouTube Analytics envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaExhausted: true&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60;, &#x60;details.resetsAt&#x60; and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **Meta ads:** every Meta throttle (codes 4, 17, 32, 613 and business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when sent, else Meta&#39;s 60-second minimum (30 seconds for the one-write-per-30-seconds limit on one object). - **Pinterest ads:** limits per user and app, per category (ads_read, ads_write, ads_analytics). &#x60;Retry-After&#x60; comes from Pinterest&#39;s &#x60;x-ratelimit-reset&#x60; when sent, otherwise 60 seconds. - **TikTok ads:** limits per app and per endpoint (per second, minute and day), answering overage with code 40100 or code 40002 &#x60;OVER_QPS_LIMIT&#x60;. Both return 429 &#x60;rate_limited&#x60; with &#x60;platform: tiktok&#x60; and &#x60;Retry-After: 10&#x60;. Space out bulk reads (e.g. one ad at a time per advertiser) instead of retrying at once.  **TikTok Smart+ review read** (&#x60;GET /v1/ads/{adId}/tiktok-smart-plus-review&#x60;) has its own stricter TikTok quota. After an overage, Zernio answers 429 for that advertiser and connection without calling TikTok for about 60 seconds, then 120, up to 240 while TikTok keeps refusing, each with up to 10% random jitter.  A successful call holds nothing back; the next overage pauses about 60 seconds again. &#x60;Retry-After&#x60; is the time left. The advertiser-wide read (&#x60;GET /v1/ads/tiktok-smart-plus-reviews&#x60;) answers 200 with &#x60;retryAfterSeconds&#x60; and &#x60;refreshState&#x60; instead. Keep one request in flight per advertiser there.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |
| **501** | Only supported on TikTok, Google and Meta (Facebook and Instagram ads). &#x60;accountId&#x60; naming a connection that is not Meta also answers 501. |  -  |

## getAdReviewWithHttpInfo

> ApiResponse<GetAdReview200Response> getAdReview getAdReviewWithHttpInfo(adId, accountId)

Read the platform&#39;s review verdict for an ad

Shows whether the platform approved an ad, where it may not deliver, and every rejection reason, without re-enabling a paused ad.  It reads the ad&#39;s review verdict from the platform now, including every rejection reason with TikTok&#39;s suggestion and the piece of content it refers to. It is read-only, so it works on a paused ad without re-enabling it.  Supported on TikTok, Google and Meta. Other platforms return 501.  ### Google  Reads &#x60;ad_group_ad.policy_summary&#x60; live. &#x60;approvalStatus&#x60; and &#x60;reviewStatus&#x60; are Google&#39;s verbatim:  - &#x60;approvalStatus&#x60;: APPROVED, APPROVED_LIMITED, AREA_OF_INTEREST_ONLY, DISAPPROVED, UNKNOWN. - &#x60;reviewStatus&#x60;: REVIEW_IN_PROGRESS, REVIEWED, UNDER_APPEAL, ELIGIBLE_MAY_SERVE. - &#x60;approved&#x60;: true for the three approved statuses, false for DISAPPROVED, null otherwise.  &#x60;policyTopics&#x60; carries every policy topic entry with its &#x60;type&#x60; (PROHIBITED, LIMITED, ...) and Google&#39;s &#x60;evidences&#x60; and &#x60;constraints&#x60; verbatim. Each PROHIBITED topic is also listed in &#x60;rejections&#x60; (reason &#x3D; the topic).  The &#x60;forbidden*&#x60; arrays are TikTok-only and always empty on Google.  ### Meta (Facebook and Instagram ads)  Reads the Ad&#39;s &#x60;ad_review_feedback&#x60;, &#x60;effective_status&#x60; and &#x60;issues_info&#x60; live.  - &#x60;reviewStatus&#x60;: Meta&#39;s &#x60;effective_status&#x60; verbatim (ACTIVE, PAUSED, PENDING_REVIEW, DISAPPROVED, PREAPPROVED, WITH_ISSUES, IN_PROCESS, ...). - &#x60;approved&#x60;: true for ACTIVE and PREAPPROVED, false for DISAPPROVED, null otherwise. - &#x60;reviewFeedback&#x60;: Meta&#39;s feedback verbatim, as &#x60;global&#x60; (reason -&gt; explanation) and &#x60;placementSpecific&#x60; (placement -&gt; reason -&gt; explanation). - &#x60;issues&#x60;: Meta&#39;s &#x60;issues_info&#x60; verbatim.  Each global reason is listed in &#x60;rejections&#x60;, and so is each placement-specific reason, with that placement in its &#x60;forbiddenPlacements&#x60;. The review&#39;s &#x60;forbiddenPlacements&#x60; lists every placement with feedback.  &#x60;forbiddenAges&#x60;, &#x60;forbiddenLocations&#x60; and &#x60;forbiddenOperatingSystems&#x60; are always empty on Meta.  When Meta returns no feedback (usually an ad in review or approved everywhere), the status comes back with empty &#x60;rejections&#x60; and empty &#x60;reviewFeedback&#x60; maps. An ACTIVE ad rejected on one placement still carries that placement&#39;s feedback.  The &#x60;effective_status&#x60; read is also stored on the ad, so &#x60;GET /v1/ads/{adId}&#x60; returns it next. A deleted ad answers 404.  ### Meta ads that are not synced yet  Pass &#x60;accountId&#x60; with a Meta platform ad id that is not in Zernio&#39;s store to read its review live through that connection. The response then has &#x60;adId: null&#x60;, &#x60;synced: false&#x60;, and nothing is stored. Synced ads answer &#x60;synced: true&#x60;.  ### TikTok  TikTok uses &#x60;/ad/review_info/&#x60;. Use it alongside the ad&#39;s &#x60;platformStatus&#x60;:  - &#x60;AD_STATUS_AUDIT&#x60;: the ad is in review (maps to &#x60;status: pending_review&#x60;). - &#x60;AD_STATUS_AD_PRE_ONLINE&#x60;: it passed and is about to deliver (also maps to &#x60;status: pending_review&#x60;). - &#x60;AD_STATUS_AUDIT_DENY&#x60;: maps to &#x60;rejected&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adId = "adId_example"; // String | Zernio ad id (24-char hex) or the platform ad id.
        String accountId = "accountId_example"; // String | Meta only. A Zernio connection id (Meta Ads or Facebook connection) used when `{adId}` is a Meta ad not in Zernio's synced store, e.g. an Ads Manager ad on an ad account reached only through a Facebook connection.  The ad is then read live from Meta through that connection, and the response carries `synced: false`. Ads Meta reports as DELETED are returned too, with their status.  Same rules as GET /v1/ads/campaigns/{campaignId}:  - Connection on a profile the API key cannot access: 404. - Ad on an ad account outside the connection's selected ad accounts: 403 `ad_account_not_selected`. - Id Meta cannot read through the connection, or not an ad (e.g. a campaign or ad set id): 404 `ad_not_found`. - Connection that is not Meta: 501.  Ignored when the ad is in the store (its own connection is used). Without it, an unsynced ad answers 404 `ad_not_found`. Writes (PUT, DELETE, status) still need the ad in the store. 
        try {
            ApiResponse<GetAdReview200Response> response = apiInstance.getAdReviewWithHttpInfo(adId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getAdReview");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adId** | **String**| Zernio ad id (24-char hex) or the platform ad id. | |
| **accountId** | **String**| Meta only. A Zernio connection id (Meta Ads or Facebook connection) used when &#x60;{adId}&#x60; is a Meta ad not in Zernio&#39;s synced store, e.g. an Ads Manager ad on an ad account reached only through a Facebook connection.  The ad is then read live from Meta through that connection, and the response carries &#x60;synced: false&#x60;. Ads Meta reports as DELETED are returned too, with their status.  Same rules as GET /v1/ads/campaigns/{campaignId}:  - Connection on a profile the API key cannot access: 404. - Ad on an ad account outside the connection&#39;s selected ad accounts: 403 &#x60;ad_account_not_selected&#x60;. - Id Meta cannot read through the connection, or not an ad (e.g. a campaign or ad set id): 404 &#x60;ad_not_found&#x60;. - Connection that is not Meta: 501.  Ignored when the ad is in the store (its own connection is used). Without it, an unsynced ad answers 404 &#x60;ad_not_found&#x60;. Writes (PUT, DELETE, status) still need the ad in the store.  | [optional] |

### Return type

ApiResponse<[**GetAdReview200Response**](GetAdReview200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **200** | The review verdict |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Ad not found, it has no platform ad id yet, or the platform has no review record for it |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted. Behavior per platform:  - **Reddit:** rate-limits per connected Reddit user (1000 requests per 10-minute window), shared by every operation on that account. Retry after the window resets; repeated calls while exhausted do not succeed and keep the budget spent. - **Google Ads:** writes and reports run on one developer token shared by every Google Ads account on Zernio. It holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. - **Google Ads envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **YouTube Analytics:** reads (channel-insights, demographics, daily-views, video-retention) use the \&quot;Queries per day\&quot; quota of the Google Cloud project the account is connected through, shared with other Zernio customers, so a 429 is not your own volume. Resets at midnight Pacific Time. - **YouTube Analytics envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaExhausted: true&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60;, &#x60;details.resetsAt&#x60; and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **Meta ads:** every Meta throttle (codes 4, 17, 32, 613 and business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when sent, else Meta&#39;s 60-second minimum (30 seconds for the one-write-per-30-seconds limit on one object). - **Pinterest ads:** limits per user and app, per category (ads_read, ads_write, ads_analytics). &#x60;Retry-After&#x60; comes from Pinterest&#39;s &#x60;x-ratelimit-reset&#x60; when sent, otherwise 60 seconds. - **TikTok ads:** limits per app and per endpoint (per second, minute and day), answering overage with code 40100 or code 40002 &#x60;OVER_QPS_LIMIT&#x60;. Both return 429 &#x60;rate_limited&#x60; with &#x60;platform: tiktok&#x60; and &#x60;Retry-After: 10&#x60;. Space out bulk reads (e.g. one ad at a time per advertiser) instead of retrying at once.  **TikTok Smart+ review read** (&#x60;GET /v1/ads/{adId}/tiktok-smart-plus-review&#x60;) has its own stricter TikTok quota. After an overage, Zernio answers 429 for that advertiser and connection without calling TikTok for about 60 seconds, then 120, up to 240 while TikTok keeps refusing, each with up to 10% random jitter.  A successful call holds nothing back; the next overage pauses about 60 seconds again. &#x60;Retry-After&#x60; is the time left. The advertiser-wide read (&#x60;GET /v1/ads/tiktok-smart-plus-reviews&#x60;) answers 200 with &#x60;retryAfterSeconds&#x60; and &#x60;refreshState&#x60; instead. Keep one request in flight per advertiser there.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |
| **501** | Only supported on TikTok, Google and Meta (Facebook and Instagram ads). &#x60;accountId&#x60; naming a connection that is not Meta also answers 501. |  -  |


## getAdSetDetails

> GetAdSetDetails200Response getAdSetDetails(adSetId, accountId, fields)

Get live ad-set details

Shows a Meta ad set&#39;s current settings straight from Meta, including its learning phase, budget, schedule and targeting.  The ad set is read live from Meta and returned verbatim. The default projection includes:  - &#x60;learning_stage_info&#x60;: learning-phase status, LEARNING / SUCCESS / FAIL / WAIVING. Meta omits its &#x60;status&#x60; key on paused ad sets. - delivery settings, budgets and schedule - dayparting (&#x60;adset_schedule&#x60;, &#x60;pacing_type&#x60;) - targeting  &#x60;fields&#x60; is a raw-passthrough override; unknown fields return Meta&#39;s 400 verbatim. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Meta ad set id (platformAdSetId).
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String fields = "id,status,ads.limit(100){id,name,status,issues_info}"; // String | Comma-separated Graph field override. Supports nested {} projections and Graph field modifiers, so a nested edge can be paged explicitly: without a .limit() modifier the expansion runs at the Meta default page size and the tail is dropped silently.
        try {
            GetAdSetDetails200Response result = apiInstance.getAdSetDetails(adSetId, accountId, fields);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getAdSetDetails");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adSetId** | **String**| Meta ad set id (platformAdSetId). | |
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **fields** | **String**| Comma-separated Graph field override. Supports nested {} projections and Graph field modifiers, so a nested edge can be paged explicitly: without a .limit() modifier the expansion runs at the Meta default page size and the tail is dropped silently. | [optional] |

### Return type

[**GetAdSetDetails200Response**](GetAdSetDetails200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | The ad set as returned by Meta |  -  |
| **400** | Invalid input, or Meta rejected the query; the message carries Meta&#39;s error |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## getAdSetDetailsWithHttpInfo

> ApiResponse<GetAdSetDetails200Response> getAdSetDetails getAdSetDetailsWithHttpInfo(adSetId, accountId, fields)

Get live ad-set details

Shows a Meta ad set&#39;s current settings straight from Meta, including its learning phase, budget, schedule and targeting.  The ad set is read live from Meta and returned verbatim. The default projection includes:  - &#x60;learning_stage_info&#x60;: learning-phase status, LEARNING / SUCCESS / FAIL / WAIVING. Meta omits its &#x60;status&#x60; key on paused ad sets. - delivery settings, budgets and schedule - dayparting (&#x60;adset_schedule&#x60;, &#x60;pacing_type&#x60;) - targeting  &#x60;fields&#x60; is a raw-passthrough override; unknown fields return Meta&#39;s 400 verbatim. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Meta ad set id (platformAdSetId).
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String fields = "id,status,ads.limit(100){id,name,status,issues_info}"; // String | Comma-separated Graph field override. Supports nested {} projections and Graph field modifiers, so a nested edge can be paged explicitly: without a .limit() modifier the expansion runs at the Meta default page size and the tail is dropped silently.
        try {
            ApiResponse<GetAdSetDetails200Response> response = apiInstance.getAdSetDetailsWithHttpInfo(adSetId, accountId, fields);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getAdSetDetails");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adSetId** | **String**| Meta ad set id (platformAdSetId). | |
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **fields** | **String**| Comma-separated Graph field override. Supports nested {} projections and Graph field modifiers, so a nested edge can be paged explicitly: without a .limit() modifier the expansion runs at the Meta default page size and the tail is dropped silently. | [optional] |

### Return type

ApiResponse<[**GetAdSetDetails200Response**](GetAdSetDetails200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | The ad set as returned by Meta |  -  |
| **400** | Invalid input, or Meta rejected the query; the message carries Meta&#39;s error |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## getAdSetTargeting

> GetAdSetTargeting200Response getAdSetTargeting(adSetId, platform)

Read a Reddit ad group&#39;s targeting and schedule

Shows a Reddit ad group&#39;s live targeting and schedule in the same shape PUT /v1/ads/ad-sets/{adSetId} takes, so you can prefill an editor.  It is read live from Reddit on every call. Reddit only; every other platform returns 501.  ### How fields come back  - Location and interest names are resolved with Reddit&#39;s targeting taxonomy. When Reddit cannot resolve them the ids stand in as names, and a location that is not a two-letter country is listed under &#x60;regions&#x60;. - Excluded DMAs are listed under &#x60;excludedLocations.regions&#x60;, since excluded locations have no metro list. - Languages come back as lowercase ISO 639-1 codes. - Targeting Zernio cannot edit (devices, platforms, carriers, automated expansion) is left out and kept on every edit. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Reddit ad group ID
        String platform = "reddit"; // String | Disambiguates when the same adSetId string exists on more than one connected platform.
        try {
            GetAdSetTargeting200Response result = apiInstance.getAdSetTargeting(adSetId, platform);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getAdSetTargeting");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adSetId** | **String**| Reddit ad group ID | |
| **platform** | **String**| Disambiguates when the same adSetId string exists on more than one connected platform. | [optional] [enum: reddit] |

### Return type

[**GetAdSetTargeting200Response**](GetAdSetTargeting200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current ad group targeting and schedule |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Ad set not found |  -  |
| **501** | The platform has no ad set targeting read (every platform but Reddit) |  -  |

## getAdSetTargetingWithHttpInfo

> ApiResponse<GetAdSetTargeting200Response> getAdSetTargeting getAdSetTargetingWithHttpInfo(adSetId, platform)

Read a Reddit ad group&#39;s targeting and schedule

Shows a Reddit ad group&#39;s live targeting and schedule in the same shape PUT /v1/ads/ad-sets/{adSetId} takes, so you can prefill an editor.  It is read live from Reddit on every call. Reddit only; every other platform returns 501.  ### How fields come back  - Location and interest names are resolved with Reddit&#39;s targeting taxonomy. When Reddit cannot resolve them the ids stand in as names, and a location that is not a two-letter country is listed under &#x60;regions&#x60;. - Excluded DMAs are listed under &#x60;excludedLocations.regions&#x60;, since excluded locations have no metro list. - Languages come back as lowercase ISO 639-1 codes. - Targeting Zernio cannot edit (devices, platforms, carriers, automated expansion) is left out and kept on every edit. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Reddit ad group ID
        String platform = "reddit"; // String | Disambiguates when the same adSetId string exists on more than one connected platform.
        try {
            ApiResponse<GetAdSetTargeting200Response> response = apiInstance.getAdSetTargetingWithHttpInfo(adSetId, platform);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getAdSetTargeting");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adSetId** | **String**| Reddit ad group ID | |
| **platform** | **String**| Disambiguates when the same adSetId string exists on more than one connected platform. | [optional] [enum: reddit] |

### Return type

ApiResponse<[**GetAdSetTargeting200Response**](GetAdSetTargeting200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current ad group targeting and schedule |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Ad set not found |  -  |
| **501** | The platform has no ad set targeting read (every platform but Reddit) |  -  |


## getAdTree

> AdTreeResponse getAdTree(page, limit, source, platform, status, adAccountId, pageId, accountId, profileId, campaignId, updatedSince, search, fromDate, toDate, hasDelivery, minSpend, sort, timeIncrement, dailyLevel, compare)

Get campaign tree

Shows your campaigns with their ad sets and ads nested inside, with spend and results rolled up at every level.  ### How it aggregates  Uses a two-stage aggregation: ads are grouped into ad sets, then ad sets into campaigns. Metrics are computed over an optional date range, then rolled up from ad level to ad set and campaign levels.  - Pagination is at the campaign level. - Ads without a campaign or ad set ID are grouped into synthetic \&quot;Ungrouped\&quot; buckets. - If no date range is provided, defaults to the last 90 days. Date range is capped at 730 days max.  ### History  When an ad account connects, Zernio imports its last 90 days of metrics, so the metrics hold no data for days before that.  When &#x60;accountId&#x60; or &#x60;adAccountId&#x60; resolves to a Meta ad account, a range reaching further back answers &#x60;202&#x60; with &#x60;backfillPending: true&#x60; and the covered part.  The older days (up to 730 days back) are imported in the background; repeat the request until it returns 200. A request scoped to no Meta account never returns &#x60;202&#x60;.  ### Daily breakdown  Pass &#x60;timeIncrement&#x3D;1&#x60; to also get a daily breakdown: each node gains a &#x60;daily[]&#x60; array of per-day metrics (same fields as the aggregated &#x60;metrics&#x60;) in the same call.  Use &#x60;dailyLevel&#x60; (&#x60;campaign&#x60; default, or &#x60;adset&#x60; / &#x60;ad&#x60;) to choose which levels carry the series. This replaces calling the tree once per day for per-campaign daily trends.  ### Deleted objects stay in the tree  Deleting an ad or a campaign is a soft delete: the Ad documents move to &#x60;status: cancelled&#x60; and are kept indefinitely. Their historical spend still counts toward the metrics of any date range they fall in. There is no pruning job and no retention window.  Filter on &#x60;status&#x60; if your view should hide them, but do that after reading the totals, not before. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        Integer page = 1; // Integer | Page number (1-based)
        Integer limit = 20; // Integer | Campaigns per page
        String source = "zernio"; // String | `all` (default) returns both Zernio-created ads and those discovered from the platform's ad manager. Matches the web UI's default view. Pass `zernio` to restrict to isExternal=false only. Status is NOT filtered by default; use the `status` param for that.
        String platform = "facebook"; // String | 
        AdStatus status = AdStatus.fromValue("active"); // AdStatus | Filter by derived campaign status (post-aggregation)
        String adAccountId = "adAccountId_example"; // String | One or more platform ad account IDs to scope the tree to (agency profiles connect a whole Business Manager, but a team usually cares about a subset).  - Comma-separate for multiple (`?adAccountId=act_1,act_2,act_3`); a single value keeps its old shape. - Max 50 accounts per request. - The plural aliases `adAccountIds` and `platformAdAccountIds` are rejected with a 400, so they cannot silently return the unfiltered fleet.
        String pageId = "pageId_example"; // String | Meta only: Facebook Page ID. Prunes the tree to ads whose creative is backed by this Page: campaigns and ad sets with no ad on the Page drop out, and rolled-up metrics cover only the Page's ads. Mirrors the same filter on /v1/ads and /v1/ads/campaigns.
        String accountId = "accountId_example"; // String | Account ID
        String profileId = "profileId_example"; // String | Profile ID
        String campaignId = "campaignId_example"; // String | Restrict the tree to one or more campaigns by platform campaign id (the id the platform assigns, e.g. Meta's numeric campaign id). Comma-separate up to 100 ids (`?campaignId=123,456`).  Filters the campaign set itself, so it works regardless of account size and pagination. Use it when you already hold campaign ids (e.g. from an `ad.status_changed` webhook) instead of paging the whole tree.
        OffsetDateTime updatedSince = OffsetDateTime.now(); // OffsetDateTime | Returns only campaigns with a change stored since this time (ISO 8601 with offset, e.g. `2026-09-30T10:00:00Z`). Each matching campaign comes back whole (every ad set and ad).  - A change is a new ad, or a change to any ad's status, review status, name, budget or creative. - Metrics are not a change: to refresh numbers, filter with `hasDelivery=true` and a date range instead. - Combines with every other filter (with `hasDelivery`/`minSpend` a campaign must match both).
        String search = "search_example"; // String | Case-insensitive substring match on campaign, ad set and ad names (`_`, `%` and spaces match literally), or an exact platform campaign, ad set or ad id.  - A campaign whose name matches returns with all its ad sets and ads. - A match on an ad set or ad name returns only the matching branch. - Filters the campaign set itself, so `pagination.total` counts only matching campaigns.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of the METRICS date range (YYYY-MM-DD). On its own it affects only the spend/impression numbers overlaid on each node, not which campaigns are returned. Pass `hasDelivery` or `minSpend` to also filter the campaign set to this window. Defaults to 90 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of metrics date range (YYYY-MM-DD). Defaults to today. Max 730-day range.
        Boolean hasDelivery = true; // Boolean | Return only campaigns that delivered between `fromDate` and `toDate`: spend above zero, or impressions served at zero spend.  Unlike `status`, which reads a campaign's CURRENT state, this filters on what happened inside the window, so a campaign that spent then and is paused today is still returned. It filters the campaign set itself, so `pagination.total` counts only matching campaigns.
        BigDecimal minSpend = new BigDecimal(78); // BigDecimal | Return only campaigns whose spend between `fromDate` and `toDate` reaches this amount. Expressed in each campaign's OWN currency (the `currency` field on the campaign node): spend is stored per ad account in its native currency and one response can span several. Implies `hasDelivery`; `minSpend=0` applies no filter.
        String sort = "newest"; // String | Campaign-level sort order. `newest` (default) / `oldest` order by the campaign's newest-ad createdAt. `spend_desc` / `spend_asc` order by aggregated spend in the requested date range; campaigns with no spend land at the end.
        Integer timeIncrement = 1; // Integer | Set to `1` to also return a daily breakdown (mirrors Meta Insights' `time_increment=1`). Only `1` (daily) is supported. See `dailyLevel` to control which levels carry it.  Each node gains a `daily[]` array of per-day metrics (same fields as the aggregated `metrics`) next to the range total, so you get per-entity daily trends in ONE call instead of one tree call per day.  The daily series covers the same date range and source data as `metrics`, except `reach` on Meta and TikTok: the range total is the platform's de-duplicated value, so daily reach does not sum to it.
        String dailyLevel = "campaign"; // String | Which tree levels get the `daily[]` series when `timeIncrement=1`. Ignored when `timeIncrement` is unset.  - `campaign` (default): on campaign nodes only. The common per-campaign-trend case, and the smallest payload. - `adset`: on ad sets too. - `ad`: on every ad in `ads[]` as well. Heaviest (a long range × up to 100 ads per ad set); scope with `campaignId` to keep responses small.
        String compare = "previous"; // String | Set to `previous` to also read the period of the same length that ends the day before `fromDate`. Every campaign, ad set and ad gains `previousMetrics` (same fields as `metrics`) and the response gains `previousRange`, so a table can show the change against the previous period in one call.
        try {
            AdTreeResponse result = apiInstance.getAdTree(page, limit, source, platform, status, adAccountId, pageId, accountId, profileId, campaignId, updatedSince, search, fromDate, toDate, hasDelivery, minSpend, sort, timeIncrement, dailyLevel, compare);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getAdTree");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page** | **Integer**| Page number (1-based) | [optional] [default to 1] |
| **limit** | **Integer**| Campaigns per page | [optional] [default to 20] |
| **source** | **String**| &#x60;all&#x60; (default) returns both Zernio-created ads and those discovered from the platform&#39;s ad manager. Matches the web UI&#39;s default view. Pass &#x60;zernio&#x60; to restrict to isExternal&#x3D;false only. Status is NOT filtered by default; use the &#x60;status&#x60; param for that. | [optional] [default to all] [enum: zernio, all] |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai, reddit] |
| **status** | [**AdStatus**](.md)| Filter by derived campaign status (post-aggregation) | [optional] [enum: active, paused, pending_review, rejected, completed, cancelled, error] |
| **adAccountId** | **String**| One or more platform ad account IDs to scope the tree to (agency profiles connect a whole Business Manager, but a team usually cares about a subset).  - Comma-separate for multiple (&#x60;?adAccountId&#x3D;act_1,act_2,act_3&#x60;); a single value keeps its old shape. - Max 50 accounts per request. - The plural aliases &#x60;adAccountIds&#x60; and &#x60;platformAdAccountIds&#x60; are rejected with a 400, so they cannot silently return the unfiltered fleet. | [optional] |
| **pageId** | **String**| Meta only: Facebook Page ID. Prunes the tree to ads whose creative is backed by this Page: campaigns and ad sets with no ad on the Page drop out, and rolled-up metrics cover only the Page&#39;s ads. Mirrors the same filter on /v1/ads and /v1/ads/campaigns. | [optional] |
| **accountId** | **String**| Account ID | [optional] |
| **profileId** | **String**| Profile ID | [optional] |
| **campaignId** | **String**| Restrict the tree to one or more campaigns by platform campaign id (the id the platform assigns, e.g. Meta&#39;s numeric campaign id). Comma-separate up to 100 ids (&#x60;?campaignId&#x3D;123,456&#x60;).  Filters the campaign set itself, so it works regardless of account size and pagination. Use it when you already hold campaign ids (e.g. from an &#x60;ad.status_changed&#x60; webhook) instead of paging the whole tree. | [optional] |
| **updatedSince** | **OffsetDateTime**| Returns only campaigns with a change stored since this time (ISO 8601 with offset, e.g. &#x60;2026-09-30T10:00:00Z&#x60;). Each matching campaign comes back whole (every ad set and ad).  - A change is a new ad, or a change to any ad&#39;s status, review status, name, budget or creative. - Metrics are not a change: to refresh numbers, filter with &#x60;hasDelivery&#x3D;true&#x60; and a date range instead. - Combines with every other filter (with &#x60;hasDelivery&#x60;/&#x60;minSpend&#x60; a campaign must match both). | [optional] |
| **search** | **String**| Case-insensitive substring match on campaign, ad set and ad names (&#x60;_&#x60;, &#x60;%&#x60; and spaces match literally), or an exact platform campaign, ad set or ad id.  - A campaign whose name matches returns with all its ad sets and ads. - A match on an ad set or ad name returns only the matching branch. - Filters the campaign set itself, so &#x60;pagination.total&#x60; counts only matching campaigns. | [optional] |
| **fromDate** | **LocalDate**| Start of the METRICS date range (YYYY-MM-DD). On its own it affects only the spend/impression numbers overlaid on each node, not which campaigns are returned. Pass &#x60;hasDelivery&#x60; or &#x60;minSpend&#x60; to also filter the campaign set to this window. Defaults to 90 days ago. | [optional] |
| **toDate** | **LocalDate**| End of metrics date range (YYYY-MM-DD). Defaults to today. Max 730-day range. | [optional] |
| **hasDelivery** | **Boolean**| Return only campaigns that delivered between &#x60;fromDate&#x60; and &#x60;toDate&#x60;: spend above zero, or impressions served at zero spend.  Unlike &#x60;status&#x60;, which reads a campaign&#39;s CURRENT state, this filters on what happened inside the window, so a campaign that spent then and is paused today is still returned. It filters the campaign set itself, so &#x60;pagination.total&#x60; counts only matching campaigns. | [optional] |
| **minSpend** | **BigDecimal**| Return only campaigns whose spend between &#x60;fromDate&#x60; and &#x60;toDate&#x60; reaches this amount. Expressed in each campaign&#39;s OWN currency (the &#x60;currency&#x60; field on the campaign node): spend is stored per ad account in its native currency and one response can span several. Implies &#x60;hasDelivery&#x60;; &#x60;minSpend&#x3D;0&#x60; applies no filter. | [optional] |
| **sort** | **String**| Campaign-level sort order. &#x60;newest&#x60; (default) / &#x60;oldest&#x60; order by the campaign&#39;s newest-ad createdAt. &#x60;spend_desc&#x60; / &#x60;spend_asc&#x60; order by aggregated spend in the requested date range; campaigns with no spend land at the end. | [optional] [default to newest] [enum: newest, oldest, spend_desc, spend_asc] |
| **timeIncrement** | **Integer**| Set to &#x60;1&#x60; to also return a daily breakdown (mirrors Meta Insights&#39; &#x60;time_increment&#x3D;1&#x60;). Only &#x60;1&#x60; (daily) is supported. See &#x60;dailyLevel&#x60; to control which levels carry it.  Each node gains a &#x60;daily[]&#x60; array of per-day metrics (same fields as the aggregated &#x60;metrics&#x60;) next to the range total, so you get per-entity daily trends in ONE call instead of one tree call per day.  The daily series covers the same date range and source data as &#x60;metrics&#x60;, except &#x60;reach&#x60; on Meta and TikTok: the range total is the platform&#39;s de-duplicated value, so daily reach does not sum to it. | [optional] [enum: 1] |
| **dailyLevel** | **String**| Which tree levels get the &#x60;daily[]&#x60; series when &#x60;timeIncrement&#x3D;1&#x60;. Ignored when &#x60;timeIncrement&#x60; is unset.  - &#x60;campaign&#x60; (default): on campaign nodes only. The common per-campaign-trend case, and the smallest payload. - &#x60;adset&#x60;: on ad sets too. - &#x60;ad&#x60;: on every ad in &#x60;ads[]&#x60; as well. Heaviest (a long range × up to 100 ads per ad set); scope with &#x60;campaignId&#x60; to keep responses small. | [optional] [default to campaign] [enum: campaign, adset, ad] |
| **compare** | **String**| Set to &#x60;previous&#x60; to also read the period of the same length that ends the day before &#x60;fromDate&#x60;. Every campaign, ad set and ad gains &#x60;previousMetrics&#x60; (same fields as &#x60;metrics&#x60;) and the response gains &#x60;previousRange&#x60;, so a table can show the change against the previous period in one call. | [optional] [enum: previous] |

### Return type

[**AdTreeResponse**](AdTreeResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nested campaign tree with pagination |  -  |
| **202** | Meta only. Historical data is incomplete and backfill remains pending. |  * Retry-After -  <br>  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |

## getAdTreeWithHttpInfo

> ApiResponse<AdTreeResponse> getAdTree getAdTreeWithHttpInfo(page, limit, source, platform, status, adAccountId, pageId, accountId, profileId, campaignId, updatedSince, search, fromDate, toDate, hasDelivery, minSpend, sort, timeIncrement, dailyLevel, compare)

Get campaign tree

Shows your campaigns with their ad sets and ads nested inside, with spend and results rolled up at every level.  ### How it aggregates  Uses a two-stage aggregation: ads are grouped into ad sets, then ad sets into campaigns. Metrics are computed over an optional date range, then rolled up from ad level to ad set and campaign levels.  - Pagination is at the campaign level. - Ads without a campaign or ad set ID are grouped into synthetic \&quot;Ungrouped\&quot; buckets. - If no date range is provided, defaults to the last 90 days. Date range is capped at 730 days max.  ### History  When an ad account connects, Zernio imports its last 90 days of metrics, so the metrics hold no data for days before that.  When &#x60;accountId&#x60; or &#x60;adAccountId&#x60; resolves to a Meta ad account, a range reaching further back answers &#x60;202&#x60; with &#x60;backfillPending: true&#x60; and the covered part.  The older days (up to 730 days back) are imported in the background; repeat the request until it returns 200. A request scoped to no Meta account never returns &#x60;202&#x60;.  ### Daily breakdown  Pass &#x60;timeIncrement&#x3D;1&#x60; to also get a daily breakdown: each node gains a &#x60;daily[]&#x60; array of per-day metrics (same fields as the aggregated &#x60;metrics&#x60;) in the same call.  Use &#x60;dailyLevel&#x60; (&#x60;campaign&#x60; default, or &#x60;adset&#x60; / &#x60;ad&#x60;) to choose which levels carry the series. This replaces calling the tree once per day for per-campaign daily trends.  ### Deleted objects stay in the tree  Deleting an ad or a campaign is a soft delete: the Ad documents move to &#x60;status: cancelled&#x60; and are kept indefinitely. Their historical spend still counts toward the metrics of any date range they fall in. There is no pruning job and no retention window.  Filter on &#x60;status&#x60; if your view should hide them, but do that after reading the totals, not before. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        Integer page = 1; // Integer | Page number (1-based)
        Integer limit = 20; // Integer | Campaigns per page
        String source = "zernio"; // String | `all` (default) returns both Zernio-created ads and those discovered from the platform's ad manager. Matches the web UI's default view. Pass `zernio` to restrict to isExternal=false only. Status is NOT filtered by default; use the `status` param for that.
        String platform = "facebook"; // String | 
        AdStatus status = AdStatus.fromValue("active"); // AdStatus | Filter by derived campaign status (post-aggregation)
        String adAccountId = "adAccountId_example"; // String | One or more platform ad account IDs to scope the tree to (agency profiles connect a whole Business Manager, but a team usually cares about a subset).  - Comma-separate for multiple (`?adAccountId=act_1,act_2,act_3`); a single value keeps its old shape. - Max 50 accounts per request. - The plural aliases `adAccountIds` and `platformAdAccountIds` are rejected with a 400, so they cannot silently return the unfiltered fleet.
        String pageId = "pageId_example"; // String | Meta only: Facebook Page ID. Prunes the tree to ads whose creative is backed by this Page: campaigns and ad sets with no ad on the Page drop out, and rolled-up metrics cover only the Page's ads. Mirrors the same filter on /v1/ads and /v1/ads/campaigns.
        String accountId = "accountId_example"; // String | Account ID
        String profileId = "profileId_example"; // String | Profile ID
        String campaignId = "campaignId_example"; // String | Restrict the tree to one or more campaigns by platform campaign id (the id the platform assigns, e.g. Meta's numeric campaign id). Comma-separate up to 100 ids (`?campaignId=123,456`).  Filters the campaign set itself, so it works regardless of account size and pagination. Use it when you already hold campaign ids (e.g. from an `ad.status_changed` webhook) instead of paging the whole tree.
        OffsetDateTime updatedSince = OffsetDateTime.now(); // OffsetDateTime | Returns only campaigns with a change stored since this time (ISO 8601 with offset, e.g. `2026-09-30T10:00:00Z`). Each matching campaign comes back whole (every ad set and ad).  - A change is a new ad, or a change to any ad's status, review status, name, budget or creative. - Metrics are not a change: to refresh numbers, filter with `hasDelivery=true` and a date range instead. - Combines with every other filter (with `hasDelivery`/`minSpend` a campaign must match both).
        String search = "search_example"; // String | Case-insensitive substring match on campaign, ad set and ad names (`_`, `%` and spaces match literally), or an exact platform campaign, ad set or ad id.  - A campaign whose name matches returns with all its ad sets and ads. - A match on an ad set or ad name returns only the matching branch. - Filters the campaign set itself, so `pagination.total` counts only matching campaigns.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of the METRICS date range (YYYY-MM-DD). On its own it affects only the spend/impression numbers overlaid on each node, not which campaigns are returned. Pass `hasDelivery` or `minSpend` to also filter the campaign set to this window. Defaults to 90 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of metrics date range (YYYY-MM-DD). Defaults to today. Max 730-day range.
        Boolean hasDelivery = true; // Boolean | Return only campaigns that delivered between `fromDate` and `toDate`: spend above zero, or impressions served at zero spend.  Unlike `status`, which reads a campaign's CURRENT state, this filters on what happened inside the window, so a campaign that spent then and is paused today is still returned. It filters the campaign set itself, so `pagination.total` counts only matching campaigns.
        BigDecimal minSpend = new BigDecimal(78); // BigDecimal | Return only campaigns whose spend between `fromDate` and `toDate` reaches this amount. Expressed in each campaign's OWN currency (the `currency` field on the campaign node): spend is stored per ad account in its native currency and one response can span several. Implies `hasDelivery`; `minSpend=0` applies no filter.
        String sort = "newest"; // String | Campaign-level sort order. `newest` (default) / `oldest` order by the campaign's newest-ad createdAt. `spend_desc` / `spend_asc` order by aggregated spend in the requested date range; campaigns with no spend land at the end.
        Integer timeIncrement = 1; // Integer | Set to `1` to also return a daily breakdown (mirrors Meta Insights' `time_increment=1`). Only `1` (daily) is supported. See `dailyLevel` to control which levels carry it.  Each node gains a `daily[]` array of per-day metrics (same fields as the aggregated `metrics`) next to the range total, so you get per-entity daily trends in ONE call instead of one tree call per day.  The daily series covers the same date range and source data as `metrics`, except `reach` on Meta and TikTok: the range total is the platform's de-duplicated value, so daily reach does not sum to it.
        String dailyLevel = "campaign"; // String | Which tree levels get the `daily[]` series when `timeIncrement=1`. Ignored when `timeIncrement` is unset.  - `campaign` (default): on campaign nodes only. The common per-campaign-trend case, and the smallest payload. - `adset`: on ad sets too. - `ad`: on every ad in `ads[]` as well. Heaviest (a long range × up to 100 ads per ad set); scope with `campaignId` to keep responses small.
        String compare = "previous"; // String | Set to `previous` to also read the period of the same length that ends the day before `fromDate`. Every campaign, ad set and ad gains `previousMetrics` (same fields as `metrics`) and the response gains `previousRange`, so a table can show the change against the previous period in one call.
        try {
            ApiResponse<AdTreeResponse> response = apiInstance.getAdTreeWithHttpInfo(page, limit, source, platform, status, adAccountId, pageId, accountId, profileId, campaignId, updatedSince, search, fromDate, toDate, hasDelivery, minSpend, sort, timeIncrement, dailyLevel, compare);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getAdTree");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page** | **Integer**| Page number (1-based) | [optional] [default to 1] |
| **limit** | **Integer**| Campaigns per page | [optional] [default to 20] |
| **source** | **String**| &#x60;all&#x60; (default) returns both Zernio-created ads and those discovered from the platform&#39;s ad manager. Matches the web UI&#39;s default view. Pass &#x60;zernio&#x60; to restrict to isExternal&#x3D;false only. Status is NOT filtered by default; use the &#x60;status&#x60; param for that. | [optional] [default to all] [enum: zernio, all] |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai, reddit] |
| **status** | [**AdStatus**](.md)| Filter by derived campaign status (post-aggregation) | [optional] [enum: active, paused, pending_review, rejected, completed, cancelled, error] |
| **adAccountId** | **String**| One or more platform ad account IDs to scope the tree to (agency profiles connect a whole Business Manager, but a team usually cares about a subset).  - Comma-separate for multiple (&#x60;?adAccountId&#x3D;act_1,act_2,act_3&#x60;); a single value keeps its old shape. - Max 50 accounts per request. - The plural aliases &#x60;adAccountIds&#x60; and &#x60;platformAdAccountIds&#x60; are rejected with a 400, so they cannot silently return the unfiltered fleet. | [optional] |
| **pageId** | **String**| Meta only: Facebook Page ID. Prunes the tree to ads whose creative is backed by this Page: campaigns and ad sets with no ad on the Page drop out, and rolled-up metrics cover only the Page&#39;s ads. Mirrors the same filter on /v1/ads and /v1/ads/campaigns. | [optional] |
| **accountId** | **String**| Account ID | [optional] |
| **profileId** | **String**| Profile ID | [optional] |
| **campaignId** | **String**| Restrict the tree to one or more campaigns by platform campaign id (the id the platform assigns, e.g. Meta&#39;s numeric campaign id). Comma-separate up to 100 ids (&#x60;?campaignId&#x3D;123,456&#x60;).  Filters the campaign set itself, so it works regardless of account size and pagination. Use it when you already hold campaign ids (e.g. from an &#x60;ad.status_changed&#x60; webhook) instead of paging the whole tree. | [optional] |
| **updatedSince** | **OffsetDateTime**| Returns only campaigns with a change stored since this time (ISO 8601 with offset, e.g. &#x60;2026-09-30T10:00:00Z&#x60;). Each matching campaign comes back whole (every ad set and ad).  - A change is a new ad, or a change to any ad&#39;s status, review status, name, budget or creative. - Metrics are not a change: to refresh numbers, filter with &#x60;hasDelivery&#x3D;true&#x60; and a date range instead. - Combines with every other filter (with &#x60;hasDelivery&#x60;/&#x60;minSpend&#x60; a campaign must match both). | [optional] |
| **search** | **String**| Case-insensitive substring match on campaign, ad set and ad names (&#x60;_&#x60;, &#x60;%&#x60; and spaces match literally), or an exact platform campaign, ad set or ad id.  - A campaign whose name matches returns with all its ad sets and ads. - A match on an ad set or ad name returns only the matching branch. - Filters the campaign set itself, so &#x60;pagination.total&#x60; counts only matching campaigns. | [optional] |
| **fromDate** | **LocalDate**| Start of the METRICS date range (YYYY-MM-DD). On its own it affects only the spend/impression numbers overlaid on each node, not which campaigns are returned. Pass &#x60;hasDelivery&#x60; or &#x60;minSpend&#x60; to also filter the campaign set to this window. Defaults to 90 days ago. | [optional] |
| **toDate** | **LocalDate**| End of metrics date range (YYYY-MM-DD). Defaults to today. Max 730-day range. | [optional] |
| **hasDelivery** | **Boolean**| Return only campaigns that delivered between &#x60;fromDate&#x60; and &#x60;toDate&#x60;: spend above zero, or impressions served at zero spend.  Unlike &#x60;status&#x60;, which reads a campaign&#39;s CURRENT state, this filters on what happened inside the window, so a campaign that spent then and is paused today is still returned. It filters the campaign set itself, so &#x60;pagination.total&#x60; counts only matching campaigns. | [optional] |
| **minSpend** | **BigDecimal**| Return only campaigns whose spend between &#x60;fromDate&#x60; and &#x60;toDate&#x60; reaches this amount. Expressed in each campaign&#39;s OWN currency (the &#x60;currency&#x60; field on the campaign node): spend is stored per ad account in its native currency and one response can span several. Implies &#x60;hasDelivery&#x60;; &#x60;minSpend&#x3D;0&#x60; applies no filter. | [optional] |
| **sort** | **String**| Campaign-level sort order. &#x60;newest&#x60; (default) / &#x60;oldest&#x60; order by the campaign&#39;s newest-ad createdAt. &#x60;spend_desc&#x60; / &#x60;spend_asc&#x60; order by aggregated spend in the requested date range; campaigns with no spend land at the end. | [optional] [default to newest] [enum: newest, oldest, spend_desc, spend_asc] |
| **timeIncrement** | **Integer**| Set to &#x60;1&#x60; to also return a daily breakdown (mirrors Meta Insights&#39; &#x60;time_increment&#x3D;1&#x60;). Only &#x60;1&#x60; (daily) is supported. See &#x60;dailyLevel&#x60; to control which levels carry it.  Each node gains a &#x60;daily[]&#x60; array of per-day metrics (same fields as the aggregated &#x60;metrics&#x60;) next to the range total, so you get per-entity daily trends in ONE call instead of one tree call per day.  The daily series covers the same date range and source data as &#x60;metrics&#x60;, except &#x60;reach&#x60; on Meta and TikTok: the range total is the platform&#39;s de-duplicated value, so daily reach does not sum to it. | [optional] [enum: 1] |
| **dailyLevel** | **String**| Which tree levels get the &#x60;daily[]&#x60; series when &#x60;timeIncrement&#x3D;1&#x60;. Ignored when &#x60;timeIncrement&#x60; is unset.  - &#x60;campaign&#x60; (default): on campaign nodes only. The common per-campaign-trend case, and the smallest payload. - &#x60;adset&#x60;: on ad sets too. - &#x60;ad&#x60;: on every ad in &#x60;ads[]&#x60; as well. Heaviest (a long range × up to 100 ads per ad set); scope with &#x60;campaignId&#x60; to keep responses small. | [optional] [default to campaign] [enum: campaign, adset, ad] |
| **compare** | **String**| Set to &#x60;previous&#x60; to also read the period of the same length that ends the day before &#x60;fromDate&#x60;. Every campaign, ad set and ad gains &#x60;previousMetrics&#x60; (same fields as &#x60;metrics&#x60;) and the response gains &#x60;previousRange&#x60;, so a table can show the change against the previous period in one call. | [optional] [enum: previous] |

### Return type

ApiResponse<[**AdTreeResponse**](AdTreeResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Nested campaign tree with pagination |  -  |
| **202** | Meta only. Historical data is incomplete and backfill remains pending. |  * Retry-After -  <br>  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |


## getAdsTimeline

> AdsTimelineResponse getAdsTimeline(accountId, adAccountId, fromDate, toDate, platform, compare)

Get daily account metrics

Returns an ads account&#39;s spend, results and other metrics day by day, ready for a daily performance chart.  The result is a single time series of daily aggregate metrics across all ads in a SocialAccount: one row per calendar day and currency in the requested range (one row per day unless the account&#39;s ad accounts bill in different currencies).  Use this for dashboards that draw a daily-spend or daily-conversions chart, instead of calling &#x60;/v1/ads/tree&#x60; once per day.  ### Parameters  - &#x60;accountId&#x60; is required. The lookup is sibling-expanded, so passing the &#x60;metaads&#x60; ID also includes ads under the linked &#x60;facebook&#x60; / &#x60;instagram&#x60; posting account (and vice-versa), the same convention as &#x60;/v1/ads/tree&#x60; and &#x60;/v1/ads&#x60;. - Date range defaults to the last 90 days. Capped at 730 days. - With adAccountId set to a Google customer id this is the customer-level performance report (clicks, cost, impressions, conversions, all conversions per day).  ### History  When an ad account connects, Zernio imports its last 90 days of metrics, so &#x60;rows&#x60; hold no data for days before that.  When &#x60;accountId&#x60; or &#x60;adAccountId&#x60; resolves to a Meta ad account, a range reaching further back answers &#x60;202&#x60; with &#x60;backfillPending: true&#x60; and the covered part. The older days (up to 730 days back) are imported in the background; repeat the request until it returns 200.  Other platforms never return &#x60;202&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String accountId = "accountId_example"; // String | Account ID. Sibling-expanded to its linked posting↔ads pair. An id that does not exist or sits on a profile the API key cannot reach answers 404 (code: account_not_found).
        String adAccountId = "adAccountId_example"; // String | Optional platform-native ad account ID (e.g. Meta `act_…`, TikTok advertiser ID). Use when the connection wraps multiple platform ad accounts and the chart should show one only. Note: rows ingested before 2026-05-13 don't carry this column; the recurring 7-day re-sync repopulates them naturally.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Inclusive start of metrics range (YYYY-MM-DD). Defaults to 90 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | Inclusive end of metrics range (YYYY-MM-DD). Defaults to today. Max 730-day range.
        String platform = "facebook"; // String | Restrict to one platform.
        String compare = "previous"; // String | Set to `previous` to also return `previousRows` for the period of the same length that ends the day before `fromDate`, with that period as `previousRange`. Needs a `fromDate` (sent or defaulted); `toDate` alone answers 400.
        try {
            AdsTimelineResponse result = apiInstance.getAdsTimeline(accountId, adAccountId, fromDate, toDate, platform, compare);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getAdsTimeline");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Account ID. Sibling-expanded to its linked posting↔ads pair. An id that does not exist or sits on a profile the API key cannot reach answers 404 (code: account_not_found). | |
| **adAccountId** | **String**| Optional platform-native ad account ID (e.g. Meta &#x60;act_…&#x60;, TikTok advertiser ID). Use when the connection wraps multiple platform ad accounts and the chart should show one only. Note: rows ingested before 2026-05-13 don&#39;t carry this column; the recurring 7-day re-sync repopulates them naturally. | [optional] |
| **fromDate** | **LocalDate**| Inclusive start of metrics range (YYYY-MM-DD). Defaults to 90 days ago. | [optional] |
| **toDate** | **LocalDate**| Inclusive end of metrics range (YYYY-MM-DD). Defaults to today. Max 730-day range. | [optional] |
| **platform** | **String**| Restrict to one platform. | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai, reddit] |
| **compare** | **String**| Set to &#x60;previous&#x60; to also return &#x60;previousRows&#x60; for the period of the same length that ends the day before &#x60;fromDate&#x60;, with that period as &#x60;previousRange&#x60;. Needs a &#x60;fromDate&#x60; (sent or defaulted); &#x60;toDate&#x60; alone answers 400. | [optional] [enum: previous] |

### Return type

[**AdsTimelineResponse**](AdsTimelineResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Daily time series of aggregate metrics. Empty &#x60;rows&#x60; means the account has no ad activity in the range. |  -  |
| **202** | Meta only. Historical data is incomplete and backfill remains pending. |  * Retry-After -  <br>  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |

## getAdsTimelineWithHttpInfo

> ApiResponse<AdsTimelineResponse> getAdsTimeline getAdsTimelineWithHttpInfo(accountId, adAccountId, fromDate, toDate, platform, compare)

Get daily account metrics

Returns an ads account&#39;s spend, results and other metrics day by day, ready for a daily performance chart.  The result is a single time series of daily aggregate metrics across all ads in a SocialAccount: one row per calendar day and currency in the requested range (one row per day unless the account&#39;s ad accounts bill in different currencies).  Use this for dashboards that draw a daily-spend or daily-conversions chart, instead of calling &#x60;/v1/ads/tree&#x60; once per day.  ### Parameters  - &#x60;accountId&#x60; is required. The lookup is sibling-expanded, so passing the &#x60;metaads&#x60; ID also includes ads under the linked &#x60;facebook&#x60; / &#x60;instagram&#x60; posting account (and vice-versa), the same convention as &#x60;/v1/ads/tree&#x60; and &#x60;/v1/ads&#x60;. - Date range defaults to the last 90 days. Capped at 730 days. - With adAccountId set to a Google customer id this is the customer-level performance report (clicks, cost, impressions, conversions, all conversions per day).  ### History  When an ad account connects, Zernio imports its last 90 days of metrics, so &#x60;rows&#x60; hold no data for days before that.  When &#x60;accountId&#x60; or &#x60;adAccountId&#x60; resolves to a Meta ad account, a range reaching further back answers &#x60;202&#x60; with &#x60;backfillPending: true&#x60; and the covered part. The older days (up to 730 days back) are imported in the background; repeat the request until it returns 200.  Other platforms never return &#x60;202&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String accountId = "accountId_example"; // String | Account ID. Sibling-expanded to its linked posting↔ads pair. An id that does not exist or sits on a profile the API key cannot reach answers 404 (code: account_not_found).
        String adAccountId = "adAccountId_example"; // String | Optional platform-native ad account ID (e.g. Meta `act_…`, TikTok advertiser ID). Use when the connection wraps multiple platform ad accounts and the chart should show one only. Note: rows ingested before 2026-05-13 don't carry this column; the recurring 7-day re-sync repopulates them naturally.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Inclusive start of metrics range (YYYY-MM-DD). Defaults to 90 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | Inclusive end of metrics range (YYYY-MM-DD). Defaults to today. Max 730-day range.
        String platform = "facebook"; // String | Restrict to one platform.
        String compare = "previous"; // String | Set to `previous` to also return `previousRows` for the period of the same length that ends the day before `fromDate`, with that period as `previousRange`. Needs a `fromDate` (sent or defaulted); `toDate` alone answers 400.
        try {
            ApiResponse<AdsTimelineResponse> response = apiInstance.getAdsTimelineWithHttpInfo(accountId, adAccountId, fromDate, toDate, platform, compare);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getAdsTimeline");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Account ID. Sibling-expanded to its linked posting↔ads pair. An id that does not exist or sits on a profile the API key cannot reach answers 404 (code: account_not_found). | |
| **adAccountId** | **String**| Optional platform-native ad account ID (e.g. Meta &#x60;act_…&#x60;, TikTok advertiser ID). Use when the connection wraps multiple platform ad accounts and the chart should show one only. Note: rows ingested before 2026-05-13 don&#39;t carry this column; the recurring 7-day re-sync repopulates them naturally. | [optional] |
| **fromDate** | **LocalDate**| Inclusive start of metrics range (YYYY-MM-DD). Defaults to 90 days ago. | [optional] |
| **toDate** | **LocalDate**| Inclusive end of metrics range (YYYY-MM-DD). Defaults to today. Max 730-day range. | [optional] |
| **platform** | **String**| Restrict to one platform. | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai, reddit] |
| **compare** | **String**| Set to &#x60;previous&#x60; to also return &#x60;previousRows&#x60; for the period of the same length that ends the day before &#x60;fromDate&#x60;, with that period as &#x60;previousRange&#x60;. Needs a &#x60;fromDate&#x60; (sent or defaulted); &#x60;toDate&#x60; alone answers 400. | [optional] [enum: previous] |

### Return type

ApiResponse<[**AdsTimelineResponse**](AdsTimelineResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Daily time series of aggregate metrics. Empty &#x60;rows&#x60; means the account has no ad activity in the range. |  -  |
| **202** | Meta only. Historical data is incomplete and backfill remains pending. |  * Retry-After -  <br>  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |


## getCampaignAdSchedule

> GetCampaignAdSchedule200Response getCampaignAdSchedule(campaignId, platform, includePerformance, windowDays, fromDate, toDate)

Read a campaign&#39;s ad schedule (dayparting)

Shows the days and hours a Google campaign runs and its bid adjustments, optionally with performance by day and hour.  The windows a Google campaign serves in, with the bid modifier on each, plus the criterion ids Google minted for them.  An EMPTY &#x60;schedule&#x60; is meaningful and is not a failed lookup: Google has no \&quot;all day\&quot; criterion, so a campaign with no ad schedule serves around the clock. &#x60;servesAroundTheClock&#x60; states that explicitly.  Set &#x60;includePerformance&#x3D;true&#x60; to also get delivery split by day of week and by hour, which is the evidence for deciding what the schedule should be. It is one extra Google call segmented by both dimensions at once, so the two views always agree.  Google Ads only. The response carries &#x60;cachedAt&#x60; and &#x60;stale&#x60;, set when a quota-exhausted call falls back to the last-good copy instead of a live read. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Numeric Google platform campaign id.
        String platform = "google"; // String | Disambiguates the campaign id when the connection spans platforms.
        Boolean includePerformance = true; // Boolean | Also return delivery by day of week and by hour. Costs one extra Google call.
        Integer windowDays = 30; // Integer | Trailing window for the performance split. Ignored when fromDate and toDate are both given.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of an explicit performance range (YYYY-MM-DD). Use together with toDate.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of an explicit performance range (YYYY-MM-DD). Must be on or after fromDate.
        try {
            GetCampaignAdSchedule200Response result = apiInstance.getCampaignAdSchedule(campaignId, platform, includePerformance, windowDays, fromDate, toDate);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getCampaignAdSchedule");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Numeric Google platform campaign id. | |
| **platform** | **String**| Disambiguates the campaign id when the connection spans platforms. | [optional] [enum: google] |
| **includePerformance** | **Boolean**| Also return delivery by day of week and by hour. Costs one extra Google call. | [optional] |
| **windowDays** | **Integer**| Trailing window for the performance split. Ignored when fromDate and toDate are both given. | [optional] [default to 30] |
| **fromDate** | **LocalDate**| Start of an explicit performance range (YYYY-MM-DD). Use together with toDate. | [optional] |
| **toDate** | **LocalDate**| End of an explicit performance range (YYYY-MM-DD). Must be on or after fromDate. | [optional] |

### Return type

[**GetCampaignAdSchedule200Response**](GetCampaignAdSchedule200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The campaign&#39;s ad schedule |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | Not a Google Ads campaign: ad schedules are a Google criterion. |  -  |

## getCampaignAdScheduleWithHttpInfo

> ApiResponse<GetCampaignAdSchedule200Response> getCampaignAdSchedule getCampaignAdScheduleWithHttpInfo(campaignId, platform, includePerformance, windowDays, fromDate, toDate)

Read a campaign&#39;s ad schedule (dayparting)

Shows the days and hours a Google campaign runs and its bid adjustments, optionally with performance by day and hour.  The windows a Google campaign serves in, with the bid modifier on each, plus the criterion ids Google minted for them.  An EMPTY &#x60;schedule&#x60; is meaningful and is not a failed lookup: Google has no \&quot;all day\&quot; criterion, so a campaign with no ad schedule serves around the clock. &#x60;servesAroundTheClock&#x60; states that explicitly.  Set &#x60;includePerformance&#x3D;true&#x60; to also get delivery split by day of week and by hour, which is the evidence for deciding what the schedule should be. It is one extra Google call segmented by both dimensions at once, so the two views always agree.  Google Ads only. The response carries &#x60;cachedAt&#x60; and &#x60;stale&#x60;, set when a quota-exhausted call falls back to the last-good copy instead of a live read. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Numeric Google platform campaign id.
        String platform = "google"; // String | Disambiguates the campaign id when the connection spans platforms.
        Boolean includePerformance = true; // Boolean | Also return delivery by day of week and by hour. Costs one extra Google call.
        Integer windowDays = 30; // Integer | Trailing window for the performance split. Ignored when fromDate and toDate are both given.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of an explicit performance range (YYYY-MM-DD). Use together with toDate.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of an explicit performance range (YYYY-MM-DD). Must be on or after fromDate.
        try {
            ApiResponse<GetCampaignAdSchedule200Response> response = apiInstance.getCampaignAdScheduleWithHttpInfo(campaignId, platform, includePerformance, windowDays, fromDate, toDate);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getCampaignAdSchedule");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Numeric Google platform campaign id. | |
| **platform** | **String**| Disambiguates the campaign id when the connection spans platforms. | [optional] [enum: google] |
| **includePerformance** | **Boolean**| Also return delivery by day of week and by hour. Costs one extra Google call. | [optional] |
| **windowDays** | **Integer**| Trailing window for the performance split. Ignored when fromDate and toDate are both given. | [optional] [default to 30] |
| **fromDate** | **LocalDate**| Start of an explicit performance range (YYYY-MM-DD). Use together with toDate. | [optional] |
| **toDate** | **LocalDate**| End of an explicit performance range (YYYY-MM-DD). Must be on or after fromDate. | [optional] |

### Return type

ApiResponse<[**GetCampaignAdSchedule200Response**](GetCampaignAdSchedule200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The campaign&#39;s ad schedule |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | Not a Google Ads campaign: ad schedules are a Google criterion. |  -  |


## getCampaignBidding

> GetCampaignBidding200Response getCampaignBidding(campaignId, accountId, platform, adAccountId, customerId)

Read a campaign&#39;s current bidding

Shows a Google campaign&#39;s current bidding strategy and targets, ready to prefill an edit.  Reads the campaign&#39;s bidding strategy on Google, cached for the quota window, for pre-filling the bid strategy block before a PUT to /v1/ads/campaigns/{campaignId}.  Google Ads only. &#x60;platform&#x60; is required and rejected when it is anything else, since a &#x60;campaignId&#x60; is not globally unique.  The response carries &#x60;cachedAt&#x60; and &#x60;stale&#x60;, set when a quota-exhausted call falls back to the last-good copy instead of a live read.  ### Strategy mapping  Maps Google&#39;s bidding strategy onto the same triplet PUT accepts:  - &#x60;LOWEST_COST_WITHOUT_CAP&#x60;: Maximize Conversions, no target - &#x60;COST_CAP&#x60; + &#x60;bidAmount&#x60;: Target CPA - &#x60;LOWEST_COST_WITH_MIN_ROAS&#x60; + &#x60;roasAverageFloor&#x60;: Target ROAS - &#x60;LOWEST_COST_WITH_BID_CAP&#x60; + &#x60;bidAmount&#x60;: Maximize Clicks with a CPC ceiling  A campaign on a portfolio strategy returns &#x60;portfolio&#x60; (id + name) and &#x60;bidSpec.portfolioBidStrategyId&#x60; instead of the triplet.  Anything else (Manual CPC, Target Impression Share, ...) returns &#x60;bidSpec: null&#x60;; show &#x60;biddingStrategyType&#x60; as-is. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Numeric Google platform campaign id.
        String accountId = "accountId_example"; // String | Zernio Google Ads SocialAccount id: resolves the customer id + refresh token.
        String platform = "google"; // String | Required: campaign IDs are not globally unique. Only \"google\" is supported today.
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID (Google customer ID, digits only). Required when the connection has multiple Google Ads accounts; optional (and inferred) when it has only one.
        String customerId = "customerId_example"; // String | Alias of adAccountId, kept for existing callers
        try {
            GetCampaignBidding200Response result = apiInstance.getCampaignBidding(campaignId, accountId, platform, adAccountId, customerId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getCampaignBidding");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Numeric Google platform campaign id. | |
| **accountId** | **String**| Zernio Google Ads SocialAccount id: resolves the customer id + refresh token. | |
| **platform** | **String**| Required: campaign IDs are not globally unique. Only \&quot;google\&quot; is supported today. | [enum: google] |
| **adAccountId** | **String**| Platform ad account ID (Google customer ID, digits only). Required when the connection has multiple Google Ads accounts; optional (and inferred) when it has only one. | [optional] |
| **customerId** | **String**| Alias of adAccountId, kept for existing callers | [optional] |

### Return type

[**GetCampaignBidding200Response**](GetCampaignBidding200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Campaign bidding |  -  |
| **400** | Invalid input (accountId, adAccountId, or a non-numeric campaignId), or a platform other than \&quot;google\&quot; |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans.  Also returned with code &#x60;ad_account_not_selected&#x60; when the connection has selected ad accounts and the ad account this request targets is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix it, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | Not a Google Ads account: the connection behind accountId resolves to another platform. |  -  |

## getCampaignBiddingWithHttpInfo

> ApiResponse<GetCampaignBidding200Response> getCampaignBidding getCampaignBiddingWithHttpInfo(campaignId, accountId, platform, adAccountId, customerId)

Read a campaign&#39;s current bidding

Shows a Google campaign&#39;s current bidding strategy and targets, ready to prefill an edit.  Reads the campaign&#39;s bidding strategy on Google, cached for the quota window, for pre-filling the bid strategy block before a PUT to /v1/ads/campaigns/{campaignId}.  Google Ads only. &#x60;platform&#x60; is required and rejected when it is anything else, since a &#x60;campaignId&#x60; is not globally unique.  The response carries &#x60;cachedAt&#x60; and &#x60;stale&#x60;, set when a quota-exhausted call falls back to the last-good copy instead of a live read.  ### Strategy mapping  Maps Google&#39;s bidding strategy onto the same triplet PUT accepts:  - &#x60;LOWEST_COST_WITHOUT_CAP&#x60;: Maximize Conversions, no target - &#x60;COST_CAP&#x60; + &#x60;bidAmount&#x60;: Target CPA - &#x60;LOWEST_COST_WITH_MIN_ROAS&#x60; + &#x60;roasAverageFloor&#x60;: Target ROAS - &#x60;LOWEST_COST_WITH_BID_CAP&#x60; + &#x60;bidAmount&#x60;: Maximize Clicks with a CPC ceiling  A campaign on a portfolio strategy returns &#x60;portfolio&#x60; (id + name) and &#x60;bidSpec.portfolioBidStrategyId&#x60; instead of the triplet.  Anything else (Manual CPC, Target Impression Share, ...) returns &#x60;bidSpec: null&#x60;; show &#x60;biddingStrategyType&#x60; as-is. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Numeric Google platform campaign id.
        String accountId = "accountId_example"; // String | Zernio Google Ads SocialAccount id: resolves the customer id + refresh token.
        String platform = "google"; // String | Required: campaign IDs are not globally unique. Only \"google\" is supported today.
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID (Google customer ID, digits only). Required when the connection has multiple Google Ads accounts; optional (and inferred) when it has only one.
        String customerId = "customerId_example"; // String | Alias of adAccountId, kept for existing callers
        try {
            ApiResponse<GetCampaignBidding200Response> response = apiInstance.getCampaignBiddingWithHttpInfo(campaignId, accountId, platform, adAccountId, customerId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getCampaignBidding");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Numeric Google platform campaign id. | |
| **accountId** | **String**| Zernio Google Ads SocialAccount id: resolves the customer id + refresh token. | |
| **platform** | **String**| Required: campaign IDs are not globally unique. Only \&quot;google\&quot; is supported today. | [enum: google] |
| **adAccountId** | **String**| Platform ad account ID (Google customer ID, digits only). Required when the connection has multiple Google Ads accounts; optional (and inferred) when it has only one. | [optional] |
| **customerId** | **String**| Alias of adAccountId, kept for existing callers | [optional] |

### Return type

ApiResponse<[**GetCampaignBidding200Response**](GetCampaignBidding200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Campaign bidding |  -  |
| **400** | Invalid input (accountId, adAccountId, or a non-numeric campaignId), or a platform other than \&quot;google\&quot; |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans.  Also returned with code &#x60;ad_account_not_selected&#x60; when the connection has selected ad accounts and the ad account this request targets is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix it, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **501** | Not a Google Ads account: the connection behind accountId resolves to another platform. |  -  |


## getCampaignConversionGoals

> GetCampaignConversionGoals200Response getCampaignConversionGoals(campaignId)

Get campaign conversion goals

Shows which conversion goals a Google campaign bids on, and whether it follows the account defaults or uses its own or a custom goal.  A Google campaign&#39;s conversion goals (CampaignConversionGoal, &#x60;biddable&#x60; per category and origin) and its goal config (ConversionGoalCampaignConfig): &#x60;goalConfigLevel&#x60; CUSTOMER means the campaign follows the account-default goals, CAMPAIGN means it uses its own goals or &#x60;customConversionGoalId&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Google campaign id
        try {
            GetCampaignConversionGoals200Response result = apiInstance.getCampaignConversionGoals(campaignId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getCampaignConversionGoals");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Google campaign id | |

### Return type

[**GetCampaignConversionGoals200Response**](GetCampaignConversionGoals200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign conversion goals |  -  |
| **400** | Invalid request |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Campaign not found |  -  |
| **409** | Campaign matches multiple accessible accounts, or the connection needs reconnecting |  -  |
| **501** | Only available on Google Ads campaigns |  -  |

## getCampaignConversionGoalsWithHttpInfo

> ApiResponse<GetCampaignConversionGoals200Response> getCampaignConversionGoals getCampaignConversionGoalsWithHttpInfo(campaignId)

Get campaign conversion goals

Shows which conversion goals a Google campaign bids on, and whether it follows the account defaults or uses its own or a custom goal.  A Google campaign&#39;s conversion goals (CampaignConversionGoal, &#x60;biddable&#x60; per category and origin) and its goal config (ConversionGoalCampaignConfig): &#x60;goalConfigLevel&#x60; CUSTOMER means the campaign follows the account-default goals, CAMPAIGN means it uses its own goals or &#x60;customConversionGoalId&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Google campaign id
        try {
            ApiResponse<GetCampaignConversionGoals200Response> response = apiInstance.getCampaignConversionGoalsWithHttpInfo(campaignId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getCampaignConversionGoals");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Google campaign id | |

### Return type

ApiResponse<[**GetCampaignConversionGoals200Response**](GetCampaignConversionGoals200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign conversion goals |  -  |
| **400** | Invalid request |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Campaign not found |  -  |
| **409** | Campaign matches multiple accessible accounts, or the connection needs reconnecting |  -  |
| **501** | Only available on Google Ads campaigns |  -  |


## getCampaignTargeting

> GetCampaignTargeting200Response getCampaignTargeting(campaignId, platform)

Read a Google campaign&#39;s device, location, excluded location, and language targeting

Shows a Google campaign&#39;s device, location, excluded location and language targeting so you can build an editor for it.  Google Ads compliance requires geo, language, budget, and bidding targeting set at creation to stay editable afterwards. This reads the campaign state so an integrator can build an editor around it.  - Cached for the quota window (10 minutes fresh, up to 7 days last-good), not always a live read. - Google only; every other platform returns 501.  ### Devices  &#x60;devices&#x60; lists the device criteria the campaign carries, which depends on its channel:  - Search campaigns have MOBILE, DESKTOP and TABLET. - Display campaigns also have CONNECTED_TV.  &#x60;bidModifier&#x60; is Google&#39;s bid adjustment for that device: &#x60;null&#x60; when it has none, and &#x60;0&#x60; when the device is switched off. &#x60;included&#x60; is false for exactly that case.  ### Locations  &#x60;excludedLocations&#x60; lists the campaign&#39;s negative location criteria (the places it never serves in).  &#x60;locations&#x60; still lists every location criterion, each flagged with &#x60;negative&#x60;, so a client reading the targeted set filters &#x60;negative: false&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Google platform campaign ID
        String platform = "google"; // String | Disambiguates when the same campaignId string exists on more than one connected platform.
        try {
            GetCampaignTargeting200Response result = apiInstance.getCampaignTargeting(campaignId, platform);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getCampaignTargeting");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Google platform campaign ID | |
| **platform** | **String**| Disambiguates when the same campaignId string exists on more than one connected platform. | [optional] [enum: google] |

### Return type

[**GetCampaignTargeting200Response**](GetCampaignTargeting200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current campaign targeting |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans). |  -  |
| **404** | Campaign not found |  -  |
| **501** | Only available on Google Ads campaigns |  -  |

## getCampaignTargetingWithHttpInfo

> ApiResponse<GetCampaignTargeting200Response> getCampaignTargeting getCampaignTargetingWithHttpInfo(campaignId, platform)

Read a Google campaign&#39;s device, location, excluded location, and language targeting

Shows a Google campaign&#39;s device, location, excluded location and language targeting so you can build an editor for it.  Google Ads compliance requires geo, language, budget, and bidding targeting set at creation to stay editable afterwards. This reads the campaign state so an integrator can build an editor around it.  - Cached for the quota window (10 minutes fresh, up to 7 days last-good), not always a live read. - Google only; every other platform returns 501.  ### Devices  &#x60;devices&#x60; lists the device criteria the campaign carries, which depends on its channel:  - Search campaigns have MOBILE, DESKTOP and TABLET. - Display campaigns also have CONNECTED_TV.  &#x60;bidModifier&#x60; is Google&#39;s bid adjustment for that device: &#x60;null&#x60; when it has none, and &#x60;0&#x60; when the device is switched off. &#x60;included&#x60; is false for exactly that case.  ### Locations  &#x60;excludedLocations&#x60; lists the campaign&#39;s negative location criteria (the places it never serves in).  &#x60;locations&#x60; still lists every location criterion, each flagged with &#x60;negative&#x60;, so a client reading the targeted set filters &#x60;negative: false&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Google platform campaign ID
        String platform = "google"; // String | Disambiguates when the same campaignId string exists on more than one connected platform.
        try {
            ApiResponse<GetCampaignTargeting200Response> response = apiInstance.getCampaignTargetingWithHttpInfo(campaignId, platform);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getCampaignTargeting");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Google platform campaign ID | |
| **platform** | **String**| Disambiguates when the same campaignId string exists on more than one connected platform. | [optional] [enum: google] |

### Return type

ApiResponse<[**GetCampaignTargeting200Response**](GetCampaignTargeting200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current campaign targeting |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans). |  -  |
| **404** | Campaign not found |  -  |
| **501** | Only available on Google Ads campaigns |  -  |


## getGoogleAssetGroup

> GetGoogleAssetGroup200Response getGoogleAssetGroup(campaignId, assetGroupId)

Get a Performance Max asset group

Shows one Performance Max asset group with its linked assets, ad strength, status and product targeting tree.  One asset group with its linked assets, ad strength, primary status and listing-group tree. Uses a 10-minute cache, served stale when Google quota is exhausted; any write below clears it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Google Ads campaign id.
        String assetGroupId = "assetGroupId_example"; // String | Google asset group id.
        try {
            GetGoogleAssetGroup200Response result = apiInstance.getGoogleAssetGroup(campaignId, assetGroupId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getGoogleAssetGroup");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Google Ads campaign id. | |
| **assetGroupId** | **String**| Google asset group id. | |

### Return type

[**GetGoogleAssetGroup200Response**](GetGoogleAssetGroup200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The asset group. |  -  |
| **400** | Invalid request |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **422** | Google Ads connection needs reconnecting. |  -  |
| **429** | Google quota or the Zernio Google operations burst limit is exhausted. |  -  |
| **501** | Campaign is not on Google Ads. |  -  |

## getGoogleAssetGroupWithHttpInfo

> ApiResponse<GetGoogleAssetGroup200Response> getGoogleAssetGroup getGoogleAssetGroupWithHttpInfo(campaignId, assetGroupId)

Get a Performance Max asset group

Shows one Performance Max asset group with its linked assets, ad strength, status and product targeting tree.  One asset group with its linked assets, ad strength, primary status and listing-group tree. Uses a 10-minute cache, served stale when Google quota is exhausted; any write below clears it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Google Ads campaign id.
        String assetGroupId = "assetGroupId_example"; // String | Google asset group id.
        try {
            ApiResponse<GetGoogleAssetGroup200Response> response = apiInstance.getGoogleAssetGroupWithHttpInfo(campaignId, assetGroupId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getGoogleAssetGroup");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Google Ads campaign id. | |
| **assetGroupId** | **String**| Google asset group id. | |

### Return type

ApiResponse<[**GetGoogleAssetGroup200Response**](GetGoogleAssetGroup200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The asset group. |  -  |
| **400** | Invalid request |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **422** | Google Ads connection needs reconnecting. |  -  |
| **429** | Google quota or the Zernio Google operations burst limit is exhausted. |  -  |
| **501** | Campaign is not on Google Ads. |  -  |


## getTikTokSmartPlusAdReview

> GetTikTokSmartPlusAdReview200Response getTikTokSmartPlusAdReview(adId)

Review status of each creative in a TikTok Smart+ ad

Shows which Spark post, video or carousel of an Upgraded Smart+ ad TikTok approved or rejected, with every rejection reason, keyed by the TikTok post id for a Spark post.  It reads TikTok&#39;s &#x60;/smart_plus/ad/review_info/&#x60; live (read-only, works on a paused ad) for the Smart+ ad that holds &#x60;adId&#x60;. It returns the ad-level verdict plus one entry per creative.  ### Which ad is read  &#x60;adId&#x60; may be the Smart+ ad itself or any creative of it synced as its own ad. Zernio finds the Smart+ ad in the ad&#39;s ad group through &#x60;/smart_plus/ad/get/&#x60;, and uses the ad group&#39;s only Smart+ ad when no creative list names the ad.  ### Creative fields  &#x60;materialType&#x60;, &#x60;tiktokItemId&#x60;, &#x60;videoId&#x60;, &#x60;name&#x60; and &#x60;operationStatus&#x60; come from the Smart+ ad&#39;s &#x60;creative_list&#x60;. Some entries come back with the review verdict and null descriptive fields:  - creatives TikTok added on its own, which it leaves out of that list (creator content, authorized TikTok posts, Creative Library content) - each image of a carousel, which TikTok lists under its own material id  TikTok returns no review timestamp; &#x60;readAt&#x60; is when Zernio read it.  ### Quota and caching  TikTok&#39;s review endpoint has a strict quota of its own (TikTok documents neither the quota nor its scope). One TikTok call reads the review of the live Smart+ ads of the ad group, up to 50 creatives in total (TikTok refuses more).  Each review is stored per connection, advertiser and Smart+ ad. A review read in the last 10 minutes is served from the store, so sibling ads are answered without a TikTok call and &#x60;readAt&#x60; can be up to 10 minutes old. An older one is read again.  Read reviews when you need them instead of sweeping every ad on a loop.  ### Over quota  When TikTok answers over quota, Zernio returns 429. It then answers 429 for that advertiser and connection without calling TikTok:  - for about 60 seconds at first - then 120, and up to 240, while TikTok keeps refusing - about 60 again after a successful call  Each pause has up to 10% of random jitter, with the time left as &#x60;Retry-After&#x60;. Reviews read in the last 10 minutes are still served. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adId = "adId_example"; // String | Zernio ad id (24-char hex) or the TikTok ad id: the Smart+ ad id or the ad id of one of its creatives.
        try {
            GetTikTokSmartPlusAdReview200Response result = apiInstance.getTikTokSmartPlusAdReview(adId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getTikTokSmartPlusAdReview");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adId** | **String**| Zernio ad id (24-char hex) or the TikTok ad id: the Smart+ ad id or the ad id of one of its creatives. | |

### Return type

[**GetTikTokSmartPlusAdReview200Response**](GetTikTokSmartPlusAdReview200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **200** | The Smart+ ad&#39;s review verdict per creative |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Ad not found, it has no TikTok ad or ad group id yet, or no Smart+ ad of its ad group holds it. In the last case &#x60;details.listedSmartPlusAds&#x60; is how many Smart+ ads TikTok lists in the ad group, deleted ones included: 0 means the ad group lists none. |  -  |
| **422** | The TikTok ad is not an Upgraded Smart+ ad (read it with GET /v1/ads/{adId}/review) |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted. Behavior per platform:  - **Reddit:** rate-limits per connected Reddit user (1000 requests per 10-minute window), shared by every operation on that account. Retry after the window resets; repeated calls while exhausted do not succeed and keep the budget spent. - **Google Ads:** writes and reports run on one developer token shared by every Google Ads account on Zernio. It holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. - **Google Ads envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **YouTube Analytics:** reads (channel-insights, demographics, daily-views, video-retention) use the \&quot;Queries per day\&quot; quota of the Google Cloud project the account is connected through, shared with other Zernio customers, so a 429 is not your own volume. Resets at midnight Pacific Time. - **YouTube Analytics envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaExhausted: true&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60;, &#x60;details.resetsAt&#x60; and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **Meta ads:** every Meta throttle (codes 4, 17, 32, 613 and business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when sent, else Meta&#39;s 60-second minimum (30 seconds for the one-write-per-30-seconds limit on one object). - **Pinterest ads:** limits per user and app, per category (ads_read, ads_write, ads_analytics). &#x60;Retry-After&#x60; comes from Pinterest&#39;s &#x60;x-ratelimit-reset&#x60; when sent, otherwise 60 seconds. - **TikTok ads:** limits per app and per endpoint (per second, minute and day), answering overage with code 40100 or code 40002 &#x60;OVER_QPS_LIMIT&#x60;. Both return 429 &#x60;rate_limited&#x60; with &#x60;platform: tiktok&#x60; and &#x60;Retry-After: 10&#x60;. Space out bulk reads (e.g. one ad at a time per advertiser) instead of retrying at once.  **TikTok Smart+ review read** (&#x60;GET /v1/ads/{adId}/tiktok-smart-plus-review&#x60;) has its own stricter TikTok quota. After an overage, Zernio answers 429 for that advertiser and connection without calling TikTok for about 60 seconds, then 120, up to 240 while TikTok keeps refusing, each with up to 10% random jitter.  A successful call holds nothing back; the next overage pauses about 60 seconds again. &#x60;Retry-After&#x60; is the time left. The advertiser-wide read (&#x60;GET /v1/ads/tiktok-smart-plus-reviews&#x60;) answers 200 with &#x60;retryAfterSeconds&#x60; and &#x60;refreshState&#x60; instead. Keep one request in flight per advertiser there.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |
| **501** | Only supported on TikTok |  -  |

## getTikTokSmartPlusAdReviewWithHttpInfo

> ApiResponse<GetTikTokSmartPlusAdReview200Response> getTikTokSmartPlusAdReview getTikTokSmartPlusAdReviewWithHttpInfo(adId)

Review status of each creative in a TikTok Smart+ ad

Shows which Spark post, video or carousel of an Upgraded Smart+ ad TikTok approved or rejected, with every rejection reason, keyed by the TikTok post id for a Spark post.  It reads TikTok&#39;s &#x60;/smart_plus/ad/review_info/&#x60; live (read-only, works on a paused ad) for the Smart+ ad that holds &#x60;adId&#x60;. It returns the ad-level verdict plus one entry per creative.  ### Which ad is read  &#x60;adId&#x60; may be the Smart+ ad itself or any creative of it synced as its own ad. Zernio finds the Smart+ ad in the ad&#39;s ad group through &#x60;/smart_plus/ad/get/&#x60;, and uses the ad group&#39;s only Smart+ ad when no creative list names the ad.  ### Creative fields  &#x60;materialType&#x60;, &#x60;tiktokItemId&#x60;, &#x60;videoId&#x60;, &#x60;name&#x60; and &#x60;operationStatus&#x60; come from the Smart+ ad&#39;s &#x60;creative_list&#x60;. Some entries come back with the review verdict and null descriptive fields:  - creatives TikTok added on its own, which it leaves out of that list (creator content, authorized TikTok posts, Creative Library content) - each image of a carousel, which TikTok lists under its own material id  TikTok returns no review timestamp; &#x60;readAt&#x60; is when Zernio read it.  ### Quota and caching  TikTok&#39;s review endpoint has a strict quota of its own (TikTok documents neither the quota nor its scope). One TikTok call reads the review of the live Smart+ ads of the ad group, up to 50 creatives in total (TikTok refuses more).  Each review is stored per connection, advertiser and Smart+ ad. A review read in the last 10 minutes is served from the store, so sibling ads are answered without a TikTok call and &#x60;readAt&#x60; can be up to 10 minutes old. An older one is read again.  Read reviews when you need them instead of sweeping every ad on a loop.  ### Over quota  When TikTok answers over quota, Zernio returns 429. It then answers 429 for that advertiser and connection without calling TikTok:  - for about 60 seconds at first - then 120, and up to 240, while TikTok keeps refusing - about 60 again after a successful call  Each pause has up to 10% of random jitter, with the time left as &#x60;Retry-After&#x60;. Reviews read in the last 10 minutes are still served. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adId = "adId_example"; // String | Zernio ad id (24-char hex) or the TikTok ad id: the Smart+ ad id or the ad id of one of its creatives.
        try {
            ApiResponse<GetTikTokSmartPlusAdReview200Response> response = apiInstance.getTikTokSmartPlusAdReviewWithHttpInfo(adId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#getTikTokSmartPlusAdReview");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adId** | **String**| Zernio ad id (24-char hex) or the TikTok ad id: the Smart+ ad id or the ad id of one of its creatives. | |

### Return type

ApiResponse<[**GetTikTokSmartPlusAdReview200Response**](GetTikTokSmartPlusAdReview200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **200** | The Smart+ ad&#39;s review verdict per creative |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Ad not found, it has no TikTok ad or ad group id yet, or no Smart+ ad of its ad group holds it. In the last case &#x60;details.listedSmartPlusAds&#x60; is how many Smart+ ads TikTok lists in the ad group, deleted ones included: 0 means the ad group lists none. |  -  |
| **422** | The TikTok ad is not an Upgraded Smart+ ad (read it with GET /v1/ads/{adId}/review) |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted. Behavior per platform:  - **Reddit:** rate-limits per connected Reddit user (1000 requests per 10-minute window), shared by every operation on that account. Retry after the window resets; repeated calls while exhausted do not succeed and keep the budget spent. - **Google Ads:** writes and reports run on one developer token shared by every Google Ads account on Zernio. It holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. - **Google Ads envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **YouTube Analytics:** reads (channel-insights, demographics, daily-views, video-retention) use the \&quot;Queries per day\&quot; quota of the Google Cloud project the account is connected through, shared with other Zernio customers, so a 429 is not your own volume. Resets at midnight Pacific Time. - **YouTube Analytics envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaExhausted: true&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60;, &#x60;details.resetsAt&#x60; and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **Meta ads:** every Meta throttle (codes 4, 17, 32, 613 and business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when sent, else Meta&#39;s 60-second minimum (30 seconds for the one-write-per-30-seconds limit on one object). - **Pinterest ads:** limits per user and app, per category (ads_read, ads_write, ads_analytics). &#x60;Retry-After&#x60; comes from Pinterest&#39;s &#x60;x-ratelimit-reset&#x60; when sent, otherwise 60 seconds. - **TikTok ads:** limits per app and per endpoint (per second, minute and day), answering overage with code 40100 or code 40002 &#x60;OVER_QPS_LIMIT&#x60;. Both return 429 &#x60;rate_limited&#x60; with &#x60;platform: tiktok&#x60; and &#x60;Retry-After: 10&#x60;. Space out bulk reads (e.g. one ad at a time per advertiser) instead of retrying at once.  **TikTok Smart+ review read** (&#x60;GET /v1/ads/{adId}/tiktok-smart-plus-review&#x60;) has its own stricter TikTok quota. After an overage, Zernio answers 429 for that advertiser and connection without calling TikTok for about 60 seconds, then 120, up to 240 while TikTok keeps refusing, each with up to 10% random jitter.  A successful call holds nothing back; the next overage pauses about 60 seconds again. &#x60;Retry-After&#x60; is the time left. The advertiser-wide read (&#x60;GET /v1/ads/tiktok-smart-plus-reviews&#x60;) answers 200 with &#x60;retryAfterSeconds&#x60; and &#x60;refreshState&#x60; instead. Keep one request in flight per advertiser there.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |
| **501** | Only supported on TikTok |  -  |


## listAdCampaigns

> ListAdCampaigns200Response listAdCampaigns(includeEmpty, page, limit, source, platform, status, adAccountId, campaignId, pageId, accountId, profileId, fromDate, toDate, hasDelivery, minSpend, live)

List campaigns

Lists your campaigns with spend, impressions and clicks summed across their ads, plus each campaign&#39;s status and budget.  Campaigns are virtual aggregations over ad documents grouped by platform campaign ID. Metrics (spend, impressions, clicks, etc.) are summed across all ads in each campaign.  Campaign status is derived from child ad statuses: active &gt; pending_review &gt; paused &gt; error &gt; completed &gt; cancelled &gt; rejected.  Google campaign budgets include amountMicros, explicitlyShared, resourceName and deliveryMethod after the next successful sync. This endpoint does not fetch Google live.  **Status freshness.** &#x60;status&#x60;, &#x60;configuredStatus&#x60;, &#x60;platformStatus&#x60;, &#x60;platformAdSetStatus&#x60; and &#x60;platformCampaignStatus&#x60; are the values Zernio last stored.  Background sync refreshes them, typically within 15 to 60 minutes (Google up to about 3 hours), and ended or long-paused objects may be refreshed less often.  Zernio&#39;s own status writes re-read the switches they change. A change made in the platform&#39;s own ads manager therefore shows up here only after the next sync.  ### Live status reads  Controllers that act on a switch should pass &#x60;live&#x3D;true&#x60;. It reads the switches from the platform now, stores them, and returns &#x60;statusReadAt&#x60; (null when the read failed and the stored values were returned).  - &#x60;live&#x3D;true&#x60; needs &#x60;limit&#x60; of 20 or less. - Each returned campaign&#39;s own switch (&#x60;platformCampaignStatus&#x60;) is read live. - Live reads cover TikTok, Meta, Google, OpenAI and Reddit. - The rolled-up &#x60;status&#x60; is not re-derived by a live read.  **Budgets here are SYNCED**, never read live, including with &#x60;live&#x3D;true&#x60;. To read the current budgets (and status) of every campaign and ad set of a Meta ad account live in one call, for example as a pre-write spend gate, use GET /v1/ads/accounts/live. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        Boolean includeEmpty = true; // Boolean | Meta only. Set true to also list campaigns with ZERO ads, with `adCount: 0` and zeroed metrics.  Campaign reads aggregate over ad documents, so such campaigns are normally invisible. The two-step create (campaign, then ads via `existingCampaignId`) leaves one behind whenever Meta rejects the ad step.  Requires `accountId` and `adAccountId`, since an empty campaign has no ad row to resolve a token or ad account from. 
        Integer page = 1; // Integer | Page number (1-based)
        Integer limit = 20; // Integer | 
        String source = "zernio"; // String | `all` (default) returns both Zernio-created ads and those discovered from the platform's ad manager. Matches the web UI's default view. Pass `zernio` to restrict to isExternal=false only. Status is NOT filtered by default; use the `status` param for that.
        String platform = "facebook"; // String | 
        AdStatus status = AdStatus.fromValue("active"); // AdStatus | Filter by derived campaign status (post-aggregation)
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID (e.g. act_123 for Meta)
        String campaignId = "campaignId_example"; // String | Platform campaign ID (the `platformCampaignId` on each returned campaign). Returns only that campaign, or an empty list when it is not visible to the caller. Mirrors the same filter on /v1/ads and /v1/ads/tree.
        String pageId = "pageId_example"; // String | Meta only: Facebook Page ID. Campaigns have no Page of their own, so this keeps campaigns having at least one ad backed by this Page, with adCount and metrics computed over those ads only. Mirrors the same filter on /v1/ads and /v1/ads/tree.
        String accountId = "accountId_example"; // String | Account ID
        String profileId = "profileId_example"; // String | Profile ID
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of metrics date range (YYYY-MM-DD, inclusive). Defaults to 90 days ago when both date params are omitted.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of metrics date range (YYYY-MM-DD, inclusive). Defaults to today. Max 730-day range.
        Boolean hasDelivery = true; // Boolean | Return only campaigns that delivered between `fromDate` and `toDate`: spend above zero, or impressions served at zero spend.  Unlike `status`, which reads a campaign's CURRENT state, this filters on what happened inside the window. It filters the campaign set itself, so `pagination.total` counts only matching campaigns. Mirrors the same filter on /v1/ads/tree.
        BigDecimal minSpend = new BigDecimal(78); // BigDecimal | Return only campaigns whose spend between `fromDate` and `toDate` reaches this amount, in each campaign's OWN currency (the `currency` field on the campaign). Implies `hasDelivery`; `minSpend=0` applies no filter. Mirrors the same filter on /v1/ads/tree.
        Boolean live = false; // Boolean | Read the on/off switches live from the platform instead of returning synced values. See \"Status freshness\" in the operation description.  - The fresh values are stored (later reads return them too), and the response carries `statusReadAt`, the time of the read. - At most 20 platform objects are read per request. - Where a read fails (credentials, platform error, no reader on that platform), stored values come back with `statusReadAt: null`.  **On X** the budget is read live too:  - GET /v1/ads/{adId}: `budget`, `adSetBudget`, `campaignBudget` and `budgetLevel` are the line item and campaign budgets X holds now (stored like the switches). - Ad set and campaign listings: `budget` is what that line item or campaign holds now (returned, not stored). A row whose budget the other level holds keeps its synced `budget`. 
        try {
            ListAdCampaigns200Response result = apiInstance.listAdCampaigns(includeEmpty, page, limit, source, platform, status, adAccountId, campaignId, pageId, accountId, profileId, fromDate, toDate, hasDelivery, minSpend, live);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listAdCampaigns");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **includeEmpty** | **Boolean**| Meta only. Set true to also list campaigns with ZERO ads, with &#x60;adCount: 0&#x60; and zeroed metrics.  Campaign reads aggregate over ad documents, so such campaigns are normally invisible. The two-step create (campaign, then ads via &#x60;existingCampaignId&#x60;) leaves one behind whenever Meta rejects the ad step.  Requires &#x60;accountId&#x60; and &#x60;adAccountId&#x60;, since an empty campaign has no ad row to resolve a token or ad account from.  | [optional] |
| **page** | **Integer**| Page number (1-based) | [optional] [default to 1] |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **source** | **String**| &#x60;all&#x60; (default) returns both Zernio-created ads and those discovered from the platform&#39;s ad manager. Matches the web UI&#39;s default view. Pass &#x60;zernio&#x60; to restrict to isExternal&#x3D;false only. Status is NOT filtered by default; use the &#x60;status&#x60; param for that. | [optional] [default to all] [enum: zernio, all] |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai, reddit] |
| **status** | [**AdStatus**](.md)| Filter by derived campaign status (post-aggregation) | [optional] [enum: active, paused, pending_review, rejected, completed, cancelled, error] |
| **adAccountId** | **String**| Platform ad account ID (e.g. act_123 for Meta) | [optional] |
| **campaignId** | **String**| Platform campaign ID (the &#x60;platformCampaignId&#x60; on each returned campaign). Returns only that campaign, or an empty list when it is not visible to the caller. Mirrors the same filter on /v1/ads and /v1/ads/tree. | [optional] |
| **pageId** | **String**| Meta only: Facebook Page ID. Campaigns have no Page of their own, so this keeps campaigns having at least one ad backed by this Page, with adCount and metrics computed over those ads only. Mirrors the same filter on /v1/ads and /v1/ads/tree. | [optional] |
| **accountId** | **String**| Account ID | [optional] |
| **profileId** | **String**| Profile ID | [optional] |
| **fromDate** | **LocalDate**| Start of metrics date range (YYYY-MM-DD, inclusive). Defaults to 90 days ago when both date params are omitted. | [optional] |
| **toDate** | **LocalDate**| End of metrics date range (YYYY-MM-DD, inclusive). Defaults to today. Max 730-day range. | [optional] |
| **hasDelivery** | **Boolean**| Return only campaigns that delivered between &#x60;fromDate&#x60; and &#x60;toDate&#x60;: spend above zero, or impressions served at zero spend.  Unlike &#x60;status&#x60;, which reads a campaign&#39;s CURRENT state, this filters on what happened inside the window. It filters the campaign set itself, so &#x60;pagination.total&#x60; counts only matching campaigns. Mirrors the same filter on /v1/ads/tree. | [optional] |
| **minSpend** | **BigDecimal**| Return only campaigns whose spend between &#x60;fromDate&#x60; and &#x60;toDate&#x60; reaches this amount, in each campaign&#39;s OWN currency (the &#x60;currency&#x60; field on the campaign). Implies &#x60;hasDelivery&#x60;; &#x60;minSpend&#x3D;0&#x60; applies no filter. Mirrors the same filter on /v1/ads/tree. | [optional] |
| **live** | **Boolean**| Read the on/off switches live from the platform instead of returning synced values. See \&quot;Status freshness\&quot; in the operation description.  - The fresh values are stored (later reads return them too), and the response carries &#x60;statusReadAt&#x60;, the time of the read. - At most 20 platform objects are read per request. - Where a read fails (credentials, platform error, no reader on that platform), stored values come back with &#x60;statusReadAt: null&#x60;.  **On X** the budget is read live too:  - GET /v1/ads/{adId}: &#x60;budget&#x60;, &#x60;adSetBudget&#x60;, &#x60;campaignBudget&#x60; and &#x60;budgetLevel&#x60; are the line item and campaign budgets X holds now (stored like the switches). - Ad set and campaign listings: &#x60;budget&#x60; is what that line item or campaign holds now (returned, not stored). A row whose budget the other level holds keeps its synced &#x60;budget&#x60;.  | [optional] [default to false] |

### Return type

[**ListAdCampaigns200Response**](ListAdCampaigns200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | Paginated campaigns |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |

## listAdCampaignsWithHttpInfo

> ApiResponse<ListAdCampaigns200Response> listAdCampaigns listAdCampaignsWithHttpInfo(includeEmpty, page, limit, source, platform, status, adAccountId, campaignId, pageId, accountId, profileId, fromDate, toDate, hasDelivery, minSpend, live)

List campaigns

Lists your campaigns with spend, impressions and clicks summed across their ads, plus each campaign&#39;s status and budget.  Campaigns are virtual aggregations over ad documents grouped by platform campaign ID. Metrics (spend, impressions, clicks, etc.) are summed across all ads in each campaign.  Campaign status is derived from child ad statuses: active &gt; pending_review &gt; paused &gt; error &gt; completed &gt; cancelled &gt; rejected.  Google campaign budgets include amountMicros, explicitlyShared, resourceName and deliveryMethod after the next successful sync. This endpoint does not fetch Google live.  **Status freshness.** &#x60;status&#x60;, &#x60;configuredStatus&#x60;, &#x60;platformStatus&#x60;, &#x60;platformAdSetStatus&#x60; and &#x60;platformCampaignStatus&#x60; are the values Zernio last stored.  Background sync refreshes them, typically within 15 to 60 minutes (Google up to about 3 hours), and ended or long-paused objects may be refreshed less often.  Zernio&#39;s own status writes re-read the switches they change. A change made in the platform&#39;s own ads manager therefore shows up here only after the next sync.  ### Live status reads  Controllers that act on a switch should pass &#x60;live&#x3D;true&#x60;. It reads the switches from the platform now, stores them, and returns &#x60;statusReadAt&#x60; (null when the read failed and the stored values were returned).  - &#x60;live&#x3D;true&#x60; needs &#x60;limit&#x60; of 20 or less. - Each returned campaign&#39;s own switch (&#x60;platformCampaignStatus&#x60;) is read live. - Live reads cover TikTok, Meta, Google, OpenAI and Reddit. - The rolled-up &#x60;status&#x60; is not re-derived by a live read.  **Budgets here are SYNCED**, never read live, including with &#x60;live&#x3D;true&#x60;. To read the current budgets (and status) of every campaign and ad set of a Meta ad account live in one call, for example as a pre-write spend gate, use GET /v1/ads/accounts/live. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        Boolean includeEmpty = true; // Boolean | Meta only. Set true to also list campaigns with ZERO ads, with `adCount: 0` and zeroed metrics.  Campaign reads aggregate over ad documents, so such campaigns are normally invisible. The two-step create (campaign, then ads via `existingCampaignId`) leaves one behind whenever Meta rejects the ad step.  Requires `accountId` and `adAccountId`, since an empty campaign has no ad row to resolve a token or ad account from. 
        Integer page = 1; // Integer | Page number (1-based)
        Integer limit = 20; // Integer | 
        String source = "zernio"; // String | `all` (default) returns both Zernio-created ads and those discovered from the platform's ad manager. Matches the web UI's default view. Pass `zernio` to restrict to isExternal=false only. Status is NOT filtered by default; use the `status` param for that.
        String platform = "facebook"; // String | 
        AdStatus status = AdStatus.fromValue("active"); // AdStatus | Filter by derived campaign status (post-aggregation)
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID (e.g. act_123 for Meta)
        String campaignId = "campaignId_example"; // String | Platform campaign ID (the `platformCampaignId` on each returned campaign). Returns only that campaign, or an empty list when it is not visible to the caller. Mirrors the same filter on /v1/ads and /v1/ads/tree.
        String pageId = "pageId_example"; // String | Meta only: Facebook Page ID. Campaigns have no Page of their own, so this keeps campaigns having at least one ad backed by this Page, with adCount and metrics computed over those ads only. Mirrors the same filter on /v1/ads and /v1/ads/tree.
        String accountId = "accountId_example"; // String | Account ID
        String profileId = "profileId_example"; // String | Profile ID
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of metrics date range (YYYY-MM-DD, inclusive). Defaults to 90 days ago when both date params are omitted.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of metrics date range (YYYY-MM-DD, inclusive). Defaults to today. Max 730-day range.
        Boolean hasDelivery = true; // Boolean | Return only campaigns that delivered between `fromDate` and `toDate`: spend above zero, or impressions served at zero spend.  Unlike `status`, which reads a campaign's CURRENT state, this filters on what happened inside the window. It filters the campaign set itself, so `pagination.total` counts only matching campaigns. Mirrors the same filter on /v1/ads/tree.
        BigDecimal minSpend = new BigDecimal(78); // BigDecimal | Return only campaigns whose spend between `fromDate` and `toDate` reaches this amount, in each campaign's OWN currency (the `currency` field on the campaign). Implies `hasDelivery`; `minSpend=0` applies no filter. Mirrors the same filter on /v1/ads/tree.
        Boolean live = false; // Boolean | Read the on/off switches live from the platform instead of returning synced values. See \"Status freshness\" in the operation description.  - The fresh values are stored (later reads return them too), and the response carries `statusReadAt`, the time of the read. - At most 20 platform objects are read per request. - Where a read fails (credentials, platform error, no reader on that platform), stored values come back with `statusReadAt: null`.  **On X** the budget is read live too:  - GET /v1/ads/{adId}: `budget`, `adSetBudget`, `campaignBudget` and `budgetLevel` are the line item and campaign budgets X holds now (stored like the switches). - Ad set and campaign listings: `budget` is what that line item or campaign holds now (returned, not stored). A row whose budget the other level holds keeps its synced `budget`. 
        try {
            ApiResponse<ListAdCampaigns200Response> response = apiInstance.listAdCampaignsWithHttpInfo(includeEmpty, page, limit, source, platform, status, adAccountId, campaignId, pageId, accountId, profileId, fromDate, toDate, hasDelivery, minSpend, live);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listAdCampaigns");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **includeEmpty** | **Boolean**| Meta only. Set true to also list campaigns with ZERO ads, with &#x60;adCount: 0&#x60; and zeroed metrics.  Campaign reads aggregate over ad documents, so such campaigns are normally invisible. The two-step create (campaign, then ads via &#x60;existingCampaignId&#x60;) leaves one behind whenever Meta rejects the ad step.  Requires &#x60;accountId&#x60; and &#x60;adAccountId&#x60;, since an empty campaign has no ad row to resolve a token or ad account from.  | [optional] |
| **page** | **Integer**| Page number (1-based) | [optional] [default to 1] |
| **limit** | **Integer**|  | [optional] [default to 20] |
| **source** | **String**| &#x60;all&#x60; (default) returns both Zernio-created ads and those discovered from the platform&#39;s ad manager. Matches the web UI&#39;s default view. Pass &#x60;zernio&#x60; to restrict to isExternal&#x3D;false only. Status is NOT filtered by default; use the &#x60;status&#x60; param for that. | [optional] [default to all] [enum: zernio, all] |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai, reddit] |
| **status** | [**AdStatus**](.md)| Filter by derived campaign status (post-aggregation) | [optional] [enum: active, paused, pending_review, rejected, completed, cancelled, error] |
| **adAccountId** | **String**| Platform ad account ID (e.g. act_123 for Meta) | [optional] |
| **campaignId** | **String**| Platform campaign ID (the &#x60;platformCampaignId&#x60; on each returned campaign). Returns only that campaign, or an empty list when it is not visible to the caller. Mirrors the same filter on /v1/ads and /v1/ads/tree. | [optional] |
| **pageId** | **String**| Meta only: Facebook Page ID. Campaigns have no Page of their own, so this keeps campaigns having at least one ad backed by this Page, with adCount and metrics computed over those ads only. Mirrors the same filter on /v1/ads and /v1/ads/tree. | [optional] |
| **accountId** | **String**| Account ID | [optional] |
| **profileId** | **String**| Profile ID | [optional] |
| **fromDate** | **LocalDate**| Start of metrics date range (YYYY-MM-DD, inclusive). Defaults to 90 days ago when both date params are omitted. | [optional] |
| **toDate** | **LocalDate**| End of metrics date range (YYYY-MM-DD, inclusive). Defaults to today. Max 730-day range. | [optional] |
| **hasDelivery** | **Boolean**| Return only campaigns that delivered between &#x60;fromDate&#x60; and &#x60;toDate&#x60;: spend above zero, or impressions served at zero spend.  Unlike &#x60;status&#x60;, which reads a campaign&#39;s CURRENT state, this filters on what happened inside the window. It filters the campaign set itself, so &#x60;pagination.total&#x60; counts only matching campaigns. Mirrors the same filter on /v1/ads/tree. | [optional] |
| **minSpend** | **BigDecimal**| Return only campaigns whose spend between &#x60;fromDate&#x60; and &#x60;toDate&#x60; reaches this amount, in each campaign&#39;s OWN currency (the &#x60;currency&#x60; field on the campaign). Implies &#x60;hasDelivery&#x60;; &#x60;minSpend&#x3D;0&#x60; applies no filter. Mirrors the same filter on /v1/ads/tree. | [optional] |
| **live** | **Boolean**| Read the on/off switches live from the platform instead of returning synced values. See \&quot;Status freshness\&quot; in the operation description.  - The fresh values are stored (later reads return them too), and the response carries &#x60;statusReadAt&#x60;, the time of the read. - At most 20 platform objects are read per request. - Where a read fails (credentials, platform error, no reader on that platform), stored values come back with &#x60;statusReadAt: null&#x60;.  **On X** the budget is read live too:  - GET /v1/ads/{adId}: &#x60;budget&#x60;, &#x60;adSetBudget&#x60;, &#x60;campaignBudget&#x60; and &#x60;budgetLevel&#x60; are the line item and campaign budgets X holds now (stored like the switches). - Ad set and campaign listings: &#x60;budget&#x60; is what that line item or campaign holds now (returned, not stored). A row whose budget the other level holds keeps its synced &#x60;budget&#x60;.  | [optional] [default to false] |

### Return type

ApiResponse<[**ListAdCampaigns200Response**](ListAdCampaigns200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **200** | Paginated campaigns |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |


## listAdGroupAssets

> ListAdGroupAssets200Response listAdGroupAssets(adSetId, accountId, adAccountId, customerId)

List ad-group assets

Lists the sitelinks, callouts, snippets and images attached directly to a Google ad group, not those inherited from the campaign or account.  Fresh reads are cached for 10 minutes; exhausted quota may return the last successful read with stale&#x3D;true. Inherited assets are not included. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Numeric Google platform id.
        String accountId = "accountId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | 
        String customerId = "customerId_example"; // String | 
        try {
            ListAdGroupAssets200Response result = apiInstance.listAdGroupAssets(adSetId, accountId, adAccountId, customerId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listAdGroupAssets");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adSetId** | **String**| Numeric Google platform id. | |
| **accountId** | **String**|  | |
| **adAccountId** | **String**|  | [optional] |
| **customerId** | **String**|  | [optional] |

### Return type

[**ListAdGroupAssets200Response**](ListAdGroupAssets200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access is required.  Also returned with code &#x60;ad_account_not_selected&#x60; when the connection has selected ad accounts and the ad account this request targets is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix it, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |

## listAdGroupAssetsWithHttpInfo

> ApiResponse<ListAdGroupAssets200Response> listAdGroupAssets listAdGroupAssetsWithHttpInfo(adSetId, accountId, adAccountId, customerId)

List ad-group assets

Lists the sitelinks, callouts, snippets and images attached directly to a Google ad group, not those inherited from the campaign or account.  Fresh reads are cached for 10 minutes; exhausted quota may return the last successful read with stale&#x3D;true. Inherited assets are not included. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Numeric Google platform id.
        String accountId = "accountId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | 
        String customerId = "customerId_example"; // String | 
        try {
            ApiResponse<ListAdGroupAssets200Response> response = apiInstance.listAdGroupAssetsWithHttpInfo(adSetId, accountId, adAccountId, customerId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listAdGroupAssets");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adSetId** | **String**| Numeric Google platform id. | |
| **accountId** | **String**|  | |
| **adAccountId** | **String**|  | [optional] |
| **customerId** | **String**|  | [optional] |

### Return type

ApiResponse<[**ListAdGroupAssets200Response**](ListAdGroupAssets200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access is required.  Also returned with code &#x60;ad_account_not_selected&#x60; when the connection has selected ad accounts and the ad account this request targets is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix it, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |


## listAdKeywords

> ListAdKeywords200Response listAdKeywords(page, limit, accountId, adAccountId, profileId, campaignId, adSetId, status, matchType, negative, search)

List Search keywords

Lists the keywords and negative keywords in your Google Search ad groups.  Returns the Google Search keyword criteria (positive and negative) synced from connected Google Ads accounts, one row per ad-group keyword.  Campaign-level negative keywords are not included; only ad-group-level criteria are.  ### Freshness  Keywords are refreshed about once a day per Google Ads customer (the keyword sweep rides the ads discovery pass on a slower slot). So keywords added on Google can take up to a day to appear.  - A customer synced for the first time is populated on the next discovery pass rather than waiting for its daily slot. - Connecting an account or triggering a manual sync refreshes it immediately. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        Integer page = 1; // Integer | Page number (1-based)
        Integer limit = 50; // Integer | 
        String accountId = "accountId_example"; // String | Account ID
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID (Google customer ID). Mirrors the same filter on /v1/ads.
        String profileId = "profileId_example"; // String | Profile ID
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        String adSetId = "adSetId_example"; // String | Platform ad group ID (Google ad group)
        String status = "active"; // String | Keyword criterion status
        String matchType = "exact"; // String | Accepted in any case.
        Boolean negative = true; // Boolean | true = negative keywords only, false = positive only. Omit for both.
        String search = "search_example"; // String | Case-insensitive substring match on the keyword text
        try {
            ListAdKeywords200Response result = apiInstance.listAdKeywords(page, limit, accountId, adAccountId, profileId, campaignId, adSetId, status, matchType, negative, search);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listAdKeywords");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page** | **Integer**| Page number (1-based) | [optional] [default to 1] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **accountId** | **String**| Account ID | [optional] |
| **adAccountId** | **String**| Platform ad account ID (Google customer ID). Mirrors the same filter on /v1/ads. | [optional] |
| **profileId** | **String**| Profile ID | [optional] |
| **campaignId** | **String**| Platform campaign ID | [optional] |
| **adSetId** | **String**| Platform ad group ID (Google ad group) | [optional] |
| **status** | **String**| Keyword criterion status | [optional] [enum: active, paused] |
| **matchType** | **String**| Accepted in any case. | [optional] [enum: exact, phrase, broad, unknown] |
| **negative** | **Boolean**| true &#x3D; negative keywords only, false &#x3D; positive only. Omit for both. | [optional] |
| **search** | **String**| Case-insensitive substring match on the keyword text | [optional] |

### Return type

[**ListAdKeywords200Response**](ListAdKeywords200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated keywords |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |

## listAdKeywordsWithHttpInfo

> ApiResponse<ListAdKeywords200Response> listAdKeywords listAdKeywordsWithHttpInfo(page, limit, accountId, adAccountId, profileId, campaignId, adSetId, status, matchType, negative, search)

List Search keywords

Lists the keywords and negative keywords in your Google Search ad groups.  Returns the Google Search keyword criteria (positive and negative) synced from connected Google Ads accounts, one row per ad-group keyword.  Campaign-level negative keywords are not included; only ad-group-level criteria are.  ### Freshness  Keywords are refreshed about once a day per Google Ads customer (the keyword sweep rides the ads discovery pass on a slower slot). So keywords added on Google can take up to a day to appear.  - A customer synced for the first time is populated on the next discovery pass rather than waiting for its daily slot. - Connecting an account or triggering a manual sync refreshes it immediately. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        Integer page = 1; // Integer | Page number (1-based)
        Integer limit = 50; // Integer | 
        String accountId = "accountId_example"; // String | Account ID
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID (Google customer ID). Mirrors the same filter on /v1/ads.
        String profileId = "profileId_example"; // String | Profile ID
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        String adSetId = "adSetId_example"; // String | Platform ad group ID (Google ad group)
        String status = "active"; // String | Keyword criterion status
        String matchType = "exact"; // String | Accepted in any case.
        Boolean negative = true; // Boolean | true = negative keywords only, false = positive only. Omit for both.
        String search = "search_example"; // String | Case-insensitive substring match on the keyword text
        try {
            ApiResponse<ListAdKeywords200Response> response = apiInstance.listAdKeywordsWithHttpInfo(page, limit, accountId, adAccountId, profileId, campaignId, adSetId, status, matchType, negative, search);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listAdKeywords");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page** | **Integer**| Page number (1-based) | [optional] [default to 1] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **accountId** | **String**| Account ID | [optional] |
| **adAccountId** | **String**| Platform ad account ID (Google customer ID). Mirrors the same filter on /v1/ads. | [optional] |
| **profileId** | **String**| Profile ID | [optional] |
| **campaignId** | **String**| Platform campaign ID | [optional] |
| **adSetId** | **String**| Platform ad group ID (Google ad group) | [optional] |
| **status** | **String**| Keyword criterion status | [optional] [enum: active, paused] |
| **matchType** | **String**| Accepted in any case. | [optional] [enum: exact, phrase, broad, unknown] |
| **negative** | **Boolean**| true &#x3D; negative keywords only, false &#x3D; positive only. Omit for both. | [optional] |
| **search** | **String**| Case-insensitive substring match on the keyword text | [optional] |

### Return type

ApiResponse<[**ListAdKeywords200Response**](ListAdKeywords200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated keywords |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |


## listAdSets

> ListAdSets200Response listAdSets(accountId, adAccountId, campaignId, adSetId, platform, status, page, limit, live)

List ad sets

Lists ad sets (ad groups on Google) with their targeting, bidding and optimization settings, optionally for one campaign.  Returns the ad sets (Google ad groups) synced for the connection, optionally filtered by platform and campaignId.  It reads the &#x60;ad_sets&#x60; table directly, independent of the &#x60;ads&#x60; rollup GET /v1/ads/tree uses. So a newly created standalone ad group with no ad yet (POST /v1/ads/ad-sets, Google only) is visible here. It stays invisible in the tree until an ad joins it via &#x60;adSetId&#x60; on POST /v1/ads/create.  ### Paging  Rows come newest first (by platform creation time, then id, so pages never overlap), 500 per page unless &#x60;limit&#x60; says otherwise. &#x60;pagination.total&#x60; counts every matching ad set and &#x60;page&#x60; reaches the rest.  ### Synced config  **This list is SYNCED, not live** (refreshed by background sync, see below). Each row also carries the ad set&#39;s config: &#x60;targeting&#x60;, &#x60;bidStrategy&#x60;, &#x60;bidAmount&#x60;, &#x60;optimizationGoal&#x60;, &#x60;billingEvent&#x60;, &#x60;promotedObject&#x60;.  So &#x60;?accountId&#x3D;...&amp;adAccountId&#x3D;act_...&#x60; returns the config of every ad set of an ad account in one call, without a &#x60;campaignId&#x60;.  To read budgets, status, targeting, promoted object and bid strategy of every campaign and ad set of a Meta ad account LIVE in one call (for example as a pre-write spend gate), use GET /v1/ads/accounts/live instead.  ### Status freshness  &#x60;status&#x60;, &#x60;configuredStatus&#x60;, &#x60;platformStatus&#x60;, &#x60;platformAdSetStatus&#x60; and &#x60;platformCampaignStatus&#x60; are the values Zernio last stored.  Background sync refreshes them, typically within 15 to 60 minutes (Google up to about 3 hours). Ended or long-paused objects may be refreshed less often. Zernio&#39;s own status writes re-read the switches they change.  A change made in the platform&#39;s own ads manager therefore shows up here only after the next sync.  ### Live reads (&#x60;live&#x3D;true&#x60;)  Controllers that act on a switch should pass &#x60;live&#x3D;true&#x60;. It reads the switches from the platform now, stores them, and returns &#x60;statusReadAt&#x60; (null when the read failed and the stored values were returned).  - &#x60;live&#x3D;true&#x60; needs a &#x60;campaignId&#x60; or &#x60;adSetId&#x60; filter. - Each listed ad set&#39;s own switch (&#x60;platformAdSetStatus&#x60;) is read live for the first 20 rows of the page. Later rows keep their synced value with &#x60;statusReadAt: null&#x60;. - To read more ad sets live, page with &#x60;limit&#x3D;20&#x60;. - Live reads cover TikTok, Meta, Google, OpenAI and Reddit. - The rolled-up &#x60;status&#x60; is not re-derived by a live read.  ### TikTok live reads  On TikTok the same live read also returns the ad group&#39;s applied &#x60;optimizationGoal&#x60; and &#x60;billingEvent&#x60;, as TikTok&#39;s adgroup/get reports them. So you can verify the goal TikTok applied rather than the one you requested.  It also returns &#x60;nativeSettings&#x60;: a fixed subset of TikTok&#39;s own adgroup/get record for the ad group, with TikTok&#39;s own values, read in that same call. It covers budget, budget_mode, schedule, placements, locations, ages, gender, languages, interests, actions, audiences and exclusions, plus the advertiser&#39;s currency and timezone.  TikTok&#39;s &#x60;schedule_start_time&#x60; / &#x60;schedule_end_time&#x60; are UTC wall clocks (\&quot;YYYY-MM-DD HH:MM:SS\&quot;, no offset); Ads Manager displays them in &#x60;advertiser_timezone&#x60;.  &#x60;configReadAt&#x60; says when it was read. It is null on every row whose native settings were not read now, so never treat a null as a match.  These are read, not retained create payloads, and are not stored. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String accountId = "accountId_example"; // String | Account ID
        String adAccountId = "adAccountId_example"; // String | Platform ad account id (Meta act_<n>). Lists every synced ad set of that ad account; no campaignId needed.
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        String adSetId = "adSetId_example"; // String | Platform ad set ID
        String platform = "facebook"; // String | 
        AdStatus status = AdStatus.fromValue("active"); // AdStatus | Filter by the ad set's stored `status`, the value each row returns. A live read does not change it. Rows whose `status` is null match no filter.
        Integer page = 1; // Integer | 
        Integer limit = 500; // Integer | 
        Boolean live = false; // Boolean | Read the on/off switches live from the platform instead of returning synced values. See \"Status freshness\" in the operation description.  - The fresh values are stored (later reads return them too), and the response carries `statusReadAt`, the time of the read. - At most 20 platform objects are read per request. - Where a read fails (credentials, platform error, no reader on that platform), stored values come back with `statusReadAt: null`.  **On X** the budget is read live too:  - GET /v1/ads/{adId}: `budget`, `adSetBudget`, `campaignBudget` and `budgetLevel` are the line item and campaign budgets X holds now (stored like the switches). - Ad set and campaign listings: `budget` is what that line item or campaign holds now (returned, not stored). A row whose budget the other level holds keeps its synced `budget`. 
        try {
            ListAdSets200Response result = apiInstance.listAdSets(accountId, adAccountId, campaignId, adSetId, platform, status, page, limit, live);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listAdSets");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Account ID | [optional] |
| **adAccountId** | **String**| Platform ad account id (Meta act_&lt;n&gt;). Lists every synced ad set of that ad account; no campaignId needed. | [optional] |
| **campaignId** | **String**| Platform campaign ID | [optional] |
| **adSetId** | **String**| Platform ad set ID | [optional] |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai, reddit] |
| **status** | [**AdStatus**](.md)| Filter by the ad set&#39;s stored &#x60;status&#x60;, the value each row returns. A live read does not change it. Rows whose &#x60;status&#x60; is null match no filter. | [optional] [enum: active, paused, pending_review, rejected, completed, cancelled, error] |
| **page** | **Integer**|  | [optional] [default to 1] |
| **limit** | **Integer**|  | [optional] [default to 500] |
| **live** | **Boolean**| Read the on/off switches live from the platform instead of returning synced values. See \&quot;Status freshness\&quot; in the operation description.  - The fresh values are stored (later reads return them too), and the response carries &#x60;statusReadAt&#x60;, the time of the read. - At most 20 platform objects are read per request. - Where a read fails (credentials, platform error, no reader on that platform), stored values come back with &#x60;statusReadAt: null&#x60;.  **On X** the budget is read live too:  - GET /v1/ads/{adId}: &#x60;budget&#x60;, &#x60;adSetBudget&#x60;, &#x60;campaignBudget&#x60; and &#x60;budgetLevel&#x60; are the line item and campaign budgets X holds now (stored like the switches). - Ad set and campaign listings: &#x60;budget&#x60; is what that line item or campaign holds now (returned, not stored). A row whose budget the other level holds keeps its synced &#x60;budget&#x60;.  | [optional] [default to false] |

### Return type

[**ListAdSets200Response**](ListAdSets200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad sets |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans). |  -  |

## listAdSetsWithHttpInfo

> ApiResponse<ListAdSets200Response> listAdSets listAdSetsWithHttpInfo(accountId, adAccountId, campaignId, adSetId, platform, status, page, limit, live)

List ad sets

Lists ad sets (ad groups on Google) with their targeting, bidding and optimization settings, optionally for one campaign.  Returns the ad sets (Google ad groups) synced for the connection, optionally filtered by platform and campaignId.  It reads the &#x60;ad_sets&#x60; table directly, independent of the &#x60;ads&#x60; rollup GET /v1/ads/tree uses. So a newly created standalone ad group with no ad yet (POST /v1/ads/ad-sets, Google only) is visible here. It stays invisible in the tree until an ad joins it via &#x60;adSetId&#x60; on POST /v1/ads/create.  ### Paging  Rows come newest first (by platform creation time, then id, so pages never overlap), 500 per page unless &#x60;limit&#x60; says otherwise. &#x60;pagination.total&#x60; counts every matching ad set and &#x60;page&#x60; reaches the rest.  ### Synced config  **This list is SYNCED, not live** (refreshed by background sync, see below). Each row also carries the ad set&#39;s config: &#x60;targeting&#x60;, &#x60;bidStrategy&#x60;, &#x60;bidAmount&#x60;, &#x60;optimizationGoal&#x60;, &#x60;billingEvent&#x60;, &#x60;promotedObject&#x60;.  So &#x60;?accountId&#x3D;...&amp;adAccountId&#x3D;act_...&#x60; returns the config of every ad set of an ad account in one call, without a &#x60;campaignId&#x60;.  To read budgets, status, targeting, promoted object and bid strategy of every campaign and ad set of a Meta ad account LIVE in one call (for example as a pre-write spend gate), use GET /v1/ads/accounts/live instead.  ### Status freshness  &#x60;status&#x60;, &#x60;configuredStatus&#x60;, &#x60;platformStatus&#x60;, &#x60;platformAdSetStatus&#x60; and &#x60;platformCampaignStatus&#x60; are the values Zernio last stored.  Background sync refreshes them, typically within 15 to 60 minutes (Google up to about 3 hours). Ended or long-paused objects may be refreshed less often. Zernio&#39;s own status writes re-read the switches they change.  A change made in the platform&#39;s own ads manager therefore shows up here only after the next sync.  ### Live reads (&#x60;live&#x3D;true&#x60;)  Controllers that act on a switch should pass &#x60;live&#x3D;true&#x60;. It reads the switches from the platform now, stores them, and returns &#x60;statusReadAt&#x60; (null when the read failed and the stored values were returned).  - &#x60;live&#x3D;true&#x60; needs a &#x60;campaignId&#x60; or &#x60;adSetId&#x60; filter. - Each listed ad set&#39;s own switch (&#x60;platformAdSetStatus&#x60;) is read live for the first 20 rows of the page. Later rows keep their synced value with &#x60;statusReadAt: null&#x60;. - To read more ad sets live, page with &#x60;limit&#x3D;20&#x60;. - Live reads cover TikTok, Meta, Google, OpenAI and Reddit. - The rolled-up &#x60;status&#x60; is not re-derived by a live read.  ### TikTok live reads  On TikTok the same live read also returns the ad group&#39;s applied &#x60;optimizationGoal&#x60; and &#x60;billingEvent&#x60;, as TikTok&#39;s adgroup/get reports them. So you can verify the goal TikTok applied rather than the one you requested.  It also returns &#x60;nativeSettings&#x60;: a fixed subset of TikTok&#39;s own adgroup/get record for the ad group, with TikTok&#39;s own values, read in that same call. It covers budget, budget_mode, schedule, placements, locations, ages, gender, languages, interests, actions, audiences and exclusions, plus the advertiser&#39;s currency and timezone.  TikTok&#39;s &#x60;schedule_start_time&#x60; / &#x60;schedule_end_time&#x60; are UTC wall clocks (\&quot;YYYY-MM-DD HH:MM:SS\&quot;, no offset); Ads Manager displays them in &#x60;advertiser_timezone&#x60;.  &#x60;configReadAt&#x60; says when it was read. It is null on every row whose native settings were not read now, so never treat a null as a match.  These are read, not retained create payloads, and are not stored. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String accountId = "accountId_example"; // String | Account ID
        String adAccountId = "adAccountId_example"; // String | Platform ad account id (Meta act_<n>). Lists every synced ad set of that ad account; no campaignId needed.
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        String adSetId = "adSetId_example"; // String | Platform ad set ID
        String platform = "facebook"; // String | 
        AdStatus status = AdStatus.fromValue("active"); // AdStatus | Filter by the ad set's stored `status`, the value each row returns. A live read does not change it. Rows whose `status` is null match no filter.
        Integer page = 1; // Integer | 
        Integer limit = 500; // Integer | 
        Boolean live = false; // Boolean | Read the on/off switches live from the platform instead of returning synced values. See \"Status freshness\" in the operation description.  - The fresh values are stored (later reads return them too), and the response carries `statusReadAt`, the time of the read. - At most 20 platform objects are read per request. - Where a read fails (credentials, platform error, no reader on that platform), stored values come back with `statusReadAt: null`.  **On X** the budget is read live too:  - GET /v1/ads/{adId}: `budget`, `adSetBudget`, `campaignBudget` and `budgetLevel` are the line item and campaign budgets X holds now (stored like the switches). - Ad set and campaign listings: `budget` is what that line item or campaign holds now (returned, not stored). A row whose budget the other level holds keeps its synced `budget`. 
        try {
            ApiResponse<ListAdSets200Response> response = apiInstance.listAdSetsWithHttpInfo(accountId, adAccountId, campaignId, adSetId, platform, status, page, limit, live);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listAdSets");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Account ID | [optional] |
| **adAccountId** | **String**| Platform ad account id (Meta act_&lt;n&gt;). Lists every synced ad set of that ad account; no campaignId needed. | [optional] |
| **campaignId** | **String**| Platform campaign ID | [optional] |
| **adSetId** | **String**| Platform ad set ID | [optional] |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai, reddit] |
| **status** | [**AdStatus**](.md)| Filter by the ad set&#39;s stored &#x60;status&#x60;, the value each row returns. A live read does not change it. Rows whose &#x60;status&#x60; is null match no filter. | [optional] [enum: active, paused, pending_review, rejected, completed, cancelled, error] |
| **page** | **Integer**|  | [optional] [default to 1] |
| **limit** | **Integer**|  | [optional] [default to 500] |
| **live** | **Boolean**| Read the on/off switches live from the platform instead of returning synced values. See \&quot;Status freshness\&quot; in the operation description.  - The fresh values are stored (later reads return them too), and the response carries &#x60;statusReadAt&#x60;, the time of the read. - At most 20 platform objects are read per request. - Where a read fails (credentials, platform error, no reader on that platform), stored values come back with &#x60;statusReadAt: null&#x60;.  **On X** the budget is read live too:  - GET /v1/ads/{adId}: &#x60;budget&#x60;, &#x60;adSetBudget&#x60;, &#x60;campaignBudget&#x60; and &#x60;budgetLevel&#x60; are the line item and campaign budgets X holds now (stored like the switches). - Ad set and campaign listings: &#x60;budget&#x60; is what that line item or campaign holds now (returned, not stored). A row whose budget the other level holds keeps its synced &#x60;budget&#x60;.  | [optional] [default to false] |

### Return type

ApiResponse<[**ListAdSets200Response**](ListAdSets200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad sets |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans). |  -  |


## listAds

> AdsListResponse listAds(page, limit, source, status, platform, accountId, adAccountId, pageId, profileId, campaignId, adSetId, platformAdId, effectiveObjectStoryId, effectiveInstagramMediaId, fromDate, toDate)

List ads

Lists your ads with their performance over a date range, including ads created directly in each platform&#39;s ads manager.  Returns a paginated list of ads with metrics computed over an optional date range. Use source&#x3D;all to include externally-synced ads from platform ad managers.  If no date range is provided, it defaults to the last 90 days. The date range is capped at 730 days max.  ### History  When an ad account connects, Zernio imports its last 90 days of metrics, so the metrics hold no data for days before that.  When &#x60;accountId&#x60; or &#x60;adAccountId&#x60; resolves to a Meta ad account, a range reaching further back answers &#x60;202&#x60; with &#x60;backfillPending: true&#x60; and the covered part. The older days (up to 730 days back) are imported in the background; repeat the request until it returns 200.  A request scoped to no Meta account never returns &#x60;202&#x60;.  ### Finding the ad behind a comment  To find the Zernio ad behind a comment you see in Meta Business Manager:  1. Filter by platformAdId (the Meta ad ID), effectiveObjectStoryId (Facebook), or effectiveInstagramMediaId (Instagram). Those are the post/media the ad&#39;s engagement lives on, and are also returned on each ad&#39;s &#x60;creative&#x60; object. 2. Call GET /v1/ads/{adId}/comments with the returned ad id. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        Integer page = 1; // Integer | Page number (1-based)
        Integer limit = 50; // Integer | 
        String source = "zernio"; // String | all (default) = Zernio-created + platform-discovered ads. zernio = restrict to Zernio-created only.
        AdStatus status = AdStatus.fromValue("active"); // AdStatus | 
        String platform = "facebook"; // String | 
        String accountId = "accountId_example"; // String | Account ID
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID (e.g. act_123 for Meta). Mirrors the same filter on /v1/ads/campaigns and /v1/ads/tree.
        String pageId = "pageId_example"; // String | Meta only: Facebook Page ID. Returns only ads whose creative is backed by this Page (a Meta ad account serves ads for every Page in the Business Manager). Matches each ad's `creative.pageId`; ads with no page signal (rare IG-only creatives) never match. Mirrors the same filter on /v1/ads/campaigns and /v1/ads/tree.
        String profileId = "profileId_example"; // String | Profile ID
        String campaignId = "campaignId_example"; // String | Platform campaign ID (filter ads within a campaign)
        String adSetId = "adSetId_example"; // String | Platform ad set ID (filter ads within an ad set, the /{adset_id}/ads read of an adset-centric dashboard).
        String platformAdId = "platformAdId_example"; // String | Meta ad ID. Returns the ad with this platform-side ad ID.
        String effectiveObjectStoryId = "effectiveObjectStoryId_example"; // String | Facebook `{pageId}_{postId}` of the post the ad's engagement lives on (Meta `effective_object_story_id`). Use to map a Business-Manager-visible post back to the Zernio ad.
        String effectiveInstagramMediaId = "effectiveInstagramMediaId_example"; // String | Instagram media ID of the boosted post (Meta `effective_instagram_media_id`). Use to map a Business-Manager-visible IG post back to the Zernio ad.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of metrics date range (YYYY-MM-DD). Defaults to 90 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of metrics date range (YYYY-MM-DD). Defaults to today. Max 730-day range.
        try {
            AdsListResponse result = apiInstance.listAds(page, limit, source, status, platform, accountId, adAccountId, pageId, profileId, campaignId, adSetId, platformAdId, effectiveObjectStoryId, effectiveInstagramMediaId, fromDate, toDate);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listAds");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page** | **Integer**| Page number (1-based) | [optional] [default to 1] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **source** | **String**| all (default) &#x3D; Zernio-created + platform-discovered ads. zernio &#x3D; restrict to Zernio-created only. | [optional] [default to all] [enum: zernio, all] |
| **status** | [**AdStatus**](.md)|  | [optional] [enum: active, paused, pending_review, rejected, completed, cancelled, error] |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai, reddit] |
| **accountId** | **String**| Account ID | [optional] |
| **adAccountId** | **String**| Platform ad account ID (e.g. act_123 for Meta). Mirrors the same filter on /v1/ads/campaigns and /v1/ads/tree. | [optional] |
| **pageId** | **String**| Meta only: Facebook Page ID. Returns only ads whose creative is backed by this Page (a Meta ad account serves ads for every Page in the Business Manager). Matches each ad&#39;s &#x60;creative.pageId&#x60;; ads with no page signal (rare IG-only creatives) never match. Mirrors the same filter on /v1/ads/campaigns and /v1/ads/tree. | [optional] |
| **profileId** | **String**| Profile ID | [optional] |
| **campaignId** | **String**| Platform campaign ID (filter ads within a campaign) | [optional] |
| **adSetId** | **String**| Platform ad set ID (filter ads within an ad set, the /{adset_id}/ads read of an adset-centric dashboard). | [optional] |
| **platformAdId** | **String**| Meta ad ID. Returns the ad with this platform-side ad ID. | [optional] |
| **effectiveObjectStoryId** | **String**| Facebook &#x60;{pageId}_{postId}&#x60; of the post the ad&#39;s engagement lives on (Meta &#x60;effective_object_story_id&#x60;). Use to map a Business-Manager-visible post back to the Zernio ad. | [optional] |
| **effectiveInstagramMediaId** | **String**| Instagram media ID of the boosted post (Meta &#x60;effective_instagram_media_id&#x60;). Use to map a Business-Manager-visible IG post back to the Zernio ad. | [optional] |
| **fromDate** | **LocalDate**| Start of metrics date range (YYYY-MM-DD). Defaults to 90 days ago. | [optional] |
| **toDate** | **LocalDate**| End of metrics date range (YYYY-MM-DD). Defaults to today. Max 730-day range. | [optional] |

### Return type

[**AdsListResponse**](AdsListResponse.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated ads |  -  |
| **202** | Meta only. Historical data is incomplete and backfill remains pending. |  * Retry-After -  <br>  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |

## listAdsWithHttpInfo

> ApiResponse<AdsListResponse> listAds listAdsWithHttpInfo(page, limit, source, status, platform, accountId, adAccountId, pageId, profileId, campaignId, adSetId, platformAdId, effectiveObjectStoryId, effectiveInstagramMediaId, fromDate, toDate)

List ads

Lists your ads with their performance over a date range, including ads created directly in each platform&#39;s ads manager.  Returns a paginated list of ads with metrics computed over an optional date range. Use source&#x3D;all to include externally-synced ads from platform ad managers.  If no date range is provided, it defaults to the last 90 days. The date range is capped at 730 days max.  ### History  When an ad account connects, Zernio imports its last 90 days of metrics, so the metrics hold no data for days before that.  When &#x60;accountId&#x60; or &#x60;adAccountId&#x60; resolves to a Meta ad account, a range reaching further back answers &#x60;202&#x60; with &#x60;backfillPending: true&#x60; and the covered part. The older days (up to 730 days back) are imported in the background; repeat the request until it returns 200.  A request scoped to no Meta account never returns &#x60;202&#x60;.  ### Finding the ad behind a comment  To find the Zernio ad behind a comment you see in Meta Business Manager:  1. Filter by platformAdId (the Meta ad ID), effectiveObjectStoryId (Facebook), or effectiveInstagramMediaId (Instagram). Those are the post/media the ad&#39;s engagement lives on, and are also returned on each ad&#39;s &#x60;creative&#x60; object. 2. Call GET /v1/ads/{adId}/comments with the returned ad id. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        Integer page = 1; // Integer | Page number (1-based)
        Integer limit = 50; // Integer | 
        String source = "zernio"; // String | all (default) = Zernio-created + platform-discovered ads. zernio = restrict to Zernio-created only.
        AdStatus status = AdStatus.fromValue("active"); // AdStatus | 
        String platform = "facebook"; // String | 
        String accountId = "accountId_example"; // String | Account ID
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID (e.g. act_123 for Meta). Mirrors the same filter on /v1/ads/campaigns and /v1/ads/tree.
        String pageId = "pageId_example"; // String | Meta only: Facebook Page ID. Returns only ads whose creative is backed by this Page (a Meta ad account serves ads for every Page in the Business Manager). Matches each ad's `creative.pageId`; ads with no page signal (rare IG-only creatives) never match. Mirrors the same filter on /v1/ads/campaigns and /v1/ads/tree.
        String profileId = "profileId_example"; // String | Profile ID
        String campaignId = "campaignId_example"; // String | Platform campaign ID (filter ads within a campaign)
        String adSetId = "adSetId_example"; // String | Platform ad set ID (filter ads within an ad set, the /{adset_id}/ads read of an adset-centric dashboard).
        String platformAdId = "platformAdId_example"; // String | Meta ad ID. Returns the ad with this platform-side ad ID.
        String effectiveObjectStoryId = "effectiveObjectStoryId_example"; // String | Facebook `{pageId}_{postId}` of the post the ad's engagement lives on (Meta `effective_object_story_id`). Use to map a Business-Manager-visible post back to the Zernio ad.
        String effectiveInstagramMediaId = "effectiveInstagramMediaId_example"; // String | Instagram media ID of the boosted post (Meta `effective_instagram_media_id`). Use to map a Business-Manager-visible IG post back to the Zernio ad.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of metrics date range (YYYY-MM-DD). Defaults to 90 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of metrics date range (YYYY-MM-DD). Defaults to today. Max 730-day range.
        try {
            ApiResponse<AdsListResponse> response = apiInstance.listAdsWithHttpInfo(page, limit, source, status, platform, accountId, adAccountId, pageId, profileId, campaignId, adSetId, platformAdId, effectiveObjectStoryId, effectiveInstagramMediaId, fromDate, toDate);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listAds");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page** | **Integer**| Page number (1-based) | [optional] [default to 1] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **source** | **String**| all (default) &#x3D; Zernio-created + platform-discovered ads. zernio &#x3D; restrict to Zernio-created only. | [optional] [default to all] [enum: zernio, all] |
| **status** | [**AdStatus**](.md)|  | [optional] [enum: active, paused, pending_review, rejected, completed, cancelled, error] |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai, reddit] |
| **accountId** | **String**| Account ID | [optional] |
| **adAccountId** | **String**| Platform ad account ID (e.g. act_123 for Meta). Mirrors the same filter on /v1/ads/campaigns and /v1/ads/tree. | [optional] |
| **pageId** | **String**| Meta only: Facebook Page ID. Returns only ads whose creative is backed by this Page (a Meta ad account serves ads for every Page in the Business Manager). Matches each ad&#39;s &#x60;creative.pageId&#x60;; ads with no page signal (rare IG-only creatives) never match. Mirrors the same filter on /v1/ads/campaigns and /v1/ads/tree. | [optional] |
| **profileId** | **String**| Profile ID | [optional] |
| **campaignId** | **String**| Platform campaign ID (filter ads within a campaign) | [optional] |
| **adSetId** | **String**| Platform ad set ID (filter ads within an ad set, the /{adset_id}/ads read of an adset-centric dashboard). | [optional] |
| **platformAdId** | **String**| Meta ad ID. Returns the ad with this platform-side ad ID. | [optional] |
| **effectiveObjectStoryId** | **String**| Facebook &#x60;{pageId}_{postId}&#x60; of the post the ad&#39;s engagement lives on (Meta &#x60;effective_object_story_id&#x60;). Use to map a Business-Manager-visible post back to the Zernio ad. | [optional] |
| **effectiveInstagramMediaId** | **String**| Instagram media ID of the boosted post (Meta &#x60;effective_instagram_media_id&#x60;). Use to map a Business-Manager-visible IG post back to the Zernio ad. | [optional] |
| **fromDate** | **LocalDate**| Start of metrics date range (YYYY-MM-DD). Defaults to 90 days ago. | [optional] |
| **toDate** | **LocalDate**| End of metrics date range (YYYY-MM-DD). Defaults to today. Max 730-day range. | [optional] |

### Return type

ApiResponse<[**AdsListResponse**](AdsListResponse.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated ads |  -  |
| **202** | Meta only. Historical data is incomplete and backfill remains pending. |  * Retry-After -  <br>  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |


## listAdsAlerts

> ListAdsAlerts200Response listAdsAlerts(accountId, profileId, includeDismissed)

List ads that need attention

Lists what needs attention across your ads, most severe first:  - ads created in the last 90 days that were rejected - campaigns the platform reports delivery issues on - Meta ad accounts with a failed or overdue payment, or disabled while holding live ads - campaigns that spent on 3 or more of the last 7 days without a result (conversion, lead, purchase or conversation goals) - budgets spent to their daily cap yesterday - ads connections that need reconnecting while they still hold live ads - ad accounts whose sync has been failing  Built from stored data and the last 7 days of synced metrics, so it costs no platform call.  Each alert has a stable &#x60;id&#x60;. Dismiss one with &#x60;POST /v1/ads/alerts/{alertId}/dismiss&#x60; to hide it for 30 days. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String accountId = "accountId_example"; // String | Only alerts of this ads connection (sibling-expanded like /v1/ads/tree). Omit for every ad account the API key can reach.
        String profileId = "profileId_example"; // String | Only alerts of the ads connections on this profile. Omit for every profile the API key can reach.
        Boolean includeDismissed = false; // Boolean | Also return dismissed alerts, with `dismissed: true`.
        try {
            ListAdsAlerts200Response result = apiInstance.listAdsAlerts(accountId, profileId, includeDismissed);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listAdsAlerts");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Only alerts of this ads connection (sibling-expanded like /v1/ads/tree). Omit for every ad account the API key can reach. | [optional] |
| **profileId** | **String**| Only alerts of the ads connections on this profile. Omit for every profile the API key can reach. | [optional] |
| **includeDismissed** | **Boolean**| Also return dismissed alerts, with &#x60;dismissed: true&#x60;. | [optional] [default to false] |

### Return type

[**ListAdsAlerts200Response**](ListAdsAlerts200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Alerts, most severe first. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |

## listAdsAlertsWithHttpInfo

> ApiResponse<ListAdsAlerts200Response> listAdsAlerts listAdsAlertsWithHttpInfo(accountId, profileId, includeDismissed)

List ads that need attention

Lists what needs attention across your ads, most severe first:  - ads created in the last 90 days that were rejected - campaigns the platform reports delivery issues on - Meta ad accounts with a failed or overdue payment, or disabled while holding live ads - campaigns that spent on 3 or more of the last 7 days without a result (conversion, lead, purchase or conversation goals) - budgets spent to their daily cap yesterday - ads connections that need reconnecting while they still hold live ads - ad accounts whose sync has been failing  Built from stored data and the last 7 days of synced metrics, so it costs no platform call.  Each alert has a stable &#x60;id&#x60;. Dismiss one with &#x60;POST /v1/ads/alerts/{alertId}/dismiss&#x60; to hide it for 30 days. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String accountId = "accountId_example"; // String | Only alerts of this ads connection (sibling-expanded like /v1/ads/tree). Omit for every ad account the API key can reach.
        String profileId = "profileId_example"; // String | Only alerts of the ads connections on this profile. Omit for every profile the API key can reach.
        Boolean includeDismissed = false; // Boolean | Also return dismissed alerts, with `dismissed: true`.
        try {
            ApiResponse<ListAdsAlerts200Response> response = apiInstance.listAdsAlertsWithHttpInfo(accountId, profileId, includeDismissed);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listAdsAlerts");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Only alerts of this ads connection (sibling-expanded like /v1/ads/tree). Omit for every ad account the API key can reach. | [optional] |
| **profileId** | **String**| Only alerts of the ads connections on this profile. Omit for every profile the API key can reach. | [optional] |
| **includeDismissed** | **Boolean**| Also return dismissed alerts, with &#x60;dismissed: true&#x60;. | [optional] [default to false] |

### Return type

ApiResponse<[**ListAdsAlerts200Response**](ListAdsAlerts200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Alerts, most severe first. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |


## listBidStrategies

> ListBidStrategies200Response listBidStrategies(accountId, adAccountId, customerId, fromDate, toDate)

List portfolio bid strategies

Lists a Google Ads account&#39;s shared bid strategies with how many campaigns use each and how they performed.  The bidding strategy report covers type, status, campaign count, clicks, cost, cost per conversion, impressions, average CPC and conversions over the date range (default last 30 days).  ### Data source  It reads Google&#39;s &#x60;bidding_strategy&#x60; resource, cached for the quota window, and draws on the shared Google Ads operations budget.  The response carries &#x60;cachedAt&#x60; and &#x60;stale&#x60;, set when a quota-exhausted call falls back to the last-good copy instead of a live read. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String accountId = "accountId_example"; // String | Google ads SocialAccount id.
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID (Google customer ID, digits only). Defaults to the account's connected customer.
        String customerId = "customerId_example"; // String | Alias of adAccountId, kept for existing callers
        LocalDate fromDate = LocalDate.now(); // LocalDate | Defaults to 30 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | Defaults to today.
        try {
            ListBidStrategies200Response result = apiInstance.listBidStrategies(accountId, adAccountId, customerId, fromDate, toDate);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listBidStrategies");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Google ads SocialAccount id. | |
| **adAccountId** | **String**| Platform ad account ID (Google customer ID, digits only). Defaults to the account&#39;s connected customer. | [optional] |
| **customerId** | **String**| Alias of adAccountId, kept for existing callers | [optional] |
| **fromDate** | **LocalDate**| Defaults to 30 days ago. | [optional] |
| **toDate** | **LocalDate**| Defaults to today. | [optional] |

### Return type

[**ListBidStrategies200Response**](ListBidStrategies200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Portfolio bid strategies |  -  |
| **400** | Invalid request |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget exhausted; retry later. |  -  |
| **501** | Only available on Google Ads accounts |  -  |

## listBidStrategiesWithHttpInfo

> ApiResponse<ListBidStrategies200Response> listBidStrategies listBidStrategiesWithHttpInfo(accountId, adAccountId, customerId, fromDate, toDate)

List portfolio bid strategies

Lists a Google Ads account&#39;s shared bid strategies with how many campaigns use each and how they performed.  The bidding strategy report covers type, status, campaign count, clicks, cost, cost per conversion, impressions, average CPC and conversions over the date range (default last 30 days).  ### Data source  It reads Google&#39;s &#x60;bidding_strategy&#x60; resource, cached for the quota window, and draws on the shared Google Ads operations budget.  The response carries &#x60;cachedAt&#x60; and &#x60;stale&#x60;, set when a quota-exhausted call falls back to the last-good copy instead of a live read. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String accountId = "accountId_example"; // String | Google ads SocialAccount id.
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID (Google customer ID, digits only). Defaults to the account's connected customer.
        String customerId = "customerId_example"; // String | Alias of adAccountId, kept for existing callers
        LocalDate fromDate = LocalDate.now(); // LocalDate | Defaults to 30 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | Defaults to today.
        try {
            ApiResponse<ListBidStrategies200Response> response = apiInstance.listBidStrategiesWithHttpInfo(accountId, adAccountId, customerId, fromDate, toDate);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listBidStrategies");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Google ads SocialAccount id. | |
| **adAccountId** | **String**| Platform ad account ID (Google customer ID, digits only). Defaults to the account&#39;s connected customer. | [optional] |
| **customerId** | **String**| Alias of adAccountId, kept for existing callers | [optional] |
| **fromDate** | **LocalDate**| Defaults to 30 days ago. | [optional] |
| **toDate** | **LocalDate**| Defaults to today. | [optional] |

### Return type

ApiResponse<[**ListBidStrategies200Response**](ListBidStrategies200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Portfolio bid strategies |  -  |
| **400** | Invalid request |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget exhausted; retry later. |  -  |
| **501** | Only available on Google Ads accounts |  -  |


## listCampaignAssets

> ListCampaignAssets200Response listCampaignAssets(campaignId, accountId, adAccountId, customerId)

List campaign assets

Lists the sitelinks, callouts and other assets attached directly to a Google campaign.  Fresh reads are cached for 10 minutes; exhausted quota may return the last successful read with stale&#x3D;true. Inherited assets are not included. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Numeric Google platform id.
        String accountId = "accountId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | 
        String customerId = "customerId_example"; // String | 
        try {
            ListCampaignAssets200Response result = apiInstance.listCampaignAssets(campaignId, accountId, adAccountId, customerId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listCampaignAssets");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Numeric Google platform id. | |
| **accountId** | **String**|  | |
| **adAccountId** | **String**|  | [optional] |
| **customerId** | **String**|  | [optional] |

### Return type

[**ListCampaignAssets200Response**](ListCampaignAssets200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Forbidden. One of:  - Ads access is required. - Code &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the ad account this request targets is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix &#x60;ad_account_not_selected&#x60;, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |

## listCampaignAssetsWithHttpInfo

> ApiResponse<ListCampaignAssets200Response> listCampaignAssets listCampaignAssetsWithHttpInfo(campaignId, accountId, adAccountId, customerId)

List campaign assets

Lists the sitelinks, callouts and other assets attached directly to a Google campaign.  Fresh reads are cached for 10 minutes; exhausted quota may return the last successful read with stale&#x3D;true. Inherited assets are not included. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Numeric Google platform id.
        String accountId = "accountId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | 
        String customerId = "customerId_example"; // String | 
        try {
            ApiResponse<ListCampaignAssets200Response> response = apiInstance.listCampaignAssetsWithHttpInfo(campaignId, accountId, adAccountId, customerId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listCampaignAssets");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Numeric Google platform id. | |
| **accountId** | **String**|  | |
| **adAccountId** | **String**|  | [optional] |
| **customerId** | **String**|  | [optional] |

### Return type

ApiResponse<[**ListCampaignAssets200Response**](ListCampaignAssets200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Forbidden. One of:  - Ads access is required. - Code &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the ad account this request targets is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix &#x60;ad_account_not_selected&#x60;, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |


## listCampaignNegativeKeywordLists

> ListAdNegativeKeywordLists200Response listCampaignNegativeKeywordLists(campaignId, platform)

List campaign negative lists

Lists the shared negative keyword lists attached to a Google campaign, separate from its own campaign-level negatives.  Google Ads shared negative keyword lists (shared_set type NEGATIVE_KEYWORDS). Reads are cached for 10 minutes; quota exhaustion may return the last successful result for up to 7 days with stale&#x3D;true. Customer selection is limited to this connection and its account scope. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | 
        String platform = "facebook"; // String | 
        try {
            ListAdNegativeKeywordLists200Response result = apiInstance.listCampaignNegativeKeywordLists(campaignId, platform);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listCampaignNegativeKeywordLists");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**|  | |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai, reddit] |

### Return type

[**ListAdNegativeKeywordLists200Response**](ListAdNegativeKeywordLists200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access and permission to the selected account are required.  Also returned with code &#x60;ad_account_not_selected&#x60; when the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | Ambiguous campaign or account selection. Use a profile-scoped key. A list still attached to a campaign may also be rejected by Google. The account may also be inactive or need reconnection (code ads_connection_required). Reconnect it and read GET /v1/accounts for its current ID before retrying. |  -  |
| **422** | Google Ads connection is missing or unavailable. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Available only on Google Ads. |  -  |

## listCampaignNegativeKeywordListsWithHttpInfo

> ApiResponse<ListAdNegativeKeywordLists200Response> listCampaignNegativeKeywordLists listCampaignNegativeKeywordListsWithHttpInfo(campaignId, platform)

List campaign negative lists

Lists the shared negative keyword lists attached to a Google campaign, separate from its own campaign-level negatives.  Google Ads shared negative keyword lists (shared_set type NEGATIVE_KEYWORDS). Reads are cached for 10 minutes; quota exhaustion may return the last successful result for up to 7 days with stale&#x3D;true. Customer selection is limited to this connection and its account scope. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | 
        String platform = "facebook"; // String | 
        try {
            ApiResponse<ListAdNegativeKeywordLists200Response> response = apiInstance.listCampaignNegativeKeywordListsWithHttpInfo(campaignId, platform);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listCampaignNegativeKeywordLists");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**|  | |
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai, reddit] |

### Return type

ApiResponse<[**ListAdNegativeKeywordLists200Response**](ListAdNegativeKeywordLists200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access and permission to the selected account are required.  Also returned with code &#x60;ad_account_not_selected&#x60; when the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | Ambiguous campaign or account selection. Use a profile-scoped key. A list still attached to a campaign may also be rejected by Google. The account may also be inactive or need reconnection (code ads_connection_required). Reconnect it and read GET /v1/accounts for its current ID before retrying. |  -  |
| **422** | Google Ads connection is missing or unavailable. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Available only on Google Ads. |  -  |


## listCampaignNegativeKeywords

> ListCampaignNegativeKeywords200Response listCampaignNegativeKeywords(campaignId, platform)

List campaign-level negative keywords

Lists the negative keywords set on a whole Google campaign, separate from ad group negatives.  It returns the campaign-level negative keywords (&#x60;campaign_criterion.negative&#x60;), distinct from the ad-group-level negatives under &#x60;GET /v1/ads/keywords&#x60;.  ### Caching and quota  Results are cached for the quota window (not synced to Postgres) and gated by the shared Google Ads operations budget, like every other on-demand Google surface.  The response carries &#x60;cachedAt&#x60; and &#x60;stale&#x60;, set when a quota-exhausted call falls back to the last-good copy instead of a live read.  ### Platform  The platform is always discovered from the campaign itself. A non-Google campaign returns 501 rather than 404, whether or not &#x60;platform&#x60; was passed. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        String platform = "facebook"; // String | Optional and NOT authoritative: the resolved campaign's own platform decides 200 vs 501, never this hint.
        try {
            ListCampaignNegativeKeywords200Response result = apiInstance.listCampaignNegativeKeywords(campaignId, platform);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listCampaignNegativeKeywords");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Platform campaign ID | |
| **platform** | **String**| Optional and NOT authoritative: the resolved campaign&#39;s own platform decides 200 vs 501, never this hint. | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai, reddit] |

### Return type

[**ListCampaignNegativeKeywords200Response**](ListCampaignNegativeKeywords200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign-level negative keywords |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Campaign not found |  -  |
| **429** | Google Ads operations budget exhausted; retry later |  -  |
| **501** | Only available on Google Ads campaigns |  -  |

## listCampaignNegativeKeywordsWithHttpInfo

> ApiResponse<ListCampaignNegativeKeywords200Response> listCampaignNegativeKeywords listCampaignNegativeKeywordsWithHttpInfo(campaignId, platform)

List campaign-level negative keywords

Lists the negative keywords set on a whole Google campaign, separate from ad group negatives.  It returns the campaign-level negative keywords (&#x60;campaign_criterion.negative&#x60;), distinct from the ad-group-level negatives under &#x60;GET /v1/ads/keywords&#x60;.  ### Caching and quota  Results are cached for the quota window (not synced to Postgres) and gated by the shared Google Ads operations budget, like every other on-demand Google surface.  The response carries &#x60;cachedAt&#x60; and &#x60;stale&#x60;, set when a quota-exhausted call falls back to the last-good copy instead of a live read.  ### Platform  The platform is always discovered from the campaign itself. A non-Google campaign returns 501 rather than 404, whether or not &#x60;platform&#x60; was passed. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        String platform = "facebook"; // String | Optional and NOT authoritative: the resolved campaign's own platform decides 200 vs 501, never this hint.
        try {
            ApiResponse<ListCampaignNegativeKeywords200Response> response = apiInstance.listCampaignNegativeKeywordsWithHttpInfo(campaignId, platform);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listCampaignNegativeKeywords");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Platform campaign ID | |
| **platform** | **String**| Optional and NOT authoritative: the resolved campaign&#39;s own platform decides 200 vs 501, never this hint. | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter, openai, reddit] |

### Return type

ApiResponse<[**ListCampaignNegativeKeywords200Response**](ListCampaignNegativeKeywords200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign-level negative keywords |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Campaign not found |  -  |
| **429** | Google Ads operations budget exhausted; retry later |  -  |
| **501** | Only available on Google Ads campaigns |  -  |


## listGoogleAssetGroups

> ListGoogleAssetGroups200Response listGoogleAssetGroups(campaignId)

List Performance Max asset groups

Lists a Performance Max campaign&#39;s asset groups with their linked text, image and YouTube assets.  campaignId is the platform campaign id returned by creation or the campaign list. The campaign must be visible to the caller.  ### Caching  Uses a 10-minute cache, with the last successful response served as stale when Google quota is exhausted.  ### What is left out  - Removed groups and asset links are excluded. - Campaign-level brand assets on campaigns with brand guidelines enabled are not included. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Google Ads campaign id.
        try {
            ListGoogleAssetGroups200Response result = apiInstance.listGoogleAssetGroups(campaignId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listGoogleAssetGroups");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Google Ads campaign id. | |

### Return type

[**ListGoogleAssetGroups200Response**](ListGoogleAssetGroups200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Asset groups and linked assets. |  -  |
| **400** | Invalid request |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **429** | Google quota or operation budget exhausted with no cached response. |  -  |
| **501** | Campaign is not on Google Ads. |  -  |

## listGoogleAssetGroupsWithHttpInfo

> ApiResponse<ListGoogleAssetGroups200Response> listGoogleAssetGroups listGoogleAssetGroupsWithHttpInfo(campaignId)

List Performance Max asset groups

Lists a Performance Max campaign&#39;s asset groups with their linked text, image and YouTube assets.  campaignId is the platform campaign id returned by creation or the campaign list. The campaign must be visible to the caller.  ### Caching  Uses a 10-minute cache, with the last successful response served as stale when Google quota is exhausted.  ### What is left out  - Removed groups and asset links are excluded. - Campaign-level brand assets on campaigns with brand guidelines enabled are not included. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Google Ads campaign id.
        try {
            ApiResponse<ListGoogleAssetGroups200Response> response = apiInstance.listGoogleAssetGroupsWithHttpInfo(campaignId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listGoogleAssetGroups");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Google Ads campaign id. | |

### Return type

ApiResponse<[**ListGoogleAssetGroups200Response**](ListGoogleAssetGroups200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Asset groups and linked assets. |  -  |
| **400** | Invalid request |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **429** | Google quota or operation budget exhausted with no cached response. |  -  |
| **501** | Campaign is not on Google Ads. |  -  |


## listGoogleRecommendations

> ListGoogleRecommendations200Response listGoogleRecommendations(accountId, adAccountId, customerId, campaignId, types)

List Google Ads recommendations

Lists Google&#39;s optimization suggestions for an ad account, with the estimated impact of each.  ### What each recommendation includes  - type - estimated impact (base vs potential metrics, cost in account currency units) - the campaign, ad group or budget they target - the type-specific payload Google returns (&#x60;details&#x60;, in Google&#39;s own shape with micros)  Filter by campaignId and types.  Cached for 10 minutes and cleared by apply or dismiss. Served stale when Google quota is exhausted. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String accountId = "accountId_example"; // String | Google ads SocialAccount id.
        String adAccountId = "adAccountId_example"; // String | Google customer id, digits only. Defaults to the connection's only customer.
        String customerId = "customerId_example"; // String | Alias of adAccountId, kept for consistency with other Google endpoints.
        String campaignId = "campaignId_example"; // String | Only recommendations targeting this campaign.
        String types = "types_example"; // String | Comma-separated Google RecommendationType values, for example CAMPAIGN_BUDGET,KEYWORD,SET_TARGET_CPA.
        try {
            ListGoogleRecommendations200Response result = apiInstance.listGoogleRecommendations(accountId, adAccountId, customerId, campaignId, types);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listGoogleRecommendations");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Google ads SocialAccount id. | |
| **adAccountId** | **String**| Google customer id, digits only. Defaults to the connection&#39;s only customer. | [optional] |
| **customerId** | **String**| Alias of adAccountId, kept for consistency with other Google endpoints. | [optional] |
| **campaignId** | **String**| Only recommendations targeting this campaign. | [optional] |
| **types** | **String**| Comma-separated Google RecommendationType values, for example CAMPAIGN_BUDGET,KEYWORD,SET_TARGET_CPA. | [optional] |

### Return type

[**ListGoogleRecommendations200Response**](ListGoogleRecommendations200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Recommendations. |  -  |
| **400** | Invalid request |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **422** | No Google Ads customer on this connection, or it needs reconnecting. |  -  |
| **429** | Google quota or the Zernio Google operations burst limit is exhausted. |  -  |
| **501** | accountId is not a Google Ads connection. |  -  |

## listGoogleRecommendationsWithHttpInfo

> ApiResponse<ListGoogleRecommendations200Response> listGoogleRecommendations listGoogleRecommendationsWithHttpInfo(accountId, adAccountId, customerId, campaignId, types)

List Google Ads recommendations

Lists Google&#39;s optimization suggestions for an ad account, with the estimated impact of each.  ### What each recommendation includes  - type - estimated impact (base vs potential metrics, cost in account currency units) - the campaign, ad group or budget they target - the type-specific payload Google returns (&#x60;details&#x60;, in Google&#39;s own shape with micros)  Filter by campaignId and types.  Cached for 10 minutes and cleared by apply or dismiss. Served stale when Google quota is exhausted. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String accountId = "accountId_example"; // String | Google ads SocialAccount id.
        String adAccountId = "adAccountId_example"; // String | Google customer id, digits only. Defaults to the connection's only customer.
        String customerId = "customerId_example"; // String | Alias of adAccountId, kept for consistency with other Google endpoints.
        String campaignId = "campaignId_example"; // String | Only recommendations targeting this campaign.
        String types = "types_example"; // String | Comma-separated Google RecommendationType values, for example CAMPAIGN_BUDGET,KEYWORD,SET_TARGET_CPA.
        try {
            ApiResponse<ListGoogleRecommendations200Response> response = apiInstance.listGoogleRecommendationsWithHttpInfo(accountId, adAccountId, customerId, campaignId, types);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listGoogleRecommendations");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Google ads SocialAccount id. | |
| **adAccountId** | **String**| Google customer id, digits only. Defaults to the connection&#39;s only customer. | [optional] |
| **customerId** | **String**| Alias of adAccountId, kept for consistency with other Google endpoints. | [optional] |
| **campaignId** | **String**| Only recommendations targeting this campaign. | [optional] |
| **types** | **String**| Comma-separated Google RecommendationType values, for example CAMPAIGN_BUDGET,KEYWORD,SET_TARGET_CPA. | [optional] |

### Return type

ApiResponse<[**ListGoogleRecommendations200Response**](ListGoogleRecommendations200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Recommendations. |  -  |
| **400** | Invalid request |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | Resource not found |  -  |
| **422** | No Google Ads customer on this connection, or it needs reconnecting. |  -  |
| **429** | Google quota or the Zernio Google operations burst limit is exhausted. |  -  |
| **501** | accountId is not a Google Ads connection. |  -  |


## listSharedBudgets

> ListSharedBudgets200Response listSharedBudgets(accountId, adAccountId)

List shared budgets

Lists a Google Ads account&#39;s shared budgets and how many campaigns draw from each.  Lists the Google Ads customer&#39;s shared campaign budgets (&#x60;campaign_budget.explicitly_shared&#x60; &#x3D; true, not removed), with how many campaigns use each. Move a campaign onto one with &#x60;sharedBudgetId&#x60; on PUT /v1/ads/campaigns/{campaignId}. Google only; other platforms return 501. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String accountId = "accountId_example"; // String | Google ads SocialAccount id.
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID (Google customer ID, digits only). Defaults to the account's connected customer.
        try {
            ListSharedBudgets200Response result = apiInstance.listSharedBudgets(accountId, adAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listSharedBudgets");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Google ads SocialAccount id. | |
| **adAccountId** | **String**| Platform ad account ID (Google customer ID, digits only). Defaults to the account&#39;s connected customer. | [optional] |

### Return type

[**ListSharedBudgets200Response**](ListSharedBudgets200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Shared budgets |  -  |
| **400** | Invalid request |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **501** | Only available on Google Ads accounts |  -  |

## listSharedBudgetsWithHttpInfo

> ApiResponse<ListSharedBudgets200Response> listSharedBudgets listSharedBudgetsWithHttpInfo(accountId, adAccountId)

List shared budgets

Lists a Google Ads account&#39;s shared budgets and how many campaigns draw from each.  Lists the Google Ads customer&#39;s shared campaign budgets (&#x60;campaign_budget.explicitly_shared&#x60; &#x3D; true, not removed), with how many campaigns use each. Move a campaign onto one with &#x60;sharedBudgetId&#x60; on PUT /v1/ads/campaigns/{campaignId}. Google only; other platforms return 501. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String accountId = "accountId_example"; // String | Google ads SocialAccount id.
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID (Google customer ID, digits only). Defaults to the account's connected customer.
        try {
            ApiResponse<ListSharedBudgets200Response> response = apiInstance.listSharedBudgetsWithHttpInfo(accountId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listSharedBudgets");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Google ads SocialAccount id. | |
| **adAccountId** | **String**| Platform ad account ID (Google customer ID, digits only). Defaults to the account&#39;s connected customer. | [optional] |

### Return type

ApiResponse<[**ListSharedBudgets200Response**](ListSharedBudgets200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Shared budgets |  -  |
| **400** | Invalid request |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **501** | Only available on Google Ads accounts |  -  |


## listTikTokSmartPlusReviews

> ListTikTokSmartPlusReviews200Response listTikTokSmartPlusReviews(accountId, adAccountId, includeDeleted, maxAgeSeconds, page, pageSize)

Review status of every TikTok Smart+ ad of an advertiser

Returns the review verdict of every Upgraded Smart+ ad of one TikTok advertiser, with each creative&#39;s verdict, in one paginated read.  Use it to refresh reviews periodically: one call (plus its pages) per advertiser per refresh, instead of &#x60;GET /v1/ads/{adId}/tiktok-smart-plus-review&#x60; per ad.  ### How Zernio reads TikTok  1. Zernio lists the advertiser&#39;s Smart+ ads with &#x60;/smart_plus/ad/get/&#x60; (deleted ones only with &#x60;includeDeleted&#x3D;true&#x60;). 2. It reads &#x60;/smart_plus/ad/review_info/&#x60; for Smart+ ads holding up to 50 creatives in total per call (TikTok refuses more). A Smart+ ad with more than 50 creatives is read alone. 3. Calls run across ad groups, one after another while TikTok accepts them, for up to 20 seconds per request. Ads not reached are read by the next request, which can come right away.  One request per advertiser and connection refreshes at a time. A parallel request sends no review call and answers what is stored with &#x60;refreshState: paused&#x60; and &#x60;retryAfterSeconds: 20&#x60;.  A full refresh of N Smart+ ads with C creatives in total costs about &#x60;ceil(N / 100)&#x60; listing calls and &#x60;ceil(C / 50)&#x60; review calls on TikTok.  When TikTok still refuses a call for its creative count, Zernio lowers the creative cap for that advertiser and reads the same ads again in smaller calls, never resending the refused size.  ### Stale while refreshing  Every review is stored for 24 hours per connection, advertiser and Smart+ ad (shared with the single-ad read). &#x60;readAt&#x60; is always the time TikTok answered, never rewritten when served from the store.  &#x60;maxAgeSeconds&#x60; (default 3600) is the freshness window:  - A review read within it is fresh and costs no TikTok call. - An older one is still returned in &#x60;items&#x60; but is read again. - A Smart+ ad never read is also read.  Each request alternates one batch of Smart+ ads never read (live, then deleted with &#x60;includeDeleted&#x3D;true&#x60;) with one batch of stale ones, oldest &#x60;readAt&#x60; first.  So a quota pause starves neither, progress carries over between requests, and an ad already read never goes back to pending. A stored review is replaced only by a successful read.  ### Response fields  - &#x60;counts&#x60;: splits the Smart+ ads on this page into &#x60;fresh&#x60;, &#x60;stale&#x60;, &#x60;pending&#x60; and &#x60;failed&#x60;. - &#x60;oldestReadAt&#x60;: the oldest &#x60;readAt&#x60; of &#x60;items&#x60;. - &#x60;incomplete&#x60;: true only while some Smart+ ad of the page has never been read (&#x60;pending &gt; 0&#x60;). - &#x60;allFresh&#x60;: staleness is reported apart. True when every item and refusal of the page is within &#x60;maxAgeSeconds&#x60; and nothing is pending. - &#x60;refreshState&#x60;: &#x60;paused&#x60; or &#x60;refused&#x60; when Zernio could not refresh some due ads of the page because review reads are held or TikTok refused them over quota. - &#x60;retryAfterSeconds&#x60; (also in the &#x60;Retry-After&#x60; header): when that later read can reach TikTok, even with nothing pending.  A page with stale items and nothing pending is complete (&#x60;incomplete: false&#x60;). Move on, and a later read refreshes it oldest first.  On 2026-10-25 TikTok&#39;s quota allowed about 130 to 230 Smart+ ads per advertiser per hour (about 11.5 ads and 4 creatives per successful call). A larger advertiser cannot be fully refreshed within one hour, so its pages stay complete but not &#x60;allFresh&#x60;.  ### Listing freshness  The listing is stored with the time it was read (&#x60;listing.readAt&#x60;) and listed again when it is older than &#x60;maxAgeSeconds&#x60;. So it can be up to &#x60;maxAgeSeconds&#x60; old: a Smart+ ad created on TikTok appears after at most that long (one hour by default).  - &#x60;listing.source: fresh&#x60;: the listing was read within &#x60;maxAgeSeconds&#x60;. - &#x60;listing.source: fallback&#x60;: relisting failed, so Zernio serves the stored listing, with the relist error in &#x60;listing.error&#x60;, instead of failing the request.  Only when no listing was ever stored does the listing error fail the request.  ### Review quota  TikTok&#39;s review endpoint has a strict quota of its own (TikTok documents neither the quota nor its scope). One request keeps reading batches (up to 50 creatives each) while TikTok accepts them.  Zernio may hold review reads after an overage: about 60 seconds, then 120 and up to 240 while TikTok keeps refusing, and about 60 again after a successful call, each with up to 10% of random jitter.  When TikTok is over quota (or reads are held), Zernio stops calling TikTok and answers 200 with the reviews it has:  - stale reviews in &#x60;items&#x60; - the Smart+ ads never read in &#x60;pendingSmartPlusAdIds&#x60; - &#x60;incomplete: true&#x60; when any are pending - &#x60;refreshState&#x60; (&#x60;paused&#x60; or &#x60;refused&#x60;) with &#x60;retryAfterSeconds&#x60; (also in the &#x60;Retry-After&#x60; header) whenever due ads were left unread  Every Smart+ ad of the page is in &#x60;items&#x60;, &#x60;failedSmartPlusAds&#x60; or &#x60;pendingSmartPlusAdIds&#x60;. Wait &#x60;retryAfterSeconds&#x60; and read the same page again: only the stale and pending ads reach TikTok.  ### Refused ads  A Smart+ ad whose review TikTok refuses on its own (for example one deleted on TikTok since the listing was read) is returned in &#x60;failedSmartPlusAds&#x60; with TikTok&#39;s error and &#x60;refusedAt&#x60;. The rest of the page is still read.  Zernio finds it by splitting the refused batch in halves, at most 16 extra TikTok calls per page. Ads still unresolved after that keep their stored review, or stay in &#x60;pendingSmartPlusAdIds&#x60; when they have none, and are read again by the next request, in turn with the other due ads.  A refusal of a single ad is stored for 24 hours and read again once it is older than &#x60;maxAgeSeconds&#x60;. When an ad has both a stored review and a stored refusal, the more recent one is returned.  When both halves of a refused batch are refused with the same TikTok error (for example a permission error), Zernio stops calling TikTok for that page:  - If every Smart+ ad of the page has a stored review or refusal, it serves them and returns the refusal in &#x60;reviewError&#x60;. - If some ad was never read, the whole request fails with that error.  ### Paging  Items are sorted by &#x60;adGroupId&#x60;, then &#x60;smartPlusAdId&#x60;, so pages are stable.  Keep one page in flight per advertiser and read its pages one after another. Parallel pages of one advertiser spend its review quota at the same time and come back incomplete.  Production logs suggest the quota is counted per advertiser (not confirmed by TikTok), so different advertisers have been read in parallel without throttling each other. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String accountId = "accountId_example"; // String | A tiktok or tiktokads account ID
        String adAccountId = "adAccountId_example"; // String | TikTok advertiser ID
        Boolean includeDeleted = false; // Boolean | Also return Smart+ ads deleted on TikTok (listed with `primary_status: STATUS_ALL`).
        Integer maxAgeSeconds = 3600; // Integer | Freshness window in seconds. Reviews, refusals and the listing read within it are served without calling TikTok; older ones are still returned but read again, oldest first.
        Integer page = 1; // Integer | 
        Integer pageSize = 500; // Integer | 
        try {
            ListTikTokSmartPlusReviews200Response result = apiInstance.listTikTokSmartPlusReviews(accountId, adAccountId, includeDeleted, maxAgeSeconds, page, pageSize);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listTikTokSmartPlusReviews");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| A tiktok or tiktokads account ID | |
| **adAccountId** | **String**| TikTok advertiser ID | |
| **includeDeleted** | **Boolean**| Also return Smart+ ads deleted on TikTok (listed with &#x60;primary_status: STATUS_ALL&#x60;). | [optional] [default to false] |
| **maxAgeSeconds** | **Integer**| Freshness window in seconds. Reviews, refusals and the listing read within it are served without calling TikTok; older ones are still returned but read again, oldest first. | [optional] [default to 3600] |
| **page** | **Integer**|  | [optional] [default to 1] |
| **pageSize** | **Integer**|  | [optional] [default to 500] |

### Return type

[**ListTikTokSmartPlusReviews200Response**](ListTikTokSmartPlusReviews200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The reviews of one page of the advertiser&#39;s Smart+ ads. Check &#x60;incomplete&#x60;: when true, some Smart+ ads of the page were never read. &#x60;allFresh&#x60; says whether every review is within &#x60;maxAgeSeconds&#x60;. |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | accountId is not a TikTok or TikTok Ads connection (code feature_not_available). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **422** | The TikTok connection has no TikTok Ads token: connect TikTok Ads first (code ads_connection_required). |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted. Behavior per platform:  - **Reddit:** rate-limits per connected Reddit user (1000 requests per 10-minute window), shared by every operation on that account. Retry after the window resets; repeated calls while exhausted do not succeed and keep the budget spent. - **Google Ads:** writes and reports run on one developer token shared by every Google Ads account on Zernio. It holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. - **Google Ads envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **YouTube Analytics:** reads (channel-insights, demographics, daily-views, video-retention) use the \&quot;Queries per day\&quot; quota of the Google Cloud project the account is connected through, shared with other Zernio customers, so a 429 is not your own volume. Resets at midnight Pacific Time. - **YouTube Analytics envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaExhausted: true&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60;, &#x60;details.resetsAt&#x60; and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **Meta ads:** every Meta throttle (codes 4, 17, 32, 613 and business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when sent, else Meta&#39;s 60-second minimum (30 seconds for the one-write-per-30-seconds limit on one object). - **Pinterest ads:** limits per user and app, per category (ads_read, ads_write, ads_analytics). &#x60;Retry-After&#x60; comes from Pinterest&#39;s &#x60;x-ratelimit-reset&#x60; when sent, otherwise 60 seconds. - **TikTok ads:** limits per app and per endpoint (per second, minute and day), answering overage with code 40100 or code 40002 &#x60;OVER_QPS_LIMIT&#x60;. Both return 429 &#x60;rate_limited&#x60; with &#x60;platform: tiktok&#x60; and &#x60;Retry-After: 10&#x60;. Space out bulk reads (e.g. one ad at a time per advertiser) instead of retrying at once.  **TikTok Smart+ review read** (&#x60;GET /v1/ads/{adId}/tiktok-smart-plus-review&#x60;) has its own stricter TikTok quota. After an overage, Zernio answers 429 for that advertiser and connection without calling TikTok for about 60 seconds, then 120, up to 240 while TikTok keeps refusing, each with up to 10% random jitter.  A successful call holds nothing back; the next overage pauses about 60 seconds again. &#x60;Retry-After&#x60; is the time left. The advertiser-wide read (&#x60;GET /v1/ads/tiktok-smart-plus-reviews&#x60;) answers 200 with &#x60;retryAfterSeconds&#x60; and &#x60;refreshState&#x60; instead. Keep one request in flight per advertiser there.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |

## listTikTokSmartPlusReviewsWithHttpInfo

> ApiResponse<ListTikTokSmartPlusReviews200Response> listTikTokSmartPlusReviews listTikTokSmartPlusReviewsWithHttpInfo(accountId, adAccountId, includeDeleted, maxAgeSeconds, page, pageSize)

Review status of every TikTok Smart+ ad of an advertiser

Returns the review verdict of every Upgraded Smart+ ad of one TikTok advertiser, with each creative&#39;s verdict, in one paginated read.  Use it to refresh reviews periodically: one call (plus its pages) per advertiser per refresh, instead of &#x60;GET /v1/ads/{adId}/tiktok-smart-plus-review&#x60; per ad.  ### How Zernio reads TikTok  1. Zernio lists the advertiser&#39;s Smart+ ads with &#x60;/smart_plus/ad/get/&#x60; (deleted ones only with &#x60;includeDeleted&#x3D;true&#x60;). 2. It reads &#x60;/smart_plus/ad/review_info/&#x60; for Smart+ ads holding up to 50 creatives in total per call (TikTok refuses more). A Smart+ ad with more than 50 creatives is read alone. 3. Calls run across ad groups, one after another while TikTok accepts them, for up to 20 seconds per request. Ads not reached are read by the next request, which can come right away.  One request per advertiser and connection refreshes at a time. A parallel request sends no review call and answers what is stored with &#x60;refreshState: paused&#x60; and &#x60;retryAfterSeconds: 20&#x60;.  A full refresh of N Smart+ ads with C creatives in total costs about &#x60;ceil(N / 100)&#x60; listing calls and &#x60;ceil(C / 50)&#x60; review calls on TikTok.  When TikTok still refuses a call for its creative count, Zernio lowers the creative cap for that advertiser and reads the same ads again in smaller calls, never resending the refused size.  ### Stale while refreshing  Every review is stored for 24 hours per connection, advertiser and Smart+ ad (shared with the single-ad read). &#x60;readAt&#x60; is always the time TikTok answered, never rewritten when served from the store.  &#x60;maxAgeSeconds&#x60; (default 3600) is the freshness window:  - A review read within it is fresh and costs no TikTok call. - An older one is still returned in &#x60;items&#x60; but is read again. - A Smart+ ad never read is also read.  Each request alternates one batch of Smart+ ads never read (live, then deleted with &#x60;includeDeleted&#x3D;true&#x60;) with one batch of stale ones, oldest &#x60;readAt&#x60; first.  So a quota pause starves neither, progress carries over between requests, and an ad already read never goes back to pending. A stored review is replaced only by a successful read.  ### Response fields  - &#x60;counts&#x60;: splits the Smart+ ads on this page into &#x60;fresh&#x60;, &#x60;stale&#x60;, &#x60;pending&#x60; and &#x60;failed&#x60;. - &#x60;oldestReadAt&#x60;: the oldest &#x60;readAt&#x60; of &#x60;items&#x60;. - &#x60;incomplete&#x60;: true only while some Smart+ ad of the page has never been read (&#x60;pending &gt; 0&#x60;). - &#x60;allFresh&#x60;: staleness is reported apart. True when every item and refusal of the page is within &#x60;maxAgeSeconds&#x60; and nothing is pending. - &#x60;refreshState&#x60;: &#x60;paused&#x60; or &#x60;refused&#x60; when Zernio could not refresh some due ads of the page because review reads are held or TikTok refused them over quota. - &#x60;retryAfterSeconds&#x60; (also in the &#x60;Retry-After&#x60; header): when that later read can reach TikTok, even with nothing pending.  A page with stale items and nothing pending is complete (&#x60;incomplete: false&#x60;). Move on, and a later read refreshes it oldest first.  On 2026-10-25 TikTok&#39;s quota allowed about 130 to 230 Smart+ ads per advertiser per hour (about 11.5 ads and 4 creatives per successful call). A larger advertiser cannot be fully refreshed within one hour, so its pages stay complete but not &#x60;allFresh&#x60;.  ### Listing freshness  The listing is stored with the time it was read (&#x60;listing.readAt&#x60;) and listed again when it is older than &#x60;maxAgeSeconds&#x60;. So it can be up to &#x60;maxAgeSeconds&#x60; old: a Smart+ ad created on TikTok appears after at most that long (one hour by default).  - &#x60;listing.source: fresh&#x60;: the listing was read within &#x60;maxAgeSeconds&#x60;. - &#x60;listing.source: fallback&#x60;: relisting failed, so Zernio serves the stored listing, with the relist error in &#x60;listing.error&#x60;, instead of failing the request.  Only when no listing was ever stored does the listing error fail the request.  ### Review quota  TikTok&#39;s review endpoint has a strict quota of its own (TikTok documents neither the quota nor its scope). One request keeps reading batches (up to 50 creatives each) while TikTok accepts them.  Zernio may hold review reads after an overage: about 60 seconds, then 120 and up to 240 while TikTok keeps refusing, and about 60 again after a successful call, each with up to 10% of random jitter.  When TikTok is over quota (or reads are held), Zernio stops calling TikTok and answers 200 with the reviews it has:  - stale reviews in &#x60;items&#x60; - the Smart+ ads never read in &#x60;pendingSmartPlusAdIds&#x60; - &#x60;incomplete: true&#x60; when any are pending - &#x60;refreshState&#x60; (&#x60;paused&#x60; or &#x60;refused&#x60;) with &#x60;retryAfterSeconds&#x60; (also in the &#x60;Retry-After&#x60; header) whenever due ads were left unread  Every Smart+ ad of the page is in &#x60;items&#x60;, &#x60;failedSmartPlusAds&#x60; or &#x60;pendingSmartPlusAdIds&#x60;. Wait &#x60;retryAfterSeconds&#x60; and read the same page again: only the stale and pending ads reach TikTok.  ### Refused ads  A Smart+ ad whose review TikTok refuses on its own (for example one deleted on TikTok since the listing was read) is returned in &#x60;failedSmartPlusAds&#x60; with TikTok&#39;s error and &#x60;refusedAt&#x60;. The rest of the page is still read.  Zernio finds it by splitting the refused batch in halves, at most 16 extra TikTok calls per page. Ads still unresolved after that keep their stored review, or stay in &#x60;pendingSmartPlusAdIds&#x60; when they have none, and are read again by the next request, in turn with the other due ads.  A refusal of a single ad is stored for 24 hours and read again once it is older than &#x60;maxAgeSeconds&#x60;. When an ad has both a stored review and a stored refusal, the more recent one is returned.  When both halves of a refused batch are refused with the same TikTok error (for example a permission error), Zernio stops calling TikTok for that page:  - If every Smart+ ad of the page has a stored review or refusal, it serves them and returns the refusal in &#x60;reviewError&#x60;. - If some ad was never read, the whole request fails with that error.  ### Paging  Items are sorted by &#x60;adGroupId&#x60;, then &#x60;smartPlusAdId&#x60;, so pages are stable.  Keep one page in flight per advertiser and read its pages one after another. Parallel pages of one advertiser spend its review quota at the same time and come back incomplete.  Production logs suggest the quota is counted per advertiser (not confirmed by TikTok), so different advertisers have been read in parallel without throttling each other. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String accountId = "accountId_example"; // String | A tiktok or tiktokads account ID
        String adAccountId = "adAccountId_example"; // String | TikTok advertiser ID
        Boolean includeDeleted = false; // Boolean | Also return Smart+ ads deleted on TikTok (listed with `primary_status: STATUS_ALL`).
        Integer maxAgeSeconds = 3600; // Integer | Freshness window in seconds. Reviews, refusals and the listing read within it are served without calling TikTok; older ones are still returned but read again, oldest first.
        Integer page = 1; // Integer | 
        Integer pageSize = 500; // Integer | 
        try {
            ApiResponse<ListTikTokSmartPlusReviews200Response> response = apiInstance.listTikTokSmartPlusReviewsWithHttpInfo(accountId, adAccountId, includeDeleted, maxAgeSeconds, page, pageSize);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#listTikTokSmartPlusReviews");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| A tiktok or tiktokads account ID | |
| **adAccountId** | **String**| TikTok advertiser ID | |
| **includeDeleted** | **Boolean**| Also return Smart+ ads deleted on TikTok (listed with &#x60;primary_status: STATUS_ALL&#x60;). | [optional] [default to false] |
| **maxAgeSeconds** | **Integer**| Freshness window in seconds. Reviews, refusals and the listing read within it are served without calling TikTok; older ones are still returned but read again, oldest first. | [optional] [default to 3600] |
| **page** | **Integer**|  | [optional] [default to 1] |
| **pageSize** | **Integer**|  | [optional] [default to 500] |

### Return type

ApiResponse<[**ListTikTokSmartPlusReviews200Response**](ListTikTokSmartPlusReviews200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The reviews of one page of the advertiser&#39;s Smart+ ads. Check &#x60;incomplete&#x60;: when true, some Smart+ ads of the page were never read. &#x60;allFresh&#x60; says whether every review is within &#x60;maxAgeSeconds&#x60;. |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | accountId is not a TikTok or TikTok Ads connection (code feature_not_available). |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **422** | The TikTok connection has no TikTok Ads token: connect TikTok Ads first (code ads_connection_required). |  -  |
| **429** | The connected account&#39;s upstream platform quota is exhausted. Behavior per platform:  - **Reddit:** rate-limits per connected Reddit user (1000 requests per 10-minute window), shared by every operation on that account. Retry after the window resets; repeated calls while exhausted do not succeed and keep the budget spent. - **Google Ads:** writes and reports run on one developer token shared by every Google Ads account on Zernio. It holds Standard access (no daily operations cap), so this only happens when Google throttles the token or your ad account. - **Google Ads envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60; (&#x60;ACCOUNT&#x60; when it is your own ad account&#39;s quota), &#x60;details.resetsAt&#x60; (ISO instant when Google accepts requests again) and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **YouTube Analytics:** reads (channel-insights, demographics, daily-views, video-retention) use the \&quot;Queries per day\&quot; quota of the Google Cloud project the account is connected through, shared with other Zernio customers, so a 429 is not your own volume. Resets at midnight Pacific Time. - **YouTube Analytics envelope:** &#x60;code: rate_limited&#x60;, &#x60;platform: google&#x60;, &#x60;details.quotaExhausted: true&#x60;, &#x60;details.quotaScope: DEVELOPER&#x60;, &#x60;details.resetsAt&#x60; and &#x60;Retry-After&#x60; counting down to it. Retrying earlier cannot succeed. - **Meta ads:** every Meta throttle (codes 4, 17, 32, 613 and business-use-case codes 80000-80014) returns 429 &#x60;rate_limited&#x60;, even when Meta answers HTTP 400. &#x60;Retry-After&#x60; comes from Meta&#39;s &#x60;x-business-use-case-usage&#x60; estimate when sent, else Meta&#39;s 60-second minimum (30 seconds for the one-write-per-30-seconds limit on one object). - **Pinterest ads:** limits per user and app, per category (ads_read, ads_write, ads_analytics). &#x60;Retry-After&#x60; comes from Pinterest&#39;s &#x60;x-ratelimit-reset&#x60; when sent, otherwise 60 seconds. - **TikTok ads:** limits per app and per endpoint (per second, minute and day), answering overage with code 40100 or code 40002 &#x60;OVER_QPS_LIMIT&#x60;. Both return 429 &#x60;rate_limited&#x60; with &#x60;platform: tiktok&#x60; and &#x60;Retry-After: 10&#x60;. Space out bulk reads (e.g. one ad at a time per advertiser) instead of retrying at once.  **TikTok Smart+ review read** (&#x60;GET /v1/ads/{adId}/tiktok-smart-plus-review&#x60;) has its own stricter TikTok quota. After an overage, Zernio answers 429 for that advertiser and connection without calling TikTok for about 60 seconds, then 120, up to 240 while TikTok keeps refusing, each with up to 10% random jitter.  A successful call holds nothing back; the next overage pauses about 60 seconds again. &#x60;Retry-After&#x60; is the time left. The advertiser-wide read (&#x60;GET /v1/ads/tiktok-smart-plus-reviews&#x60;) answers 200 with &#x60;retryAfterSeconds&#x60; and &#x60;refreshState&#x60; instead. Keep one request in flight per advertiser there.  |  * Retry-After - Seconds remaining until the upstream quota resets. <br>  |


## removeAdGroupAssets

> RemoveCampaignAssets200Response removeAdGroupAssets(adSetId, accountId, assetResourceNames, adGroupAssetResourceNames, adAccountId, customerId)

Remove ad-group assets

Detaches assets from a Google ad group without deleting them, so they stay in the account and on anything else they are attached to.  Google assets cannot be deleted. Other attachments remain. assetResourceNames is retained for compatibility. Fields go in the query string. A JSON body with the same fields is also accepted and, when sent, the query string is ignored. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Numeric Google platform id.
        String accountId = "accountId_example"; // String | Zernio Google Ads connection id.
        List<String> assetResourceNames = Arrays.asList(); // List<String> | Asset resource names, retained for compatibility. Repeat the parameter or pass a comma-separated list.
        List<String> adGroupAssetResourceNames = Arrays.asList(); // List<String> | ad_group_asset resource names to remove, e.g. customers/1234567890/adGroupAssets/456~123~CALLOUT. Repeat the parameter or pass a comma-separated list.
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID (Google customer ID, digits only). Required when the connection has multiple customers.
        String customerId = "customerId_example"; // String | Alias of adAccountId, kept for existing callers
        try {
            RemoveCampaignAssets200Response result = apiInstance.removeAdGroupAssets(adSetId, accountId, assetResourceNames, adGroupAssetResourceNames, adAccountId, customerId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#removeAdGroupAssets");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adSetId** | **String**| Numeric Google platform id. | |
| **accountId** | **String**| Zernio Google Ads connection id. | |
| **assetResourceNames** | [**List&lt;String&gt;**](String.md)| Asset resource names, retained for compatibility. Repeat the parameter or pass a comma-separated list. | |
| **adGroupAssetResourceNames** | [**List&lt;String&gt;**](String.md)| ad_group_asset resource names to remove, e.g. customers/1234567890/adGroupAssets/456~123~CALLOUT. Repeat the parameter or pass a comma-separated list. | |
| **adAccountId** | **String**| Platform ad account ID (Google customer ID, digits only). Required when the connection has multiple customers. | [optional] |
| **customerId** | **String**| Alias of adAccountId, kept for existing callers | [optional] |

### Return type

[**RemoveCampaignAssets200Response**](RemoveCampaignAssets200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access is required.  Also returned with code &#x60;ad_account_not_selected&#x60; when the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix it, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |

## removeAdGroupAssetsWithHttpInfo

> ApiResponse<RemoveCampaignAssets200Response> removeAdGroupAssets removeAdGroupAssetsWithHttpInfo(adSetId, accountId, assetResourceNames, adGroupAssetResourceNames, adAccountId, customerId)

Remove ad-group assets

Detaches assets from a Google ad group without deleting them, so they stay in the account and on anything else they are attached to.  Google assets cannot be deleted. Other attachments remain. assetResourceNames is retained for compatibility. Fields go in the query string. A JSON body with the same fields is also accepted and, when sent, the query string is ignored. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Numeric Google platform id.
        String accountId = "accountId_example"; // String | Zernio Google Ads connection id.
        List<String> assetResourceNames = Arrays.asList(); // List<String> | Asset resource names, retained for compatibility. Repeat the parameter or pass a comma-separated list.
        List<String> adGroupAssetResourceNames = Arrays.asList(); // List<String> | ad_group_asset resource names to remove, e.g. customers/1234567890/adGroupAssets/456~123~CALLOUT. Repeat the parameter or pass a comma-separated list.
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID (Google customer ID, digits only). Required when the connection has multiple customers.
        String customerId = "customerId_example"; // String | Alias of adAccountId, kept for existing callers
        try {
            ApiResponse<RemoveCampaignAssets200Response> response = apiInstance.removeAdGroupAssetsWithHttpInfo(adSetId, accountId, assetResourceNames, adGroupAssetResourceNames, adAccountId, customerId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#removeAdGroupAssets");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adSetId** | **String**| Numeric Google platform id. | |
| **accountId** | **String**| Zernio Google Ads connection id. | |
| **assetResourceNames** | [**List&lt;String&gt;**](String.md)| Asset resource names, retained for compatibility. Repeat the parameter or pass a comma-separated list. | |
| **adGroupAssetResourceNames** | [**List&lt;String&gt;**](String.md)| ad_group_asset resource names to remove, e.g. customers/1234567890/adGroupAssets/456~123~CALLOUT. Repeat the parameter or pass a comma-separated list. | |
| **adAccountId** | **String**| Platform ad account ID (Google customer ID, digits only). Required when the connection has multiple customers. | [optional] |
| **customerId** | **String**| Alias of adAccountId, kept for existing callers | [optional] |

### Return type

ApiResponse<[**RemoveCampaignAssets200Response**](RemoveCampaignAssets200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access is required.  Also returned with code &#x60;ad_account_not_selected&#x60; when the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix it, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |


## removeAdKeyword

> RemoveAdKeyword200Response removeAdKeyword(keywordId)

Remove a Search keyword

Removes a single keyword or negative keyword from a Google Search ad group.  Removes one keyword criterion (positive or negative) from its ad group (M.140). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String keywordId = "keywordId_example"; // String | Zernio keyword ID (`id`), or Google's native `{adSetId}~{platformCriterionId}` (the tail of `resourceName`, e.g. 1234567890~987654321). A bare criterion id is rejected because it is only unique within its ad group.
        try {
            RemoveAdKeyword200Response result = apiInstance.removeAdKeyword(keywordId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#removeAdKeyword");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **keywordId** | **String**| Zernio keyword ID (&#x60;id&#x60;), or Google&#39;s native &#x60;{adSetId}~{platformCriterionId}&#x60; (the tail of &#x60;resourceName&#x60;, e.g. 1234567890~987654321). A bare criterion id is rejected because it is only unique within its ad group. | |

### Return type

[**RemoveAdKeyword200Response**](RemoveAdKeyword200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Keyword removed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |

## removeAdKeywordWithHttpInfo

> ApiResponse<RemoveAdKeyword200Response> removeAdKeyword removeAdKeywordWithHttpInfo(keywordId)

Remove a Search keyword

Removes a single keyword or negative keyword from a Google Search ad group.  Removes one keyword criterion (positive or negative) from its ad group (M.140). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String keywordId = "keywordId_example"; // String | Zernio keyword ID (`id`), or Google's native `{adSetId}~{platformCriterionId}` (the tail of `resourceName`, e.g. 1234567890~987654321). A bare criterion id is rejected because it is only unique within its ad group.
        try {
            ApiResponse<RemoveAdKeyword200Response> response = apiInstance.removeAdKeywordWithHttpInfo(keywordId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#removeAdKeyword");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **keywordId** | **String**| Zernio keyword ID (&#x60;id&#x60;), or Google&#39;s native &#x60;{adSetId}~{platformCriterionId}&#x60; (the tail of &#x60;resourceName&#x60;, e.g. 1234567890~987654321). A bare criterion id is rejected because it is only unique within its ad group. | |

### Return type

ApiResponse<[**RemoveAdKeyword200Response**](RemoveAdKeyword200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Keyword removed |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |


## removeCampaignAssets

> RemoveCampaignAssets200Response removeCampaignAssets(campaignId, accountId, assetResourceNames, campaignAssetResourceNames, adAccountId, customerId)

Remove campaign assets

Detaches assets from a Google campaign without deleting them, so they stay in the account and on anything else they are attached to.  Google assets cannot be deleted. Other attachments remain. assetResourceNames is retained for compatibility. Fields go in the query string. A JSON body with the same fields is also accepted and, when sent, the query string is ignored. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Numeric Google platform id.
        String accountId = "accountId_example"; // String | Zernio Google Ads connection id.
        List<String> assetResourceNames = Arrays.asList(); // List<String> | Asset resource names, retained for compatibility. Repeat the parameter or pass a comma-separated list.
        List<String> campaignAssetResourceNames = Arrays.asList(); // List<String> | campaign_asset resource names to remove, e.g. customers/1234567890/campaignAssets/456~123~CALLOUT. Repeat the parameter or pass a comma-separated list.
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID (Google customer ID, digits only). Required when the connection has multiple customers.
        String customerId = "customerId_example"; // String | Alias of adAccountId, kept for existing callers
        try {
            RemoveCampaignAssets200Response result = apiInstance.removeCampaignAssets(campaignId, accountId, assetResourceNames, campaignAssetResourceNames, adAccountId, customerId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#removeCampaignAssets");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Numeric Google platform id. | |
| **accountId** | **String**| Zernio Google Ads connection id. | |
| **assetResourceNames** | [**List&lt;String&gt;**](String.md)| Asset resource names, retained for compatibility. Repeat the parameter or pass a comma-separated list. | |
| **campaignAssetResourceNames** | [**List&lt;String&gt;**](String.md)| campaign_asset resource names to remove, e.g. customers/1234567890/campaignAssets/456~123~CALLOUT. Repeat the parameter or pass a comma-separated list. | |
| **adAccountId** | **String**| Platform ad account ID (Google customer ID, digits only). Required when the connection has multiple customers. | [optional] |
| **customerId** | **String**| Alias of adAccountId, kept for existing callers | [optional] |

### Return type

[**RemoveCampaignAssets200Response**](RemoveCampaignAssets200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access is required.  Also returned with code &#x60;ad_account_not_selected&#x60; when the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection), or use a connection that has it selected.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |

## removeCampaignAssetsWithHttpInfo

> ApiResponse<RemoveCampaignAssets200Response> removeCampaignAssets removeCampaignAssetsWithHttpInfo(campaignId, accountId, assetResourceNames, campaignAssetResourceNames, adAccountId, customerId)

Remove campaign assets

Detaches assets from a Google campaign without deleting them, so they stay in the account and on anything else they are attached to.  Google assets cannot be deleted. Other attachments remain. assetResourceNames is retained for compatibility. Fields go in the query string. A JSON body with the same fields is also accepted and, when sent, the query string is ignored. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Numeric Google platform id.
        String accountId = "accountId_example"; // String | Zernio Google Ads connection id.
        List<String> assetResourceNames = Arrays.asList(); // List<String> | Asset resource names, retained for compatibility. Repeat the parameter or pass a comma-separated list.
        List<String> campaignAssetResourceNames = Arrays.asList(); // List<String> | campaign_asset resource names to remove, e.g. customers/1234567890/campaignAssets/456~123~CALLOUT. Repeat the parameter or pass a comma-separated list.
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID (Google customer ID, digits only). Required when the connection has multiple customers.
        String customerId = "customerId_example"; // String | Alias of adAccountId, kept for existing callers
        try {
            ApiResponse<RemoveCampaignAssets200Response> response = apiInstance.removeCampaignAssetsWithHttpInfo(campaignId, accountId, assetResourceNames, campaignAssetResourceNames, adAccountId, customerId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#removeCampaignAssets");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Numeric Google platform id. | |
| **accountId** | **String**| Zernio Google Ads connection id. | |
| **assetResourceNames** | [**List&lt;String&gt;**](String.md)| Asset resource names, retained for compatibility. Repeat the parameter or pass a comma-separated list. | |
| **campaignAssetResourceNames** | [**List&lt;String&gt;**](String.md)| campaign_asset resource names to remove, e.g. customers/1234567890/campaignAssets/456~123~CALLOUT. Repeat the parameter or pass a comma-separated list. | |
| **adAccountId** | **String**| Platform ad account ID (Google customer ID, digits only). Required when the connection has multiple customers. | [optional] |
| **customerId** | **String**| Alias of adAccountId, kept for existing callers | [optional] |

### Return type

ApiResponse<[**RemoveCampaignAssets200Response**](RemoveCampaignAssets200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access is required.  Also returned with code &#x60;ad_account_not_selected&#x60; when the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection), or use a connection that has it selected.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |


## removeGoogleAssetGroup

> RemoveGoogleAssetGroup200Response removeGoogleAssetGroup(campaignId, assetGroupId, validateOnly)

Remove a Performance Max asset group

Permanently removes an asset group from a Performance Max campaign (this cannot be undone).  Removes the asset group on Google (status REMOVED, not reversible). Pass validateOnly&#x3D;true to validate without removing. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | 
        String assetGroupId = "assetGroupId_example"; // String | 
        Boolean validateOnly = false; // Boolean | 
        try {
            RemoveGoogleAssetGroup200Response result = apiInstance.removeGoogleAssetGroup(campaignId, assetGroupId, validateOnly);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#removeGoogleAssetGroup");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**|  | |
| **assetGroupId** | **String**|  | |
| **validateOnly** | **Boolean**|  | [optional] [default to false] |

### Return type

[**RemoveGoogleAssetGroup200Response**](RemoveGoogleAssetGroup200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Removed (or validated). |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **404** | Resource not found |  -  |
| **422** | Google Ads connection needs reconnecting. |  -  |
| **429** | Google quota or the Zernio Google operations burst limit is exhausted. |  -  |
| **501** | Campaign is not on Google Ads. |  -  |

## removeGoogleAssetGroupWithHttpInfo

> ApiResponse<RemoveGoogleAssetGroup200Response> removeGoogleAssetGroup removeGoogleAssetGroupWithHttpInfo(campaignId, assetGroupId, validateOnly)

Remove a Performance Max asset group

Permanently removes an asset group from a Performance Max campaign (this cannot be undone).  Removes the asset group on Google (status REMOVED, not reversible). Pass validateOnly&#x3D;true to validate without removing. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | 
        String assetGroupId = "assetGroupId_example"; // String | 
        Boolean validateOnly = false; // Boolean | 
        try {
            ApiResponse<RemoveGoogleAssetGroup200Response> response = apiInstance.removeGoogleAssetGroupWithHttpInfo(campaignId, assetGroupId, validateOnly);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#removeGoogleAssetGroup");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**|  | |
| **assetGroupId** | **String**|  | |
| **validateOnly** | **Boolean**|  | [optional] [default to false] |

### Return type

ApiResponse<[**RemoveGoogleAssetGroup200Response**](RemoveGoogleAssetGroup200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Removed (or validated). |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **404** | Resource not found |  -  |
| **422** | Google Ads connection needs reconnecting. |  -  |
| **429** | Google quota or the Zernio Google operations burst limit is exhausted. |  -  |
| **501** | Campaign is not on Google Ads. |  -  |


## replaceCampaignNegativeKeywordLists

> ReplaceAdNegativeKeywordListKeywords200Response replaceCampaignNegativeKeywordLists(campaignId, replaceCampaignNegativeKeywordListsRequest)

Replace campaign negative lists

Sets exactly which shared negative keyword lists apply to a Google campaign, or detaches them all, without changing the lists themselves.  Send listIds&#x3D;[] to detach all negative keyword lists. Only campaign_shared_set links are changed; the lists and their keywords are preserved. Every list must belong to the campaign customer and have type NEGATIVE_KEYWORDS. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | 
        ReplaceCampaignNegativeKeywordListsRequest replaceCampaignNegativeKeywordListsRequest = new ReplaceCampaignNegativeKeywordListsRequest(); // ReplaceCampaignNegativeKeywordListsRequest | 
        try {
            ReplaceAdNegativeKeywordListKeywords200Response result = apiInstance.replaceCampaignNegativeKeywordLists(campaignId, replaceCampaignNegativeKeywordListsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#replaceCampaignNegativeKeywordLists");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**|  | |
| **replaceCampaignNegativeKeywordListsRequest** | [**ReplaceCampaignNegativeKeywordListsRequest**](ReplaceCampaignNegativeKeywordListsRequest.md)|  | |

### Return type

[**ReplaceAdNegativeKeywordListKeywords200Response**](ReplaceAdNegativeKeywordListKeywords200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access and permission to the selected account are required.  Also returned with code &#x60;ad_account_not_selected&#x60; when the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection), or use a connection that has it selected.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | Ambiguous campaign or account selection. Use a profile-scoped key. A list still attached to a campaign may also be rejected by Google. The account may also be inactive or need reconnection (code ads_connection_required). Reconnect it and read GET /v1/accounts for its current ID before retrying. |  -  |
| **422** | Google Ads connection is missing or unavailable. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Available only on Google Ads. |  -  |

## replaceCampaignNegativeKeywordListsWithHttpInfo

> ApiResponse<ReplaceAdNegativeKeywordListKeywords200Response> replaceCampaignNegativeKeywordLists replaceCampaignNegativeKeywordListsWithHttpInfo(campaignId, replaceCampaignNegativeKeywordListsRequest)

Replace campaign negative lists

Sets exactly which shared negative keyword lists apply to a Google campaign, or detaches them all, without changing the lists themselves.  Send listIds&#x3D;[] to detach all negative keyword lists. Only campaign_shared_set links are changed; the lists and their keywords are preserved. Every list must belong to the campaign customer and have type NEGATIVE_KEYWORDS. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | 
        ReplaceCampaignNegativeKeywordListsRequest replaceCampaignNegativeKeywordListsRequest = new ReplaceCampaignNegativeKeywordListsRequest(); // ReplaceCampaignNegativeKeywordListsRequest | 
        try {
            ApiResponse<ReplaceAdNegativeKeywordListKeywords200Response> response = apiInstance.replaceCampaignNegativeKeywordListsWithHttpInfo(campaignId, replaceCampaignNegativeKeywordListsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#replaceCampaignNegativeKeywordLists");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**|  | |
| **replaceCampaignNegativeKeywordListsRequest** | [**ReplaceCampaignNegativeKeywordListsRequest**](ReplaceCampaignNegativeKeywordListsRequest.md)|  | |

### Return type

ApiResponse<[**ReplaceAdNegativeKeywordListKeywords200Response**](ReplaceAdNegativeKeywordListKeywords200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access and permission to the selected account are required.  Also returned with code &#x60;ad_account_not_selected&#x60; when the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection), or use a connection that has it selected.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | Ambiguous campaign or account selection. Use a profile-scoped key. A list still attached to a campaign may also be rejected by Google. The account may also be inactive or need reconnection (code ads_connection_required). Reconnect it and read GET /v1/accounts for its current ID before retrying. |  -  |
| **422** | Google Ads connection is missing or unavailable. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Available only on Google Ads. |  -  |


## replaceCampaignNegativeKeywords

> ReplaceCampaignNegativeKeywords200Response replaceCampaignNegativeKeywords(campaignId, replaceCampaignNegativeKeywordsRequest)

Replace campaign-level negative keywords

Replaces a Google campaign&#39;s full list of campaign-level negative keywords, or clears it.  Replaces the FULL set of campaign-level negative keywords (C.270): the desired list is diffed against what Google already has, and the difference is applied as one &#x60;create&#x60;/&#x60;remove&#x60; mutate. Send an empty array to clear every campaign negative.  The platform is always discovered from the campaign itself; a non-Google campaign returns 501 rather than 404, whether or not &#x60;platform&#x60; was sent. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        ReplaceCampaignNegativeKeywordsRequest replaceCampaignNegativeKeywordsRequest = new ReplaceCampaignNegativeKeywordsRequest(); // ReplaceCampaignNegativeKeywordsRequest | 
        try {
            ReplaceCampaignNegativeKeywords200Response result = apiInstance.replaceCampaignNegativeKeywords(campaignId, replaceCampaignNegativeKeywordsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#replaceCampaignNegativeKeywords");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Platform campaign ID | |
| **replaceCampaignNegativeKeywordsRequest** | [**ReplaceCampaignNegativeKeywordsRequest**](ReplaceCampaignNegativeKeywordsRequest.md)|  | |

### Return type

[**ReplaceCampaignNegativeKeywords200Response**](ReplaceCampaignNegativeKeywords200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign-level negative keywords replaced |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **404** | Campaign not found |  -  |
| **429** | Google Ads operations budget exhausted; retry later |  -  |
| **501** | Only available on Google Ads campaigns |  -  |

## replaceCampaignNegativeKeywordsWithHttpInfo

> ApiResponse<ReplaceCampaignNegativeKeywords200Response> replaceCampaignNegativeKeywords replaceCampaignNegativeKeywordsWithHttpInfo(campaignId, replaceCampaignNegativeKeywordsRequest)

Replace campaign-level negative keywords

Replaces a Google campaign&#39;s full list of campaign-level negative keywords, or clears it.  Replaces the FULL set of campaign-level negative keywords (C.270): the desired list is diffed against what Google already has, and the difference is applied as one &#x60;create&#x60;/&#x60;remove&#x60; mutate. Send an empty array to clear every campaign negative.  The platform is always discovered from the campaign itself; a non-Google campaign returns 501 rather than 404, whether or not &#x60;platform&#x60; was sent. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        ReplaceCampaignNegativeKeywordsRequest replaceCampaignNegativeKeywordsRequest = new ReplaceCampaignNegativeKeywordsRequest(); // ReplaceCampaignNegativeKeywordsRequest | 
        try {
            ApiResponse<ReplaceCampaignNegativeKeywords200Response> response = apiInstance.replaceCampaignNegativeKeywordsWithHttpInfo(campaignId, replaceCampaignNegativeKeywordsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#replaceCampaignNegativeKeywords");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Platform campaign ID | |
| **replaceCampaignNegativeKeywordsRequest** | [**ReplaceCampaignNegativeKeywordsRequest**](ReplaceCampaignNegativeKeywordsRequest.md)|  | |

### Return type

ApiResponse<[**ReplaceCampaignNegativeKeywords200Response**](ReplaceCampaignNegativeKeywords200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign-level negative keywords replaced |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **404** | Campaign not found |  -  |
| **429** | Google Ads operations budget exhausted; retry later |  -  |
| **501** | Only available on Google Ads campaigns |  -  |


## replaceGoogleListingGroupFilters

> ReplaceGoogleListingGroupFilters200Response replaceGoogleListingGroupFilters(campaignId, assetGroupId, replaceGoogleListingGroupFiltersRequest)

Replace an asset group&#39;s listing-group tree

Replaces the product targeting tree of a Performance Max retail asset group; only works on campaigns linked to Merchant Center.  The current product (listing-group) tree is removed and the new one created in one atomic request. Read the current tree with GET on the asset group.  - Requires a campaign linked to Merchant Center. Other campaigns return 400 LISTING_SOURCE_NOT_ALLOWED from Google. - validateOnly: true validates without writing. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Google Ads campaign id.
        String assetGroupId = "assetGroupId_example"; // String | Google asset group id.
        ReplaceGoogleListingGroupFiltersRequest replaceGoogleListingGroupFiltersRequest = new ReplaceGoogleListingGroupFiltersRequest(); // ReplaceGoogleListingGroupFiltersRequest | 
        try {
            ReplaceGoogleListingGroupFilters200Response result = apiInstance.replaceGoogleListingGroupFilters(campaignId, assetGroupId, replaceGoogleListingGroupFiltersRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#replaceGoogleListingGroupFilters");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Google Ads campaign id. | |
| **assetGroupId** | **String**| Google asset group id. | |
| **replaceGoogleListingGroupFiltersRequest** | [**ReplaceGoogleListingGroupFiltersRequest**](ReplaceGoogleListingGroupFiltersRequest.md)|  | |

### Return type

[**ReplaceGoogleListingGroupFilters200Response**](ReplaceGoogleListingGroupFilters200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tree replaced (or validated). |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **404** | Resource not found |  -  |
| **422** | Google Ads connection needs reconnecting. |  -  |
| **429** | Google quota or the Zernio Google operations burst limit is exhausted. |  -  |
| **501** | Campaign is not on Google Ads. |  -  |

## replaceGoogleListingGroupFiltersWithHttpInfo

> ApiResponse<ReplaceGoogleListingGroupFilters200Response> replaceGoogleListingGroupFilters replaceGoogleListingGroupFiltersWithHttpInfo(campaignId, assetGroupId, replaceGoogleListingGroupFiltersRequest)

Replace an asset group&#39;s listing-group tree

Replaces the product targeting tree of a Performance Max retail asset group; only works on campaigns linked to Merchant Center.  The current product (listing-group) tree is removed and the new one created in one atomic request. Read the current tree with GET on the asset group.  - Requires a campaign linked to Merchant Center. Other campaigns return 400 LISTING_SOURCE_NOT_ALLOWED from Google. - validateOnly: true validates without writing. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Google Ads campaign id.
        String assetGroupId = "assetGroupId_example"; // String | Google asset group id.
        ReplaceGoogleListingGroupFiltersRequest replaceGoogleListingGroupFiltersRequest = new ReplaceGoogleListingGroupFiltersRequest(); // ReplaceGoogleListingGroupFiltersRequest | 
        try {
            ApiResponse<ReplaceGoogleListingGroupFilters200Response> response = apiInstance.replaceGoogleListingGroupFiltersWithHttpInfo(campaignId, assetGroupId, replaceGoogleListingGroupFiltersRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#replaceGoogleListingGroupFilters");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Google Ads campaign id. | |
| **assetGroupId** | **String**| Google asset group id. | |
| **replaceGoogleListingGroupFiltersRequest** | [**ReplaceGoogleListingGroupFiltersRequest**](ReplaceGoogleListingGroupFiltersRequest.md)|  | |

### Return type

ApiResponse<[**ReplaceGoogleListingGroupFilters200Response**](ReplaceGoogleListingGroupFilters200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tree replaced (or validated). |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **404** | Resource not found |  -  |
| **422** | Google Ads connection needs reconnecting. |  -  |
| **429** | Google quota or the Zernio Google operations burst limit is exhausted. |  -  |
| **501** | Campaign is not on Google Ads. |  -  |


## updateAd

> UpdateAd200Response updateAd(adId, updateAdRequest)

Update ad

Changes an ad&#39;s status, budget, targeting or creative and applies the change on the platform.  Patch one or more fields on an ad. Status, budget, targeting, and creative changes are propagated to the platform.  ### Per-platform support  - **Meta** (Facebook + Instagram): all fields supported. - **TikTok**: status, budget, &#x60;name&#x60; (renames the ad), targeting (via &#x60;/v2/adgroup/update/&#x60;), and creative (via &#x60;/v2/ad/update/&#x60; patch-style: &#x60;headline&#x60; is ignored, &#x60;body&#x60; becomes &#x60;ad_text&#x60;). - **Google**: see the Google sections below. - **LinkedIn**: status, budget, targeting and creative (details below). - **Pinterest / X / OpenAI Ads**: status + budget only. Sending &#x60;targeting&#x60; or &#x60;creative&#x60; returns 501 with code &#x60;feature_not_available&#x60;. OpenAI Ads budget is the campaign&#39;s spend cap, daily or lifetime (see &#x60;budget.type&#x60; below). - **Reddit Ads**: status, budget, &#x60;name&#x60; (renames the ad) and targeting (details below).  ### Google  Supported: status, budget, and these targeting edits:  - KEYWORD edits via &#x60;targeting.keywords&#x60; / &#x60;targeting.negativeKeywords&#x60; - DEVICE bid adjustments via &#x60;targeting.devices&#x60; - LOCATION edits via &#x60;targeting.locations&#x60; (or the equivalent top-level &#x60;targeting.countries&#x60; / &#x60;regions&#x60; / &#x60;cities&#x60; / &#x60;zips&#x60; / &#x60;metros&#x60;) - LANGUAGE edits via &#x60;targeting.languages&#x60;  Each list you send becomes the FULL new set of its kind: criteria not in the list are removed. Devices are the exception: Google cannot remove them, so they are switched off with a bid modifier of 0 instead. A kind left out is untouched.  Any other &#x60;targeting&#x60; field returns 400: Google cannot mutate it post-create without recreating the campaign.  Creative edits are dispatched on the ad&#39;s &#x60;advertisingChannelType&#x60;. Every supported field replaces a whole set; a field you omit is preserved.  - **Search**: top-level &#x60;headlines&#x60;, &#x60;descriptions&#x60; and &#x60;finalUrls&#x60;. Use 3-15 headlines (1-30 characters) and 2-4 descriptions (1-90 characters). Omit an asset to remove it; omit pinnedField on an included asset to unpin it. Updates do not pad or truncate text. The legacy creative fields remain unsupported. - **Display**: top-level &#x60;headlines&#x60; (1-5, no pinnedField, display ads have no pinned positions), &#x60;descriptions&#x60; (1-5) and &#x60;finalUrls&#x60;, plus &#x60;creative.longHeadline&#x60;, &#x60;creative.businessName&#x60;, &#x60;creative.imageUrl&#x60; (the landscape marketing image) and &#x60;creative.squareImageUrl&#x60;. - **Performance Max**: top-level &#x60;assetGroup&#x60;, which swaps asset roles on the ad&#39;s asset group. The other creative fields return 422 for this channel, and &#x60;assetGroup&#x60; returns 422 on any other channel. - **Demand Gen**: top-level &#x60;demandGen&#x60; (see GoogleDemandGenUpdate): creative, channel and audience changes in one atomic Google request. The other creative fields return 422 for this channel.  For Display, each image URL is uploaded as a new Google asset and the ad is pointed at it.  Google assets are immutable, so the previous asset stays in the account&#39;s asset library. A new landscape image also updates &#x60;creative.assetResourceName&#x60; to the new asset, and each replaced image updates its own role in &#x60;creative.assets&#x60;.  For Demand Gen, &#x60;targeting&#x60; takes locations, languages, &#x60;locationTargetingType&#x60; and &#x60;devices&#x60;. Locations and languages are written to the ad&#39;s ad group, which Demand Gen requires, so they apply to every ad in that ad group. Campaigns migrated from Discovery that still target on the campaign keep being written there.  ### LinkedIn  - **Status and budget**: supported. - **Targeting**: countries or regions, excludedLocations (countries), the B2B facets, and audience segments. Applied to the LinkedIn Campaign via PARTIAL_UPDATE, and REPLACES the campaign&#39;s entire targetingCriteria, not a merge. - **Creative**: uploads new media, creates a replacement inline creative on the same campaign, and pauses the old one.  ### Reddit Ads  - &#x60;budget&#x60; goes to the ad&#39;s ad group, or to its campaign when the ad group spends a campaign budget. It keeps its daily or lifetime type (422 to switch). - &#x60;targeting&#x60; REPLACES the ad group&#39;s whole targeting (geo, communities, conversation keywords, interests, audiences, languages, gender), so it applies to every ad in the ad group. - &#x60;creative&#x60; returns 501: a Reddit ad runs a post, so create a new ad with the new creative instead.  ### Google location and language replacement  Locations, languages and devices are campaign-level criteria on Google, so these edits apply to every ad group and ad in the ad&#39;s campaign. Send the complete list you want to keep.  Zernio diffs it against the campaign&#39;s live criteria and sends the removes and the creates in ONE &#x60;googleAds:mutate&#x60;, so the campaign is never left with a half-applied set. Criteria already in the list keep their criterion ID and history. Excluded (negative) locations are left untouched.  - An empty location list returns 400. A Google campaign with no location criteria targets every country, which is never what \&quot;remove my locations\&quot; means, so omit the field instead. - Send either &#x60;targeting.locations&#x60; or the top-level geo fields, not both: mixing them returns 400.  ### Google radius targeting  &#x60;customLocations&#x60; is editable and is replaced the same way, but as its OWN set. Google models a place (LOCATION) and a point plus radius (PROXIMITY) as different criterion types, so the two are independent:  - Sending &#x60;customLocations&#x60; replaces every radius and leaves the cities and countries alone. - Sending places replaces those and leaves the radius alone. - Send &#x60;customLocations: []&#x60; to drop radius targeting entirely.  A circle you re-send unchanged keeps its criterion ID rather than being removed and recreated.  ### Google keyword replacement  These edits affect the ad&#39;s entire ad group, including sibling ads. Positive (&#x60;targeting.keywords&#x60;) and negative (&#x60;targeting.negativeKeywords&#x60;) sets are independent: omit a field to leave that set unchanged, or send &#x60;[]&#x60; to remove every keyword of that kind.  Zernio compares each supplied set with Google&#39;s live criteria by case-insensitive keyword text and match type. Text comparison does not trim whitespace.  A matching criterion is left untouched, retaining its criterion ID, enabled/paused status, keyword-level bid overrides, labels, and criterion-associated history/statistics. Zernio does not reset its quality score; Google continues to calculate scores and statistics normally.  A bare string or an object without &#x60;matchType&#x60; means &#x60;broad&#x60;, not the existing criterion&#39;s match type. For example, resending an existing &#x60;{ \&quot;text\&quot;: \&quot;plumber\&quot;, \&quot;matchType\&quot;: \&quot;exact\&quot; }&#x60; preserves it; sending &#x60;\&quot;plumber\&quot;&#x60; instead removes that EXACT criterion and requests a BROAD one.  Changing text or match type removes criteria no longer requested and creates any missing criteria. New criteria get new IDs and do not inherit removed criteria&#39;s bid overrides, labels, or history. Historical reporting for a removed criterion is not transferred to its replacement.  ### Other keyword endpoints  - To add keywords without replacing a set, use [POST /v1/ads/keywords](https://docs.zernio.com/ad-campaigns/add-ad-keywords). - Use &#x60;PATCH /v1/ads/keywords/{keywordId}&#x60; to pause/enable one keyword. - Use &#x60;DELETE /v1/ads/keywords/{keywordId}&#x60; to remove it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adId = "adId_example"; // String | 
        UpdateAdRequest updateAdRequest = new UpdateAdRequest(); // UpdateAdRequest | 
        try {
            UpdateAd200Response result = apiInstance.updateAd(adId, updateAdRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAd");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adId** | **String**|  | |
| **updateAdRequest** | [**UpdateAdRequest**](UpdateAdRequest.md)|  | |

### Return type

[**UpdateAd200Response**](UpdateAd200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad updated |  -  |
| **400** | Invalid update. Causes:  - Invalid status transition, or budget below minimum. - A LinkedIn creative update without imageUrl or videoUrl, or a LinkedIn targeting update without countries or regions. - A Google targeting update that is unsupported, empty, mixes locations with the top-level geo fields, or names an unknown country or language code. - Code &#x60;missing_required_field&#x60;: the body has none of the updatable fields (status, budget, targeting, name, creative, headlines, descriptions, finalUrls, assetGroup, demandGen), e.g. &#x60;{}&#x60; or only misspelled keys. Unknown keys are ignored, so such a body would otherwise change nothing.  |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Returned with one of these codes:  - &#x60;ads_allowance_exceeded&#x60;: the team has no payment method on file and has reached the 500 free live ads. Add a card to resume. - &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix &#x60;ad_account_not_selected&#x60;, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | Resource not found |  -  |
| **429** | Meta admits one write per 30 seconds to a metered object, ad creatives above all. Zernio waits out two of those windows and replays the call before surfacing this, so it only appears when the object is being edited faster than that. Retry in 30 seconds. |  -  |
| **422** | The edit cannot be applied. One of:  - The ad has no campaign or ad group on the platform yet. - The Google targeting edit asks for something that is create-only (&#x60;locations.customLocations&#x60;). - A creative field the ad&#39;s channel cannot carry: assetGroup on a non-Performance-Max ad, a Google Display field on a Search ad, a pinnedField on a Display headline, or any Google-only field on another platform. - A Google creative edit cannot reach Google at all (the ad has no &#x60;platformAdId&#x60;, or its ad account cannot be loaded). This returns 422 rather than a 200 that changed nothing. |  -  |
| **501** | targeting or creative not supported on the platform (supported on Meta, TikTok, and LinkedIn) |  -  |
| **502** | Meta accepted the request then failed to produce the media (upload session, chunk transfer, processing timeout, or a response with no image hash). Inspect &#x60;platformError.reason&#x60;. Also returned with code &#x60;platform_api_error&#x60; when a Meta or LinkedIn targeting update cannot read the current targeting: nothing is written, so retry the request. |  -  |

## updateAdWithHttpInfo

> ApiResponse<UpdateAd200Response> updateAd updateAdWithHttpInfo(adId, updateAdRequest)

Update ad

Changes an ad&#39;s status, budget, targeting or creative and applies the change on the platform.  Patch one or more fields on an ad. Status, budget, targeting, and creative changes are propagated to the platform.  ### Per-platform support  - **Meta** (Facebook + Instagram): all fields supported. - **TikTok**: status, budget, &#x60;name&#x60; (renames the ad), targeting (via &#x60;/v2/adgroup/update/&#x60;), and creative (via &#x60;/v2/ad/update/&#x60; patch-style: &#x60;headline&#x60; is ignored, &#x60;body&#x60; becomes &#x60;ad_text&#x60;). - **Google**: see the Google sections below. - **LinkedIn**: status, budget, targeting and creative (details below). - **Pinterest / X / OpenAI Ads**: status + budget only. Sending &#x60;targeting&#x60; or &#x60;creative&#x60; returns 501 with code &#x60;feature_not_available&#x60;. OpenAI Ads budget is the campaign&#39;s spend cap, daily or lifetime (see &#x60;budget.type&#x60; below). - **Reddit Ads**: status, budget, &#x60;name&#x60; (renames the ad) and targeting (details below).  ### Google  Supported: status, budget, and these targeting edits:  - KEYWORD edits via &#x60;targeting.keywords&#x60; / &#x60;targeting.negativeKeywords&#x60; - DEVICE bid adjustments via &#x60;targeting.devices&#x60; - LOCATION edits via &#x60;targeting.locations&#x60; (or the equivalent top-level &#x60;targeting.countries&#x60; / &#x60;regions&#x60; / &#x60;cities&#x60; / &#x60;zips&#x60; / &#x60;metros&#x60;) - LANGUAGE edits via &#x60;targeting.languages&#x60;  Each list you send becomes the FULL new set of its kind: criteria not in the list are removed. Devices are the exception: Google cannot remove them, so they are switched off with a bid modifier of 0 instead. A kind left out is untouched.  Any other &#x60;targeting&#x60; field returns 400: Google cannot mutate it post-create without recreating the campaign.  Creative edits are dispatched on the ad&#39;s &#x60;advertisingChannelType&#x60;. Every supported field replaces a whole set; a field you omit is preserved.  - **Search**: top-level &#x60;headlines&#x60;, &#x60;descriptions&#x60; and &#x60;finalUrls&#x60;. Use 3-15 headlines (1-30 characters) and 2-4 descriptions (1-90 characters). Omit an asset to remove it; omit pinnedField on an included asset to unpin it. Updates do not pad or truncate text. The legacy creative fields remain unsupported. - **Display**: top-level &#x60;headlines&#x60; (1-5, no pinnedField, display ads have no pinned positions), &#x60;descriptions&#x60; (1-5) and &#x60;finalUrls&#x60;, plus &#x60;creative.longHeadline&#x60;, &#x60;creative.businessName&#x60;, &#x60;creative.imageUrl&#x60; (the landscape marketing image) and &#x60;creative.squareImageUrl&#x60;. - **Performance Max**: top-level &#x60;assetGroup&#x60;, which swaps asset roles on the ad&#39;s asset group. The other creative fields return 422 for this channel, and &#x60;assetGroup&#x60; returns 422 on any other channel. - **Demand Gen**: top-level &#x60;demandGen&#x60; (see GoogleDemandGenUpdate): creative, channel and audience changes in one atomic Google request. The other creative fields return 422 for this channel.  For Display, each image URL is uploaded as a new Google asset and the ad is pointed at it.  Google assets are immutable, so the previous asset stays in the account&#39;s asset library. A new landscape image also updates &#x60;creative.assetResourceName&#x60; to the new asset, and each replaced image updates its own role in &#x60;creative.assets&#x60;.  For Demand Gen, &#x60;targeting&#x60; takes locations, languages, &#x60;locationTargetingType&#x60; and &#x60;devices&#x60;. Locations and languages are written to the ad&#39;s ad group, which Demand Gen requires, so they apply to every ad in that ad group. Campaigns migrated from Discovery that still target on the campaign keep being written there.  ### LinkedIn  - **Status and budget**: supported. - **Targeting**: countries or regions, excludedLocations (countries), the B2B facets, and audience segments. Applied to the LinkedIn Campaign via PARTIAL_UPDATE, and REPLACES the campaign&#39;s entire targetingCriteria, not a merge. - **Creative**: uploads new media, creates a replacement inline creative on the same campaign, and pauses the old one.  ### Reddit Ads  - &#x60;budget&#x60; goes to the ad&#39;s ad group, or to its campaign when the ad group spends a campaign budget. It keeps its daily or lifetime type (422 to switch). - &#x60;targeting&#x60; REPLACES the ad group&#39;s whole targeting (geo, communities, conversation keywords, interests, audiences, languages, gender), so it applies to every ad in the ad group. - &#x60;creative&#x60; returns 501: a Reddit ad runs a post, so create a new ad with the new creative instead.  ### Google location and language replacement  Locations, languages and devices are campaign-level criteria on Google, so these edits apply to every ad group and ad in the ad&#39;s campaign. Send the complete list you want to keep.  Zernio diffs it against the campaign&#39;s live criteria and sends the removes and the creates in ONE &#x60;googleAds:mutate&#x60;, so the campaign is never left with a half-applied set. Criteria already in the list keep their criterion ID and history. Excluded (negative) locations are left untouched.  - An empty location list returns 400. A Google campaign with no location criteria targets every country, which is never what \&quot;remove my locations\&quot; means, so omit the field instead. - Send either &#x60;targeting.locations&#x60; or the top-level geo fields, not both: mixing them returns 400.  ### Google radius targeting  &#x60;customLocations&#x60; is editable and is replaced the same way, but as its OWN set. Google models a place (LOCATION) and a point plus radius (PROXIMITY) as different criterion types, so the two are independent:  - Sending &#x60;customLocations&#x60; replaces every radius and leaves the cities and countries alone. - Sending places replaces those and leaves the radius alone. - Send &#x60;customLocations: []&#x60; to drop radius targeting entirely.  A circle you re-send unchanged keeps its criterion ID rather than being removed and recreated.  ### Google keyword replacement  These edits affect the ad&#39;s entire ad group, including sibling ads. Positive (&#x60;targeting.keywords&#x60;) and negative (&#x60;targeting.negativeKeywords&#x60;) sets are independent: omit a field to leave that set unchanged, or send &#x60;[]&#x60; to remove every keyword of that kind.  Zernio compares each supplied set with Google&#39;s live criteria by case-insensitive keyword text and match type. Text comparison does not trim whitespace.  A matching criterion is left untouched, retaining its criterion ID, enabled/paused status, keyword-level bid overrides, labels, and criterion-associated history/statistics. Zernio does not reset its quality score; Google continues to calculate scores and statistics normally.  A bare string or an object without &#x60;matchType&#x60; means &#x60;broad&#x60;, not the existing criterion&#39;s match type. For example, resending an existing &#x60;{ \&quot;text\&quot;: \&quot;plumber\&quot;, \&quot;matchType\&quot;: \&quot;exact\&quot; }&#x60; preserves it; sending &#x60;\&quot;plumber\&quot;&#x60; instead removes that EXACT criterion and requests a BROAD one.  Changing text or match type removes criteria no longer requested and creates any missing criteria. New criteria get new IDs and do not inherit removed criteria&#39;s bid overrides, labels, or history. Historical reporting for a removed criterion is not transferred to its replacement.  ### Other keyword endpoints  - To add keywords without replacing a set, use [POST /v1/ads/keywords](https://docs.zernio.com/ad-campaigns/add-ad-keywords). - Use &#x60;PATCH /v1/ads/keywords/{keywordId}&#x60; to pause/enable one keyword. - Use &#x60;DELETE /v1/ads/keywords/{keywordId}&#x60; to remove it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adId = "adId_example"; // String | 
        UpdateAdRequest updateAdRequest = new UpdateAdRequest(); // UpdateAdRequest | 
        try {
            ApiResponse<UpdateAd200Response> response = apiInstance.updateAdWithHttpInfo(adId, updateAdRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAd");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adId** | **String**|  | |
| **updateAdRequest** | [**UpdateAdRequest**](UpdateAdRequest.md)|  | |

### Return type

ApiResponse<[**UpdateAd200Response**](UpdateAd200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad updated |  -  |
| **400** | Invalid update. Causes:  - Invalid status transition, or budget below minimum. - A LinkedIn creative update without imageUrl or videoUrl, or a LinkedIn targeting update without countries or regions. - A Google targeting update that is unsupported, empty, mixes locations with the top-level geo fields, or names an unknown country or language code. - Code &#x60;missing_required_field&#x60;: the body has none of the updatable fields (status, budget, targeting, name, creative, headlines, descriptions, finalUrls, assetGroup, demandGen), e.g. &#x60;{}&#x60; or only misspelled keys. Unknown keys are ignored, so such a body would otherwise change nothing.  |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Returned with one of these codes:  - &#x60;ads_allowance_exceeded&#x60;: the team has no payment method on file and has reached the 500 free live ads. Add a card to resume. - &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix &#x60;ad_account_not_selected&#x60;, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | Resource not found |  -  |
| **429** | Meta admits one write per 30 seconds to a metered object, ad creatives above all. Zernio waits out two of those windows and replays the call before surfacing this, so it only appears when the object is being edited faster than that. Retry in 30 seconds. |  -  |
| **422** | The edit cannot be applied. One of:  - The ad has no campaign or ad group on the platform yet. - The Google targeting edit asks for something that is create-only (&#x60;locations.customLocations&#x60;). - A creative field the ad&#39;s channel cannot carry: assetGroup on a non-Performance-Max ad, a Google Display field on a Search ad, a pinnedField on a Display headline, or any Google-only field on another platform. - A Google creative edit cannot reach Google at all (the ad has no &#x60;platformAdId&#x60;, or its ad account cannot be loaded). This returns 422 rather than a 200 that changed nothing. |  -  |
| **501** | targeting or creative not supported on the platform (supported on Meta, TikTok, and LinkedIn) |  -  |
| **502** | Meta accepted the request then failed to produce the media (upload session, chunk transfer, processing timeout, or a response with no image hash). Inspect &#x60;platformError.reason&#x60;. Also returned with code &#x60;platform_api_error&#x60; when a Meta or LinkedIn targeting update cannot read the current targeting: nothing is written, so retry the request. |  -  |


## updateAdCampaign

> UpdateAdCampaign200Response updateAdCampaign(campaignId, updateAdCampaignRequest)

Update a campaign

Changes a campaign&#39;s settings, such as its name, budget, bidding or tracking URLs.  Send at least one of &#x60;budget&#x60;, &#x60;bidStrategy&#x60;, &#x60;portfolioBidStrategyId&#x60;, &#x60;targetImpressionShare&#x60;, &#x60;manualCpc&#x60;, &#x60;networkSettings&#x60;, &#x60;trackingUrlTemplate&#x60;, &#x60;finalUrlSuffix&#x60;, &#x60;sharedBudgetId&#x60;, &#x60;name&#x60; or &#x60;platformSpecificData&#x60;. An unsupported field is always an error, never a silent drop.  | Body field | Meta | Google | Others | |---|---|---|---| | &#x60;bidStrategy&#x60; | Yes | Yes | 501 | | &#x60;bidAmount&#x60;, &#x60;roasAverageFloor&#x60; | 400 (ad-set level) | Yes | 400 | | &#x60;portfolioBidStrategyId&#x60; | 400 | Yes | 400 | | &#x60;targetImpressionShare&#x60; | 400 | Search only | 400 | | &#x60;manualCpc&#x60; | 400 | Search and Display | 400 | | &#x60;networkSettings&#x60; | 400 | Search only | 400 | | &#x60;trackingUrlTemplate&#x60;, &#x60;finalUrlSuffix&#x60; | 400 | Yes | 400 | | &#x60;sharedBudgetId&#x60; | 400 | Yes | 400 | | &#x60;budget&#x60; (CBO; ABO returns 409) | Yes | Daily only | OpenAI and Reddit: daily or lifetime; others 501 | | &#x60;name&#x60; | Yes | 501 | Reddit: Yes; others 501 | | &#x60;platformSpecificData.spendCap&#x60; | Yes | 400 | 400 | | &#x60;accountId&#x60; (empty campaigns) | Yes | - | - |  ### Meta  Meta budget edits check the live campaign budget, so an older local ABO stamp cannot block a CBO campaign. A successful edit repairs local ad budget fields. A live ABO campaign still returns 409 with the ad-set budget endpoint.  &#x60;accountId&#x60; forwards the update straight to Meta for a campaign with zero ads, which would otherwise 404. The response then carries &#x60;updated: 0&#x60;.  ### Google bidding  - &#x60;LOWEST_COST_WITHOUT_CAP&#x60; &#x3D; Maximize Conversions - &#x60;COST_CAP&#x60; + &#x60;bidAmount&#x60; &#x3D; Target CPA - &#x60;LOWEST_COST_WITH_MIN_ROAS&#x60; + &#x60;roasAverageFloor&#x60; &#x3D; Target ROAS - &#x60;LOWEST_COST_WITH_BID_CAP&#x60; + &#x60;bidAmount&#x60; &#x3D; Maximize Clicks with a CPC ceiling - &#x60;portfolioBidStrategyId&#x60; attaches a portfolio strategy instead (exclusive with &#x60;bidStrategy&#x60;) - &#x60;targetImpressionShare&#x60; switches the campaign to Target impression share - &#x60;manualCpc: { maxCpc }&#x60; switches to Manual CPC: every ad group of the campaign gets &#x60;maxCpc&#x60; as its bid, in the same mutate  &#x60;targetImpressionShare&#x60; and &#x60;manualCpc&#x60; are each exclusive with every other strategy field.  Setting the standard triplet on a campaign that is currently on a PORTFOLIO strategy is rejected. Detach it in Google Ads first, since it is shared across campaigns.  ### Google network and tracking URLs  &#x60;networkSettings&#x60;, &#x60;trackingUrlTemplate&#x60; and &#x60;finalUrlSuffix&#x60; go out in one campaign update. Each field is sent written on its own leaf, so an omitted one keeps its current value. An empty string clears a URL field.  ### Google budgets  Google budget updates read the current budget before mutation. Shared budgets return 409 unless allowSharedBudgetUpdate&#x3D;true is explicitly supplied, because the change affects every campaign using that budget.  A budget counts as shared when Google flags it as shared or when more than one campaign uses it (older budgets can serve several campaigns without the flag). Unknown sharing state also returns 409.  ### Google shared budgets (&#x60;sharedBudgetId&#x60;)  - &#x60;sharedBudgetId&#x60; moves the campaign onto a shared budget from GET /v1/ads/shared-budgets. It also needs &#x60;allowSharedBudgetUpdate: true&#x60; (409 otherwise), because the campaign then splits that budget with every campaign on it. &#x60;budget&#x60; cannot ride along. - &#x60;sharedBudgetId: null&#x60; moves it back onto a new budget of its own, sized by &#x60;budget&#x60; (required, daily). The new budget and the switch go out in one atomic Google mutate. - A campaign that already has its own budget returns 409 for null.  The budget a campaign leaves is not removed. The response carries the budget the campaign now uses.  ### OpenAI Ads  Campaigns carry exactly one spend cap. &#x60;budget.type&#x60; daily or lifetime replaces whichever cap the campaign had, with a minimum of 1 in the ad account&#39;s currency (422 below it).  Lifetime can switch to daily, but OpenAI never switches a daily cap back to lifetime (422).  ### Reddit Ads  - &#x60;budget&#x60; changes the amount of a campaign budget (Reddit campaign budget optimization). - A campaign whose ad groups carry the budget returns 409 or 422; use PUT /v1/ads/ad-sets/{adSetId} there. - Reddit cannot switch a published budget between daily and lifetime, so &#x60;budget.type&#x60; must match the current one (422 otherwise). - &#x60;bidStrategy&#x60; is set per ad group on Reddit (PUT /v1/ads/ad-sets/{adSetId}). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        UpdateAdCampaignRequest updateAdCampaignRequest = new UpdateAdCampaignRequest(); // UpdateAdCampaignRequest | 
        try {
            UpdateAdCampaign200Response result = apiInstance.updateAdCampaign(campaignId, updateAdCampaignRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdCampaign");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Platform campaign ID | |
| **updateAdCampaignRequest** | [**UpdateAdCampaignRequest**](UpdateAdCampaignRequest.md)|  | |

### Return type

[**UpdateAdCampaign200Response**](UpdateAdCampaign200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign updated |  -  |
| **400** | Invalid input, or a field the resolved platform does not support at the campaign level (see the support table) |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Returned with these codes:  - &#x60;ads_allowance_exceeded&#x60;: the team has no payment method on file and has reached the 500 free live ads. Add a card to resume. - &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;. - &#x60;ad_account_not_selected&#x60; fix: add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection), or use a connection that has it selected.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | Meta campaign is ABO, or the Google budget is shared without allowSharedBudgetUpdate&#x3D;true, or sharing state cannot be verified. The account may also be inactive or need reconnection (code ads_connection_required). Reconnect it and read GET /v1/accounts for its current ID before retrying. |  -  |
| **501** | Operation not supported on this platform |  -  |

## updateAdCampaignWithHttpInfo

> ApiResponse<UpdateAdCampaign200Response> updateAdCampaign updateAdCampaignWithHttpInfo(campaignId, updateAdCampaignRequest)

Update a campaign

Changes a campaign&#39;s settings, such as its name, budget, bidding or tracking URLs.  Send at least one of &#x60;budget&#x60;, &#x60;bidStrategy&#x60;, &#x60;portfolioBidStrategyId&#x60;, &#x60;targetImpressionShare&#x60;, &#x60;manualCpc&#x60;, &#x60;networkSettings&#x60;, &#x60;trackingUrlTemplate&#x60;, &#x60;finalUrlSuffix&#x60;, &#x60;sharedBudgetId&#x60;, &#x60;name&#x60; or &#x60;platformSpecificData&#x60;. An unsupported field is always an error, never a silent drop.  | Body field | Meta | Google | Others | |---|---|---|---| | &#x60;bidStrategy&#x60; | Yes | Yes | 501 | | &#x60;bidAmount&#x60;, &#x60;roasAverageFloor&#x60; | 400 (ad-set level) | Yes | 400 | | &#x60;portfolioBidStrategyId&#x60; | 400 | Yes | 400 | | &#x60;targetImpressionShare&#x60; | 400 | Search only | 400 | | &#x60;manualCpc&#x60; | 400 | Search and Display | 400 | | &#x60;networkSettings&#x60; | 400 | Search only | 400 | | &#x60;trackingUrlTemplate&#x60;, &#x60;finalUrlSuffix&#x60; | 400 | Yes | 400 | | &#x60;sharedBudgetId&#x60; | 400 | Yes | 400 | | &#x60;budget&#x60; (CBO; ABO returns 409) | Yes | Daily only | OpenAI and Reddit: daily or lifetime; others 501 | | &#x60;name&#x60; | Yes | 501 | Reddit: Yes; others 501 | | &#x60;platformSpecificData.spendCap&#x60; | Yes | 400 | 400 | | &#x60;accountId&#x60; (empty campaigns) | Yes | - | - |  ### Meta  Meta budget edits check the live campaign budget, so an older local ABO stamp cannot block a CBO campaign. A successful edit repairs local ad budget fields. A live ABO campaign still returns 409 with the ad-set budget endpoint.  &#x60;accountId&#x60; forwards the update straight to Meta for a campaign with zero ads, which would otherwise 404. The response then carries &#x60;updated: 0&#x60;.  ### Google bidding  - &#x60;LOWEST_COST_WITHOUT_CAP&#x60; &#x3D; Maximize Conversions - &#x60;COST_CAP&#x60; + &#x60;bidAmount&#x60; &#x3D; Target CPA - &#x60;LOWEST_COST_WITH_MIN_ROAS&#x60; + &#x60;roasAverageFloor&#x60; &#x3D; Target ROAS - &#x60;LOWEST_COST_WITH_BID_CAP&#x60; + &#x60;bidAmount&#x60; &#x3D; Maximize Clicks with a CPC ceiling - &#x60;portfolioBidStrategyId&#x60; attaches a portfolio strategy instead (exclusive with &#x60;bidStrategy&#x60;) - &#x60;targetImpressionShare&#x60; switches the campaign to Target impression share - &#x60;manualCpc: { maxCpc }&#x60; switches to Manual CPC: every ad group of the campaign gets &#x60;maxCpc&#x60; as its bid, in the same mutate  &#x60;targetImpressionShare&#x60; and &#x60;manualCpc&#x60; are each exclusive with every other strategy field.  Setting the standard triplet on a campaign that is currently on a PORTFOLIO strategy is rejected. Detach it in Google Ads first, since it is shared across campaigns.  ### Google network and tracking URLs  &#x60;networkSettings&#x60;, &#x60;trackingUrlTemplate&#x60; and &#x60;finalUrlSuffix&#x60; go out in one campaign update. Each field is sent written on its own leaf, so an omitted one keeps its current value. An empty string clears a URL field.  ### Google budgets  Google budget updates read the current budget before mutation. Shared budgets return 409 unless allowSharedBudgetUpdate&#x3D;true is explicitly supplied, because the change affects every campaign using that budget.  A budget counts as shared when Google flags it as shared or when more than one campaign uses it (older budgets can serve several campaigns without the flag). Unknown sharing state also returns 409.  ### Google shared budgets (&#x60;sharedBudgetId&#x60;)  - &#x60;sharedBudgetId&#x60; moves the campaign onto a shared budget from GET /v1/ads/shared-budgets. It also needs &#x60;allowSharedBudgetUpdate: true&#x60; (409 otherwise), because the campaign then splits that budget with every campaign on it. &#x60;budget&#x60; cannot ride along. - &#x60;sharedBudgetId: null&#x60; moves it back onto a new budget of its own, sized by &#x60;budget&#x60; (required, daily). The new budget and the switch go out in one atomic Google mutate. - A campaign that already has its own budget returns 409 for null.  The budget a campaign leaves is not removed. The response carries the budget the campaign now uses.  ### OpenAI Ads  Campaigns carry exactly one spend cap. &#x60;budget.type&#x60; daily or lifetime replaces whichever cap the campaign had, with a minimum of 1 in the ad account&#39;s currency (422 below it).  Lifetime can switch to daily, but OpenAI never switches a daily cap back to lifetime (422).  ### Reddit Ads  - &#x60;budget&#x60; changes the amount of a campaign budget (Reddit campaign budget optimization). - A campaign whose ad groups carry the budget returns 409 or 422; use PUT /v1/ads/ad-sets/{adSetId} there. - Reddit cannot switch a published budget between daily and lifetime, so &#x60;budget.type&#x60; must match the current one (422 otherwise). - &#x60;bidStrategy&#x60; is set per ad group on Reddit (PUT /v1/ads/ad-sets/{adSetId}). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        UpdateAdCampaignRequest updateAdCampaignRequest = new UpdateAdCampaignRequest(); // UpdateAdCampaignRequest | 
        try {
            ApiResponse<UpdateAdCampaign200Response> response = apiInstance.updateAdCampaignWithHttpInfo(campaignId, updateAdCampaignRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdCampaign");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Platform campaign ID | |
| **updateAdCampaignRequest** | [**UpdateAdCampaignRequest**](UpdateAdCampaignRequest.md)|  | |

### Return type

ApiResponse<[**UpdateAdCampaign200Response**](UpdateAdCampaign200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign updated |  -  |
| **400** | Invalid input, or a field the resolved platform does not support at the campaign level (see the support table) |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Returned with these codes:  - &#x60;ads_allowance_exceeded&#x60;: the team has no payment method on file and has reached the 500 free live ads. Add a card to resume. - &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;. - &#x60;ad_account_not_selected&#x60; fix: add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection), or use a connection that has it selected.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **409** | Meta campaign is ABO, or the Google budget is shared without allowSharedBudgetUpdate&#x3D;true, or sharing state cannot be verified. The account may also be inactive or need reconnection (code ads_connection_required). Reconnect it and read GET /v1/accounts for its current ID before retrying. |  -  |
| **501** | Operation not supported on this platform |  -  |


## updateAdCampaignStatus

> UpdateAdCampaignStatus200Response updateAdCampaignStatus(campaignId, updateAdCampaignStatusRequest)

Pause or resume a campaign

Pauses or resumes a campaign, leaving the on/off switches of its ad sets and ads as they are.  It writes the campaign&#39;s own on/off switch and nothing else, on every platform: Meta, TikTok, Google, LinkedIn campaign group, Pinterest, X, ChatGPT (OpenAI).  Its ad sets and ads keep their own switches:  - Pausing stops their delivery through the campaign. - Resuming lets each of them deliver again only if its own switch is on.  An ad set or ad you paused individually stays paused. Resume it with PUT /v1/ads/ad-sets/{adSetId}/status or PUT /v1/ads/{adId}/status. See the Status model in the Ad Campaigns tag.  ### Live read, then write  The campaign&#39;s switch is read from the platform first.  - **Already in the requested state:** nothing is written (&#x60;updated: 0&#x60;, &#x60;skipped: 1&#x60;, with the reason). - **Otherwise:** the switch is written (&#x60;updated: 1&#x60;), read back and stored. The delivery status of the ads under it (up to 20) is re-read and stored, so an immediate GET returns what the platform now reports.  When the campaign delivers in the requested state but some of its ads are stored in the other state, those ads are re-read and stored (up to 20, at most once every 10 minutes per campaign).  An example is ads switched on in the platform&#39;s own UI and still stored &#x60;paused&#x60;.  A stored switch never skips a write, and when the platform cannot be read the write always goes out.  On Meta the check reads the campaign&#39;s own &#x60;status&#x60;, so a delivery status such as &#x60;IN_PROCESS&#x60; or &#x60;WITH_ISSUES&#x60; does not force a write. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        UpdateAdCampaignStatusRequest updateAdCampaignStatusRequest = new UpdateAdCampaignStatusRequest(); // UpdateAdCampaignStatusRequest | 
        try {
            UpdateAdCampaignStatus200Response result = apiInstance.updateAdCampaignStatus(campaignId, updateAdCampaignStatusRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdCampaignStatus");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Platform campaign ID | |
| **updateAdCampaignStatusRequest** | [**UpdateAdCampaignStatusRequest**](UpdateAdCampaignStatusRequest.md)|  | |

### Return type

[**UpdateAdCampaignStatus200Response**](UpdateAdCampaignStatus200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign status updated |  -  |
| **400** | Invalid input or campaign spans multiple accounts |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Forbidden. Two codes:  - &#x60;ads_allowance_exceeded&#x60;: the team has no payment method on file and has reached the 500 free live ads. Add a card to resume. - &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix &#x60;ad_account_not_selected&#x60;, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | No ads found for this campaign |  -  |

## updateAdCampaignStatusWithHttpInfo

> ApiResponse<UpdateAdCampaignStatus200Response> updateAdCampaignStatus updateAdCampaignStatusWithHttpInfo(campaignId, updateAdCampaignStatusRequest)

Pause or resume a campaign

Pauses or resumes a campaign, leaving the on/off switches of its ad sets and ads as they are.  It writes the campaign&#39;s own on/off switch and nothing else, on every platform: Meta, TikTok, Google, LinkedIn campaign group, Pinterest, X, ChatGPT (OpenAI).  Its ad sets and ads keep their own switches:  - Pausing stops their delivery through the campaign. - Resuming lets each of them deliver again only if its own switch is on.  An ad set or ad you paused individually stays paused. Resume it with PUT /v1/ads/ad-sets/{adSetId}/status or PUT /v1/ads/{adId}/status. See the Status model in the Ad Campaigns tag.  ### Live read, then write  The campaign&#39;s switch is read from the platform first.  - **Already in the requested state:** nothing is written (&#x60;updated: 0&#x60;, &#x60;skipped: 1&#x60;, with the reason). - **Otherwise:** the switch is written (&#x60;updated: 1&#x60;), read back and stored. The delivery status of the ads under it (up to 20) is re-read and stored, so an immediate GET returns what the platform now reports.  When the campaign delivers in the requested state but some of its ads are stored in the other state, those ads are re-read and stored (up to 20, at most once every 10 minutes per campaign).  An example is ads switched on in the platform&#39;s own UI and still stored &#x60;paused&#x60;.  A stored switch never skips a write, and when the platform cannot be read the write always goes out.  On Meta the check reads the campaign&#39;s own &#x60;status&#x60;, so a delivery status such as &#x60;IN_PROCESS&#x60; or &#x60;WITH_ISSUES&#x60; does not force a write. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign ID
        UpdateAdCampaignStatusRequest updateAdCampaignStatusRequest = new UpdateAdCampaignStatusRequest(); // UpdateAdCampaignStatusRequest | 
        try {
            ApiResponse<UpdateAdCampaignStatus200Response> response = apiInstance.updateAdCampaignStatusWithHttpInfo(campaignId, updateAdCampaignStatusRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdCampaignStatus");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Platform campaign ID | |
| **updateAdCampaignStatusRequest** | [**UpdateAdCampaignStatusRequest**](UpdateAdCampaignStatusRequest.md)|  | |

### Return type

ApiResponse<[**UpdateAdCampaignStatus200Response**](UpdateAdCampaignStatus200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign status updated |  -  |
| **400** | Invalid input or campaign spans multiple accounts |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Forbidden. Two codes:  - &#x60;ads_allowance_exceeded&#x60;: the team has no payment method on file and has reached the 500 free live ads. Add a card to resume. - &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix &#x60;ad_account_not_selected&#x60;, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | No ads found for this campaign |  -  |


## updateAdGroupAssets

> UpdateCampaignAssets200Response updateAdGroupAssets(adSetId, updateCampaignAssetsRequest)

Update ad-group assets

Edits a Google ad group&#39;s existing assets in place; the change applies everywhere that asset is used.  Send updates with assetResourceName and the fields to change. An asset is shared: changes affect every attachment using it. Omitted fields stay unchanged. The operation consumes the Google operations budget and invalidates affected cached lists. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Numeric Google platform id.
        UpdateCampaignAssetsRequest updateCampaignAssetsRequest = new UpdateCampaignAssetsRequest(); // UpdateCampaignAssetsRequest | 
        try {
            UpdateCampaignAssets200Response result = apiInstance.updateAdGroupAssets(adSetId, updateCampaignAssetsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdGroupAssets");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adSetId** | **String**| Numeric Google platform id. | |
| **updateCampaignAssetsRequest** | [**UpdateCampaignAssetsRequest**](UpdateCampaignAssetsRequest.md)|  | |

### Return type

[**UpdateCampaignAssets200Response**](UpdateCampaignAssets200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Forbidden. One of:  - Ads access is required. - Code &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the ad account this request targets is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix &#x60;ad_account_not_selected&#x60;, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |

## updateAdGroupAssetsWithHttpInfo

> ApiResponse<UpdateCampaignAssets200Response> updateAdGroupAssets updateAdGroupAssetsWithHttpInfo(adSetId, updateCampaignAssetsRequest)

Update ad-group assets

Edits a Google ad group&#39;s existing assets in place; the change applies everywhere that asset is used.  Send updates with assetResourceName and the fields to change. An asset is shared: changes affect every attachment using it. Omitted fields stay unchanged. The operation consumes the Google operations budget and invalidates affected cached lists. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Numeric Google platform id.
        UpdateCampaignAssetsRequest updateCampaignAssetsRequest = new UpdateCampaignAssetsRequest(); // UpdateCampaignAssetsRequest | 
        try {
            ApiResponse<UpdateCampaignAssets200Response> response = apiInstance.updateAdGroupAssetsWithHttpInfo(adSetId, updateCampaignAssetsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdGroupAssets");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adSetId** | **String**| Numeric Google platform id. | |
| **updateCampaignAssetsRequest** | [**UpdateCampaignAssetsRequest**](UpdateCampaignAssetsRequest.md)|  | |

### Return type

ApiResponse<[**UpdateCampaignAssets200Response**](UpdateCampaignAssets200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Forbidden. One of:  - Ads access is required. - Code &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the ad account this request targets is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix &#x60;ad_account_not_selected&#x60;, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |


## updateAdKeyword

> UpdateAdKeyword200Response updateAdKeyword(keywordId, updateAdKeywordRequest)

Pause or enable a Search keyword

Pauses or re-enables a single Google Search keyword.  Changes &#x60;ad_group_criterion.status&#x60; for one keyword criterion (M.140). Negative keywords have no status on Google and cannot be paused or enabled. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String keywordId = "keywordId_example"; // String | Zernio keyword ID (`id`), or Google's native `{adSetId}~{platformCriterionId}` (the tail of `resourceName`, e.g. 1234567890~987654321). A bare criterion id is rejected because it is only unique within its ad group.
        UpdateAdKeywordRequest updateAdKeywordRequest = new UpdateAdKeywordRequest(); // UpdateAdKeywordRequest | 
        try {
            UpdateAdKeyword200Response result = apiInstance.updateAdKeyword(keywordId, updateAdKeywordRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdKeyword");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **keywordId** | **String**| Zernio keyword ID (&#x60;id&#x60;), or Google&#39;s native &#x60;{adSetId}~{platformCriterionId}&#x60; (the tail of &#x60;resourceName&#x60;, e.g. 1234567890~987654321). A bare criterion id is rejected because it is only unique within its ad group. | |
| **updateAdKeywordRequest** | [**UpdateAdKeywordRequest**](UpdateAdKeywordRequest.md)|  | |

### Return type

[**UpdateAdKeyword200Response**](UpdateAdKeyword200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Keyword updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **422** | Negative keywords have no status on Google; they cannot be paused or enabled. |  -  |

## updateAdKeywordWithHttpInfo

> ApiResponse<UpdateAdKeyword200Response> updateAdKeyword updateAdKeywordWithHttpInfo(keywordId, updateAdKeywordRequest)

Pause or enable a Search keyword

Pauses or re-enables a single Google Search keyword.  Changes &#x60;ad_group_criterion.status&#x60; for one keyword criterion (M.140). Negative keywords have no status on Google and cannot be paused or enabled. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String keywordId = "keywordId_example"; // String | Zernio keyword ID (`id`), or Google's native `{adSetId}~{platformCriterionId}` (the tail of `resourceName`, e.g. 1234567890~987654321). A bare criterion id is rejected because it is only unique within its ad group.
        UpdateAdKeywordRequest updateAdKeywordRequest = new UpdateAdKeywordRequest(); // UpdateAdKeywordRequest | 
        try {
            ApiResponse<UpdateAdKeyword200Response> response = apiInstance.updateAdKeywordWithHttpInfo(keywordId, updateAdKeywordRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdKeyword");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **keywordId** | **String**| Zernio keyword ID (&#x60;id&#x60;), or Google&#39;s native &#x60;{adSetId}~{platformCriterionId}&#x60; (the tail of &#x60;resourceName&#x60;, e.g. 1234567890~987654321). A bare criterion id is rejected because it is only unique within its ad group. | |
| **updateAdKeywordRequest** | [**UpdateAdKeywordRequest**](UpdateAdKeywordRequest.md)|  | |

### Return type

ApiResponse<[**UpdateAdKeyword200Response**](UpdateAdKeyword200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Keyword updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **422** | Negative keywords have no status on Google; they cannot be paused or enabled. |  -  |


## updateAdSet

> UpdateAdSet200Response updateAdSet(adSetId, updateAdSetRequest)

Update an ad set

Changes an ad set&#39;s settings, such as its budget, bid strategy, status or delivery options. At least one updatable field is required.  Use it for:  - ABO budget updates. - Ad-set-scoped pause/resume. - Bid-strategy edits. - Meta value-rule-set attach/detach. - Meta beneficiary and payer: &#x60;dsaBeneficiary&#x60; / &#x60;dsaPayor&#x60; for the EU, &#x60;regionalRegulatedCategories&#x60; / &#x60;regionalRegulationIdentities&#x60; for the regional regimes. - Meta-only post-launch delivery settings via &#x60;platformSpecificData&#x60;.  ### Value rule sets (Meta only)  See &#x60;/v1/ads/value-rule-sets&#x60;.  - ATTACH or REPLACE: send &#x60;valueRuleSetId&#x60;. Attachment is driven by the id&#39;s presence, so &#x60;valueRulesApplied: true&#x60; is optional. Sending a different id replaces the previous association; there is no separate replace call. - DETACH: send &#x60;valueRulesApplied: false&#x60; and OMIT &#x60;valueRuleSetId&#x60;. - Sending &#x60;valueRulesApplied: false&#x60; TOGETHER with &#x60;valueRuleSetId&#x60; returns 400 &#x60;mutually_exclusive_fields&#x60;. - Eligibility: only ad sets on &#x60;LOWEST_COST_WITHOUT_CAP&#x60; or &#x60;COST_CAP&#x60;. Meta rejects the rest server-side. - Read back with &#x60;GET /v1/ads/ad-sets/{adSetId}?fields&#x3D;value_rule_set_id&#x60;. Meta does not document &#x60;value_rules_applied&#x60; as a readable ad-set field, so the boolean cannot be read back.  The &#x60;mutually_exclusive_fields&#x60; error is deliberate. Meta attaches the rule set whenever &#x60;value_rule_set_id&#x60; is present, even with &#x60;value_rules_applied&#x60; false, so echoing stored state while asking to detach would silently keep the bid adjustments live.  ### Bid strategy compatibility (per Meta&#39;s spec)  - &#x60;LOWEST_COST_WITHOUT_CAP&#x60;: no &#x60;bidAmount&#x60;, no &#x60;roasAverageFloor&#x60;. - &#x60;LOWEST_COST_WITH_BID_CAP&#x60; / &#x60;COST_CAP&#x60;: &#x60;bidAmount&#x60; REQUIRED (whole currency units). - &#x60;LOWEST_COST_WITH_MIN_ROAS&#x60;: &#x60;roasAverageFloor&#x60; REQUIRED (decimal multiplier, e.g. 2.0 &#x3D; 2.0x ROAS).  Meta only: send &#x60;bidAmount&#x60; WITHOUT &#x60;bidStrategy&#x60; to change the cap amount on an ad set whose strategy (its own, or the campaign&#39;s under CBO) is COST_CAP / LOWEST_COST_WITH_BID_CAP, leaving the strategy untouched.  Send &#x60;roasAverageFloor&#x60; WITHOUT &#x60;bidStrategy&#x60; the same way to change the floor of a LOWEST_COST_WITH_MIN_ROAS ad set. Either field against an incompatible current strategy is a 400.  Meta CBO (the campaign holds the budget): the campaign also holds the bid strategy, so only &#x60;bidAmount&#x60; or &#x60;roasAverageFloor&#x60; is written on the ad set. A &#x60;bidStrategy&#x60; equal to the campaign&#39;s is accepted; a different one is a 409 (change it with PUT /v1/ads/campaigns/{campaignId}).  ### Delivery settings and budget  Delivery settings are validated by Meta against the campaign objective. Incompatible combinations (e.g. a billingEvent the optimization goal doesn&#39;t allow) surface as 400s from Meta.  When updating &#x60;budget&#x60; on an ad set whose campaign holds the budget (CBO), the response is 409 with code &#x60;invalid_field_value&#x60;. Send it to PUT /v1/ads/campaigns/{campaignId} instead.  ### Status  &#x60;status&#x60; behaves exactly as PUT /v1/ads/ad-sets/{adSetId}/status describes. Only the ad set&#39;s own switch is written and its ads keep theirs. &#x60;statusUpdated&#x60; / &#x60;statusSkipped&#x60; report whether that switch was written or a live read showed it already in place.  ### Placements and targeting (Meta only)  &#x60;placements&#x60; and &#x60;targeting&#x60; take the same shapes as POST /v1/ads/create. Meta replaces an ad set&#39;s targeting wholesale, so Zernio reads the live targeting first, changes only what the request names and writes the merged spec back.  Custom audiences, geo, age, interest groups and &#x60;targeting_automation&#x60; you do not send are kept.  - &#x60;placements&#x60; replaces the whole placement set. - &#x60;placements: null&#x60; returns the ad set to automatic placements. - Omitting it leaves placements as they are.  Other platforms return 400 for either field before anything in the request is written (use PUT /v1/ads/{adId} with &#x60;targeting&#x60; where that platform supports it).  The live read and the &#x60;incomeTier&#x60; lookup run before any other field is written, so a 502 or 422 from them leaves the ad set unchanged.  ### Reddit Ads: budget, name and bidding  - &#x60;budget&#x60; changes the ad group&#39;s amount. An ad group that spends its campaign budget returns 422 (update the campaign instead). - Reddit cannot switch a published budget between daily and lifetime, so &#x60;budget.type&#x60; must match the current one (422 otherwise). - &#x60;name&#x60; renames the ad group.  &#x60;bidStrategy&#x60; maps to the ad group&#39;s &#x60;bid_strategy&#x60;:  - LOWEST_COST_WITHOUT_CAP: automatic bidding (BIDLESS). - LOWEST_COST_WITH_BID_CAP: MANUAL_BIDDING with &#x60;bidAmount&#x60; as the bid. - COST_CAP: MAXIMIZE_VOLUME with &#x60;bidAmount&#x60; as the cap. - LOWEST_COST_WITH_MIN_ROAS: returns 422.  ### Reddit Ads: targeting and schedule  &#x60;targeting&#x60; (same shape as on create; &#x60;placements&#x60; is a 400) and &#x60;startDate&#x60; / &#x60;endDate&#x60; change the ad group with one PATCH to Reddit. Read the current values with GET /v1/ads/ad-sets/{adSetId}/targeting.  Zernio reads the live ad group first and replaces only the targeting groups the request names:  - The included locations (&#x60;countries&#x60;, &#x60;regions&#x60;, &#x60;metros&#x60;, &#x60;cities&#x60;, &#x60;zips&#x60;) are one list on Reddit, so sending any of them replaces all included locations. - Devices, platforms, carriers and automated expansion set in Reddit Ads Manager are kept.  The schedule is checked against the campaign before anything in the request is written. Each of these returns 400 naming &#x60;startDate&#x60; or &#x60;endDate&#x60;:  - The ad group starts before a campaign that starts in the future. - The ad group ends after the campaign&#39;s end. - Under campaign budget optimization, it must end by the campaign end (and has no end date when the campaign has none).  Zernio never resends the PATCH on its own, so after a 5xx read the ad group back before retrying. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Platform ad set ID
        UpdateAdSetRequest updateAdSetRequest = new UpdateAdSetRequest(); // UpdateAdSetRequest | 
        try {
            UpdateAdSet200Response result = apiInstance.updateAdSet(adSetId, updateAdSetRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdSet");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adSetId** | **String**| Platform ad set ID | |
| **updateAdSetRequest** | [**UpdateAdSetRequest**](UpdateAdSetRequest.md)|  | |

### Return type

[**UpdateAdSet200Response**](UpdateAdSet200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad set updated |  -  |
| **400** | Invalid input, including:  - &#x60;placements&#x60; on a platform other than Meta, or &#x60;targeting&#x60; on a platform other than Meta and Reddit. - A Reddit &#x60;startDate&#x60; or &#x60;endDate&#x60; that is not a date, or a Reddit schedule the campaign does not allow. - A targeting field the platform cannot honour. - &#x60;placements&#x60; sent both at the top level and inside &#x60;targeting&#x60;. - A &#x60;platformSpecificData.promotedObject&#x60; key Meta cannot change on an existing ad set (anything but &#x60;pixelId&#x60;, &#x60;customEventType&#x60;, &#x60;customEventStr&#x60;, &#x60;applicationId&#x60; and &#x60;productCatalogId&#x60;). |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Returned with these codes:  - &#x60;ads_allowance_exceeded&#x60;: the team has no payment method on file and has reached the 500 free live ads. Add a card to resume. - &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;. - &#x60;ad_account_not_selected&#x60; fix: add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection), or use a connection that has it selected.  |  -  |
| **404** | Ad set not found |  -  |
| **409** | Conflict. Nothing is written.  - Campaign is CBO: a budget, or a bidStrategy other than the campaign&#39;s (Meta), belongs on /v1/ads/campaigns/{campaignId}. - Code &#x60;invalid_resource_state&#x60;: the ad set has no ads yet and the request sends &#x60;status&#x60;, &#x60;budget&#x60;, &#x60;bidStrategy&#x60;, &#x60;bidAmount&#x60; or &#x60;roasAverageFloor&#x60;. These are written through its ads on every platform except Reddit, so add an ad first. A Reddit ad group with no ads takes these fields directly. |  -  |
| **422** | bidStrategy is LOWEST_COST_WITH_MIN_ROAS on OpenAI or Reddit (unsupported: no ROAS-based bidding), a Reddit budget that the ad group cannot take (campaign budget, or a daily/lifetime switch), or a &#x60;targeting.incomeTier&#x60; Meta has no income segment for |  -  |
| **502** | Meta: the ad set&#39;s live targeting could not be read, so the placements or targeting update was not written |  -  |
| **501** | bidStrategy not supported on the platform (Meta, TikTok, OpenAI and Reddit only) |  -  |

## updateAdSetWithHttpInfo

> ApiResponse<UpdateAdSet200Response> updateAdSet updateAdSetWithHttpInfo(adSetId, updateAdSetRequest)

Update an ad set

Changes an ad set&#39;s settings, such as its budget, bid strategy, status or delivery options. At least one updatable field is required.  Use it for:  - ABO budget updates. - Ad-set-scoped pause/resume. - Bid-strategy edits. - Meta value-rule-set attach/detach. - Meta beneficiary and payer: &#x60;dsaBeneficiary&#x60; / &#x60;dsaPayor&#x60; for the EU, &#x60;regionalRegulatedCategories&#x60; / &#x60;regionalRegulationIdentities&#x60; for the regional regimes. - Meta-only post-launch delivery settings via &#x60;platformSpecificData&#x60;.  ### Value rule sets (Meta only)  See &#x60;/v1/ads/value-rule-sets&#x60;.  - ATTACH or REPLACE: send &#x60;valueRuleSetId&#x60;. Attachment is driven by the id&#39;s presence, so &#x60;valueRulesApplied: true&#x60; is optional. Sending a different id replaces the previous association; there is no separate replace call. - DETACH: send &#x60;valueRulesApplied: false&#x60; and OMIT &#x60;valueRuleSetId&#x60;. - Sending &#x60;valueRulesApplied: false&#x60; TOGETHER with &#x60;valueRuleSetId&#x60; returns 400 &#x60;mutually_exclusive_fields&#x60;. - Eligibility: only ad sets on &#x60;LOWEST_COST_WITHOUT_CAP&#x60; or &#x60;COST_CAP&#x60;. Meta rejects the rest server-side. - Read back with &#x60;GET /v1/ads/ad-sets/{adSetId}?fields&#x3D;value_rule_set_id&#x60;. Meta does not document &#x60;value_rules_applied&#x60; as a readable ad-set field, so the boolean cannot be read back.  The &#x60;mutually_exclusive_fields&#x60; error is deliberate. Meta attaches the rule set whenever &#x60;value_rule_set_id&#x60; is present, even with &#x60;value_rules_applied&#x60; false, so echoing stored state while asking to detach would silently keep the bid adjustments live.  ### Bid strategy compatibility (per Meta&#39;s spec)  - &#x60;LOWEST_COST_WITHOUT_CAP&#x60;: no &#x60;bidAmount&#x60;, no &#x60;roasAverageFloor&#x60;. - &#x60;LOWEST_COST_WITH_BID_CAP&#x60; / &#x60;COST_CAP&#x60;: &#x60;bidAmount&#x60; REQUIRED (whole currency units). - &#x60;LOWEST_COST_WITH_MIN_ROAS&#x60;: &#x60;roasAverageFloor&#x60; REQUIRED (decimal multiplier, e.g. 2.0 &#x3D; 2.0x ROAS).  Meta only: send &#x60;bidAmount&#x60; WITHOUT &#x60;bidStrategy&#x60; to change the cap amount on an ad set whose strategy (its own, or the campaign&#39;s under CBO) is COST_CAP / LOWEST_COST_WITH_BID_CAP, leaving the strategy untouched.  Send &#x60;roasAverageFloor&#x60; WITHOUT &#x60;bidStrategy&#x60; the same way to change the floor of a LOWEST_COST_WITH_MIN_ROAS ad set. Either field against an incompatible current strategy is a 400.  Meta CBO (the campaign holds the budget): the campaign also holds the bid strategy, so only &#x60;bidAmount&#x60; or &#x60;roasAverageFloor&#x60; is written on the ad set. A &#x60;bidStrategy&#x60; equal to the campaign&#39;s is accepted; a different one is a 409 (change it with PUT /v1/ads/campaigns/{campaignId}).  ### Delivery settings and budget  Delivery settings are validated by Meta against the campaign objective. Incompatible combinations (e.g. a billingEvent the optimization goal doesn&#39;t allow) surface as 400s from Meta.  When updating &#x60;budget&#x60; on an ad set whose campaign holds the budget (CBO), the response is 409 with code &#x60;invalid_field_value&#x60;. Send it to PUT /v1/ads/campaigns/{campaignId} instead.  ### Status  &#x60;status&#x60; behaves exactly as PUT /v1/ads/ad-sets/{adSetId}/status describes. Only the ad set&#39;s own switch is written and its ads keep theirs. &#x60;statusUpdated&#x60; / &#x60;statusSkipped&#x60; report whether that switch was written or a live read showed it already in place.  ### Placements and targeting (Meta only)  &#x60;placements&#x60; and &#x60;targeting&#x60; take the same shapes as POST /v1/ads/create. Meta replaces an ad set&#39;s targeting wholesale, so Zernio reads the live targeting first, changes only what the request names and writes the merged spec back.  Custom audiences, geo, age, interest groups and &#x60;targeting_automation&#x60; you do not send are kept.  - &#x60;placements&#x60; replaces the whole placement set. - &#x60;placements: null&#x60; returns the ad set to automatic placements. - Omitting it leaves placements as they are.  Other platforms return 400 for either field before anything in the request is written (use PUT /v1/ads/{adId} with &#x60;targeting&#x60; where that platform supports it).  The live read and the &#x60;incomeTier&#x60; lookup run before any other field is written, so a 502 or 422 from them leaves the ad set unchanged.  ### Reddit Ads: budget, name and bidding  - &#x60;budget&#x60; changes the ad group&#39;s amount. An ad group that spends its campaign budget returns 422 (update the campaign instead). - Reddit cannot switch a published budget between daily and lifetime, so &#x60;budget.type&#x60; must match the current one (422 otherwise). - &#x60;name&#x60; renames the ad group.  &#x60;bidStrategy&#x60; maps to the ad group&#39;s &#x60;bid_strategy&#x60;:  - LOWEST_COST_WITHOUT_CAP: automatic bidding (BIDLESS). - LOWEST_COST_WITH_BID_CAP: MANUAL_BIDDING with &#x60;bidAmount&#x60; as the bid. - COST_CAP: MAXIMIZE_VOLUME with &#x60;bidAmount&#x60; as the cap. - LOWEST_COST_WITH_MIN_ROAS: returns 422.  ### Reddit Ads: targeting and schedule  &#x60;targeting&#x60; (same shape as on create; &#x60;placements&#x60; is a 400) and &#x60;startDate&#x60; / &#x60;endDate&#x60; change the ad group with one PATCH to Reddit. Read the current values with GET /v1/ads/ad-sets/{adSetId}/targeting.  Zernio reads the live ad group first and replaces only the targeting groups the request names:  - The included locations (&#x60;countries&#x60;, &#x60;regions&#x60;, &#x60;metros&#x60;, &#x60;cities&#x60;, &#x60;zips&#x60;) are one list on Reddit, so sending any of them replaces all included locations. - Devices, platforms, carriers and automated expansion set in Reddit Ads Manager are kept.  The schedule is checked against the campaign before anything in the request is written. Each of these returns 400 naming &#x60;startDate&#x60; or &#x60;endDate&#x60;:  - The ad group starts before a campaign that starts in the future. - The ad group ends after the campaign&#39;s end. - Under campaign budget optimization, it must end by the campaign end (and has no end date when the campaign has none).  Zernio never resends the PATCH on its own, so after a 5xx read the ad group back before retrying. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Platform ad set ID
        UpdateAdSetRequest updateAdSetRequest = new UpdateAdSetRequest(); // UpdateAdSetRequest | 
        try {
            ApiResponse<UpdateAdSet200Response> response = apiInstance.updateAdSetWithHttpInfo(adSetId, updateAdSetRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdSet");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adSetId** | **String**| Platform ad set ID | |
| **updateAdSetRequest** | [**UpdateAdSetRequest**](UpdateAdSetRequest.md)|  | |

### Return type

ApiResponse<[**UpdateAdSet200Response**](UpdateAdSet200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad set updated |  -  |
| **400** | Invalid input, including:  - &#x60;placements&#x60; on a platform other than Meta, or &#x60;targeting&#x60; on a platform other than Meta and Reddit. - A Reddit &#x60;startDate&#x60; or &#x60;endDate&#x60; that is not a date, or a Reddit schedule the campaign does not allow. - A targeting field the platform cannot honour. - &#x60;placements&#x60; sent both at the top level and inside &#x60;targeting&#x60;. - A &#x60;platformSpecificData.promotedObject&#x60; key Meta cannot change on an existing ad set (anything but &#x60;pixelId&#x60;, &#x60;customEventType&#x60;, &#x60;customEventStr&#x60;, &#x60;applicationId&#x60; and &#x60;productCatalogId&#x60;). |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Returned with these codes:  - &#x60;ads_allowance_exceeded&#x60;: the team has no payment method on file and has reached the 500 free live ads. Add a card to resume. - &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;. - &#x60;ad_account_not_selected&#x60; fix: add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection), or use a connection that has it selected.  |  -  |
| **404** | Ad set not found |  -  |
| **409** | Conflict. Nothing is written.  - Campaign is CBO: a budget, or a bidStrategy other than the campaign&#39;s (Meta), belongs on /v1/ads/campaigns/{campaignId}. - Code &#x60;invalid_resource_state&#x60;: the ad set has no ads yet and the request sends &#x60;status&#x60;, &#x60;budget&#x60;, &#x60;bidStrategy&#x60;, &#x60;bidAmount&#x60; or &#x60;roasAverageFloor&#x60;. These are written through its ads on every platform except Reddit, so add an ad first. A Reddit ad group with no ads takes these fields directly. |  -  |
| **422** | bidStrategy is LOWEST_COST_WITH_MIN_ROAS on OpenAI or Reddit (unsupported: no ROAS-based bidding), a Reddit budget that the ad group cannot take (campaign budget, or a daily/lifetime switch), or a &#x60;targeting.incomeTier&#x60; Meta has no income segment for |  -  |
| **502** | Meta: the ad set&#39;s live targeting could not be read, so the placements or targeting update was not written |  -  |
| **501** | bidStrategy not supported on the platform (Meta, TikTok, OpenAI and Reddit only) |  -  |


## updateAdSetStatus

> UpdateAdSetStatus200Response updateAdSetStatus(adSetId, updateAdCampaignStatusRequest)

Pause or resume a single ad set

Pauses or resumes one ad set without touching its campaign, its sibling ad sets or the switches of its ads.  It is a thin wrapper over PUT /v1/ads/ad-sets/{adSetId} for callers that only want the status toggle and prefer a symmetric URL to /v1/ads/campaigns/{campaignId}/status.  ### What is written  It writes the ad set&#39;s own on/off switch and nothing else, on every platform:  - Meta: &#x60;configured_status&#x60; - TikTok: ad group &#x60;operation_status&#x60; - Google: ad group status - LinkedIn: campaign - Pinterest: ad group - X: line item - ChatGPT (OpenAI): ad group - Reddit: ad group &#x60;configured_status&#x60;  Its ads keep their own switches: an ad you paused individually stays paused when the ad set resumes.  The campaign above is not touched either, so an ad set resumed under a paused campaign reads &#x60;status: paused&#x60; until the campaign is resumed too. See the Status model in the Ad Campaigns tag.  ### Live read, then write  The ad set&#39;s switch is read from the platform first.  - When that live read shows it already in the requested state, nothing is written (&#x60;updated: 0&#x60;, &#x60;skipped: 1&#x60;, with the reason). - In that case, when the ad set delivers in that state but some of its ads are stored in the other state, those ads (up to 20, at most once every 10 minutes per ad set) are re-read and stored. - Otherwise the switch is written (&#x60;updated: 1&#x60;), read back and stored. The delivery status of its ads (up to 20) is re-read and stored, so an immediate GET returns what the platform now reports.  A stored switch never skips a write, and when the platform cannot be read the write always goes out.  On Meta and Reddit the check reads the ad set&#39;s own switch (&#x60;status&#x60; / &#x60;configured_status&#x60;). So a repeated request skips even while &#x60;platformAdSetStatus&#x60; reads &#x60;CAMPAIGN_PAUSED&#x60;, &#x60;WITH_ISSUES&#x60; or &#x60;IN_PROCESS&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Platform ad set ID
        UpdateAdCampaignStatusRequest updateAdCampaignStatusRequest = new UpdateAdCampaignStatusRequest(); // UpdateAdCampaignStatusRequest | 
        try {
            UpdateAdSetStatus200Response result = apiInstance.updateAdSetStatus(adSetId, updateAdCampaignStatusRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdSetStatus");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adSetId** | **String**| Platform ad set ID | |
| **updateAdCampaignStatusRequest** | [**UpdateAdCampaignStatusRequest**](UpdateAdCampaignStatusRequest.md)|  | |

### Return type

[**UpdateAdSetStatus200Response**](UpdateAdSetStatus200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad set status updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | One of two refusals:  - &#x60;ads_allowance_exceeded&#x60;: the team has no payment method on file and has reached the 500 free live ads. Add a card to resume. - &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the ad account this request targets is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix &#x60;ad_account_not_selected&#x60;, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | Ad set not found |  -  |
| **409** | Code &#x60;invalid_resource_state&#x60;: the ad set has no ads yet, and on this platform its switch is written through its ads. Add an ad first. A Reddit ad group with no ads is switched directly. |  -  |

## updateAdSetStatusWithHttpInfo

> ApiResponse<UpdateAdSetStatus200Response> updateAdSetStatus updateAdSetStatusWithHttpInfo(adSetId, updateAdCampaignStatusRequest)

Pause or resume a single ad set

Pauses or resumes one ad set without touching its campaign, its sibling ad sets or the switches of its ads.  It is a thin wrapper over PUT /v1/ads/ad-sets/{adSetId} for callers that only want the status toggle and prefer a symmetric URL to /v1/ads/campaigns/{campaignId}/status.  ### What is written  It writes the ad set&#39;s own on/off switch and nothing else, on every platform:  - Meta: &#x60;configured_status&#x60; - TikTok: ad group &#x60;operation_status&#x60; - Google: ad group status - LinkedIn: campaign - Pinterest: ad group - X: line item - ChatGPT (OpenAI): ad group - Reddit: ad group &#x60;configured_status&#x60;  Its ads keep their own switches: an ad you paused individually stays paused when the ad set resumes.  The campaign above is not touched either, so an ad set resumed under a paused campaign reads &#x60;status: paused&#x60; until the campaign is resumed too. See the Status model in the Ad Campaigns tag.  ### Live read, then write  The ad set&#39;s switch is read from the platform first.  - When that live read shows it already in the requested state, nothing is written (&#x60;updated: 0&#x60;, &#x60;skipped: 1&#x60;, with the reason). - In that case, when the ad set delivers in that state but some of its ads are stored in the other state, those ads (up to 20, at most once every 10 minutes per ad set) are re-read and stored. - Otherwise the switch is written (&#x60;updated: 1&#x60;), read back and stored. The delivery status of its ads (up to 20) is re-read and stored, so an immediate GET returns what the platform now reports.  A stored switch never skips a write, and when the platform cannot be read the write always goes out.  On Meta and Reddit the check reads the ad set&#39;s own switch (&#x60;status&#x60; / &#x60;configured_status&#x60;). So a repeated request skips even while &#x60;platformAdSetStatus&#x60; reads &#x60;CAMPAIGN_PAUSED&#x60;, &#x60;WITH_ISSUES&#x60; or &#x60;IN_PROCESS&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adSetId = "adSetId_example"; // String | Platform ad set ID
        UpdateAdCampaignStatusRequest updateAdCampaignStatusRequest = new UpdateAdCampaignStatusRequest(); // UpdateAdCampaignStatusRequest | 
        try {
            ApiResponse<UpdateAdSetStatus200Response> response = apiInstance.updateAdSetStatusWithHttpInfo(adSetId, updateAdCampaignStatusRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdSetStatus");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adSetId** | **String**| Platform ad set ID | |
| **updateAdCampaignStatusRequest** | [**UpdateAdCampaignStatusRequest**](UpdateAdCampaignStatusRequest.md)|  | |

### Return type

ApiResponse<[**UpdateAdSetStatus200Response**](UpdateAdSetStatus200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad set status updated |  -  |
| **400** | Invalid input |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | One of two refusals:  - &#x60;ads_allowance_exceeded&#x60;: the team has no payment method on file and has reached the 500 free live ads. Add a card to resume. - &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the ad account this request targets is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix &#x60;ad_account_not_selected&#x60;, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | Ad set not found |  -  |
| **409** | Code &#x60;invalid_resource_state&#x60;: the ad set has no ads yet, and on this platform its switch is written through its ads. Add an ad first. A Reddit ad group with no ads is switched directly. |  -  |


## updateAdStatus

> UpdateAdStatus200Response updateAdStatus(adId, updateAdKeywordRequest)

Pause or resume a single ad

Pauses or resumes a single ad without touching its ad set, campaign or sibling ads.  ### What it flips  Ad-scoped pause/resume flips ONLY this ad&#39;s own switch, never its parent ad set or campaign, so sibling ads keep running:  - Meta &#x60;configured_status&#x60; - TikTok &#x60;operation_status&#x60; - Google ad group ad status - LinkedIn creative - Pinterest ad - Reddit ad &#x60;configured_status&#x60;  X is the exception: its smallest switch is the line item.  It is a thin wrapper over the &#x60;status&#x60; field of PUT /v1/ads/{adId}, for callers that want a URL symmetric to /v1/ads/campaigns/{campaignId}/status and /v1/ads/ad-sets/{adSetId}/status.  ### Own switch vs delivery status  The ad&#39;s own switch is independent of its delivery status.  - An ad paused only because its campaign or ad set is off (&#x60;status: paused&#x60;, &#x60;configuredStatus: ACTIVE&#x60;) can still be switched off here. - Switching an ad on under a paused campaign leaves it &#x60;paused&#x60; until the campaign is resumed.  After the write the switch is read back from the platform and returned as &#x60;configuredStatus&#x60;, together with the resulting delivery &#x60;status&#x60;.  ### Identifiers  &#x60;{adId}&#x60; accepts the same identifier dialects as GET/PUT /v1/ads/{adId}: Zernio hex &#x60;_id&#x60;, Meta numeric &#x60;platformAdId&#x60;, or the creative&#39;s effective story/media IDs.  &#x60;platform&#x60; is inferred from the ad, so it&#39;s not required in the body.  ### Skips  These requests are skipped:  - Ads in terminal statuses (rejected, completed, cancelled). - A request whose target already matches the ad&#39;s own switch as read LIVE from the platform. A stored value is never trusted alone, since the switch may have been changed in the platform&#39;s own UI.  A skip also returns that live read. The rolled-up &#x60;status&#x60; never decides a skip. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adId = "adId_example"; // String | Zernio `_id` (hex), Meta `platformAdId` (numeric), or one of the creative's effective story/media IDs.
        UpdateAdKeywordRequest updateAdKeywordRequest = new UpdateAdKeywordRequest(); // UpdateAdKeywordRequest | 
        try {
            UpdateAdStatus200Response result = apiInstance.updateAdStatus(adId, updateAdKeywordRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdStatus");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adId** | **String**| Zernio &#x60;_id&#x60; (hex), Meta &#x60;platformAdId&#x60; (numeric), or one of the creative&#39;s effective story/media IDs. | |
| **updateAdKeywordRequest** | [**UpdateAdKeywordRequest**](UpdateAdKeywordRequest.md)|  | |

### Return type

[**UpdateAdStatus200Response**](UpdateAdStatus200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad status updated (or skipped when no change was needed) |  -  |
| **400** | Invalid input |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Forbidden. The code says why:  - &#x60;ads_allowance_exceeded&#x60;: the team has no payment method on file and has reached the 500 free live ads. Add a card to resume. - &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the ad account this request targets is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix &#x60;ad_account_not_selected&#x60;, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | Ad not found |  -  |

## updateAdStatusWithHttpInfo

> ApiResponse<UpdateAdStatus200Response> updateAdStatus updateAdStatusWithHttpInfo(adId, updateAdKeywordRequest)

Pause or resume a single ad

Pauses or resumes a single ad without touching its ad set, campaign or sibling ads.  ### What it flips  Ad-scoped pause/resume flips ONLY this ad&#39;s own switch, never its parent ad set or campaign, so sibling ads keep running:  - Meta &#x60;configured_status&#x60; - TikTok &#x60;operation_status&#x60; - Google ad group ad status - LinkedIn creative - Pinterest ad - Reddit ad &#x60;configured_status&#x60;  X is the exception: its smallest switch is the line item.  It is a thin wrapper over the &#x60;status&#x60; field of PUT /v1/ads/{adId}, for callers that want a URL symmetric to /v1/ads/campaigns/{campaignId}/status and /v1/ads/ad-sets/{adSetId}/status.  ### Own switch vs delivery status  The ad&#39;s own switch is independent of its delivery status.  - An ad paused only because its campaign or ad set is off (&#x60;status: paused&#x60;, &#x60;configuredStatus: ACTIVE&#x60;) can still be switched off here. - Switching an ad on under a paused campaign leaves it &#x60;paused&#x60; until the campaign is resumed.  After the write the switch is read back from the platform and returned as &#x60;configuredStatus&#x60;, together with the resulting delivery &#x60;status&#x60;.  ### Identifiers  &#x60;{adId}&#x60; accepts the same identifier dialects as GET/PUT /v1/ads/{adId}: Zernio hex &#x60;_id&#x60;, Meta numeric &#x60;platformAdId&#x60;, or the creative&#39;s effective story/media IDs.  &#x60;platform&#x60; is inferred from the ad, so it&#39;s not required in the body.  ### Skips  These requests are skipped:  - Ads in terminal statuses (rejected, completed, cancelled). - A request whose target already matches the ad&#39;s own switch as read LIVE from the platform. A stored value is never trusted alone, since the switch may have been changed in the platform&#39;s own UI.  A skip also returns that live read. The rolled-up &#x60;status&#x60; never decides a skip. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String adId = "adId_example"; // String | Zernio `_id` (hex), Meta `platformAdId` (numeric), or one of the creative's effective story/media IDs.
        UpdateAdKeywordRequest updateAdKeywordRequest = new UpdateAdKeywordRequest(); // UpdateAdKeywordRequest | 
        try {
            ApiResponse<UpdateAdStatus200Response> response = apiInstance.updateAdStatusWithHttpInfo(adId, updateAdKeywordRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateAdStatus");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adId** | **String**| Zernio &#x60;_id&#x60; (hex), Meta &#x60;platformAdId&#x60; (numeric), or one of the creative&#39;s effective story/media IDs. | |
| **updateAdKeywordRequest** | [**UpdateAdKeywordRequest**](UpdateAdKeywordRequest.md)|  | |

### Return type

ApiResponse<[**UpdateAdStatus200Response**](UpdateAdStatus200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad status updated (or skipped when no change was needed) |  -  |
| **400** | Invalid input |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Forbidden. The code says why:  - &#x60;ads_allowance_exceeded&#x60;: the team has no payment method on file and has reached the 500 free live ads. Add a card to resume. - &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the ad account this request targets is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix &#x60;ad_account_not_selected&#x60;, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | Ad not found |  -  |


## updateBidStrategy

> UpdateBidStrategy200Response updateBidStrategy(strategyId, updateBidStrategyRequest)

Update portfolio bid strategy

Renames a shared Google Ads bid strategy or changes its target CPA or ROAS.  The strategy&#39;s status is output only on Google&#39;s side, so it cannot be changed here; remove a strategy in Google Ads.  ### When to send &#x60;type&#x60;  &#x60;type&#x60; is only needed alongside &#x60;targetCpa&#x60;/&#x60;targetRoas&#x60;, to disambiguate the field Google writes to:  - TARGET_CPA and MAXIMIZE_CONVERSIONS both take a target CPA. - TARGET_ROAS and MAXIMIZE_CONVERSION_VALUE both take a target ROAS.  The strategy&#39;s family is otherwise immutable once created. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String strategyId = "strategyId_example"; // String | Numeric Google Ads bid strategy id.
        UpdateBidStrategyRequest updateBidStrategyRequest = new UpdateBidStrategyRequest(); // UpdateBidStrategyRequest | 
        try {
            UpdateBidStrategy200Response result = apiInstance.updateBidStrategy(strategyId, updateBidStrategyRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateBidStrategy");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **strategyId** | **String**| Numeric Google Ads bid strategy id. | |
| **updateBidStrategyRequest** | [**UpdateBidStrategyRequest**](UpdateBidStrategyRequest.md)|  | |

### Return type

[**UpdateBidStrategy200Response**](UpdateBidStrategy200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Bid strategy updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget exhausted; retry later. |  -  |
| **501** | Only available on Google Ads accounts |  -  |

## updateBidStrategyWithHttpInfo

> ApiResponse<UpdateBidStrategy200Response> updateBidStrategy updateBidStrategyWithHttpInfo(strategyId, updateBidStrategyRequest)

Update portfolio bid strategy

Renames a shared Google Ads bid strategy or changes its target CPA or ROAS.  The strategy&#39;s status is output only on Google&#39;s side, so it cannot be changed here; remove a strategy in Google Ads.  ### When to send &#x60;type&#x60;  &#x60;type&#x60; is only needed alongside &#x60;targetCpa&#x60;/&#x60;targetRoas&#x60;, to disambiguate the field Google writes to:  - TARGET_CPA and MAXIMIZE_CONVERSIONS both take a target CPA. - TARGET_ROAS and MAXIMIZE_CONVERSION_VALUE both take a target ROAS.  The strategy&#39;s family is otherwise immutable once created. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String strategyId = "strategyId_example"; // String | Numeric Google Ads bid strategy id.
        UpdateBidStrategyRequest updateBidStrategyRequest = new UpdateBidStrategyRequest(); // UpdateBidStrategyRequest | 
        try {
            ApiResponse<UpdateBidStrategy200Response> response = apiInstance.updateBidStrategyWithHttpInfo(strategyId, updateBidStrategyRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateBidStrategy");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **strategyId** | **String**| Numeric Google Ads bid strategy id. | |
| **updateBidStrategyRequest** | [**UpdateBidStrategyRequest**](UpdateBidStrategyRequest.md)|  | |

### Return type

ApiResponse<[**UpdateBidStrategy200Response**](UpdateBidStrategy200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Bid strategy updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget exhausted; retry later. |  -  |
| **501** | Only available on Google Ads accounts |  -  |


## updateCampaignAdSchedule

> UpdateCampaignAdSchedule200Response updateCampaignAdSchedule(campaignId, updateCampaignAdScheduleRequest)

Replace a campaign&#39;s ad schedule (dayparting)

Replaces the days and hours a Google campaign runs, or clears them so it serves around the clock.  This is a REPLACE, not a merge: windows you leave out stop serving. Send &#x60;schedule: []&#x60; to clear dayparting, which returns the campaign to serving around the clock.  ### Rules  Google rules are enforced here, so you get a named field instead of a criterion error:  - at most 6 windows per day - a window must end after it starts - windows on the same day may not overlap - &#x60;endHour&#x60; 24 is midnight and cannot carry minutes - minutes are quarter-hours only (0, 15, 30, 45) - &#x60;bidModifier&#x60; is 0.1-10.0. Google&#39;s 0 means \&quot;off\&quot; for devices only, so a window is switched off by leaving it out.  Windows are half-open (Google is exclusive of the end minute), so 09:00-12:00 and 12:00-17:00 on the same day are adjacent and both valid.  ### How it is applied  Google cannot edit an ad schedule in place (every AdScheduleInfo field is prohibited on update). So this removes the live criteria and creates the new ones in a single atomic mutate.  The response is read back from Google and carries the new criterion ids. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Numeric Google platform campaign id.
        UpdateCampaignAdScheduleRequest updateCampaignAdScheduleRequest = new UpdateCampaignAdScheduleRequest(); // UpdateCampaignAdScheduleRequest | 
        try {
            UpdateCampaignAdSchedule200Response result = apiInstance.updateCampaignAdSchedule(campaignId, updateCampaignAdScheduleRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateCampaignAdSchedule");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Numeric Google platform campaign id. | |
| **updateCampaignAdScheduleRequest** | [**UpdateCampaignAdScheduleRequest**](UpdateCampaignAdScheduleRequest.md)|  | |

### Return type

[**UpdateCampaignAdSchedule200Response**](UpdateCampaignAdSchedule200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The schedule as Google stored it |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; it is included by default on usage-based plans.  Also returned with code &#x60;ad_account_not_selected&#x60; when the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection), or use a connection that has it selected.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **422** | The schedule breaks a Google rule: too many windows on a day, an overlap, a window that ends before it starts, minutes on hour 24, or a bid modifier outside 0.1-10.0. |  -  |
| **501** | Not a Google Ads campaign: ad schedules are a Google criterion. |  -  |

## updateCampaignAdScheduleWithHttpInfo

> ApiResponse<UpdateCampaignAdSchedule200Response> updateCampaignAdSchedule updateCampaignAdScheduleWithHttpInfo(campaignId, updateCampaignAdScheduleRequest)

Replace a campaign&#39;s ad schedule (dayparting)

Replaces the days and hours a Google campaign runs, or clears them so it serves around the clock.  This is a REPLACE, not a merge: windows you leave out stop serving. Send &#x60;schedule: []&#x60; to clear dayparting, which returns the campaign to serving around the clock.  ### Rules  Google rules are enforced here, so you get a named field instead of a criterion error:  - at most 6 windows per day - a window must end after it starts - windows on the same day may not overlap - &#x60;endHour&#x60; 24 is midnight and cannot carry minutes - minutes are quarter-hours only (0, 15, 30, 45) - &#x60;bidModifier&#x60; is 0.1-10.0. Google&#39;s 0 means \&quot;off\&quot; for devices only, so a window is switched off by leaving it out.  Windows are half-open (Google is exclusive of the end minute), so 09:00-12:00 and 12:00-17:00 on the same day are adjacent and both valid.  ### How it is applied  Google cannot edit an ad schedule in place (every AdScheduleInfo field is prohibited on update). So this removes the live criteria and creates the new ones in a single atomic mutate.  The response is read back from Google and carries the new criterion ids. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Numeric Google platform campaign id.
        UpdateCampaignAdScheduleRequest updateCampaignAdScheduleRequest = new UpdateCampaignAdScheduleRequest(); // UpdateCampaignAdScheduleRequest | 
        try {
            ApiResponse<UpdateCampaignAdSchedule200Response> response = apiInstance.updateCampaignAdScheduleWithHttpInfo(campaignId, updateCampaignAdScheduleRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateCampaignAdSchedule");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Numeric Google platform campaign id. | |
| **updateCampaignAdScheduleRequest** | [**UpdateCampaignAdScheduleRequest**](UpdateCampaignAdScheduleRequest.md)|  | |

### Return type

ApiResponse<[**UpdateCampaignAdSchedule200Response**](UpdateCampaignAdSchedule200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The schedule as Google stored it |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; it is included by default on usage-based plans.  Also returned with code &#x60;ad_account_not_selected&#x60; when the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection), or use a connection that has it selected.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **422** | The schedule breaks a Google rule: too many windows on a day, an overlap, a window that ends before it starts, minutes on hour 24, or a bid modifier outside 0.1-10.0. |  -  |
| **501** | Not a Google Ads campaign: ad schedules are a Google criterion. |  -  |


## updateCampaignAssets

> UpdateCampaignAssets200Response updateCampaignAssets(campaignId, updateCampaignAssetsRequest)

Update campaign assets

Edits a Google campaign&#39;s existing assets, such as sitelinks or callouts, in place; the change applies everywhere that asset is used.  Send updates with assetResourceName and the fields to change. An asset is shared: changes affect every attachment using it. Omitted fields stay unchanged. The operation consumes the Google operations budget and invalidates affected cached lists. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Numeric Google platform id.
        UpdateCampaignAssetsRequest updateCampaignAssetsRequest = new UpdateCampaignAssetsRequest(); // UpdateCampaignAssetsRequest | 
        try {
            UpdateCampaignAssets200Response result = apiInstance.updateCampaignAssets(campaignId, updateCampaignAssetsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateCampaignAssets");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Numeric Google platform id. | |
| **updateCampaignAssetsRequest** | [**UpdateCampaignAssetsRequest**](UpdateCampaignAssetsRequest.md)|  | |

### Return type

[**UpdateCampaignAssets200Response**](UpdateCampaignAssets200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access is required.  Also returned with code &#x60;ad_account_not_selected&#x60; when the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |

## updateCampaignAssetsWithHttpInfo

> ApiResponse<UpdateCampaignAssets200Response> updateCampaignAssets updateCampaignAssetsWithHttpInfo(campaignId, updateCampaignAssetsRequest)

Update campaign assets

Edits a Google campaign&#39;s existing assets, such as sitelinks or callouts, in place; the change applies everywhere that asset is used.  Send updates with assetResourceName and the fields to change. An asset is shared: changes affect every attachment using it. Omitted fields stay unchanged. The operation consumes the Google operations budget and invalidates affected cached lists. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Numeric Google platform id.
        UpdateCampaignAssetsRequest updateCampaignAssetsRequest = new UpdateCampaignAssetsRequest(); // UpdateCampaignAssetsRequest | 
        try {
            ApiResponse<UpdateCampaignAssets200Response> response = apiInstance.updateCampaignAssetsWithHttpInfo(campaignId, updateCampaignAssetsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateCampaignAssets");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Numeric Google platform id. | |
| **updateCampaignAssetsRequest** | [**UpdateCampaignAssetsRequest**](UpdateCampaignAssetsRequest.md)|  | |

### Return type

ApiResponse<[**UpdateCampaignAssets200Response**](UpdateCampaignAssets200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **409** | The account exists but is inactive or needs reconnection. Reconnect it, then read GET /v1/accounts for its current account ID before retrying. Code: ads_connection_required. |  -  |
| **200** | Assets returned. |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Ads access is required.  Also returned with code &#x60;ad_account_not_selected&#x60; when the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | The account or requested resource was not found or is not accessible. An account ID may have been disconnected and removed. Read GET /v1/accounts for current account IDs. |  -  |
| **429** | Google Ads operations budget or platform quota exhausted. |  -  |
| **501** | Only supported on Google Ads. |  -  |


## updateCampaignConversionGoals

> UpdateCampaignConversionGoals200Response updateCampaignConversionGoals(campaignId, updateCampaignConversionGoalsRequest)

Update campaign conversion goals

Changes which conversions a Google campaign bids on, switching between account-default goals, its own goals or a custom goal.  In one mutate, it can:  - set &#x60;biddable&#x60; on campaign goals - switch &#x60;goalConfigLevel&#x60; - point the campaign at a custom conversion goal  &#x60;customConversionGoalId: null&#x60; clears it. Google refuses that (400) while the campaign stays at CAMPAIGN level with no biddable goals, so send &#x60;goalConfigLevel: CUSTOMER&#x60; with it to fall back to the account goals.  Returns the re-read campaign goals. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Google campaign id
        UpdateCampaignConversionGoalsRequest updateCampaignConversionGoalsRequest = new UpdateCampaignConversionGoalsRequest(); // UpdateCampaignConversionGoalsRequest | 
        try {
            UpdateCampaignConversionGoals200Response result = apiInstance.updateCampaignConversionGoals(campaignId, updateCampaignConversionGoalsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateCampaignConversionGoals");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Google campaign id | |
| **updateCampaignConversionGoalsRequest** | [**UpdateCampaignConversionGoalsRequest**](UpdateCampaignConversionGoalsRequest.md)|  | |

### Return type

[**UpdateCampaignConversionGoals200Response**](UpdateCampaignConversionGoals200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign goals updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **404** | Campaign not found |  -  |
| **409** | Campaign matches multiple accessible accounts, or the connection needs reconnecting |  -  |
| **501** | Only available on Google Ads campaigns |  -  |

## updateCampaignConversionGoalsWithHttpInfo

> ApiResponse<UpdateCampaignConversionGoals200Response> updateCampaignConversionGoals updateCampaignConversionGoalsWithHttpInfo(campaignId, updateCampaignConversionGoalsRequest)

Update campaign conversion goals

Changes which conversions a Google campaign bids on, switching between account-default goals, its own goals or a custom goal.  In one mutate, it can:  - set &#x60;biddable&#x60; on campaign goals - switch &#x60;goalConfigLevel&#x60; - point the campaign at a custom conversion goal  &#x60;customConversionGoalId: null&#x60; clears it. Google refuses that (400) while the campaign stays at CAMPAIGN level with no biddable goals, so send &#x60;goalConfigLevel: CUSTOMER&#x60; with it to fall back to the account goals.  Returns the re-read campaign goals. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Google campaign id
        UpdateCampaignConversionGoalsRequest updateCampaignConversionGoalsRequest = new UpdateCampaignConversionGoalsRequest(); // UpdateCampaignConversionGoalsRequest | 
        try {
            ApiResponse<UpdateCampaignConversionGoals200Response> response = apiInstance.updateCampaignConversionGoalsWithHttpInfo(campaignId, updateCampaignConversionGoalsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateCampaignConversionGoals");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Google campaign id | |
| **updateCampaignConversionGoalsRequest** | [**UpdateCampaignConversionGoalsRequest**](UpdateCampaignConversionGoalsRequest.md)|  | |

### Return type

ApiResponse<[**UpdateCampaignConversionGoals200Response**](UpdateCampaignConversionGoals200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign goals updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **404** | Campaign not found |  -  |
| **409** | Campaign matches multiple accessible accounts, or the connection needs reconnecting |  -  |
| **501** | Only available on Google Ads campaigns |  -  |


## updateCampaignTargeting

> UpdateCampaignTargeting200Response updateCampaignTargeting(campaignId, updateCampaignTargetingRequest)

Edit a Google campaign&#39;s device, location, excluded location, or language targeting

Changes a Google campaign&#39;s device, location, excluded location or language targeting after it was created. Google only; every other platform returns 501.  Google Ads compliance row M.10: geo and language targeting set at creation must stay editable afterwards.  Send at least one of &#x60;devices&#x60;, &#x60;locations&#x60;, &#x60;excludedLocations&#x60;, &#x60;languages&#x60;, &#x60;locationTargetingType&#x60;. Each provided field REPLACES that field&#39;s existing criteria on the campaign (a full set, not a delta). Fields left out of the body are untouched.  ### Fields  - &#x60;devices&#x60;: the full set of device bid modifiers. A supported device you leave out is switched off with a bid modifier of 0, since Google cannot remove a device criterion. A device the campaign&#39;s channel does not carry, and a set that switches every device off, both return 422. - &#x60;locations&#x60;: see below. - &#x60;excludedLocations&#x60;: see below. - &#x60;languages&#x60;: an array of Google&#39;s language codes (ISO 639-1, plus variants such as &#x60;zh_CN&#x60;). An unknown code returns 400. - &#x60;locationTargetingType&#x60;: switches who the location targeting reaches. &#x60;presence&#x60; (people in or regularly in the locations) or &#x60;presence_or_interest&#x60; (also people searching for or interested in them). Example: &#x60;{ \&quot;platform\&quot;: \&quot;google\&quot;, \&quot;targeting\&quot;: { \&quot;locationTargetingType\&quot;: \&quot;presence\&quot; } }&#x60;.  ### Locations  &#x60;locations&#x60; accepts the same shapes as campaign creation: a bare array of ISO country codes, or an object with &#x60;countries&#x60;/&#x60;regions&#x60;/&#x60;cities&#x60;/&#x60;zips&#x60;/&#x60;metros&#x60; key lists (&#x60;key&#x60; from GET /v1/ads/targeting/search?dimension&#x3D;geo).  Excluded locations are left untouched by &#x60;locations&#x60;. An empty location list returns 400 instead of removing every criterion: a Google campaign with no location criteria targets every country, so omit &#x60;locations&#x60; to leave targeting alone.  ### Excluded locations  &#x60;excludedLocations&#x60; takes the same two shapes and replaces the campaign&#39;s negative location criteria (the places it never serves in), leaving the targeted &#x60;locations&#x60; untouched.  - An empty list (or &#x60;{}&#x60;) removes every exclusion. - Radius exclusions are not supported. - A place cannot be both targeted and excluded: a request whose result would leave one on both sides returns 400 before anything is written. - Moving a place from one side to the other in the same request is applied atomically.  Example: &#x60;{ \&quot;platform\&quot;: \&quot;google\&quot;, \&quot;targeting\&quot;: { \&quot;excludedLocations\&quot;: { \&quot;countries\&quot;: [\&quot;CA\&quot;], \&quot;regions\&quot;: [\&quot;21137\&quot;] } } }&#x60;.  ### Atomic writes and response  The removes and the creates go out in ONE Google &#x60;googleAds:mutate&#x60;, so a failed edit leaves the campaign&#39;s previous set intact rather than a half-applied one.  The response includes the refreshed &#x60;devices&#x60;/&#x60;locations&#x60;/&#x60;excludedLocations&#x60;/&#x60;languages&#x60; state read back from Google after the edit. It also invalidates the cached copy &#x60;GET&#x60; on this campaign would otherwise keep serving.  ### Demand Gen  Google keeps a Demand Gen campaign&#39;s locations and languages on its ad groups and refuses them on the campaign.  - With one ad group, they are written there and the response carries its &#x60;adGroupId&#x60; (the campaign-level &#x60;locations&#x60;/&#x60;languages&#x60; read back then stay empty). - With several ad groups, the call returns 400 naming them. Edit each one with PUT /v1/ads/{adId} &#x60;targeting&#x60; on an ad of that ad group. - Campaigns migrated from Discovery that still target on the campaign keep being written there. - &#x60;devices&#x60; and &#x60;locationTargetingType&#x60; stay campaign-level. - &#x60;excludedLocations&#x60; is not available on Demand Gen yet and returns 400. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Google platform campaign ID
        UpdateCampaignTargetingRequest updateCampaignTargetingRequest = new UpdateCampaignTargetingRequest(); // UpdateCampaignTargetingRequest | 
        try {
            UpdateCampaignTargeting200Response result = apiInstance.updateCampaignTargeting(campaignId, updateCampaignTargetingRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateCampaignTargeting");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Google platform campaign ID | |
| **updateCampaignTargetingRequest** | [**UpdateCampaignTargetingRequest**](UpdateCampaignTargetingRequest.md)|  | |

### Return type

[**UpdateCampaignTargeting200Response**](UpdateCampaignTargeting200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Targeting updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Returned with one of these codes:  - &#x60;ads_allowance_exceeded&#x60;: the team has no payment method on file and has reached the 500 free live ads. Add a card to resume. - &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix &#x60;ad_account_not_selected&#x60;, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | Campaign not found |  -  |
| **501** | Only available on Google Ads campaigns |  -  |

## updateCampaignTargetingWithHttpInfo

> ApiResponse<UpdateCampaignTargeting200Response> updateCampaignTargeting updateCampaignTargetingWithHttpInfo(campaignId, updateCampaignTargetingRequest)

Edit a Google campaign&#39;s device, location, excluded location, or language targeting

Changes a Google campaign&#39;s device, location, excluded location or language targeting after it was created. Google only; every other platform returns 501.  Google Ads compliance row M.10: geo and language targeting set at creation must stay editable afterwards.  Send at least one of &#x60;devices&#x60;, &#x60;locations&#x60;, &#x60;excludedLocations&#x60;, &#x60;languages&#x60;, &#x60;locationTargetingType&#x60;. Each provided field REPLACES that field&#39;s existing criteria on the campaign (a full set, not a delta). Fields left out of the body are untouched.  ### Fields  - &#x60;devices&#x60;: the full set of device bid modifiers. A supported device you leave out is switched off with a bid modifier of 0, since Google cannot remove a device criterion. A device the campaign&#39;s channel does not carry, and a set that switches every device off, both return 422. - &#x60;locations&#x60;: see below. - &#x60;excludedLocations&#x60;: see below. - &#x60;languages&#x60;: an array of Google&#39;s language codes (ISO 639-1, plus variants such as &#x60;zh_CN&#x60;). An unknown code returns 400. - &#x60;locationTargetingType&#x60;: switches who the location targeting reaches. &#x60;presence&#x60; (people in or regularly in the locations) or &#x60;presence_or_interest&#x60; (also people searching for or interested in them). Example: &#x60;{ \&quot;platform\&quot;: \&quot;google\&quot;, \&quot;targeting\&quot;: { \&quot;locationTargetingType\&quot;: \&quot;presence\&quot; } }&#x60;.  ### Locations  &#x60;locations&#x60; accepts the same shapes as campaign creation: a bare array of ISO country codes, or an object with &#x60;countries&#x60;/&#x60;regions&#x60;/&#x60;cities&#x60;/&#x60;zips&#x60;/&#x60;metros&#x60; key lists (&#x60;key&#x60; from GET /v1/ads/targeting/search?dimension&#x3D;geo).  Excluded locations are left untouched by &#x60;locations&#x60;. An empty location list returns 400 instead of removing every criterion: a Google campaign with no location criteria targets every country, so omit &#x60;locations&#x60; to leave targeting alone.  ### Excluded locations  &#x60;excludedLocations&#x60; takes the same two shapes and replaces the campaign&#39;s negative location criteria (the places it never serves in), leaving the targeted &#x60;locations&#x60; untouched.  - An empty list (or &#x60;{}&#x60;) removes every exclusion. - Radius exclusions are not supported. - A place cannot be both targeted and excluded: a request whose result would leave one on both sides returns 400 before anything is written. - Moving a place from one side to the other in the same request is applied atomically.  Example: &#x60;{ \&quot;platform\&quot;: \&quot;google\&quot;, \&quot;targeting\&quot;: { \&quot;excludedLocations\&quot;: { \&quot;countries\&quot;: [\&quot;CA\&quot;], \&quot;regions\&quot;: [\&quot;21137\&quot;] } } }&#x60;.  ### Atomic writes and response  The removes and the creates go out in ONE Google &#x60;googleAds:mutate&#x60;, so a failed edit leaves the campaign&#39;s previous set intact rather than a half-applied one.  The response includes the refreshed &#x60;devices&#x60;/&#x60;locations&#x60;/&#x60;excludedLocations&#x60;/&#x60;languages&#x60; state read back from Google after the edit. It also invalidates the cached copy &#x60;GET&#x60; on this campaign would otherwise keep serving.  ### Demand Gen  Google keeps a Demand Gen campaign&#39;s locations and languages on its ad groups and refuses them on the campaign.  - With one ad group, they are written there and the response carries its &#x60;adGroupId&#x60; (the campaign-level &#x60;locations&#x60;/&#x60;languages&#x60; read back then stay empty). - With several ad groups, the call returns 400 naming them. Edit each one with PUT /v1/ads/{adId} &#x60;targeting&#x60; on an ad of that ad group. - Campaigns migrated from Discovery that still target on the campaign keep being written there. - &#x60;devices&#x60; and &#x60;locationTargetingType&#x60; stay campaign-level. - &#x60;excludedLocations&#x60; is not available on Demand Gen yet and returns 400. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Google platform campaign ID
        UpdateCampaignTargetingRequest updateCampaignTargetingRequest = new UpdateCampaignTargetingRequest(); // UpdateCampaignTargetingRequest | 
        try {
            ApiResponse<UpdateCampaignTargeting200Response> response = apiInstance.updateCampaignTargetingWithHttpInfo(campaignId, updateCampaignTargetingRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateCampaignTargeting");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Google platform campaign ID | |
| **updateCampaignTargetingRequest** | [**UpdateCampaignTargetingRequest**](UpdateCampaignTargetingRequest.md)|  | |

### Return type

ApiResponse<[**UpdateCampaignTargeting200Response**](UpdateCampaignTargeting200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Targeting updated |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Returned with one of these codes:  - &#x60;ads_allowance_exceeded&#x60;: the team has no payment method on file and has reached the 500 free live ads. Add a card to resume. - &#x60;ad_account_not_selected&#x60;: the connection has selected ad accounts and the targeted ad account is not among them. &#x60;details&#x60; carries &#x60;accountId&#x60;, &#x60;adAccountId&#x60; and &#x60;selectedAdAccountIds&#x60;.  To fix &#x60;ad_account_not_selected&#x60;, add the ad account to the selection (GET /v1/connect/{platform}/ads with adAccountIds, which replaces the selection) or use a connection that has it selected.  |  -  |
| **404** | Campaign not found |  -  |
| **501** | Only available on Google Ads campaigns |  -  |


## updateGoogleAssetGroup

> UpdateGoogleAssetGroup200Response updateGoogleAssetGroup(campaignId, assetGroupId, updateGoogleAssetGroupRequest)

Update a Performance Max asset group

Changes a Performance Max asset group&#39;s name, status, final URLs or display paths.  Change the name, status (ENABLED or PAUSED), final URLs or display paths. Only the fields sent are written; null on path1 or path2 clears it. Change assets with the /assets endpoint and product targeting with /listing-group-filters. validateOnly: true validates without writing. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Google Ads campaign id.
        String assetGroupId = "assetGroupId_example"; // String | Google asset group id.
        UpdateGoogleAssetGroupRequest updateGoogleAssetGroupRequest = new UpdateGoogleAssetGroupRequest(); // UpdateGoogleAssetGroupRequest | 
        try {
            UpdateGoogleAssetGroup200Response result = apiInstance.updateGoogleAssetGroup(campaignId, assetGroupId, updateGoogleAssetGroupRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateGoogleAssetGroup");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Google Ads campaign id. | |
| **assetGroupId** | **String**| Google asset group id. | |
| **updateGoogleAssetGroupRequest** | [**UpdateGoogleAssetGroupRequest**](UpdateGoogleAssetGroupRequest.md)|  | |

### Return type

[**UpdateGoogleAssetGroup200Response**](UpdateGoogleAssetGroup200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated (or validated). |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **404** | Resource not found |  -  |
| **422** | Google Ads connection needs reconnecting. |  -  |
| **429** | Google quota or the Zernio Google operations burst limit is exhausted. |  -  |
| **501** | Campaign is not on Google Ads. |  -  |

## updateGoogleAssetGroupWithHttpInfo

> ApiResponse<UpdateGoogleAssetGroup200Response> updateGoogleAssetGroup updateGoogleAssetGroupWithHttpInfo(campaignId, assetGroupId, updateGoogleAssetGroupRequest)

Update a Performance Max asset group

Changes a Performance Max asset group&#39;s name, status, final URLs or display paths.  Change the name, status (ENABLED or PAUSED), final URLs or display paths. Only the fields sent are written; null on path1 or path2 clears it. Change assets with the /assets endpoint and product targeting with /listing-group-filters. validateOnly: true validates without writing. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdCampaignsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdCampaignsApi apiInstance = new AdCampaignsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Google Ads campaign id.
        String assetGroupId = "assetGroupId_example"; // String | Google asset group id.
        UpdateGoogleAssetGroupRequest updateGoogleAssetGroupRequest = new UpdateGoogleAssetGroupRequest(); // UpdateGoogleAssetGroupRequest | 
        try {
            ApiResponse<UpdateGoogleAssetGroup200Response> response = apiInstance.updateGoogleAssetGroupWithHttpInfo(campaignId, assetGroupId, updateGoogleAssetGroupRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdCampaignsApi#updateGoogleAssetGroup");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Google Ads campaign id. | |
| **assetGroupId** | **String**| Google asset group id. | |
| **updateGoogleAssetGroupRequest** | [**UpdateGoogleAssetGroupRequest**](UpdateGoogleAssetGroupRequest.md)|  | |

### Return type

ApiResponse<[**UpdateGoogleAssetGroup200Response**](UpdateGoogleAssetGroup200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated (or validated). |  -  |
| **400** | Invalid request |  -  |
| **401** | Missing or invalid API key. &#x60;code&#x60; is &#x60;missing_credentials&#x60; when no Authorization header was sent and &#x60;invalid_credentials&#x60; when the key is unknown, revoked or expired. |  -  |
| **403** | Code &#x60;ad_account_not_selected&#x60;. The connection has selected ad accounts (its ad-account scope, set with the dashboard picker or GET /v1/connect/{platform}/ads with adAccountIds) and the targeted ad account is not among them. The connection may not act on it, even though its token can reach it.  &#x60;details&#x60; carries &#x60;accountId&#x60; (the connection), &#x60;adAccountId&#x60; (the refused ad account) and &#x60;selectedAdAccountIds&#x60;.  Fix: add the ad account to the selection (adAccountIds replaces the whole selection, so pass the ids already selected plus this one) or use a connection that has it selected. Connections without a selection keep reaching every ad account their token can manage.  |  -  |
| **404** | Resource not found |  -  |
| **422** | Google Ads connection needs reconnecting. |  -  |
| **429** | Google quota or the Zernio Google operations burst limit is exhausted. |  -  |
| **501** | Campaign is not on Google Ads. |  -  |

