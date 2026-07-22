# AdsApi

All URIs are relative to *https://zernio.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addConversionAssociations**](AdsApi.md#addConversionAssociations) | **POST** /v1/accounts/{accountId}/conversion-destinations/{destinationId}/associations | Associate campaigns |
| [**addConversionAssociationsWithHttpInfo**](AdsApi.md#addConversionAssociationsWithHttpInfo) | **POST** /v1/accounts/{accountId}/conversion-destinations/{destinationId}/associations | Associate campaigns |
| [**adjustConversions**](AdsApi.md#adjustConversions) | **POST** /v1/ads/conversions/adjustments | Adjust uploaded conversions |
| [**adjustConversionsWithHttpInfo**](AdsApi.md#adjustConversionsWithHttpInfo) | **POST** /v1/ads/conversions/adjustments | Adjust uploaded conversions |
| [**archiveLeadForm**](AdsApi.md#archiveLeadForm) | **DELETE** /v1/ads/lead-forms/{formId} | Archive a lead form |
| [**archiveLeadFormWithHttpInfo**](AdsApi.md#archiveLeadFormWithHttpInfo) | **DELETE** /v1/ads/lead-forms/{formId} | Archive a lead form |
| [**boostPost**](AdsApi.md#boostPost) | **POST** /v1/ads/boost | Boost post as ad |
| [**boostPostWithHttpInfo**](AdsApi.md#boostPostWithHttpInfo) | **POST** /v1/ads/boost | Boost post as ad |
| [**cancelRfReservation**](AdsApi.md#cancelRfReservation) | **DELETE** /v1/ads/rf-predictions/{predictionId} | Cancel a Reach &amp; Frequency reservation (Meta) |
| [**cancelRfReservationWithHttpInfo**](AdsApi.md#cancelRfReservationWithHttpInfo) | **DELETE** /v1/ads/rf-predictions/{predictionId} | Cancel a Reach &amp; Frequency reservation (Meta) |
| [**createAdCreative**](AdsApi.md#createAdCreative) | **POST** /v1/ads/creatives | Create a standalone creative (Meta) |
| [**createAdCreativeWithHttpInfo**](AdsApi.md#createAdCreativeWithHttpInfo) | **POST** /v1/ads/creatives | Create a standalone creative (Meta) |
| [**createAdInsightsReport**](AdsApi.md#createAdInsightsReport) | **POST** /v1/ads/insights/reports | Submit an async insights report run (Meta) |
| [**createAdInsightsReportWithHttpInfo**](AdsApi.md#createAdInsightsReportWithHttpInfo) | **POST** /v1/ads/insights/reports | Submit an async insights report run (Meta) |
| [**createCallAd**](AdsApi.md#createCallAd) | **POST** /v1/ads/call | Create Click-to-Call ad |
| [**createCallAdWithHttpInfo**](AdsApi.md#createCallAdWithHttpInfo) | **POST** /v1/ads/call | Create Click-to-Call ad |
| [**createConversionDestination**](AdsApi.md#createConversionDestination) | **POST** /v1/accounts/{accountId}/conversion-destinations | Create a conversion destination |
| [**createConversionDestinationWithHttpInfo**](AdsApi.md#createConversionDestinationWithHttpInfo) | **POST** /v1/accounts/{accountId}/conversion-destinations | Create a conversion destination |
| [**createCtwaAd**](AdsApi.md#createCtwaAd) | **POST** /v1/ads/ctwa | Create Click-to-WhatsApp ad (deprecated) |
| [**createCtwaAdWithHttpInfo**](AdsApi.md#createCtwaAdWithHttpInfo) | **POST** /v1/ads/ctwa | Create Click-to-WhatsApp ad (deprecated) |
| [**createLeadForm**](AdsApi.md#createLeadForm) | **POST** /v1/ads/lead-forms | Create a lead form |
| [**createLeadFormWithHttpInfo**](AdsApi.md#createLeadFormWithHttpInfo) | **POST** /v1/ads/lead-forms | Create a lead form |
| [**createMessagingAd**](AdsApi.md#createMessagingAd) | **POST** /v1/ads/messaging | Create click-to-message ad (WhatsApp / Messenger / Instagram Direct) |
| [**createMessagingAdWithHttpInfo**](AdsApi.md#createMessagingAdWithHttpInfo) | **POST** /v1/ads/messaging | Create click-to-message ad (WhatsApp / Messenger / Instagram Direct) |
| [**createRfPrediction**](AdsApi.md#createRfPrediction) | **POST** /v1/ads/rf-predictions | Create a Reach &amp; Frequency prediction (Meta) |
| [**createRfPredictionWithHttpInfo**](AdsApi.md#createRfPredictionWithHttpInfo) | **POST** /v1/ads/rf-predictions | Create a Reach &amp; Frequency prediction (Meta) |
| [**createStandaloneAd**](AdsApi.md#createStandaloneAd) | **POST** /v1/ads/create | Create standalone ad |
| [**createStandaloneAdWithHttpInfo**](AdsApi.md#createStandaloneAdWithHttpInfo) | **POST** /v1/ads/create | Create standalone ad |
| [**createTestLead**](AdsApi.md#createTestLead) | **POST** /v1/ads/lead-forms/{formId}/test-leads | Create a test lead |
| [**createTestLeadWithHttpInfo**](AdsApi.md#createTestLeadWithHttpInfo) | **POST** /v1/ads/lead-forms/{formId}/test-leads | Create a test lead |
| [**deleteAd**](AdsApi.md#deleteAd) | **DELETE** /v1/ads/{adId} | Cancel an ad |
| [**deleteAdWithHttpInfo**](AdsApi.md#deleteAdWithHttpInfo) | **DELETE** /v1/ads/{adId} | Cancel an ad |
| [**deleteAdCreative**](AdsApi.md#deleteAdCreative) | **DELETE** /v1/ads/creatives/{creativeId} | Delete a creative (Meta) |
| [**deleteAdCreativeWithHttpInfo**](AdsApi.md#deleteAdCreativeWithHttpInfo) | **DELETE** /v1/ads/creatives/{creativeId} | Delete a creative (Meta) |
| [**deleteConversionDestination**](AdsApi.md#deleteConversionDestination) | **DELETE** /v1/accounts/{accountId}/conversion-destinations/{destinationId} | Delete a conversion destination |
| [**deleteConversionDestinationWithHttpInfo**](AdsApi.md#deleteConversionDestinationWithHttpInfo) | **DELETE** /v1/accounts/{accountId}/conversion-destinations/{destinationId} | Delete a conversion destination |
| [**duplicateAd**](AdsApi.md#duplicateAd) | **POST** /v1/ads/{adId}/duplicate | Duplicate an ad (Meta) |
| [**duplicateAdWithHttpInfo**](AdsApi.md#duplicateAdWithHttpInfo) | **POST** /v1/ads/{adId}/duplicate | Duplicate an ad (Meta) |
| [**estimateAdReach**](AdsApi.md#estimateAdReach) | **POST** /v1/ads/targeting/reach-estimate | Estimate audience reach |
| [**estimateAdReachWithHttpInfo**](AdsApi.md#estimateAdReachWithHttpInfo) | **POST** /v1/ads/targeting/reach-estimate | Estimate audience reach |
| [**generateAdPreviews**](AdsApi.md#generateAdPreviews) | **POST** /v1/ads/preview | Render pre-create ad previews (Meta) |
| [**generateAdPreviewsWithHttpInfo**](AdsApi.md#generateAdPreviewsWithHttpInfo) | **POST** /v1/ads/preview | Render pre-create ad previews (Meta) |
| [**getAd**](AdsApi.md#getAd) | **GET** /v1/ads/{adId} | Get ad details |
| [**getAdWithHttpInfo**](AdsApi.md#getAdWithHttpInfo) | **GET** /v1/ads/{adId} | Get ad details |
| [**getAdAccountFinance**](AdsApi.md#getAdAccountFinance) | **GET** /v1/ads/accounts/finance | Ad account finances (Meta) |
| [**getAdAccountFinanceWithHttpInfo**](AdsApi.md#getAdAccountFinanceWithHttpInfo) | **GET** /v1/ads/accounts/finance | Ad account finances (Meta) |
| [**getAdAnalytics**](AdsApi.md#getAdAnalytics) | **GET** /v1/ads/{adId}/analytics | Get ad analytics |
| [**getAdAnalyticsWithHttpInfo**](AdsApi.md#getAdAnalyticsWithHttpInfo) | **GET** /v1/ads/{adId}/analytics | Get ad analytics |
| [**getAdComments**](AdsApi.md#getAdComments) | **GET** /v1/ads/{adId}/comments | List comments on an ad |
| [**getAdCommentsWithHttpInfo**](AdsApi.md#getAdCommentsWithHttpInfo) | **GET** /v1/ads/{adId}/comments | List comments on an ad |
| [**getAdCreative**](AdsApi.md#getAdCreative) | **GET** /v1/ads/creatives/{creativeId} | Creative details (Meta) |
| [**getAdCreativeWithHttpInfo**](AdsApi.md#getAdCreativeWithHttpInfo) | **GET** /v1/ads/creatives/{creativeId} | Creative details (Meta) |
| [**getAdInsightsReport**](AdsApi.md#getAdInsightsReport) | **GET** /v1/ads/insights/reports/{reportRunId} | Poll an async insights report run (Meta) |
| [**getAdInsightsReportWithHttpInfo**](AdsApi.md#getAdInsightsReportWithHttpInfo) | **GET** /v1/ads/insights/reports/{reportRunId} | Poll an async insights report run (Meta) |
| [**getAdPreviews**](AdsApi.md#getAdPreviews) | **GET** /v1/ads/{adId}/preview | Render previews of an existing ad (Meta) |
| [**getAdPreviewsWithHttpInfo**](AdsApi.md#getAdPreviewsWithHttpInfo) | **GET** /v1/ads/{adId}/preview | Render previews of an existing ad (Meta) |
| [**getAdTrackingTags**](AdsApi.md#getAdTrackingTags) | **GET** /v1/ads/{adId}/tracking-tags | Get ad tracking tags |
| [**getAdTrackingTagsWithHttpInfo**](AdsApi.md#getAdTrackingTagsWithHttpInfo) | **GET** /v1/ads/{adId}/tracking-tags | Get ad tracking tags |
| [**getAdsActivityLog**](AdsApi.md#getAdsActivityLog) | **GET** /v1/ads/activity | Ad account change / audit log (Meta) |
| [**getAdsActivityLogWithHttpInfo**](AdsApi.md#getAdsActivityLogWithHttpInfo) | **GET** /v1/ads/activity | Ad account change / audit log (Meta) |
| [**getCampaignAnalytics**](AdsApi.md#getCampaignAnalytics) | **GET** /v1/ads/campaigns/{campaignId}/analytics | Get campaign analytics |
| [**getCampaignAnalyticsWithHttpInfo**](AdsApi.md#getCampaignAnalyticsWithHttpInfo) | **GET** /v1/ads/campaigns/{campaignId}/analytics | Get campaign analytics |
| [**getConversionDestination**](AdsApi.md#getConversionDestination) | **GET** /v1/accounts/{accountId}/conversion-destinations/{destinationId} | Get a conversion destination |
| [**getConversionDestinationWithHttpInfo**](AdsApi.md#getConversionDestinationWithHttpInfo) | **GET** /v1/accounts/{accountId}/conversion-destinations/{destinationId} | Get a conversion destination |
| [**getConversionMetrics**](AdsApi.md#getConversionMetrics) | **GET** /v1/accounts/{accountId}/conversion-destinations/{destinationId}/metrics | Get attribution metrics |
| [**getConversionMetricsWithHttpInfo**](AdsApi.md#getConversionMetricsWithHttpInfo) | **GET** /v1/accounts/{accountId}/conversion-destinations/{destinationId}/metrics | Get attribution metrics |
| [**getConversionsQuality**](AdsApi.md#getConversionsQuality) | **GET** /v1/ads/conversions/quality | Get Event Match Quality |
| [**getConversionsQualityWithHttpInfo**](AdsApi.md#getConversionsQualityWithHttpInfo) | **GET** /v1/ads/conversions/quality | Get Event Match Quality |
| [**getDsaDefaults**](AdsApi.md#getDsaDefaults) | **GET** /v1/ads/dsa-defaults | Get ad account DSA defaults |
| [**getDsaDefaultsWithHttpInfo**](AdsApi.md#getDsaDefaultsWithHttpInfo) | **GET** /v1/ads/dsa-defaults | Get ad account DSA defaults |
| [**getDsaRecommendations**](AdsApi.md#getDsaRecommendations) | **GET** /v1/ads/dsa-recommendations | List DSA beneficiary/payor suggestions |
| [**getDsaRecommendationsWithHttpInfo**](AdsApi.md#getDsaRecommendationsWithHttpInfo) | **GET** /v1/ads/dsa-recommendations | List DSA beneficiary/payor suggestions |
| [**getLeadForm**](AdsApi.md#getLeadForm) | **GET** /v1/ads/lead-forms/{formId} | Get a lead form |
| [**getLeadFormWithHttpInfo**](AdsApi.md#getLeadFormWithHttpInfo) | **GET** /v1/ads/lead-forms/{formId} | Get a lead form |
| [**getLinkedInBidPricing**](AdsApi.md#getLinkedInBidPricing) | **POST** /v1/ads/targeting/bid-pricing | Suggested bid and budget bounds (LinkedIn) |
| [**getLinkedInBidPricingWithHttpInfo**](AdsApi.md#getLinkedInBidPricingWithHttpInfo) | **POST** /v1/ads/targeting/bid-pricing | Suggested bid and budget bounds (LinkedIn) |
| [**getLinkedInSupplyForecast**](AdsApi.md#getLinkedInSupplyForecast) | **POST** /v1/ads/targeting/supply-forecast | Impressions, clicks and spend forecast (LinkedIn) |
| [**getLinkedInSupplyForecastWithHttpInfo**](AdsApi.md#getLinkedInSupplyForecastWithHttpInfo) | **POST** /v1/ads/targeting/supply-forecast | Impressions, clicks and spend forecast (LinkedIn) |
| [**getRfPrediction**](AdsApi.md#getRfPrediction) | **GET** /v1/ads/rf-predictions/{predictionId} | Read a Reach &amp; Frequency prediction (Meta) |
| [**getRfPredictionWithHttpInfo**](AdsApi.md#getRfPredictionWithHttpInfo) | **GET** /v1/ads/rf-predictions/{predictionId} | Read a Reach &amp; Frequency prediction (Meta) |
| [**listAdAccounts**](AdsApi.md#listAdAccounts) | **GET** /v1/ads/accounts | List ad accounts |
| [**listAdAccountsWithHttpInfo**](AdsApi.md#listAdAccountsWithHttpInfo) | **GET** /v1/ads/accounts | List ad accounts |
| [**listAdCatalogProductSets**](AdsApi.md#listAdCatalogProductSets) | **GET** /v1/ads/catalogs/{catalogId}/product-sets | List a catalog&#39;s product sets |
| [**listAdCatalogProductSetsWithHttpInfo**](AdsApi.md#listAdCatalogProductSetsWithHttpInfo) | **GET** /v1/ads/catalogs/{catalogId}/product-sets | List a catalog&#39;s product sets |
| [**listAdCatalogs**](AdsApi.md#listAdCatalogs) | **GET** /v1/ads/catalogs | List Meta product catalogs |
| [**listAdCatalogsWithHttpInfo**](AdsApi.md#listAdCatalogsWithHttpInfo) | **GET** /v1/ads/catalogs | List Meta product catalogs |
| [**listAdCreatives**](AdsApi.md#listAdCreatives) | **GET** /v1/ads/creatives | Creative library (Meta) |
| [**listAdCreativesWithHttpInfo**](AdsApi.md#listAdCreativesWithHttpInfo) | **GET** /v1/ads/creatives | Creative library (Meta) |
| [**listAdImages**](AdsApi.md#listAdImages) | **GET** /v1/ads/images | Ad image library (Meta) |
| [**listAdImagesWithHttpInfo**](AdsApi.md#listAdImagesWithHttpInfo) | **GET** /v1/ads/images | Ad image library (Meta) |
| [**listAdLabels**](AdsApi.md#listAdLabels) | **GET** /v1/ads/labels | Ad labels (Meta) |
| [**listAdLabelsWithHttpInfo**](AdsApi.md#listAdLabelsWithHttpInfo) | **GET** /v1/ads/labels | Ad labels (Meta) |
| [**listAdStudies**](AdsApi.md#listAdStudies) | **GET** /v1/ads/studies | A/B tests and lift studies (Meta) |
| [**listAdStudiesWithHttpInfo**](AdsApi.md#listAdStudiesWithHttpInfo) | **GET** /v1/ads/studies | A/B tests and lift studies (Meta) |
| [**listAds**](AdsApi.md#listAds) | **GET** /v1/ads | List ads |
| [**listAdsWithHttpInfo**](AdsApi.md#listAdsWithHttpInfo) | **GET** /v1/ads | List ads |
| [**listAdsBusinessCenters**](AdsApi.md#listAdsBusinessCenters) | **GET** /v1/ads/business-centers | List TikTok Business Centers |
| [**listAdsBusinessCentersWithHttpInfo**](AdsApi.md#listAdsBusinessCentersWithHttpInfo) | **GET** /v1/ads/business-centers | List TikTok Business Centers |
| [**listConversionAssociations**](AdsApi.md#listConversionAssociations) | **GET** /v1/accounts/{accountId}/conversion-destinations/{destinationId}/associations | List associated campaigns |
| [**listConversionAssociationsWithHttpInfo**](AdsApi.md#listConversionAssociationsWithHttpInfo) | **GET** /v1/accounts/{accountId}/conversion-destinations/{destinationId}/associations | List associated campaigns |
| [**listConversionDestinations**](AdsApi.md#listConversionDestinations) | **GET** /v1/accounts/{accountId}/conversion-destinations | List conversion destinations |
| [**listConversionDestinationsWithHttpInfo**](AdsApi.md#listConversionDestinationsWithHttpInfo) | **GET** /v1/accounts/{accountId}/conversion-destinations | List conversion destinations |
| [**listFormLeads**](AdsApi.md#listFormLeads) | **GET** /v1/ads/lead-forms/{formId}/leads | List leads for a single form |
| [**listFormLeadsWithHttpInfo**](AdsApi.md#listFormLeadsWithHttpInfo) | **GET** /v1/ads/lead-forms/{formId}/leads | List leads for a single form |
| [**listHighDemandPeriods**](AdsApi.md#listHighDemandPeriods) | **GET** /v1/ads/high-demand-periods | High demand periods / budget schedules (Meta) |
| [**listHighDemandPeriodsWithHttpInfo**](AdsApi.md#listHighDemandPeriodsWithHttpInfo) | **GET** /v1/ads/high-demand-periods | High demand periods / budget schedules (Meta) |
| [**listLeadForms**](AdsApi.md#listLeadForms) | **GET** /v1/ads/lead-forms | List lead forms |
| [**listLeadFormsWithHttpInfo**](AdsApi.md#listLeadFormsWithHttpInfo) | **GET** /v1/ads/lead-forms | List lead forms |
| [**listLeads**](AdsApi.md#listLeads) | **GET** /v1/ads/leads | List submitted leads |
| [**listLeadsWithHttpInfo**](AdsApi.md#listLeadsWithHttpInfo) | **GET** /v1/ads/leads | List submitted leads |
| [**listMetaBusinesses**](AdsApi.md#listMetaBusinesses) | **GET** /v1/ads/businesses | Businesses list (Meta) |
| [**listMetaBusinessesWithHttpInfo**](AdsApi.md#listMetaBusinessesWithHttpInfo) | **GET** /v1/ads/businesses | Businesses list (Meta) |
| [**listWhatsAppConversions**](AdsApi.md#listWhatsAppConversions) | **GET** /v1/whatsapp/conversions | List conversion events |
| [**listWhatsAppConversionsWithHttpInfo**](AdsApi.md#listWhatsAppConversionsWithHttpInfo) | **GET** /v1/whatsapp/conversions | List conversion events |
| [**queryAdInsights**](AdsApi.md#queryAdInsights) | **GET** /v1/ads/insights | Flexible live insights query (Meta) |
| [**queryAdInsightsWithHttpInfo**](AdsApi.md#queryAdInsightsWithHttpInfo) | **GET** /v1/ads/insights | Flexible live insights query (Meta) |
| [**removeConversionAssociations**](AdsApi.md#removeConversionAssociations) | **DELETE** /v1/accounts/{accountId}/conversion-destinations/{destinationId}/associations | Remove associated campaigns |
| [**removeConversionAssociationsWithHttpInfo**](AdsApi.md#removeConversionAssociationsWithHttpInfo) | **DELETE** /v1/accounts/{accountId}/conversion-destinations/{destinationId}/associations | Remove associated campaigns |
| [**reserveRfPrediction**](AdsApi.md#reserveRfPrediction) | **POST** /v1/ads/rf-predictions/{predictionId}/reserve | Reserve a Reach &amp; Frequency prediction (Meta) |
| [**reserveRfPredictionWithHttpInfo**](AdsApi.md#reserveRfPredictionWithHttpInfo) | **POST** /v1/ads/rf-predictions/{predictionId}/reserve | Reserve a Reach &amp; Frequency prediction (Meta) |
| [**searchAdInterests**](AdsApi.md#searchAdInterests) | **GET** /v1/ads/interests | Search targeting interests |
| [**searchAdInterestsWithHttpInfo**](AdsApi.md#searchAdInterestsWithHttpInfo) | **GET** /v1/ads/interests | Search targeting interests |
| [**searchAdTargeting**](AdsApi.md#searchAdTargeting) | **GET** /v1/ads/targeting/search | Search targeting options |
| [**searchAdTargetingWithHttpInfo**](AdsApi.md#searchAdTargetingWithHttpInfo) | **GET** /v1/ads/targeting/search | Search targeting options |
| [**sendConversions**](AdsApi.md#sendConversions) | **POST** /v1/ads/conversions | Send conversion events |
| [**sendConversionsWithHttpInfo**](AdsApi.md#sendConversionsWithHttpInfo) | **POST** /v1/ads/conversions | Send conversion events |
| [**sendWhatsAppConversion**](AdsApi.md#sendWhatsAppConversion) | **POST** /v1/whatsapp/conversions | Send WhatsApp conversion event |
| [**sendWhatsAppConversionWithHttpInfo**](AdsApi.md#sendWhatsAppConversionWithHttpInfo) | **POST** /v1/whatsapp/conversions | Send WhatsApp conversion event |
| [**updateAd**](AdsApi.md#updateAd) | **PUT** /v1/ads/{adId} | Update ad |
| [**updateAdWithHttpInfo**](AdsApi.md#updateAdWithHttpInfo) | **PUT** /v1/ads/{adId} | Update ad |
| [**updateAdAccount**](AdsApi.md#updateAdAccount) | **PATCH** /v1/ads/accounts | Update ad account settings |
| [**updateAdAccountWithHttpInfo**](AdsApi.md#updateAdAccountWithHttpInfo) | **PATCH** /v1/ads/accounts | Update ad account settings |
| [**updateAdCreative**](AdsApi.md#updateAdCreative) | **PUT** /v1/ads/creatives/{creativeId} | Rename a creative (Meta) |
| [**updateAdCreativeWithHttpInfo**](AdsApi.md#updateAdCreativeWithHttpInfo) | **PUT** /v1/ads/creatives/{creativeId} | Rename a creative (Meta) |
| [**updateAdStatus**](AdsApi.md#updateAdStatus) | **PUT** /v1/ads/{adId}/status | Pause or resume a single ad |
| [**updateAdStatusWithHttpInfo**](AdsApi.md#updateAdStatusWithHttpInfo) | **PUT** /v1/ads/{adId}/status | Pause or resume a single ad |
| [**updateAdTrackingTags**](AdsApi.md#updateAdTrackingTags) | **PATCH** /v1/ads/{adId}/tracking-tags | Set ad tracking tags |
| [**updateAdTrackingTagsWithHttpInfo**](AdsApi.md#updateAdTrackingTagsWithHttpInfo) | **PATCH** /v1/ads/{adId}/tracking-tags | Set ad tracking tags |
| [**updateConversionDestination**](AdsApi.md#updateConversionDestination) | **PATCH** /v1/accounts/{accountId}/conversion-destinations/{destinationId} | Update a conversion destination |
| [**updateConversionDestinationWithHttpInfo**](AdsApi.md#updateConversionDestinationWithHttpInfo) | **PATCH** /v1/accounts/{accountId}/conversion-destinations/{destinationId} | Update a conversion destination |
| [**uploadAdImage**](AdsApi.md#uploadAdImage) | **POST** /v1/ads/images | Upload an ad image from base64 (Meta) |
| [**uploadAdImageWithHttpInfo**](AdsApi.md#uploadAdImageWithHttpInfo) | **POST** /v1/ads/images | Upload an ad image from base64 (Meta) |



## addConversionAssociations

> AddConversionAssociations200Response addConversionAssociations(accountId, destinationId, addConversionAssociationsRequest)

Associate campaigns

Associate one or more campaigns with this conversion rule. Returns a per-campaign success/failure result so callers can retry only the rows that failed (e.g. wrong campaign type for the rule&#39;s objective). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String destinationId = "destinationId_example"; // String | 
        AddConversionAssociationsRequest addConversionAssociationsRequest = new AddConversionAssociationsRequest(); // AddConversionAssociationsRequest | 
        try {
            AddConversionAssociations200Response result = apiInstance.addConversionAssociations(accountId, destinationId, addConversionAssociationsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#addConversionAssociations");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**|  | |
| **destinationId** | **String**|  | |
| **addConversionAssociationsRequest** | [**AddConversionAssociationsRequest**](AddConversionAssociationsRequest.md)|  | |

### Return type

[**AddConversionAssociations200Response**](AddConversionAssociations200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-campaign batch result. Status is 200 even when some rows failed — inspect &#x60;failed[]&#x60; for details. Inputs that fail local URN validation are bucketed into &#x60;failed&#x60; without ever hitting LinkedIn.  |  -  |
| **400** | Invalid body. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on or LinkedIn reconnect required. |  -  |
| **404** | Account or destination not found. |  -  |
| **405** | Platform does not support associations. |  -  |
| **429** | LinkedIn rate limit hit. Retry with backoff. |  -  |

## addConversionAssociationsWithHttpInfo

> ApiResponse<AddConversionAssociations200Response> addConversionAssociations addConversionAssociationsWithHttpInfo(accountId, destinationId, addConversionAssociationsRequest)

Associate campaigns

Associate one or more campaigns with this conversion rule. Returns a per-campaign success/failure result so callers can retry only the rows that failed (e.g. wrong campaign type for the rule&#39;s objective). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String destinationId = "destinationId_example"; // String | 
        AddConversionAssociationsRequest addConversionAssociationsRequest = new AddConversionAssociationsRequest(); // AddConversionAssociationsRequest | 
        try {
            ApiResponse<AddConversionAssociations200Response> response = apiInstance.addConversionAssociationsWithHttpInfo(accountId, destinationId, addConversionAssociationsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#addConversionAssociations");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**|  | |
| **destinationId** | **String**|  | |
| **addConversionAssociationsRequest** | [**AddConversionAssociationsRequest**](AddConversionAssociationsRequest.md)|  | |

### Return type

ApiResponse<[**AddConversionAssociations200Response**](AddConversionAssociations200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-campaign batch result. Status is 200 even when some rows failed — inspect &#x60;failed[]&#x60; for details. Inputs that fail local URN validation are bucketed into &#x60;failed&#x60; without ever hitting LinkedIn.  |  -  |
| **400** | Invalid body. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on or LinkedIn reconnect required. |  -  |
| **404** | Account or destination not found. |  -  |
| **405** | Platform does not support associations. |  -  |
| **429** | LinkedIn rate limit hit. Retry with backoff. |  -  |


## adjustConversions

> AdjustConversions200Response adjustConversions(adjustConversionsRequest)

Adjust uploaded conversions

Adjust conversions that were previously uploaded via &#x60;POST /v1/ads/conversions&#x60; — retract them, restate their value, or enhance them with first-party data. Requires the Ads add-on.  **Google Ads only.** Google handles adjustments through the classic Google Ads API (&#x60;ConversionAdjustmentUploadService&#x60;); the Data Manager &#x60;ingestEvents&#x60; path used for sending conversions is ingest-only. Meta and LinkedIn have no equivalent, so this endpoint returns &#x60;405&#x60; for those platforms.  Adjustment types:  - &#x60;RETRACTION&#x60; — remove the conversion entirely (refund, chargeback, cancelled order, churn). - &#x60;RESTATEMENT&#x60; — change the conversion&#39;s value (upgrade / downgrade / partial refund). Send the corrected **total** value in &#x60;restatementValue&#x60; (not a delta). - &#x60;ENHANCEMENT&#x60; — attach first-party identifiers (hashed email / phone) to an existing conversion (enhanced conversions applied after the fact).  Identifying the original conversion (per adjustment):  - &#x60;orderId&#x60; — the transaction ID you sent as &#x60;eventId&#x60; on the original conversion. Recommended, and **required** for &#x60;ENHANCEMENT&#x60;. - or &#x60;gclid&#x60; + &#x60;conversionTime&#x60; — the click ID and the original conversion&#39;s time (unix seconds). Not available for &#x60;ENHANCEMENT&#x60;.  &#x60;destinationId&#x60; is the conversion action resource name, e.g. &#x60;customers/1234567890/conversionActions/987654321&#x60; (same value you send to &#x60;POST /v1/ads/conversions&#x60;). PII in &#x60;user&#x60; is hashed with SHA-256 server-side (Gmail-specific normalization included). Send plaintext.  Times are unix seconds; we convert to Google&#39;s required &#x60;yyyy-MM-dd HH:mm:ss+00:00&#x60; format. Up to 2000 adjustments per request; partial failure is supported (inspect &#x60;adjustmentsFailed&#x60; / &#x60;failures[]&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        AdjustConversionsRequest adjustConversionsRequest = new AdjustConversionsRequest(); // AdjustConversionsRequest | 
        try {
            AdjustConversions200Response result = apiInstance.adjustConversions(adjustConversionsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#adjustConversions");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adjustConversionsRequest** | [**AdjustConversionsRequest**](AdjustConversionsRequest.md)|  | |

### Return type

[**AdjustConversions200Response**](AdjustConversions200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Adjustments processed. Inspect &#x60;adjustmentsFailed&#x60; and &#x60;failures[]&#x60; for partial failure (Google reports per-row errors via partial failure).  |  -  |
| **400** | Invalid body, or a malformed adjustment (missing key, missing restatementValue for RESTATEMENT, missing identifiers for ENHANCEMENT). |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans). |  -  |
| **404** | Account not found or not accessible. |  -  |
| **405** | Conversion adjustments are only available for Google Ads (the account&#39;s platform is not &#x60;googleads&#x60;). |  -  |

## adjustConversionsWithHttpInfo

> ApiResponse<AdjustConversions200Response> adjustConversions adjustConversionsWithHttpInfo(adjustConversionsRequest)

Adjust uploaded conversions

Adjust conversions that were previously uploaded via &#x60;POST /v1/ads/conversions&#x60; — retract them, restate their value, or enhance them with first-party data. Requires the Ads add-on.  **Google Ads only.** Google handles adjustments through the classic Google Ads API (&#x60;ConversionAdjustmentUploadService&#x60;); the Data Manager &#x60;ingestEvents&#x60; path used for sending conversions is ingest-only. Meta and LinkedIn have no equivalent, so this endpoint returns &#x60;405&#x60; for those platforms.  Adjustment types:  - &#x60;RETRACTION&#x60; — remove the conversion entirely (refund, chargeback, cancelled order, churn). - &#x60;RESTATEMENT&#x60; — change the conversion&#39;s value (upgrade / downgrade / partial refund). Send the corrected **total** value in &#x60;restatementValue&#x60; (not a delta). - &#x60;ENHANCEMENT&#x60; — attach first-party identifiers (hashed email / phone) to an existing conversion (enhanced conversions applied after the fact).  Identifying the original conversion (per adjustment):  - &#x60;orderId&#x60; — the transaction ID you sent as &#x60;eventId&#x60; on the original conversion. Recommended, and **required** for &#x60;ENHANCEMENT&#x60;. - or &#x60;gclid&#x60; + &#x60;conversionTime&#x60; — the click ID and the original conversion&#39;s time (unix seconds). Not available for &#x60;ENHANCEMENT&#x60;.  &#x60;destinationId&#x60; is the conversion action resource name, e.g. &#x60;customers/1234567890/conversionActions/987654321&#x60; (same value you send to &#x60;POST /v1/ads/conversions&#x60;). PII in &#x60;user&#x60; is hashed with SHA-256 server-side (Gmail-specific normalization included). Send plaintext.  Times are unix seconds; we convert to Google&#39;s required &#x60;yyyy-MM-dd HH:mm:ss+00:00&#x60; format. Up to 2000 adjustments per request; partial failure is supported (inspect &#x60;adjustmentsFailed&#x60; / &#x60;failures[]&#x60;). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        AdjustConversionsRequest adjustConversionsRequest = new AdjustConversionsRequest(); // AdjustConversionsRequest | 
        try {
            ApiResponse<AdjustConversions200Response> response = apiInstance.adjustConversionsWithHttpInfo(adjustConversionsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#adjustConversions");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adjustConversionsRequest** | [**AdjustConversionsRequest**](AdjustConversionsRequest.md)|  | |

### Return type

ApiResponse<[**AdjustConversions200Response**](AdjustConversions200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Adjustments processed. Inspect &#x60;adjustmentsFailed&#x60; and &#x60;failures[]&#x60; for partial failure (Google reports per-row errors via partial failure).  |  -  |
| **400** | Invalid body, or a malformed adjustment (missing key, missing restatementValue for RESTATEMENT, missing identifiers for ENHANCEMENT). |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans). |  -  |
| **404** | Account not found or not accessible. |  -  |
| **405** | Conversion adjustments are only available for Google Ads (the account&#39;s platform is not &#x60;googleads&#x60;). |  -  |


## archiveLeadForm

> ArchiveLeadForm200Response archiveLeadForm(formId, accountId)

Archive a lead form

Meta has no hard delete for forms; this archives the form (status&#x3D;ARCHIVED).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String formId = "formId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            ArchiveLeadForm200Response result = apiInstance.archiveLeadForm(formId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#archiveLeadForm");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **formId** | **String**|  | |
| **accountId** | **String**|  | |

### Return type

[**ArchiveLeadForm200Response**](ArchiveLeadForm200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Archived. |  -  |
| **401** | Unauthorized |  -  |

## archiveLeadFormWithHttpInfo

> ApiResponse<ArchiveLeadForm200Response> archiveLeadForm archiveLeadFormWithHttpInfo(formId, accountId)

Archive a lead form

Meta has no hard delete for forms; this archives the form (status&#x3D;ARCHIVED).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String formId = "formId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<ArchiveLeadForm200Response> response = apiInstance.archiveLeadFormWithHttpInfo(formId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#archiveLeadForm");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **formId** | **String**|  | |
| **accountId** | **String**|  | |

### Return type

ApiResponse<[**ArchiveLeadForm200Response**](ArchiveLeadForm200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Archived. |  -  |
| **401** | Unauthorized |  -  |


## boostPost

> UpdateAd200Response boostPost(boostPostRequest)

Boost post as ad

Creates a paid ad campaign from an existing published post. Creates the full platform campaign hierarchy (campaign, ad set, ad).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        BoostPostRequest boostPostRequest = new BoostPostRequest(); // BoostPostRequest | 
        try {
            UpdateAd200Response result = apiInstance.boostPost(boostPostRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#boostPost");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
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
| **201** | Ad created |  -  |
| **400** | Missing required fields or invalid values |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **422** | Platform ads connection required (TikTok Ads, X Ads), missing linked account, or — for TikTok — the connected TikTok user is not authorized as an Identity on the target advertiser. Returned with code &#x60;ads_connection_required&#x60;; the message includes the actionable \&quot;TikTok Ads Manager → Assets → Identity\&quot; remediation step.  |  -  |

## boostPostWithHttpInfo

> ApiResponse<UpdateAd200Response> boostPost boostPostWithHttpInfo(boostPostRequest)

Boost post as ad

Creates a paid ad campaign from an existing published post. Creates the full platform campaign hierarchy (campaign, ad set, ad).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        BoostPostRequest boostPostRequest = new BoostPostRequest(); // BoostPostRequest | 
        try {
            ApiResponse<UpdateAd200Response> response = apiInstance.boostPostWithHttpInfo(boostPostRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#boostPost");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
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
| **201** | Ad created |  -  |
| **400** | Missing required fields or invalid values |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **422** | Platform ads connection required (TikTok Ads, X Ads), missing linked account, or — for TikTok — the connected TikTok user is not authorized as an Identity on the target advertiser. Returned with code &#x60;ads_connection_required&#x60;; the message includes the actionable \&quot;TikTok Ads Manager → Assets → Identity\&quot; remediation step.  |  -  |


## cancelRfReservation

> void cancelRfReservation(predictionId, accountId, adAccountId)

Cancel a Reach &amp; Frequency reservation (Meta)

Releases a RESERVATION&#39;s locked price and inventory. Unreserved predictions expire on their own.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String predictionId = "predictionId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | 
        try {
            apiInstance.cancelRfReservation(predictionId, accountId, adAccountId);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#cancelRfReservation");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **predictionId** | **String**|  | |
| **accountId** | **String**|  | |
| **adAccountId** | **String**|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reservation cancelled |  -  |
| **400** | Invalid input, or Meta rejected the cancel |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## cancelRfReservationWithHttpInfo

> ApiResponse<Void> cancelRfReservation cancelRfReservationWithHttpInfo(predictionId, accountId, adAccountId)

Cancel a Reach &amp; Frequency reservation (Meta)

Releases a RESERVATION&#39;s locked price and inventory. Unreserved predictions expire on their own.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String predictionId = "predictionId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | 
        try {
            ApiResponse<Void> response = apiInstance.cancelRfReservationWithHttpInfo(predictionId, accountId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#cancelRfReservation");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **predictionId** | **String**|  | |
| **accountId** | **String**|  | |
| **adAccountId** | **String**|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reservation cancelled |  -  |
| **400** | Invalid input, or Meta rejected the cancel |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## createAdCreative

> CreateAdCreative201Response createAdCreative(createAdCreativeRequest)

Create a standalone creative (Meta)

Creates a creative in the library WITHOUT an ad, reusable on the create endpoints via &#x60;existingCreativeId&#x60;. Provide exactly one of &#x60;imageUrl&#x60; (uploaded server-side), &#x60;imageHash&#x60; (from POST /v1/ads/images or the library list), or &#x60;carouselCards&#x60; (2-10 hand-built cards). The Page (and linked Instagram account, when present) is resolved from &#x60;accountId&#x60; as the story actor. Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        CreateAdCreativeRequest createAdCreativeRequest = new CreateAdCreativeRequest(); // CreateAdCreativeRequest | 
        try {
            CreateAdCreative201Response result = apiInstance.createAdCreative(createAdCreativeRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#createAdCreative");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createAdCreativeRequest** | [**CreateAdCreativeRequest**](CreateAdCreativeRequest.md)|  | |

### Return type

[**CreateAdCreative201Response**](CreateAdCreative201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Creative created |  -  |
| **400** | Invalid input, or Meta rejected the create |  -  |
| **401** | Unauthorized |  -  |
| **422** | No Facebook Page found to act as the story actor |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## createAdCreativeWithHttpInfo

> ApiResponse<CreateAdCreative201Response> createAdCreative createAdCreativeWithHttpInfo(createAdCreativeRequest)

Create a standalone creative (Meta)

Creates a creative in the library WITHOUT an ad, reusable on the create endpoints via &#x60;existingCreativeId&#x60;. Provide exactly one of &#x60;imageUrl&#x60; (uploaded server-side), &#x60;imageHash&#x60; (from POST /v1/ads/images or the library list), or &#x60;carouselCards&#x60; (2-10 hand-built cards). The Page (and linked Instagram account, when present) is resolved from &#x60;accountId&#x60; as the story actor. Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        CreateAdCreativeRequest createAdCreativeRequest = new CreateAdCreativeRequest(); // CreateAdCreativeRequest | 
        try {
            ApiResponse<CreateAdCreative201Response> response = apiInstance.createAdCreativeWithHttpInfo(createAdCreativeRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#createAdCreative");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createAdCreativeRequest** | [**CreateAdCreativeRequest**](CreateAdCreativeRequest.md)|  | |

### Return type

ApiResponse<[**CreateAdCreative201Response**](CreateAdCreative201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Creative created |  -  |
| **400** | Invalid input, or Meta rejected the create |  -  |
| **401** | Unauthorized |  -  |
| **422** | No Facebook Page found to act as the story actor |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## createAdInsightsReport

> CreateAdInsightsReport202Response createAdInsightsReport(createAdInsightsReportRequest)

Submit an async insights report run (Meta)

Submits an asynchronous Meta insights report. Same query surface as GET /v1/ads/insights, but in the JSON body; Meta processes the report server-side, which is the right choice for long ranges or large accounts where the sync query is slow or rate-limited. Returns a &#x60;reportRunId&#x60; to poll via GET /v1/ads/insights/reports/{reportRunId}. Meta only. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        CreateAdInsightsReportRequest createAdInsightsReportRequest = new CreateAdInsightsReportRequest(); // CreateAdInsightsReportRequest | 
        try {
            CreateAdInsightsReport202Response result = apiInstance.createAdInsightsReport(createAdInsightsReportRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#createAdInsightsReport");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createAdInsightsReportRequest** | [**CreateAdInsightsReportRequest**](CreateAdInsightsReportRequest.md)|  | |

### Return type

[**CreateAdInsightsReport202Response**](CreateAdInsightsReport202Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Report run submitted |  -  |
| **400** | Invalid input, or Meta rejected the report parameters |  -  |
| **401** | Unauthorized |  -  |
| **429** | Meta rate limit reached |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## createAdInsightsReportWithHttpInfo

> ApiResponse<CreateAdInsightsReport202Response> createAdInsightsReport createAdInsightsReportWithHttpInfo(createAdInsightsReportRequest)

Submit an async insights report run (Meta)

Submits an asynchronous Meta insights report. Same query surface as GET /v1/ads/insights, but in the JSON body; Meta processes the report server-side, which is the right choice for long ranges or large accounts where the sync query is slow or rate-limited. Returns a &#x60;reportRunId&#x60; to poll via GET /v1/ads/insights/reports/{reportRunId}. Meta only. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        CreateAdInsightsReportRequest createAdInsightsReportRequest = new CreateAdInsightsReportRequest(); // CreateAdInsightsReportRequest | 
        try {
            ApiResponse<CreateAdInsightsReport202Response> response = apiInstance.createAdInsightsReportWithHttpInfo(createAdInsightsReportRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#createAdInsightsReport");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createAdInsightsReportRequest** | [**CreateAdInsightsReportRequest**](CreateAdInsightsReportRequest.md)|  | |

### Return type

ApiResponse<[**CreateAdInsightsReport202Response**](CreateAdInsightsReport202Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Report run submitted |  -  |
| **400** | Invalid input, or Meta rejected the report parameters |  -  |
| **401** | Unauthorized |  -  |
| **429** | Meta rate limit reached |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## createCallAd

> void createCallAd(createCallAdRequest)

Create Click-to-Call ad

Same shape and flow as POST /v1/ads/ctwa, but the CTA is CALL_NOW dialing &#x60;phoneNumber&#x60; via a tel: link. The ad set is destination_type PHONE_CALL optimizing QUALITY_CALL and the campaign objective defaults to OUTCOME_LEADS. Supports the same single-creative and multi-creative shapes as CTWA.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        CreateCallAdRequest createCallAdRequest = new CreateCallAdRequest(); // CreateCallAdRequest | 
        try {
            apiInstance.createCallAd(createCallAdRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#createCallAd");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createCallAdRequest** | [**CreateCallAdRequest**](CreateCallAdRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Ad(s) created and submitted for review |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |
| **422** | No Facebook Page resolved for the account |  -  |

## createCallAdWithHttpInfo

> ApiResponse<Void> createCallAd createCallAdWithHttpInfo(createCallAdRequest)

Create Click-to-Call ad

Same shape and flow as POST /v1/ads/ctwa, but the CTA is CALL_NOW dialing &#x60;phoneNumber&#x60; via a tel: link. The ad set is destination_type PHONE_CALL optimizing QUALITY_CALL and the campaign objective defaults to OUTCOME_LEADS. Supports the same single-creative and multi-creative shapes as CTWA.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        CreateCallAdRequest createCallAdRequest = new CreateCallAdRequest(); // CreateCallAdRequest | 
        try {
            ApiResponse<Void> response = apiInstance.createCallAdWithHttpInfo(createCallAdRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#createCallAd");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createCallAdRequest** | [**CreateCallAdRequest**](CreateCallAdRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Ad(s) created and submitted for review |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |
| **422** | No Facebook Page resolved for the account |  -  |


## createConversionDestination

> CreateConversionDestination201Response createConversionDestination(accountId, createConversionDestinationRequest)

Create a conversion destination

Create a new conversion destination on the platform. Supported for LinkedIn (conversion rule) and Google Ads (conversion action). Meta manages destinations in its own UI and returns 405.  **LinkedIn:** creation is NOT idempotent. A retry creates a second destination. Deduplicate before retrying.  **Google Ads:** calling with a name that already exists reuses the existing conversion action transparently (the response is identical to a fresh create). Calling with the same name but a different category returns a typed &#x60;IDEMPOTENCY_CONFLICT&#x60; (409) rather than silently returning the mismatched action.  **LinkedIn:** the rule is created with &#x60;conversionMethod&#x3D;CONVERSIONS_API&#x60; and (by default) auto-associated with all of the ad account&#39;s campaigns via &#x60;autoAssociationType&#x3D;ALL_CAMPAIGNS&#x60;. Pass &#x60;autoAssociationType: NONE&#x60; to opt out and manage associations explicitly via the associations endpoints below.  365-day attribution windows are only valid for &#x60;SUBMIT_APPLICATION&#x60;, &#x60;PURCHASE&#x60;, &#x60;ADD_TO_CART&#x60;, &#x60;QUALIFIED_LEAD&#x60;, and &#x60;LEAD&#x60; rule types; the API rejects other combinations locally.  **Google Ads:** the conversion action is created with &#x60;type&#x3D;UPLOAD_CLICKS&#x60; (required for API-uploaded offline conversions, immutable after creation). The &#x60;type&#x60; field carries the Google &#x60;ConversionActionCategory&#x60; enum value, e.g. &#x60;PURCHASE&#x60;, &#x60;SUBSCRIBE_PAID&#x60;, &#x60;SIGNUP&#x60;, &#x60;IMPORTED_LEAD&#x60;, &#x60;BOOK_APPOINTMENT&#x60;. Unified standard event names (e.g. &#x60;Purchase&#x60;, &#x60;Subscribe&#x60;, &#x60;CompleteRegistration&#x60;, &#x60;Lead&#x60;, &#x60;Schedule&#x60;) are resolved to their Google category equivalents automatically. The action defaults to secondary (non-primary) to avoid immediately steering Smart Bidding; pass &#x60;primaryForGoal: true&#x60; to opt in. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | SocialAccount ID (linkedinads or googleads).
        CreateConversionDestinationRequest createConversionDestinationRequest = new CreateConversionDestinationRequest(); // CreateConversionDestinationRequest | 
        try {
            CreateConversionDestination201Response result = apiInstance.createConversionDestination(accountId, createConversionDestinationRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#createConversionDestination");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| SocialAccount ID (linkedinads or googleads). | |
| **createConversionDestinationRequest** | [**CreateConversionDestinationRequest**](CreateConversionDestinationRequest.md)|  | |

### Return type

[**CreateConversionDestination201Response**](CreateConversionDestination201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Destination created |  -  |
| **400** | Invalid body or platform validation failure. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), or the connected LinkedIn account lacks the &#x60;rw_conversions&#x60; scope (reconnect required).  |  -  |
| **404** | Account not found or not accessible. |  -  |
| **405** | Platform does not support destination creation. |  -  |
| **409** | Google Ads only. A conversion action with the given name already exists but has a different category. Use a different name or use the existing destination. Error code: &#x60;IDEMPOTENCY_CONFLICT&#x60;.  |  -  |
| **429** | Rate limit hit. Retry with backoff. |  -  |

## createConversionDestinationWithHttpInfo

> ApiResponse<CreateConversionDestination201Response> createConversionDestination createConversionDestinationWithHttpInfo(accountId, createConversionDestinationRequest)

Create a conversion destination

Create a new conversion destination on the platform. Supported for LinkedIn (conversion rule) and Google Ads (conversion action). Meta manages destinations in its own UI and returns 405.  **LinkedIn:** creation is NOT idempotent. A retry creates a second destination. Deduplicate before retrying.  **Google Ads:** calling with a name that already exists reuses the existing conversion action transparently (the response is identical to a fresh create). Calling with the same name but a different category returns a typed &#x60;IDEMPOTENCY_CONFLICT&#x60; (409) rather than silently returning the mismatched action.  **LinkedIn:** the rule is created with &#x60;conversionMethod&#x3D;CONVERSIONS_API&#x60; and (by default) auto-associated with all of the ad account&#39;s campaigns via &#x60;autoAssociationType&#x3D;ALL_CAMPAIGNS&#x60;. Pass &#x60;autoAssociationType: NONE&#x60; to opt out and manage associations explicitly via the associations endpoints below.  365-day attribution windows are only valid for &#x60;SUBMIT_APPLICATION&#x60;, &#x60;PURCHASE&#x60;, &#x60;ADD_TO_CART&#x60;, &#x60;QUALIFIED_LEAD&#x60;, and &#x60;LEAD&#x60; rule types; the API rejects other combinations locally.  **Google Ads:** the conversion action is created with &#x60;type&#x3D;UPLOAD_CLICKS&#x60; (required for API-uploaded offline conversions, immutable after creation). The &#x60;type&#x60; field carries the Google &#x60;ConversionActionCategory&#x60; enum value, e.g. &#x60;PURCHASE&#x60;, &#x60;SUBSCRIBE_PAID&#x60;, &#x60;SIGNUP&#x60;, &#x60;IMPORTED_LEAD&#x60;, &#x60;BOOK_APPOINTMENT&#x60;. Unified standard event names (e.g. &#x60;Purchase&#x60;, &#x60;Subscribe&#x60;, &#x60;CompleteRegistration&#x60;, &#x60;Lead&#x60;, &#x60;Schedule&#x60;) are resolved to their Google category equivalents automatically. The action defaults to secondary (non-primary) to avoid immediately steering Smart Bidding; pass &#x60;primaryForGoal: true&#x60; to opt in. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | SocialAccount ID (linkedinads or googleads).
        CreateConversionDestinationRequest createConversionDestinationRequest = new CreateConversionDestinationRequest(); // CreateConversionDestinationRequest | 
        try {
            ApiResponse<CreateConversionDestination201Response> response = apiInstance.createConversionDestinationWithHttpInfo(accountId, createConversionDestinationRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#createConversionDestination");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| SocialAccount ID (linkedinads or googleads). | |
| **createConversionDestinationRequest** | [**CreateConversionDestinationRequest**](CreateConversionDestinationRequest.md)|  | |

### Return type

ApiResponse<[**CreateConversionDestination201Response**](CreateConversionDestination201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Destination created |  -  |
| **400** | Invalid body or platform validation failure. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), or the connected LinkedIn account lacks the &#x60;rw_conversions&#x60; scope (reconnect required).  |  -  |
| **404** | Account not found or not accessible. |  -  |
| **405** | Platform does not support destination creation. |  -  |
| **409** | Google Ads only. A conversion action with the given name already exists but has a different category. Use a different name or use the existing destination. Error code: &#x60;IDEMPOTENCY_CONFLICT&#x60;.  |  -  |
| **429** | Rate limit hit. Retry with backoff. |  -  |


## createCtwaAd

> CreateCtwaAd201Response createCtwaAd(ctwaAdRequestBody)

Create Click-to-WhatsApp ad (deprecated)

Deprecated: use POST /v1/ads/messaging with &#x60;destination: whatsapp&#x60;. This endpoint stays available for back-compat; no removal planned.  Creates one or more Click-to-WhatsApp (CTWA) ads on Meta under a single campaign and ad set. When tapped, each ad opens a WhatsApp conversation with the business attached to the supplied Facebook Page. The full hierarchy (campaign, ad set, creative(s), ad(s)) is created and activated in one call. The CTA is locked to WHATSAPP_MESSAGE and the destination is hard-coded to api.whatsapp.com/send; Meta resolves the actual WhatsApp number from the Page-to-WA pairing configured in Page settings or Business Manager.  Supports two mutually-exclusive shapes:  - **Single-creative**: supply top-level &#x60;headline&#x60;, &#x60;body&#x60;, and one of &#x60;imageUrl&#x60; / &#x60;video&#x60;. Creates 1 campaign + 1 ad set + 1 ad.  - **Multi-creative**: supply a &#x60;creatives[]&#x60; array with N entries (each carrying its own headline, body, and image/video). Creates 1 campaign + 1 ad set + N ads sharing budget and targeting so Meta A/Bs the creatives inside a single auction instead of fragmenting budget across N parallel campaigns. Recommended when launching multiple creative variants for the same campaign.  Prerequisites enforced by Meta (surfaced as platform_error on failure): the Facebook Page must be paired with a verified WhatsApp Business number, the WhatsApp Business Account must be business-verified, and the Meta access token must carry ads_management.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        CtwaAdRequestBody ctwaAdRequestBody = new CtwaAdRequestBody(); // CtwaAdRequestBody | 
        try {
            CreateCtwaAd201Response result = apiInstance.createCtwaAd(ctwaAdRequestBody);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#createCtwaAd");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ctwaAdRequestBody** | [**CtwaAdRequestBody**](CtwaAdRequestBody.md)|  | |

### Return type

[**CreateCtwaAd201Response**](CreateCtwaAd201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | CTWA ad(s) created and submitted to Meta for review. Response is a tagged union discriminated by &#x60;adType&#x60;:  - &#x60;adType: \&quot;single\&quot;&#x60; → single-creative request: &#x60;{ adType, ad,   message }&#x60; where &#x60;ad&#x60; is the persisted Ad document. - &#x60;adType: \&quot;multi\&quot;&#x60; → multi-creative request: &#x60;{ adType, ads,   platformCampaignId, platformAdSetId, message }&#x60; where &#x60;ads&#x60; is   the array of N persisted Ad documents all sharing the returned   campaign and ad set IDs.  Generated SDK clients can narrow on &#x60;adType&#x60; instead of sniffing for field presence.  |  -  |
| **400** | Invalid body. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | SocialAccount not found. |  -  |
| **422** | Page is not connected to a verified WhatsApp number. |  -  |
| **502** | Meta rejected the request (e.g. WABA business verification missing). Inspect &#x60;platformError&#x60; for the upstream Meta payload.  |  -  |

## createCtwaAdWithHttpInfo

> ApiResponse<CreateCtwaAd201Response> createCtwaAd createCtwaAdWithHttpInfo(ctwaAdRequestBody)

Create Click-to-WhatsApp ad (deprecated)

Deprecated: use POST /v1/ads/messaging with &#x60;destination: whatsapp&#x60;. This endpoint stays available for back-compat; no removal planned.  Creates one or more Click-to-WhatsApp (CTWA) ads on Meta under a single campaign and ad set. When tapped, each ad opens a WhatsApp conversation with the business attached to the supplied Facebook Page. The full hierarchy (campaign, ad set, creative(s), ad(s)) is created and activated in one call. The CTA is locked to WHATSAPP_MESSAGE and the destination is hard-coded to api.whatsapp.com/send; Meta resolves the actual WhatsApp number from the Page-to-WA pairing configured in Page settings or Business Manager.  Supports two mutually-exclusive shapes:  - **Single-creative**: supply top-level &#x60;headline&#x60;, &#x60;body&#x60;, and one of &#x60;imageUrl&#x60; / &#x60;video&#x60;. Creates 1 campaign + 1 ad set + 1 ad.  - **Multi-creative**: supply a &#x60;creatives[]&#x60; array with N entries (each carrying its own headline, body, and image/video). Creates 1 campaign + 1 ad set + N ads sharing budget and targeting so Meta A/Bs the creatives inside a single auction instead of fragmenting budget across N parallel campaigns. Recommended when launching multiple creative variants for the same campaign.  Prerequisites enforced by Meta (surfaced as platform_error on failure): the Facebook Page must be paired with a verified WhatsApp Business number, the WhatsApp Business Account must be business-verified, and the Meta access token must carry ads_management.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        CtwaAdRequestBody ctwaAdRequestBody = new CtwaAdRequestBody(); // CtwaAdRequestBody | 
        try {
            ApiResponse<CreateCtwaAd201Response> response = apiInstance.createCtwaAdWithHttpInfo(ctwaAdRequestBody);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#createCtwaAd");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ctwaAdRequestBody** | [**CtwaAdRequestBody**](CtwaAdRequestBody.md)|  | |

### Return type

ApiResponse<[**CreateCtwaAd201Response**](CreateCtwaAd201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | CTWA ad(s) created and submitted to Meta for review. Response is a tagged union discriminated by &#x60;adType&#x60;:  - &#x60;adType: \&quot;single\&quot;&#x60; → single-creative request: &#x60;{ adType, ad,   message }&#x60; where &#x60;ad&#x60; is the persisted Ad document. - &#x60;adType: \&quot;multi\&quot;&#x60; → multi-creative request: &#x60;{ adType, ads,   platformCampaignId, platformAdSetId, message }&#x60; where &#x60;ads&#x60; is   the array of N persisted Ad documents all sharing the returned   campaign and ad set IDs.  Generated SDK clients can narrow on &#x60;adType&#x60; instead of sniffing for field presence.  |  -  |
| **400** | Invalid body. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | SocialAccount not found. |  -  |
| **422** | Page is not connected to a verified WhatsApp number. |  -  |
| **502** | Meta rejected the request (e.g. WABA business verification missing). Inspect &#x60;platformError&#x60; for the upstream Meta payload.  |  -  |


## createLeadForm

> CreateLeadForm200Response createLeadForm(createLeadFormRequest)

Create a lead form

Creates a Lead Gen form on the connected Facebook Page (POST /{page-id}/leadgen_forms). NOT idempotent — a retry creates a second form. Prefilled question types (EMAIL, PHONE, FULL_NAME, …) must omit label/key; CUSTOM questions require both. Requires the Ads add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        CreateLeadFormRequest createLeadFormRequest = new CreateLeadFormRequest(); // CreateLeadFormRequest | 
        try {
            CreateLeadForm200Response result = apiInstance.createLeadForm(createLeadFormRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#createLeadForm");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createLeadFormRequest** | [**CreateLeadFormRequest**](CreateLeadFormRequest.md)|  | |

### Return type

[**CreateLeadForm200Response**](CreateLeadForm200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Created form. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required. |  -  |

## createLeadFormWithHttpInfo

> ApiResponse<CreateLeadForm200Response> createLeadForm createLeadFormWithHttpInfo(createLeadFormRequest)

Create a lead form

Creates a Lead Gen form on the connected Facebook Page (POST /{page-id}/leadgen_forms). NOT idempotent — a retry creates a second form. Prefilled question types (EMAIL, PHONE, FULL_NAME, …) must omit label/key; CUSTOM questions require both. Requires the Ads add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        CreateLeadFormRequest createLeadFormRequest = new CreateLeadFormRequest(); // CreateLeadFormRequest | 
        try {
            ApiResponse<CreateLeadForm200Response> response = apiInstance.createLeadFormWithHttpInfo(createLeadFormRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#createLeadForm");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createLeadFormRequest** | [**CreateLeadFormRequest**](CreateLeadFormRequest.md)|  | |

### Return type

ApiResponse<[**CreateLeadForm200Response**](CreateLeadForm200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Created form. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required. |  -  |


## createMessagingAd

> void createMessagingAd(createMessagingAdRequest)

Create click-to-message ad (WhatsApp / Messenger / Instagram Direct)

Creates a click-to-message ad; &#x60;destination&#x60; selects where the tapped ad opens a conversation: WhatsApp, the Page&#39;s Messenger inbox or the linked Instagram account&#39;s Direct inbox. The ad set is created with the matching destination_type and CONVERSATIONS optimization; the campaign objective defaults to OUTCOME_ENGAGEMENT. Supports single-creative and multi-creative shapes. Supersedes POST /v1/ads/ctwa (deprecated, equivalent to &#x60;destination: whatsapp&#x60;).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        CreateMessagingAdRequest createMessagingAdRequest = new CreateMessagingAdRequest(); // CreateMessagingAdRequest | 
        try {
            apiInstance.createMessagingAd(createMessagingAdRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#createMessagingAd");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createMessagingAdRequest** | [**CreateMessagingAdRequest**](CreateMessagingAdRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Ad(s) created and submitted for review |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |
| **422** | No Facebook Page resolved for the account |  -  |

## createMessagingAdWithHttpInfo

> ApiResponse<Void> createMessagingAd createMessagingAdWithHttpInfo(createMessagingAdRequest)

Create click-to-message ad (WhatsApp / Messenger / Instagram Direct)

Creates a click-to-message ad; &#x60;destination&#x60; selects where the tapped ad opens a conversation: WhatsApp, the Page&#39;s Messenger inbox or the linked Instagram account&#39;s Direct inbox. The ad set is created with the matching destination_type and CONVERSATIONS optimization; the campaign objective defaults to OUTCOME_ENGAGEMENT. Supports single-creative and multi-creative shapes. Supersedes POST /v1/ads/ctwa (deprecated, equivalent to &#x60;destination: whatsapp&#x60;).

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        CreateMessagingAdRequest createMessagingAdRequest = new CreateMessagingAdRequest(); // CreateMessagingAdRequest | 
        try {
            ApiResponse<Void> response = apiInstance.createMessagingAdWithHttpInfo(createMessagingAdRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#createMessagingAd");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createMessagingAdRequest** | [**CreateMessagingAdRequest**](CreateMessagingAdRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Ad(s) created and submitted for review |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **404** | Account not found |  -  |
| **422** | No Facebook Page resolved for the account |  -  |


## createRfPrediction

> CreateRfPrediction201Response createRfPrediction(createRfPredictionRequest)

Create a Reach &amp; Frequency prediction (Meta)

Creates an R&amp;F prediction — a QUOTE, nothing is bought and no ad entities are created. Provide a date range plus exactly one of &#x60;budgetAmount&#x60; (Meta predicts reach) or &#x60;reach&#x60; (Meta predicts the budget). The response carries the estimate and its allowed bounds (min/max budget and reach). Predictions expire on their own; to buy, reserve one via POST /v1/ads/rf-predictions/{predictionId}/reserve and pass the RESERVED id to POST /v1/ads/create with &#x60;buyingType: \&quot;RESERVED\&quot;&#x60;.  Reservation campaigns reject automatic placements, so omitted &#x60;placements&#x60; default to Facebook feed (+ Instagram stream when a linked IG professional account resolves); Instagram placements require that IG account. Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        CreateRfPredictionRequest createRfPredictionRequest = new CreateRfPredictionRequest(); // CreateRfPredictionRequest | 
        try {
            CreateRfPrediction201Response result = apiInstance.createRfPrediction(createRfPredictionRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#createRfPrediction");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createRfPredictionRequest** | [**CreateRfPredictionRequest**](CreateRfPredictionRequest.md)|  | |

### Return type

[**CreateRfPrediction201Response**](CreateRfPrediction201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Prediction created (usually ready within seconds) |  -  |
| **400** | Invalid input, or Meta rejected the prediction — message carries Meta&#39;s error |  -  |
| **401** | Unauthorized |  -  |
| **422** | No Facebook Page resolved for the account |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## createRfPredictionWithHttpInfo

> ApiResponse<CreateRfPrediction201Response> createRfPrediction createRfPredictionWithHttpInfo(createRfPredictionRequest)

Create a Reach &amp; Frequency prediction (Meta)

Creates an R&amp;F prediction — a QUOTE, nothing is bought and no ad entities are created. Provide a date range plus exactly one of &#x60;budgetAmount&#x60; (Meta predicts reach) or &#x60;reach&#x60; (Meta predicts the budget). The response carries the estimate and its allowed bounds (min/max budget and reach). Predictions expire on their own; to buy, reserve one via POST /v1/ads/rf-predictions/{predictionId}/reserve and pass the RESERVED id to POST /v1/ads/create with &#x60;buyingType: \&quot;RESERVED\&quot;&#x60;.  Reservation campaigns reject automatic placements, so omitted &#x60;placements&#x60; default to Facebook feed (+ Instagram stream when a linked IG professional account resolves); Instagram placements require that IG account. Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        CreateRfPredictionRequest createRfPredictionRequest = new CreateRfPredictionRequest(); // CreateRfPredictionRequest | 
        try {
            ApiResponse<CreateRfPrediction201Response> response = apiInstance.createRfPredictionWithHttpInfo(createRfPredictionRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#createRfPrediction");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createRfPredictionRequest** | [**CreateRfPredictionRequest**](CreateRfPredictionRequest.md)|  | |

### Return type

ApiResponse<[**CreateRfPrediction201Response**](CreateRfPrediction201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Prediction created (usually ready within seconds) |  -  |
| **400** | Invalid input, or Meta rejected the prediction — message carries Meta&#39;s error |  -  |
| **401** | Unauthorized |  -  |
| **422** | No Facebook Page resolved for the account |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## createStandaloneAd

> CreateStandaloneAd200Response createStandaloneAd(createStandaloneAdRequest, idempotencyKey)

Create standalone ad

Creates a paid ad with custom creative across Meta, Google Ads, Pinterest, TikTok, X/Twitter, and LinkedIn. Supports three mutually-exclusive request shapes selected by the body, a legacy single-creative shape (all platforms, default), a Meta-only multi-creative shape via the creatives array (one ad set with N ads sharing budget and targeting), and a Meta-only attach shape via adSetId (adds one new ad to an existing ad set). Per-platform required fields, budget minimums, and video-ad rules are documented on each property below. LinkedIn creates a Single Image or Single Video Ad backed by a Direct Sponsored Content \&quot;dark post\&quot; authored by a Company Page (see &#x60;organizationId&#x60;); supported goals are engagement, traffic, awareness, and video_views (video ads use the &#x60;video&#x60; field; video_views requires a video), and traffic ads require &#x60;linkUrl&#x60;.  **Idempotency:** this endpoint is not idempotent at the platform level (a blind retry creates a second campaign/ad set/ad). Send an &#x60;Idempotency-Key&#x60; header to make retries safe: the first request with a given key creates the ad and we store the response; a retry with the same key replays that exact response (with &#x60;Idempotent-Replayed: true&#x60;) instead of creating duplicates. Reusing a key with a different body returns 422; a key whose first request is still in flight returns 409 (retry after a short backoff). Keys are scoped to your credential and expire after 24h.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        CreateStandaloneAdRequest createStandaloneAdRequest = new CreateStandaloneAdRequest(); // CreateStandaloneAdRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes create retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409.
        try {
            CreateStandaloneAd200Response result = apiInstance.createStandaloneAd(createStandaloneAdRequest, idempotencyKey);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#createStandaloneAd");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
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
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes create retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. | [optional] |

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
| **200** | validateOnly dry-run passed — nothing was created |  -  |
| **201** | Ad(s) created |  -  |
| **400** | Missing required fields, invalid values, non-Meta platform used with creatives[] / adSetId, or a Meta validateOnly validation failure (verbatim) |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **422** | Platform ads connection required (TikTok Ads, X Ads) or missing linked account |  -  |

## createStandaloneAdWithHttpInfo

> ApiResponse<CreateStandaloneAd200Response> createStandaloneAd createStandaloneAdWithHttpInfo(createStandaloneAdRequest, idempotencyKey)

Create standalone ad

Creates a paid ad with custom creative across Meta, Google Ads, Pinterest, TikTok, X/Twitter, and LinkedIn. Supports three mutually-exclusive request shapes selected by the body, a legacy single-creative shape (all platforms, default), a Meta-only multi-creative shape via the creatives array (one ad set with N ads sharing budget and targeting), and a Meta-only attach shape via adSetId (adds one new ad to an existing ad set). Per-platform required fields, budget minimums, and video-ad rules are documented on each property below. LinkedIn creates a Single Image or Single Video Ad backed by a Direct Sponsored Content \&quot;dark post\&quot; authored by a Company Page (see &#x60;organizationId&#x60;); supported goals are engagement, traffic, awareness, and video_views (video ads use the &#x60;video&#x60; field; video_views requires a video), and traffic ads require &#x60;linkUrl&#x60;.  **Idempotency:** this endpoint is not idempotent at the platform level (a blind retry creates a second campaign/ad set/ad). Send an &#x60;Idempotency-Key&#x60; header to make retries safe: the first request with a given key creates the ad and we store the response; a retry with the same key replays that exact response (with &#x60;Idempotent-Replayed: true&#x60;) instead of creating duplicates. Reusing a key with a different body returns 422; a key whose first request is still in flight returns 409 (retry after a short backoff). Keys are scoped to your credential and expire after 24h.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        CreateStandaloneAdRequest createStandaloneAdRequest = new CreateStandaloneAdRequest(); // CreateStandaloneAdRequest | 
        String idempotencyKey = "idempotencyKey_example"; // String | Optional client-generated unique key (e.g. a UUID) that makes create retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409.
        try {
            ApiResponse<CreateStandaloneAd200Response> response = apiInstance.createStandaloneAdWithHttpInfo(createStandaloneAdRequest, idempotencyKey);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#createStandaloneAd");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
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
| **idempotencyKey** | **String**| Optional client-generated unique key (e.g. a UUID) that makes create retries safe. Same key + same body replays the original response; same key + different body → 422; key still processing → 409. | [optional] |

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
| **200** | validateOnly dry-run passed — nothing was created |  -  |
| **201** | Ad(s) created |  -  |
| **400** | Missing required fields, invalid values, non-Meta platform used with creatives[] / adSetId, or a Meta validateOnly validation failure (verbatim) |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **422** | Platform ads connection required (TikTok Ads, X Ads) or missing linked account |  -  |


## createTestLead

> CreateTestLead200Response createTestLead(formId, createTestLeadRequest)

Create a test lead

Submits a test lead against the form (POST /{form-id}/test_leads) to exercise retrieval without waiting for real ad impressions. Meta allows one test lead per form at a time. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String formId = "formId_example"; // String | 
        CreateTestLeadRequest createTestLeadRequest = new CreateTestLeadRequest(); // CreateTestLeadRequest | 
        try {
            CreateTestLead200Response result = apiInstance.createTestLead(formId, createTestLeadRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#createTestLead");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **formId** | **String**|  | |
| **createTestLeadRequest** | [**CreateTestLeadRequest**](CreateTestLeadRequest.md)|  | |

### Return type

[**CreateTestLead200Response**](CreateTestLead200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Test lead created. |  -  |
| **401** | Unauthorized |  -  |

## createTestLeadWithHttpInfo

> ApiResponse<CreateTestLead200Response> createTestLead createTestLeadWithHttpInfo(formId, createTestLeadRequest)

Create a test lead

Submits a test lead against the form (POST /{form-id}/test_leads) to exercise retrieval without waiting for real ad impressions. Meta allows one test lead per form at a time. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String formId = "formId_example"; // String | 
        CreateTestLeadRequest createTestLeadRequest = new CreateTestLeadRequest(); // CreateTestLeadRequest | 
        try {
            ApiResponse<CreateTestLead200Response> response = apiInstance.createTestLeadWithHttpInfo(formId, createTestLeadRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#createTestLead");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **formId** | **String**|  | |
| **createTestLeadRequest** | [**CreateTestLeadRequest**](CreateTestLeadRequest.md)|  | |

### Return type

ApiResponse<[**CreateTestLead200Response**](CreateTestLead200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Test lead created. |  -  |
| **401** | Unauthorized |  -  |


## deleteAd

> DeleteAccountGroup200Response deleteAd(adId)

Cancel an ad

Cancels the ad on the platform and marks it as cancelled in the database. The ad is preserved for history.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String adId = "adId_example"; // String | 
        try {
            DeleteAccountGroup200Response result = apiInstance.deleteAd(adId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#deleteAd");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
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
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## deleteAdWithHttpInfo

> ApiResponse<DeleteAccountGroup200Response> deleteAd deleteAdWithHttpInfo(adId)

Cancel an ad

Cancels the ad on the platform and marks it as cancelled in the database. The ad is preserved for history.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String adId = "adId_example"; // String | 
        try {
            ApiResponse<DeleteAccountGroup200Response> response = apiInstance.deleteAdWithHttpInfo(adId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#deleteAd");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
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
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## deleteAdCreative

> DeleteAdCreative200Response deleteAdCreative(creativeId, accountId)

Delete a creative (Meta)

Deletes a creative from the library. Meta only allows deleting creatives not referenced by any ad — otherwise its 400 surfaces verbatim.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String creativeId = "creativeId_example"; // String | Platform creative id
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        try {
            DeleteAdCreative200Response result = apiInstance.deleteAdCreative(creativeId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#deleteAdCreative");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **creativeId** | **String**| Platform creative id | |
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |

### Return type

[**DeleteAdCreative200Response**](DeleteAdCreative200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Creative deleted |  -  |
| **400** | Invalid input, the creative is in use, or Meta rejected the delete |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## deleteAdCreativeWithHttpInfo

> ApiResponse<DeleteAdCreative200Response> deleteAdCreative deleteAdCreativeWithHttpInfo(creativeId, accountId)

Delete a creative (Meta)

Deletes a creative from the library. Meta only allows deleting creatives not referenced by any ad — otherwise its 400 surfaces verbatim.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String creativeId = "creativeId_example"; // String | Platform creative id
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        try {
            ApiResponse<DeleteAdCreative200Response> response = apiInstance.deleteAdCreativeWithHttpInfo(creativeId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#deleteAdCreative");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **creativeId** | **String**| Platform creative id | |
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |

### Return type

ApiResponse<[**DeleteAdCreative200Response**](DeleteAdCreative200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Creative deleted |  -  |
| **400** | Invalid input, the creative is in use, or Meta rejected the delete |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## deleteConversionDestination

> void deleteConversionDestination(accountId, destinationId, adAccountId)

Delete a conversion destination

LinkedIn-only today. LinkedIn does not expose hard-delete on conversion rules — what their UI calls \&quot;delete\&quot; is the same &#x60;enabled: false&#x60; flip we apply here. The rule remains fetchable via GET with &#x60;status: &#39;inactive&#39;&#x60;; the unified discovery endpoint hides it by default.  &#x60;adAccountId&#x60; may be passed as a query parameter (recommended) or as a JSON body field for clients that can send DELETE bodies. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String destinationId = "destinationId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | Required as query OR in JSON body.
        try {
            apiInstance.deleteConversionDestination(accountId, destinationId, adAccountId);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#deleteConversionDestination");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**|  | |
| **destinationId** | **String**|  | |
| **adAccountId** | **String**| Required as query OR in JSON body. | [optional] |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Soft-deleted. |  -  |
| **400** | adAccountId missing. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on or LinkedIn reconnect required. |  -  |
| **404** | Account or destination not found. |  -  |
| **405** | Platform does not support deleting destinations. |  -  |
| **429** | LinkedIn rate limit hit. Retry with backoff. |  -  |

## deleteConversionDestinationWithHttpInfo

> ApiResponse<Void> deleteConversionDestination deleteConversionDestinationWithHttpInfo(accountId, destinationId, adAccountId)

Delete a conversion destination

LinkedIn-only today. LinkedIn does not expose hard-delete on conversion rules — what their UI calls \&quot;delete\&quot; is the same &#x60;enabled: false&#x60; flip we apply here. The rule remains fetchable via GET with &#x60;status: &#39;inactive&#39;&#x60;; the unified discovery endpoint hides it by default.  &#x60;adAccountId&#x60; may be passed as a query parameter (recommended) or as a JSON body field for clients that can send DELETE bodies. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String destinationId = "destinationId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | Required as query OR in JSON body.
        try {
            ApiResponse<Void> response = apiInstance.deleteConversionDestinationWithHttpInfo(accountId, destinationId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#deleteConversionDestination");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**|  | |
| **destinationId** | **String**|  | |
| **adAccountId** | **String**| Required as query OR in JSON body. | [optional] |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Soft-deleted. |  -  |
| **400** | adAccountId missing. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on or LinkedIn reconnect required. |  -  |
| **404** | Account or destination not found. |  -  |
| **405** | Platform does not support deleting destinations. |  -  |
| **429** | LinkedIn rate limit hit. Retry with backoff. |  -  |


## duplicateAd

> DuplicateAd200Response duplicateAd(adId, duplicateAdRequest)

Duplicate an ad (Meta)

Duplicates a single ad via Meta&#39;s native &#x60;POST /{ad-id}/copies&#x60;. The copy is created paused. &#x60;adSetId&#x60; retargets the copy into another ad set; omitted &#x3D; the source&#39;s own ad set. Accepts the Zernio ad id or the platform ad id. Sync discovery is triggered automatically (&#x60;syncAfter: false&#x60; to skip). Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String adId = "adId_example"; // String | Zernio ad ID or platform ad ID
        DuplicateAdRequest duplicateAdRequest = new DuplicateAdRequest(); // DuplicateAdRequest | 
        try {
            DuplicateAd200Response result = apiInstance.duplicateAd(adId, duplicateAdRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#duplicateAd");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
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
| **200** | Ad duplicated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **404** | Ad not found |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## duplicateAdWithHttpInfo

> ApiResponse<DuplicateAd200Response> duplicateAd duplicateAdWithHttpInfo(adId, duplicateAdRequest)

Duplicate an ad (Meta)

Duplicates a single ad via Meta&#39;s native &#x60;POST /{ad-id}/copies&#x60;. The copy is created paused. &#x60;adSetId&#x60; retargets the copy into another ad set; omitted &#x3D; the source&#39;s own ad set. Accepts the Zernio ad id or the platform ad id. Sync discovery is triggered automatically (&#x60;syncAfter: false&#x60; to skip). Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String adId = "adId_example"; // String | Zernio ad ID or platform ad ID
        DuplicateAdRequest duplicateAdRequest = new DuplicateAdRequest(); // DuplicateAdRequest | 
        try {
            ApiResponse<DuplicateAd200Response> response = apiInstance.duplicateAdWithHttpInfo(adId, duplicateAdRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#duplicateAd");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
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
| **200** | Ad duplicated |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **404** | Ad not found |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## estimateAdReach

> EstimateAdReach200Response estimateAdReach(estimateAdReachRequest)

Estimate audience reach

Returns a normalized pre-flight audience-size estimate for a targeting spec, before any campaign is created. Backed by each platform&#39;s native reach API (Meta &#x60;delivery_estimate&#x60;, LinkedIn &#x60;audienceCounts&#x60;, X &#x60;audience_summary&#x60;, Pinterest &#x60;audience_sizing&#x60;).  Platforms without a usable pre-flight reach API (Google Search/Display, TikTok) return &#x60;available: false&#x60; with no bounds, so clients can hide or grey out the estimate rather than treat the absence as an error. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        EstimateAdReachRequest estimateAdReachRequest = new EstimateAdReachRequest(); // EstimateAdReachRequest | 
        try {
            EstimateAdReach200Response result = apiInstance.estimateAdReach(estimateAdReachRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#estimateAdReach");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **estimateAdReachRequest** | [**EstimateAdReachRequest**](EstimateAdReachRequest.md)|  | |

### Return type

[**EstimateAdReach200Response**](EstimateAdReach200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Normalized reach estimate |  -  |
| **400** | Missing required fields or a targeting field the platform cannot honour |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |

## estimateAdReachWithHttpInfo

> ApiResponse<EstimateAdReach200Response> estimateAdReach estimateAdReachWithHttpInfo(estimateAdReachRequest)

Estimate audience reach

Returns a normalized pre-flight audience-size estimate for a targeting spec, before any campaign is created. Backed by each platform&#39;s native reach API (Meta &#x60;delivery_estimate&#x60;, LinkedIn &#x60;audienceCounts&#x60;, X &#x60;audience_summary&#x60;, Pinterest &#x60;audience_sizing&#x60;).  Platforms without a usable pre-flight reach API (Google Search/Display, TikTok) return &#x60;available: false&#x60; with no bounds, so clients can hide or grey out the estimate rather than treat the absence as an error. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        EstimateAdReachRequest estimateAdReachRequest = new EstimateAdReachRequest(); // EstimateAdReachRequest | 
        try {
            ApiResponse<EstimateAdReach200Response> response = apiInstance.estimateAdReachWithHttpInfo(estimateAdReachRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#estimateAdReach");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **estimateAdReachRequest** | [**EstimateAdReachRequest**](EstimateAdReachRequest.md)|  | |

### Return type

ApiResponse<[**EstimateAdReach200Response**](EstimateAdReach200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Normalized reach estimate |  -  |
| **400** | Missing required fields or a targeting field the platform cannot honour |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |


## generateAdPreviews

> GenerateAdPreviews200Response generateAdPreviews(generateAdPreviewsRequest)

Render pre-create ad previews (Meta)

Renders how a creative would look per placement BEFORE any ad exists, via Meta&#39;s &#x60;/generatepreviews&#x60;. Provide exactly one creative source: &#x60;existingCreativeId&#x60; or &#x60;creativeSpec&#x60;. Each preview is an HTML &#x60;&lt;iframe&gt;&#x60; snippet embeddable directly. Unknown &#x60;formats&#x60; values return Meta&#39;s 400 verbatim. Meta only. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        GenerateAdPreviewsRequest generateAdPreviewsRequest = new GenerateAdPreviewsRequest(); // GenerateAdPreviewsRequest | 
        try {
            GenerateAdPreviews200Response result = apiInstance.generateAdPreviews(generateAdPreviewsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#generateAdPreviews");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **generateAdPreviewsRequest** | [**GenerateAdPreviewsRequest**](GenerateAdPreviewsRequest.md)|  | |

### Return type

[**GenerateAdPreviews200Response**](GenerateAdPreviews200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rendered previews |  -  |
| **400** | Invalid input, or Meta rejected the creative spec / ad_format — message carries Meta&#39;s error |  -  |
| **401** | Unauthorized |  -  |
| **429** | Meta rate limit reached |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## generateAdPreviewsWithHttpInfo

> ApiResponse<GenerateAdPreviews200Response> generateAdPreviews generateAdPreviewsWithHttpInfo(generateAdPreviewsRequest)

Render pre-create ad previews (Meta)

Renders how a creative would look per placement BEFORE any ad exists, via Meta&#39;s &#x60;/generatepreviews&#x60;. Provide exactly one creative source: &#x60;existingCreativeId&#x60; or &#x60;creativeSpec&#x60;. Each preview is an HTML &#x60;&lt;iframe&gt;&#x60; snippet embeddable directly. Unknown &#x60;formats&#x60; values return Meta&#39;s 400 verbatim. Meta only. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        GenerateAdPreviewsRequest generateAdPreviewsRequest = new GenerateAdPreviewsRequest(); // GenerateAdPreviewsRequest | 
        try {
            ApiResponse<GenerateAdPreviews200Response> response = apiInstance.generateAdPreviewsWithHttpInfo(generateAdPreviewsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#generateAdPreviews");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **generateAdPreviewsRequest** | [**GenerateAdPreviewsRequest**](GenerateAdPreviewsRequest.md)|  | |

### Return type

ApiResponse<[**GenerateAdPreviews200Response**](GenerateAdPreviews200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rendered previews |  -  |
| **400** | Invalid input, or Meta rejected the creative spec / ad_format — message carries Meta&#39;s error |  -  |
| **401** | Unauthorized |  -  |
| **429** | Meta rate limit reached |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## getAd

> GetAd200Response getAd(adId)

Get ad details

Returns an ad with its creative, targeting, status, and performance metrics.  The &#x60;{adId}&#x60; path segment accepts any identifier dialect Zernio indexes for the ad: - the Zernio internal &#x60;_id&#x60; (24-char hex) - Meta&#39;s numeric &#x60;platformAdId&#x60; (the value shipped in &#x60;comment.received&#x60; webhooks as &#x60;comment.ad.id&#x60;) - the creative&#39;s &#x60;effective_object_story_id&#x60; (&#x60;{pageId}_{postId}&#x60; shape, Facebook side) - the creative&#39;s &#x60;effective_instagram_media_id&#x60; (Instagram side)  Any of the four resolve to the same ad. Caller doesn&#39;t need a translation step. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String adId = "adId_example"; // String | Zernio `_id` (hex), Meta `platformAdId` (numeric), or one of the creative's effective story/media IDs. See description for details. 
        try {
            GetAd200Response result = apiInstance.getAd(adId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getAd");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
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
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |

## getAdWithHttpInfo

> ApiResponse<GetAd200Response> getAd getAdWithHttpInfo(adId)

Get ad details

Returns an ad with its creative, targeting, status, and performance metrics.  The &#x60;{adId}&#x60; path segment accepts any identifier dialect Zernio indexes for the ad: - the Zernio internal &#x60;_id&#x60; (24-char hex) - Meta&#39;s numeric &#x60;platformAdId&#x60; (the value shipped in &#x60;comment.received&#x60; webhooks as &#x60;comment.ad.id&#x60;) - the creative&#39;s &#x60;effective_object_story_id&#x60; (&#x60;{pageId}_{postId}&#x60; shape, Facebook side) - the creative&#39;s &#x60;effective_instagram_media_id&#x60; (Instagram side)  Any of the four resolve to the same ad. Caller doesn&#39;t need a translation step. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String adId = "adId_example"; // String | Zernio `_id` (hex), Meta `platformAdId` (numeric), or one of the creative's effective story/media IDs. See description for details. 
        try {
            ApiResponse<GetAd200Response> response = apiInstance.getAdWithHttpInfo(adId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getAd");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
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
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |


## getAdAccountFinance

> GetAdAccountFinance200Response getAdAccountFinance(accountId, adAccountId)

Ad account finances (Meta)

Finances of one Meta ad account: prepaid &#x60;balance&#x60;, lifetime &#x60;amountSpent&#x60;, account &#x60;spendCap&#x60; (null &#x3D; no cap) and the &#x60;fundingSource&#x60;. Money values are converted from Meta&#39;s minor units to whole units of &#x60;currency&#x60;. Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>).
        try {
            GetAdAccountFinance200Response result = apiInstance.getAdAccountFinance(accountId, adAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getAdAccountFinance");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **adAccountId** | **String**| Meta ad account id (act_&lt;n&gt;). | |

### Return type

[**GetAdAccountFinance200Response**](GetAdAccountFinance200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account finances |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## getAdAccountFinanceWithHttpInfo

> ApiResponse<GetAdAccountFinance200Response> getAdAccountFinance getAdAccountFinanceWithHttpInfo(accountId, adAccountId)

Ad account finances (Meta)

Finances of one Meta ad account: prepaid &#x60;balance&#x60;, lifetime &#x60;amountSpent&#x60;, account &#x60;spendCap&#x60; (null &#x3D; no cap) and the &#x60;fundingSource&#x60;. Money values are converted from Meta&#39;s minor units to whole units of &#x60;currency&#x60;. Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>).
        try {
            ApiResponse<GetAdAccountFinance200Response> response = apiInstance.getAdAccountFinanceWithHttpInfo(accountId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getAdAccountFinance");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **adAccountId** | **String**| Meta ad account id (act_&lt;n&gt;). | |

### Return type

ApiResponse<[**GetAdAccountFinance200Response**](GetAdAccountFinance200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account finances |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## getAdAnalytics

> GetAdAnalytics200Response getAdAnalytics(adId, fromDate, toDate, breakdowns)

Get ad analytics

Returns detailed performance analytics for an ad. Includes summary metrics, a daily timeline over the requested date range, and optional demographic breakdowns (Meta and TikTok only). If no date range is provided, defaults to the last 90 days. Date range is capped at 730 days max. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String adId = "adId_example"; // String | 
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of date range (YYYY-MM-DD). Defaults to 90 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of date range (YYYY-MM-DD). Defaults to today. Max 730-day range.
        String breakdowns = "breakdowns_example"; // String | Comma-separated breakdown dimensions.  **Meta**: age, gender, country, publisher_platform, device_platform, region.  **TikTok**: gender, age, country_code, platform, ac, language.  **LinkedIn** (firmographics): job_title, job_function, seniority, industry, company, company_size, country, region. Rows carry the raw pivot `value` plus a resolved `name`. LinkedIn serves these aggregated over the whole range, delays the data 12-24h, and omits segments with fewer than 3 events. 
        try {
            GetAdAnalytics200Response result = apiInstance.getAdAnalytics(adId, fromDate, toDate, breakdowns);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getAdAnalytics");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
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
| **fromDate** | **LocalDate**| Start of date range (YYYY-MM-DD). Defaults to 90 days ago. | [optional] |
| **toDate** | **LocalDate**| End of date range (YYYY-MM-DD). Defaults to today. Max 730-day range. | [optional] |
| **breakdowns** | **String**| Comma-separated breakdown dimensions.  **Meta**: age, gender, country, publisher_platform, device_platform, region.  **TikTok**: gender, age, country_code, platform, ac, language.  **LinkedIn** (firmographics): job_title, job_function, seniority, industry, company, company_size, country, region. Rows carry the raw pivot &#x60;value&#x60; plus a resolved &#x60;name&#x60;. LinkedIn serves these aggregated over the whole range, delays the data 12-24h, and omits segments with fewer than 3 events.  | [optional] |

### Return type

[**GetAdAnalytics200Response**](GetAdAnalytics200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad analytics |  -  |
| **202** | Part of the requested date range predates the ingested history; a background backfill job has been queued. The body has the same shape as the 200 response, carries the currently-available data, and includes &#x60;backfillPending: true&#x60;. A &#x60;Retry-After&#x60; header carries the recommended poll interval in seconds. Allow the job a short time to run (typically 1-3 minutes) and submit the request again; once ingestion completes the same request returns 200 with the full range. |  -  |
| **400** | Invalid parameter (e.g. an unknown &#x60;breakdowns&#x60; dimension). The message lists the offending value(s) and the supported set. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |

## getAdAnalyticsWithHttpInfo

> ApiResponse<GetAdAnalytics200Response> getAdAnalytics getAdAnalyticsWithHttpInfo(adId, fromDate, toDate, breakdowns)

Get ad analytics

Returns detailed performance analytics for an ad. Includes summary metrics, a daily timeline over the requested date range, and optional demographic breakdowns (Meta and TikTok only). If no date range is provided, defaults to the last 90 days. Date range is capped at 730 days max. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String adId = "adId_example"; // String | 
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of date range (YYYY-MM-DD). Defaults to 90 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of date range (YYYY-MM-DD). Defaults to today. Max 730-day range.
        String breakdowns = "breakdowns_example"; // String | Comma-separated breakdown dimensions.  **Meta**: age, gender, country, publisher_platform, device_platform, region.  **TikTok**: gender, age, country_code, platform, ac, language.  **LinkedIn** (firmographics): job_title, job_function, seniority, industry, company, company_size, country, region. Rows carry the raw pivot `value` plus a resolved `name`. LinkedIn serves these aggregated over the whole range, delays the data 12-24h, and omits segments with fewer than 3 events. 
        try {
            ApiResponse<GetAdAnalytics200Response> response = apiInstance.getAdAnalyticsWithHttpInfo(adId, fromDate, toDate, breakdowns);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getAdAnalytics");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
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
| **fromDate** | **LocalDate**| Start of date range (YYYY-MM-DD). Defaults to 90 days ago. | [optional] |
| **toDate** | **LocalDate**| End of date range (YYYY-MM-DD). Defaults to today. Max 730-day range. | [optional] |
| **breakdowns** | **String**| Comma-separated breakdown dimensions.  **Meta**: age, gender, country, publisher_platform, device_platform, region.  **TikTok**: gender, age, country_code, platform, ac, language.  **LinkedIn** (firmographics): job_title, job_function, seniority, industry, company, company_size, country, region. Rows carry the raw pivot &#x60;value&#x60; plus a resolved &#x60;name&#x60;. LinkedIn serves these aggregated over the whole range, delays the data 12-24h, and omits segments with fewer than 3 events.  | [optional] |

### Return type

ApiResponse<[**GetAdAnalytics200Response**](GetAdAnalytics200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad analytics |  -  |
| **202** | Part of the requested date range predates the ingested history; a background backfill job has been queued. The body has the same shape as the 200 response, carries the currently-available data, and includes &#x60;backfillPending: true&#x60;. A &#x60;Retry-After&#x60; header carries the recommended poll interval in seconds. Allow the job a short time to run (typically 1-3 minutes) and submit the request again; once ingestion completes the same request returns 200 with the full range. |  -  |
| **400** | Invalid parameter (e.g. an unknown &#x60;breakdowns&#x60; dimension). The message lists the offending value(s) and the supported set. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |


## getAdComments

> GetAdComments200Response getAdComments(adId, placement, limit, cursor)

List comments on an ad

Returns comments on an ad&#39;s underlying creative post. Useful for moderating or analyzing engagement on dark posts (ad creatives that never went live organically), which the regular GET /v1/inbox/comments/{postId} endpoint cannot serve because dark posts are not in Zernio&#39;s post database.  An ad that runs on both Facebook feed and Instagram feed has two separate underlying posts with separate comment threads (the creative&#39;s effective_object_story_id and effective_instagram_media_id). Use the &#x60;placement&#x60; query param to pick one; with no param the Instagram side is returned when it exists, otherwise Facebook. The identifiers are read from the ad record (persisted during sync) with a Marketing-API fallback for ads that predate the field.  For Instagram-placed comments, the Instagram account that runs the ad must be connected to Zernio — those comments are read through that account&#39;s token. If no connected Instagram account on the profile can read the ad&#39;s media, the call returns ads_connection_required (the Facebook side, if any, is still readable via ?placement&#x3D;facebook).  Meta-only. Other ad platforms (TikTok, LinkedIn, Pinterest, Google, X) do not expose a public per-ad comments API and return feature_not_available.  Requires the Ads add-on. Response shape matches GET /v1/inbox/comments/{postId}.  The &#x60;{adId}&#x60; path segment accepts any identifier dialect Zernio indexes for the ad: Zernio internal &#x60;_id&#x60; (24-char hex), Meta&#39;s numeric &#x60;platformAdId&#x60; (the value shipped in &#x60;comment.received&#x60; webhooks as &#x60;comment.ad.id&#x60;), or the creative&#39;s &#x60;effective_object_story_id&#x60; / &#x60;effective_instagram_media_id&#x60;. Caller doesn&#39;t need a translation step. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String adId = "adId_example"; // String | Internal Zernio ad ID (ObjectId).
        String placement = "facebook"; // String | Which side of the ad to return comments for. Omit to default to the Instagram side when present, else Facebook. Returns ad_not_commentable if the ad has no such placement.
        Integer limit = 25; // Integer | 
        String cursor = "cursor_example"; // String | Pagination cursor from a previous response.
        try {
            GetAdComments200Response result = apiInstance.getAdComments(adId, placement, limit, cursor);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getAdComments");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adId** | **String**| Internal Zernio ad ID (ObjectId). | |
| **placement** | **String**| Which side of the ad to return comments for. Omit to default to the Instagram side when present, else Facebook. Returns ad_not_commentable if the ad has no such placement. | [optional] [enum: facebook, instagram] |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **cursor** | **String**| Pagination cursor from a previous response. | [optional] |

### Return type

[**GetAdComments200Response**](GetAdComments200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comments on the ad |  -  |
| **400** | Invalid ad ID format, or the ad&#39;s creative format does not expose a commentable underlying post (code ad_not_commentable).  |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (legacy plans need the Ads add-on; included by default on usage-based plans), or ad platform is not Meta (code feature_not_available). |  -  |
| **404** | Resource not found |  -  |
| **422** | Ads account token unavailable, or (for Instagram-placed ads) no connected Instagram account on the profile can read the ad&#39;s media (code ads_connection_required).  |  -  |

## getAdCommentsWithHttpInfo

> ApiResponse<GetAdComments200Response> getAdComments getAdCommentsWithHttpInfo(adId, placement, limit, cursor)

List comments on an ad

Returns comments on an ad&#39;s underlying creative post. Useful for moderating or analyzing engagement on dark posts (ad creatives that never went live organically), which the regular GET /v1/inbox/comments/{postId} endpoint cannot serve because dark posts are not in Zernio&#39;s post database.  An ad that runs on both Facebook feed and Instagram feed has two separate underlying posts with separate comment threads (the creative&#39;s effective_object_story_id and effective_instagram_media_id). Use the &#x60;placement&#x60; query param to pick one; with no param the Instagram side is returned when it exists, otherwise Facebook. The identifiers are read from the ad record (persisted during sync) with a Marketing-API fallback for ads that predate the field.  For Instagram-placed comments, the Instagram account that runs the ad must be connected to Zernio — those comments are read through that account&#39;s token. If no connected Instagram account on the profile can read the ad&#39;s media, the call returns ads_connection_required (the Facebook side, if any, is still readable via ?placement&#x3D;facebook).  Meta-only. Other ad platforms (TikTok, LinkedIn, Pinterest, Google, X) do not expose a public per-ad comments API and return feature_not_available.  Requires the Ads add-on. Response shape matches GET /v1/inbox/comments/{postId}.  The &#x60;{adId}&#x60; path segment accepts any identifier dialect Zernio indexes for the ad: Zernio internal &#x60;_id&#x60; (24-char hex), Meta&#39;s numeric &#x60;platformAdId&#x60; (the value shipped in &#x60;comment.received&#x60; webhooks as &#x60;comment.ad.id&#x60;), or the creative&#39;s &#x60;effective_object_story_id&#x60; / &#x60;effective_instagram_media_id&#x60;. Caller doesn&#39;t need a translation step. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String adId = "adId_example"; // String | Internal Zernio ad ID (ObjectId).
        String placement = "facebook"; // String | Which side of the ad to return comments for. Omit to default to the Instagram side when present, else Facebook. Returns ad_not_commentable if the ad has no such placement.
        Integer limit = 25; // Integer | 
        String cursor = "cursor_example"; // String | Pagination cursor from a previous response.
        try {
            ApiResponse<GetAdComments200Response> response = apiInstance.getAdCommentsWithHttpInfo(adId, placement, limit, cursor);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getAdComments");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adId** | **String**| Internal Zernio ad ID (ObjectId). | |
| **placement** | **String**| Which side of the ad to return comments for. Omit to default to the Instagram side when present, else Facebook. Returns ad_not_commentable if the ad has no such placement. | [optional] [enum: facebook, instagram] |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **cursor** | **String**| Pagination cursor from a previous response. | [optional] |

### Return type

ApiResponse<[**GetAdComments200Response**](GetAdComments200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Comments on the ad |  -  |
| **400** | Invalid ad ID format, or the ad&#39;s creative format does not expose a commentable underlying post (code ad_not_commentable).  |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (legacy plans need the Ads add-on; included by default on usage-based plans), or ad platform is not Meta (code feature_not_available). |  -  |
| **404** | Resource not found |  -  |
| **422** | Ads account token unavailable, or (for Instagram-placed ads) no connected Instagram account on the profile can read the ad&#39;s media (code ads_connection_required).  |  -  |


## getAdCreative

> GetAdCreative200Response getAdCreative(creativeId, accountId, fields)

Creative details (Meta)

One creative&#39;s details, verbatim from Meta. &#x60;fields&#x60; is a raw-passthrough override of the default projection. Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String creativeId = "creativeId_example"; // String | Platform creative id
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String fields = "fields_example"; // String | Comma-separated Graph field override (supports nested {} projections).
        try {
            GetAdCreative200Response result = apiInstance.getAdCreative(creativeId, accountId, fields);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getAdCreative");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **creativeId** | **String**| Platform creative id | |
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **fields** | **String**| Comma-separated Graph field override (supports nested {} projections). | [optional] |

### Return type

[**GetAdCreative200Response**](GetAdCreative200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Creative details |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## getAdCreativeWithHttpInfo

> ApiResponse<GetAdCreative200Response> getAdCreative getAdCreativeWithHttpInfo(creativeId, accountId, fields)

Creative details (Meta)

One creative&#39;s details, verbatim from Meta. &#x60;fields&#x60; is a raw-passthrough override of the default projection. Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String creativeId = "creativeId_example"; // String | Platform creative id
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String fields = "fields_example"; // String | Comma-separated Graph field override (supports nested {} projections).
        try {
            ApiResponse<GetAdCreative200Response> response = apiInstance.getAdCreativeWithHttpInfo(creativeId, accountId, fields);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getAdCreative");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **creativeId** | **String**| Platform creative id | |
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **fields** | **String**| Comma-separated Graph field override (supports nested {} projections). | [optional] |

### Return type

ApiResponse<[**GetAdCreative200Response**](GetAdCreative200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Creative details |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## getAdInsightsReport

> GetAdInsightsReport200Response getAdInsightsReport(reportRunId, accountId, limit, after)

Poll an async insights report run (Meta)

Status and results for a report run created via POST /v1/ads/insights/reports. While the job runs, returns &#x60;status&#x60; and &#x60;percentCompletion&#x60;. Once &#x60;status&#x60; is \&quot;Job Completed\&quot; the response also carries a &#x60;data&#x60; page, cursor-paginated via &#x60;limit&#x60; / &#x60;after&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String reportRunId = "reportRunId_example"; // String | 
        String accountId = "accountId_example"; // String | Zernio SocialAccount id used to resolve the Meta token (must be the same connection that created the run).
        Integer limit = 25; // Integer | 
        String after = "after_example"; // String | 
        try {
            GetAdInsightsReport200Response result = apiInstance.getAdInsightsReport(reportRunId, accountId, limit, after);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getAdInsightsReport");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **reportRunId** | **String**|  | |
| **accountId** | **String**| Zernio SocialAccount id used to resolve the Meta token (must be the same connection that created the run). | |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **after** | **String**|  | [optional] |

### Return type

[**GetAdInsightsReport200Response**](GetAdInsightsReport200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Report run status (plus results when completed) |  -  |
| **400** | Invalid input, or the report run is not readable with this account&#39;s token |  -  |
| **401** | Unauthorized |  -  |
| **429** | Meta rate limit reached |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## getAdInsightsReportWithHttpInfo

> ApiResponse<GetAdInsightsReport200Response> getAdInsightsReport getAdInsightsReportWithHttpInfo(reportRunId, accountId, limit, after)

Poll an async insights report run (Meta)

Status and results for a report run created via POST /v1/ads/insights/reports. While the job runs, returns &#x60;status&#x60; and &#x60;percentCompletion&#x60;. Once &#x60;status&#x60; is \&quot;Job Completed\&quot; the response also carries a &#x60;data&#x60; page, cursor-paginated via &#x60;limit&#x60; / &#x60;after&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String reportRunId = "reportRunId_example"; // String | 
        String accountId = "accountId_example"; // String | Zernio SocialAccount id used to resolve the Meta token (must be the same connection that created the run).
        Integer limit = 25; // Integer | 
        String after = "after_example"; // String | 
        try {
            ApiResponse<GetAdInsightsReport200Response> response = apiInstance.getAdInsightsReportWithHttpInfo(reportRunId, accountId, limit, after);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getAdInsightsReport");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **reportRunId** | **String**|  | |
| **accountId** | **String**| Zernio SocialAccount id used to resolve the Meta token (must be the same connection that created the run). | |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **after** | **String**|  | [optional] |

### Return type

ApiResponse<[**GetAdInsightsReport200Response**](GetAdInsightsReport200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Report run status (plus results when completed) |  -  |
| **400** | Invalid input, or the report run is not readable with this account&#39;s token |  -  |
| **401** | Unauthorized |  -  |
| **429** | Meta rate limit reached |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## getAdPreviews

> GetAdPreviews200Response getAdPreviews(adId, formats)

Render previews of an existing ad (Meta)

Renders an EXISTING ad per placement via Meta&#39;s &#x60;/{ad_id}/previews&#x60;. Each preview is an HTML &#x60;&lt;iframe&gt;&#x60; snippet embeddable directly. Unknown &#x60;formats&#x60; values return Meta&#39;s 400 verbatim. Meta only. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String adId = "adId_example"; // String | Zernio ad id (24-char hex).
        String formats = "formats_example"; // String | Comma-separated Meta ad_format values (max 10), one preview per format. Defaults to DESKTOP_FEED_STANDARD.
        try {
            GetAdPreviews200Response result = apiInstance.getAdPreviews(adId, formats);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getAdPreviews");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adId** | **String**| Zernio ad id (24-char hex). | |
| **formats** | **String**| Comma-separated Meta ad_format values (max 10), one preview per format. Defaults to DESKTOP_FEED_STANDARD. | [optional] |

### Return type

[**GetAdPreviews200Response**](GetAdPreviews200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rendered previews |  -  |
| **400** | Invalid input, or Meta rejected the ad_format — message carries Meta&#39;s error |  -  |
| **401** | Unauthorized |  -  |
| **404** | Ad not found |  -  |
| **429** | Meta rate limit reached |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## getAdPreviewsWithHttpInfo

> ApiResponse<GetAdPreviews200Response> getAdPreviews getAdPreviewsWithHttpInfo(adId, formats)

Render previews of an existing ad (Meta)

Renders an EXISTING ad per placement via Meta&#39;s &#x60;/{ad_id}/previews&#x60;. Each preview is an HTML &#x60;&lt;iframe&gt;&#x60; snippet embeddable directly. Unknown &#x60;formats&#x60; values return Meta&#39;s 400 verbatim. Meta only. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String adId = "adId_example"; // String | Zernio ad id (24-char hex).
        String formats = "formats_example"; // String | Comma-separated Meta ad_format values (max 10), one preview per format. Defaults to DESKTOP_FEED_STANDARD.
        try {
            ApiResponse<GetAdPreviews200Response> response = apiInstance.getAdPreviewsWithHttpInfo(adId, formats);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getAdPreviews");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adId** | **String**| Zernio ad id (24-char hex). | |
| **formats** | **String**| Comma-separated Meta ad_format values (max 10), one preview per format. Defaults to DESKTOP_FEED_STANDARD. | [optional] |

### Return type

ApiResponse<[**GetAdPreviews200Response**](GetAdPreviews200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rendered previews |  -  |
| **400** | Invalid input, or Meta rejected the ad_format — message carries Meta&#39;s error |  -  |
| **401** | Unauthorized |  -  |
| **404** | Ad not found |  -  |
| **429** | Meta rate limit reached |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## getAdTrackingTags

> GetAdTrackingTags200Response getAdTrackingTags(adId)

Get ad tracking tags

Unified read of the platform&#39;s native click-URL tracking params. - Meta (facebook/instagram): the creative&#39;s &#x60;url_tags&#x60; (and template_url_spec). - Google (googleads): the campaign&#39;s &#x60;trackingUrlTemplate&#x60; + &#x60;finalUrlSuffix&#x60;.   Subject to the Google Ads API access-tier daily quota; bulk audits need Standard access. - LinkedIn (linkedinads): the campaign&#39;s Dynamic UTM &#x60;dynamicValueParameters&#x60; + &#x60;customValueParameters&#x60;. Returns 405 for platforms without a click-URL tracking surface (TikTok, X, Pinterest). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String adId = "adId_example"; // String | Ad id (hex _id, platformAdId, or effective story/media id).
        try {
            GetAdTrackingTags200Response result = apiInstance.getAdTrackingTags(adId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getAdTrackingTags");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adId** | **String**| Ad id (hex _id, platformAdId, or effective story/media id). | |

### Return type

[**GetAdTrackingTags200Response**](GetAdTrackingTags200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tracking tags for the ad&#39;s platform (shape varies by platform). |  -  |
| **401** | Unauthorized |  -  |
| **404** | Ad not found |  -  |
| **405** | Platform has no click-URL tracking surface |  -  |

## getAdTrackingTagsWithHttpInfo

> ApiResponse<GetAdTrackingTags200Response> getAdTrackingTags getAdTrackingTagsWithHttpInfo(adId)

Get ad tracking tags

Unified read of the platform&#39;s native click-URL tracking params. - Meta (facebook/instagram): the creative&#39;s &#x60;url_tags&#x60; (and template_url_spec). - Google (googleads): the campaign&#39;s &#x60;trackingUrlTemplate&#x60; + &#x60;finalUrlSuffix&#x60;.   Subject to the Google Ads API access-tier daily quota; bulk audits need Standard access. - LinkedIn (linkedinads): the campaign&#39;s Dynamic UTM &#x60;dynamicValueParameters&#x60; + &#x60;customValueParameters&#x60;. Returns 405 for platforms without a click-URL tracking surface (TikTok, X, Pinterest). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String adId = "adId_example"; // String | Ad id (hex _id, platformAdId, or effective story/media id).
        try {
            ApiResponse<GetAdTrackingTags200Response> response = apiInstance.getAdTrackingTagsWithHttpInfo(adId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getAdTrackingTags");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **adId** | **String**| Ad id (hex _id, platformAdId, or effective story/media id). | |

### Return type

ApiResponse<[**GetAdTrackingTags200Response**](GetAdTrackingTags200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Tracking tags for the ad&#39;s platform (shape varies by platform). |  -  |
| **401** | Unauthorized |  -  |
| **404** | Ad not found |  -  |
| **405** | Platform has no click-URL tracking surface |  -  |


## getAdsActivityLog

> GetAdsActivityLog200Response getAdsActivityLog(accountId, adAccountId, since, until, objectId, limit, after)

Ad account change / audit log (Meta)

Account-level audit log from Meta&#39;s &#x60;/act_X/activities&#x60;: who changed what and when (creates, edits, status flips, budget changes...) with Meta&#39;s translated event names and the structured before/after in &#x60;extra_data&#x60;. Rows are returned verbatim. Meta has no server-side per-object filter on this edge, so &#x60;objectId&#x60; filters the returned page client-side (combine with paging to walk history for one campaign/ad set/ad). Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>).
        LocalDate since = LocalDate.now(); // LocalDate | Start of range (YYYY-MM-DD).
        LocalDate until = LocalDate.now(); // LocalDate | End of range (YYYY-MM-DD).
        String objectId = "objectId_example"; // String | Client-side filter to one Meta object id (campaign, ad set or ad).
        Integer limit = 50; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            GetAdsActivityLog200Response result = apiInstance.getAdsActivityLog(accountId, adAccountId, since, until, objectId, limit, after);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getAdsActivityLog");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **adAccountId** | **String**| Meta ad account id (act_&lt;n&gt;). | |
| **since** | **LocalDate**| Start of range (YYYY-MM-DD). | [optional] |
| **until** | **LocalDate**| End of range (YYYY-MM-DD). | [optional] |
| **objectId** | **String**| Client-side filter to one Meta object id (campaign, ad set or ad). | [optional] |
| **limit** | **Integer**| Rows per page | [optional] [default to 50] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

[**GetAdsActivityLog200Response**](GetAdsActivityLog200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Activity rows (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## getAdsActivityLogWithHttpInfo

> ApiResponse<GetAdsActivityLog200Response> getAdsActivityLog getAdsActivityLogWithHttpInfo(accountId, adAccountId, since, until, objectId, limit, after)

Ad account change / audit log (Meta)

Account-level audit log from Meta&#39;s &#x60;/act_X/activities&#x60;: who changed what and when (creates, edits, status flips, budget changes...) with Meta&#39;s translated event names and the structured before/after in &#x60;extra_data&#x60;. Rows are returned verbatim. Meta has no server-side per-object filter on this edge, so &#x60;objectId&#x60; filters the returned page client-side (combine with paging to walk history for one campaign/ad set/ad). Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>).
        LocalDate since = LocalDate.now(); // LocalDate | Start of range (YYYY-MM-DD).
        LocalDate until = LocalDate.now(); // LocalDate | End of range (YYYY-MM-DD).
        String objectId = "objectId_example"; // String | Client-side filter to one Meta object id (campaign, ad set or ad).
        Integer limit = 50; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ApiResponse<GetAdsActivityLog200Response> response = apiInstance.getAdsActivityLogWithHttpInfo(accountId, adAccountId, since, until, objectId, limit, after);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getAdsActivityLog");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **adAccountId** | **String**| Meta ad account id (act_&lt;n&gt;). | |
| **since** | **LocalDate**| Start of range (YYYY-MM-DD). | [optional] |
| **until** | **LocalDate**| End of range (YYYY-MM-DD). | [optional] |
| **objectId** | **String**| Client-side filter to one Meta object id (campaign, ad set or ad). | [optional] |
| **limit** | **Integer**| Rows per page | [optional] [default to 50] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

ApiResponse<[**GetAdsActivityLog200Response**](GetAdsActivityLog200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Activity rows (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## getCampaignAnalytics

> GetCampaignAnalytics200Response getCampaignAnalytics(campaignId, platform, fromDate, toDate, breakdowns)

Get campaign analytics

Returns performance analytics for a whole campaign in one call: summary metrics, a daily timeline over the requested date range (summed across the campaign&#39;s ads), and optional demographic breakdowns. Breakdowns are fetched live from Meta at the campaign level (one call per dimension, no per-ad fan-out), so an agency dashboard gets campaign-level age/gender/etc. without summing thousands of per-ad reads. &#x60;campaignId&#x60; is the platform campaign id; pass &#x60;platform&#x60; when a campaign id could be ambiguous across platforms. If no date range is provided, defaults to the last 90 days. Date range is capped at 730 days max. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign id (platformCampaignId).
        String platform = "platform_example"; // String | Disambiguate when the campaign id exists across platforms (e.g. facebook, instagram).
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of date range (YYYY-MM-DD). Defaults to 90 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of date range (YYYY-MM-DD). Defaults to today. Max 730-day range.
        String breakdowns = "breakdowns_example"; // String | Comma-separated breakdown dimensions.  **Meta**: age, gender, country, publisher_platform, device_platform, region, platform_position, impression_device, video_asset, image_asset, body_asset, title_asset.  **LinkedIn** (firmographics): job_title, job_function, seniority, industry, company, company_size, country, region. Rows carry the raw pivot `value` plus a resolved `name`. LinkedIn serves these aggregated over the whole range, delays the data 12-24h, and omits segments with fewer than 3 events. 
        try {
            GetCampaignAnalytics200Response result = apiInstance.getCampaignAnalytics(campaignId, platform, fromDate, toDate, breakdowns);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getCampaignAnalytics");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Platform campaign id (platformCampaignId). | |
| **platform** | **String**| Disambiguate when the campaign id exists across platforms (e.g. facebook, instagram). | [optional] |
| **fromDate** | **LocalDate**| Start of date range (YYYY-MM-DD). Defaults to 90 days ago. | [optional] |
| **toDate** | **LocalDate**| End of date range (YYYY-MM-DD). Defaults to today. Max 730-day range. | [optional] |
| **breakdowns** | **String**| Comma-separated breakdown dimensions.  **Meta**: age, gender, country, publisher_platform, device_platform, region, platform_position, impression_device, video_asset, image_asset, body_asset, title_asset.  **LinkedIn** (firmographics): job_title, job_function, seniority, industry, company, company_size, country, region. Rows carry the raw pivot &#x60;value&#x60; plus a resolved &#x60;name&#x60;. LinkedIn serves these aggregated over the whole range, delays the data 12-24h, and omits segments with fewer than 3 events.  | [optional] |

### Return type

[**GetCampaignAnalytics200Response**](GetCampaignAnalytics200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign analytics |  -  |
| **202** | Part of the requested date range predates the ingested history; a background backfill job has been queued. The body has the same shape as the 200 response, carries the currently-available data, and includes &#x60;backfillPending: true&#x60;. A &#x60;Retry-After&#x60; header carries the recommended poll interval in seconds. Allow the job a short time to run (typically 1-3 minutes) and submit the request again; once ingestion completes the same request returns 200 with the full range. |  -  |
| **400** | Invalid parameter (e.g. an unknown &#x60;breakdowns&#x60; dimension). The message lists the offending value(s) and the supported set. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |

## getCampaignAnalyticsWithHttpInfo

> ApiResponse<GetCampaignAnalytics200Response> getCampaignAnalytics getCampaignAnalyticsWithHttpInfo(campaignId, platform, fromDate, toDate, breakdowns)

Get campaign analytics

Returns performance analytics for a whole campaign in one call: summary metrics, a daily timeline over the requested date range (summed across the campaign&#39;s ads), and optional demographic breakdowns. Breakdowns are fetched live from Meta at the campaign level (one call per dimension, no per-ad fan-out), so an agency dashboard gets campaign-level age/gender/etc. without summing thousands of per-ad reads. &#x60;campaignId&#x60; is the platform campaign id; pass &#x60;platform&#x60; when a campaign id could be ambiguous across platforms. If no date range is provided, defaults to the last 90 days. Date range is capped at 730 days max. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String campaignId = "campaignId_example"; // String | Platform campaign id (platformCampaignId).
        String platform = "platform_example"; // String | Disambiguate when the campaign id exists across platforms (e.g. facebook, instagram).
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of date range (YYYY-MM-DD). Defaults to 90 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of date range (YYYY-MM-DD). Defaults to today. Max 730-day range.
        String breakdowns = "breakdowns_example"; // String | Comma-separated breakdown dimensions.  **Meta**: age, gender, country, publisher_platform, device_platform, region, platform_position, impression_device, video_asset, image_asset, body_asset, title_asset.  **LinkedIn** (firmographics): job_title, job_function, seniority, industry, company, company_size, country, region. Rows carry the raw pivot `value` plus a resolved `name`. LinkedIn serves these aggregated over the whole range, delays the data 12-24h, and omits segments with fewer than 3 events. 
        try {
            ApiResponse<GetCampaignAnalytics200Response> response = apiInstance.getCampaignAnalyticsWithHttpInfo(campaignId, platform, fromDate, toDate, breakdowns);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getCampaignAnalytics");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **campaignId** | **String**| Platform campaign id (platformCampaignId). | |
| **platform** | **String**| Disambiguate when the campaign id exists across platforms (e.g. facebook, instagram). | [optional] |
| **fromDate** | **LocalDate**| Start of date range (YYYY-MM-DD). Defaults to 90 days ago. | [optional] |
| **toDate** | **LocalDate**| End of date range (YYYY-MM-DD). Defaults to today. Max 730-day range. | [optional] |
| **breakdowns** | **String**| Comma-separated breakdown dimensions.  **Meta**: age, gender, country, publisher_platform, device_platform, region, platform_position, impression_device, video_asset, image_asset, body_asset, title_asset.  **LinkedIn** (firmographics): job_title, job_function, seniority, industry, company, company_size, country, region. Rows carry the raw pivot &#x60;value&#x60; plus a resolved &#x60;name&#x60;. LinkedIn serves these aggregated over the whole range, delays the data 12-24h, and omits segments with fewer than 3 events.  | [optional] |

### Return type

ApiResponse<[**GetCampaignAnalytics200Response**](GetCampaignAnalytics200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Campaign analytics |  -  |
| **202** | Part of the requested date range predates the ingested history; a background backfill job has been queued. The body has the same shape as the 200 response, carries the currently-available data, and includes &#x60;backfillPending: true&#x60;. A &#x60;Retry-After&#x60; header carries the recommended poll interval in seconds. Allow the job a short time to run (typically 1-3 minutes) and submit the request again; once ingestion completes the same request returns 200 with the full range. |  -  |
| **400** | Invalid parameter (e.g. an unknown &#x60;breakdowns&#x60; dimension). The message lists the offending value(s) and the supported set. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Resource not found |  -  |


## getConversionDestination

> GetConversionDestination200Response getConversionDestination(accountId, destinationId, adAccountId)

Get a conversion destination

LinkedIn-only today. Returns the full destination record for one conversion rule. The &#x60;adAccountId&#x60; query parameter is required because LinkedIn rules are scoped to a sponsored ad account. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String destinationId = "destinationId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | Numeric ID or full `urn:li:sponsoredAccount:{id}` URN.
        try {
            GetConversionDestination200Response result = apiInstance.getConversionDestination(accountId, destinationId, adAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getConversionDestination");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**|  | |
| **destinationId** | **String**|  | |
| **adAccountId** | **String**| Numeric ID or full &#x60;urn:li:sponsoredAccount:{id}&#x60; URN. | |

### Return type

[**GetConversionDestination200Response**](GetConversionDestination200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Destination fetched |  -  |
| **400** | Validation error. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on or LinkedIn reconnect required. |  -  |
| **404** | Account or destination not found. |  -  |
| **405** | Platform does not support fetching a single destination. |  -  |
| **429** | LinkedIn rate limit hit. Retry with backoff. |  -  |

## getConversionDestinationWithHttpInfo

> ApiResponse<GetConversionDestination200Response> getConversionDestination getConversionDestinationWithHttpInfo(accountId, destinationId, adAccountId)

Get a conversion destination

LinkedIn-only today. Returns the full destination record for one conversion rule. The &#x60;adAccountId&#x60; query parameter is required because LinkedIn rules are scoped to a sponsored ad account. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String destinationId = "destinationId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | Numeric ID or full `urn:li:sponsoredAccount:{id}` URN.
        try {
            ApiResponse<GetConversionDestination200Response> response = apiInstance.getConversionDestinationWithHttpInfo(accountId, destinationId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getConversionDestination");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**|  | |
| **destinationId** | **String**|  | |
| **adAccountId** | **String**| Numeric ID or full &#x60;urn:li:sponsoredAccount:{id}&#x60; URN. | |

### Return type

ApiResponse<[**GetConversionDestination200Response**](GetConversionDestination200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Destination fetched |  -  |
| **400** | Validation error. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on or LinkedIn reconnect required. |  -  |
| **404** | Account or destination not found. |  -  |
| **405** | Platform does not support fetching a single destination. |  -  |
| **429** | LinkedIn rate limit hit. Retry with backoff. |  -  |


## getConversionMetrics

> GetConversionMetrics200Response getConversionMetrics(accountId, destinationId, adAccountId, startDate, endDate, granularity)

Get attribution metrics

LinkedIn-only today. Returns conversion-attribution metrics (&#x60;externalWebsiteConversions&#x60;, &#x60;externalWebsitePostClickConversions&#x60;, &#x60;externalWebsitePostViewConversions&#x60;, &#x60;conversionValueInLocalCurrency&#x60;, &#x60;qualifiedLeads&#x60;, &#x60;costInLocalCurrency&#x60;) bucketed by date.  Date-range constraints (passed through from LinkedIn): - &#x60;granularity&#x3D;DAILY&#x60; is retained for ~6 months only - &#x60;granularity&#x3D;ALL&#x60; with a range &gt; 6 months auto-rounds to month boundaries - &#x60;granularity&#x3D;MONTHLY&#x60;/&#x60;YEARLY&#x60; retains 24 months  Throttle: LinkedIn caps adAnalytics at 45M metric values per 5-minute window across the calling token. Single-rule queries are well within that limit; surfaces as 429 if hit. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String destinationId = "destinationId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | 
        String startDate = "startDate_example"; // String | 
        String endDate = "endDate_example"; // String | 
        String granularity = "ALL"; // String | 
        try {
            GetConversionMetrics200Response result = apiInstance.getConversionMetrics(accountId, destinationId, adAccountId, startDate, endDate, granularity);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getConversionMetrics");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**|  | |
| **destinationId** | **String**|  | |
| **adAccountId** | **String**|  | |
| **startDate** | **String**|  | |
| **endDate** | **String**|  | [optional] |
| **granularity** | **String**|  | [optional] [default to DAILY] [enum: ALL, DAILY, MONTHLY, YEARLY] |

### Return type

[**GetConversionMetrics200Response**](GetConversionMetrics200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metrics rows |  -  |
| **400** | Validation error or invalid date range. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on or LinkedIn reconnect required. |  -  |
| **404** | Account or destination not found. |  -  |
| **405** | Platform does not support metrics readback. |  -  |
| **429** | LinkedIn analytics rate limit hit. |  -  |

## getConversionMetricsWithHttpInfo

> ApiResponse<GetConversionMetrics200Response> getConversionMetrics getConversionMetricsWithHttpInfo(accountId, destinationId, adAccountId, startDate, endDate, granularity)

Get attribution metrics

LinkedIn-only today. Returns conversion-attribution metrics (&#x60;externalWebsiteConversions&#x60;, &#x60;externalWebsitePostClickConversions&#x60;, &#x60;externalWebsitePostViewConversions&#x60;, &#x60;conversionValueInLocalCurrency&#x60;, &#x60;qualifiedLeads&#x60;, &#x60;costInLocalCurrency&#x60;) bucketed by date.  Date-range constraints (passed through from LinkedIn): - &#x60;granularity&#x3D;DAILY&#x60; is retained for ~6 months only - &#x60;granularity&#x3D;ALL&#x60; with a range &gt; 6 months auto-rounds to month boundaries - &#x60;granularity&#x3D;MONTHLY&#x60;/&#x60;YEARLY&#x60; retains 24 months  Throttle: LinkedIn caps adAnalytics at 45M metric values per 5-minute window across the calling token. Single-rule queries are well within that limit; surfaces as 429 if hit. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String destinationId = "destinationId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | 
        String startDate = "startDate_example"; // String | 
        String endDate = "endDate_example"; // String | 
        String granularity = "ALL"; // String | 
        try {
            ApiResponse<GetConversionMetrics200Response> response = apiInstance.getConversionMetricsWithHttpInfo(accountId, destinationId, adAccountId, startDate, endDate, granularity);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getConversionMetrics");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**|  | |
| **destinationId** | **String**|  | |
| **adAccountId** | **String**|  | |
| **startDate** | **String**|  | |
| **endDate** | **String**|  | [optional] |
| **granularity** | **String**|  | [optional] [default to DAILY] [enum: ALL, DAILY, MONTHLY, YEARLY] |

### Return type

ApiResponse<[**GetConversionMetrics200Response**](GetConversionMetrics200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Metrics rows |  -  |
| **400** | Validation error or invalid date range. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on or LinkedIn reconnect required. |  -  |
| **404** | Account or destination not found. |  -  |
| **405** | Platform does not support metrics readback. |  -  |
| **429** | LinkedIn analytics rate limit hit. |  -  |


## getConversionsQuality

> GetConversionsQuality200Response getConversionsQuality(accountId, destinationId)

Get Event Match Quality

Reads Meta Event Match Quality (EMQ) and pixel↔CAPI event coverage for a pixel/dataset, live from Meta&#39;s Dataset Quality API. Web events only (a Meta limitation). Meta-only; other platforms return 405. Requires the Ads add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | SocialAccount _id (must be a metaads account).
        String destinationId = "destinationId_example"; // String | Meta pixel/dataset ID.
        try {
            GetConversionsQuality200Response result = apiInstance.getConversionsQuality(accountId, destinationId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getConversionsQuality");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| SocialAccount _id (must be a metaads account). | |
| **destinationId** | **String**| Meta pixel/dataset ID. | |

### Return type

[**GetConversionsQuality200Response**](GetConversionsQuality200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Match-quality rows, one per event name. |  -  |
| **401** | Unauthorized |  -  |
| **405** | Platform does not expose Event Match Quality (non-Meta). |  -  |

## getConversionsQualityWithHttpInfo

> ApiResponse<GetConversionsQuality200Response> getConversionsQuality getConversionsQualityWithHttpInfo(accountId, destinationId)

Get Event Match Quality

Reads Meta Event Match Quality (EMQ) and pixel↔CAPI event coverage for a pixel/dataset, live from Meta&#39;s Dataset Quality API. Web events only (a Meta limitation). Meta-only; other platforms return 405. Requires the Ads add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | SocialAccount _id (must be a metaads account).
        String destinationId = "destinationId_example"; // String | Meta pixel/dataset ID.
        try {
            ApiResponse<GetConversionsQuality200Response> response = apiInstance.getConversionsQualityWithHttpInfo(accountId, destinationId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getConversionsQuality");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| SocialAccount _id (must be a metaads account). | |
| **destinationId** | **String**| Meta pixel/dataset ID. | |

### Return type

ApiResponse<[**GetConversionsQuality200Response**](GetConversionsQuality200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Match-quality rows, one per event name. |  -  |
| **401** | Unauthorized |  -  |
| **405** | Platform does not expose Event Match Quality (non-Meta). |  -  |


## getDsaDefaults

> UpdateAdAccount200Response getDsaDefaults(accountId, adAccountId)

Get ad account DSA defaults

Returns the default DSA beneficiary and payor currently set on a Meta ad account, whether they were set via &#x60;PATCH /v1/ads/accounts&#x60; or in Meta Ads Manager. Fields are omitted when no default is configured. Meta accounts only. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | Social account ID (metaads, or a facebook/instagram posting account)
        String adAccountId = "adAccountId_example"; // String | Meta ad account ID (act_...)
        try {
            UpdateAdAccount200Response result = apiInstance.getDsaDefaults(accountId, adAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getDsaDefaults");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Social account ID (metaads, or a facebook/instagram posting account) | |
| **adAccountId** | **String**| Meta ad account ID (act_...) | |

### Return type

[**UpdateAdAccount200Response**](UpdateAdAccount200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current DSA defaults (empty object when none are set) |  -  |
| **400** | Non-Meta adAccountId |  -  |
| **401** | Unauthorized |  -  |
| **404** | Social account not found |  -  |

## getDsaDefaultsWithHttpInfo

> ApiResponse<UpdateAdAccount200Response> getDsaDefaults getDsaDefaultsWithHttpInfo(accountId, adAccountId)

Get ad account DSA defaults

Returns the default DSA beneficiary and payor currently set on a Meta ad account, whether they were set via &#x60;PATCH /v1/ads/accounts&#x60; or in Meta Ads Manager. Fields are omitted when no default is configured. Meta accounts only. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | Social account ID (metaads, or a facebook/instagram posting account)
        String adAccountId = "adAccountId_example"; // String | Meta ad account ID (act_...)
        try {
            ApiResponse<UpdateAdAccount200Response> response = apiInstance.getDsaDefaultsWithHttpInfo(accountId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getDsaDefaults");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Social account ID (metaads, or a facebook/instagram posting account) | |
| **adAccountId** | **String**| Meta ad account ID (act_...) | |

### Return type

ApiResponse<[**UpdateAdAccount200Response**](UpdateAdAccount200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current DSA defaults (empty object when none are set) |  -  |
| **400** | Non-Meta adAccountId |  -  |
| **401** | Unauthorized |  -  |
| **404** | Social account not found |  -  |


## getDsaRecommendations

> GetDsaRecommendations200Response getDsaRecommendations(accountId, adAccountId)

List DSA beneficiary/payor suggestions

Returns Meta&#39;s suggested beneficiary/payor names for an ad account, derived by Meta from the account&#39;s recent activity. Useful for prefilling &#x60;dsaBeneficiary&#x60;/&#x60;dsaPayor&#x60; inputs, or the defaults sent to &#x60;PATCH /v1/ads/accounts&#x60;, in your own UI.  Meta returns a single flat list. Entries are not labeled as beneficiary or payor, and since these are legal disclosures Zernio never applies them automatically: let your user pick the right entity. The list may be empty for accounts with little activity. Meta accounts only. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | Social account ID (metaads, or a facebook/instagram posting account)
        String adAccountId = "adAccountId_example"; // String | Meta ad account ID (act_...)
        try {
            GetDsaRecommendations200Response result = apiInstance.getDsaRecommendations(accountId, adAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getDsaRecommendations");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Social account ID (metaads, or a facebook/instagram posting account) | |
| **adAccountId** | **String**| Meta ad account ID (act_...) | |

### Return type

[**GetDsaRecommendations200Response**](GetDsaRecommendations200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Suggested DSA strings (may be empty when Meta has no recommendations) |  -  |
| **400** | Non-Meta adAccountId |  -  |
| **401** | Unauthorized |  -  |
| **404** | Social account not found |  -  |

## getDsaRecommendationsWithHttpInfo

> ApiResponse<GetDsaRecommendations200Response> getDsaRecommendations getDsaRecommendationsWithHttpInfo(accountId, adAccountId)

List DSA beneficiary/payor suggestions

Returns Meta&#39;s suggested beneficiary/payor names for an ad account, derived by Meta from the account&#39;s recent activity. Useful for prefilling &#x60;dsaBeneficiary&#x60;/&#x60;dsaPayor&#x60; inputs, or the defaults sent to &#x60;PATCH /v1/ads/accounts&#x60;, in your own UI.  Meta returns a single flat list. Entries are not labeled as beneficiary or payor, and since these are legal disclosures Zernio never applies them automatically: let your user pick the right entity. The list may be empty for accounts with little activity. Meta accounts only. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | Social account ID (metaads, or a facebook/instagram posting account)
        String adAccountId = "adAccountId_example"; // String | Meta ad account ID (act_...)
        try {
            ApiResponse<GetDsaRecommendations200Response> response = apiInstance.getDsaRecommendationsWithHttpInfo(accountId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getDsaRecommendations");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Social account ID (metaads, or a facebook/instagram posting account) | |
| **adAccountId** | **String**| Meta ad account ID (act_...) | |

### Return type

ApiResponse<[**GetDsaRecommendations200Response**](GetDsaRecommendations200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Suggested DSA strings (may be empty when Meta has no recommendations) |  -  |
| **400** | Non-Meta adAccountId |  -  |
| **401** | Unauthorized |  -  |
| **404** | Social account not found |  -  |


## getLeadForm

> GetLeadForm200Response getLeadForm(formId, accountId)

Get a lead form

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String formId = "formId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            GetLeadForm200Response result = apiInstance.getLeadForm(formId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getLeadForm");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **formId** | **String**|  | |
| **accountId** | **String**|  | |

### Return type

[**GetLeadForm200Response**](GetLeadForm200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Form metadata. |  -  |
| **401** | Unauthorized |  -  |

## getLeadFormWithHttpInfo

> ApiResponse<GetLeadForm200Response> getLeadForm getLeadFormWithHttpInfo(formId, accountId)

Get a lead form

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String formId = "formId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        try {
            ApiResponse<GetLeadForm200Response> response = apiInstance.getLeadFormWithHttpInfo(formId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getLeadForm");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **formId** | **String**|  | |
| **accountId** | **String**|  | |

### Return type

ApiResponse<[**GetLeadForm200Response**](GetLeadForm200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Form metadata. |  -  |
| **401** | Unauthorized |  -  |


## getLinkedInBidPricing

> GetLinkedInBidPricing200Response getLinkedInBidPricing(getLinkedInBidPricingRequest)

Suggested bid and budget bounds (LinkedIn)

LinkedIn-only. Returns the suggested bid and bid limits for a targeting spec, plus the daily-budget bounds LinkedIn will accept. Use it before creating a campaign to pick a bid inside the allowed range and warn the user if their daily budget is below the minimum. Wraps LinkedIn&#39;s &#x60;adBudgetPricing&#x60; finder.  Non-LinkedIn accounts return &#x60;available: false&#x60; so clients can hide the pricing UI without treating it as a failure. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        GetLinkedInBidPricingRequest getLinkedInBidPricingRequest = new GetLinkedInBidPricingRequest(); // GetLinkedInBidPricingRequest | 
        try {
            GetLinkedInBidPricing200Response result = apiInstance.getLinkedInBidPricing(getLinkedInBidPricingRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getLinkedInBidPricing");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **getLinkedInBidPricingRequest** | [**GetLinkedInBidPricingRequest**](GetLinkedInBidPricingRequest.md)|  | |

### Return type

[**GetLinkedInBidPricing200Response**](GetLinkedInBidPricing200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pricing insights |  -  |
| **400** | Invalid targeting or unsupported objective/optimization/bid combination. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. |  -  |
| **404** | Resource not found |  -  |

## getLinkedInBidPricingWithHttpInfo

> ApiResponse<GetLinkedInBidPricing200Response> getLinkedInBidPricing getLinkedInBidPricingWithHttpInfo(getLinkedInBidPricingRequest)

Suggested bid and budget bounds (LinkedIn)

LinkedIn-only. Returns the suggested bid and bid limits for a targeting spec, plus the daily-budget bounds LinkedIn will accept. Use it before creating a campaign to pick a bid inside the allowed range and warn the user if their daily budget is below the minimum. Wraps LinkedIn&#39;s &#x60;adBudgetPricing&#x60; finder.  Non-LinkedIn accounts return &#x60;available: false&#x60; so clients can hide the pricing UI without treating it as a failure. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        GetLinkedInBidPricingRequest getLinkedInBidPricingRequest = new GetLinkedInBidPricingRequest(); // GetLinkedInBidPricingRequest | 
        try {
            ApiResponse<GetLinkedInBidPricing200Response> response = apiInstance.getLinkedInBidPricingWithHttpInfo(getLinkedInBidPricingRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getLinkedInBidPricing");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **getLinkedInBidPricingRequest** | [**GetLinkedInBidPricingRequest**](GetLinkedInBidPricingRequest.md)|  | |

### Return type

ApiResponse<[**GetLinkedInBidPricing200Response**](GetLinkedInBidPricing200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pricing insights |  -  |
| **400** | Invalid targeting or unsupported objective/optimization/bid combination. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. |  -  |
| **404** | Resource not found |  -  |


## getLinkedInSupplyForecast

> GetLinkedInSupplyForecast200Response getLinkedInSupplyForecast(getLinkedInSupplyForecastRequest)

Impressions, clicks and spend forecast (LinkedIn)

LinkedIn-only. Forecasted impressions, clicks, spend and ~20 other metrics for a targeting spec over a time range. Wraps LinkedIn&#39;s &#x60;adSupplyForecasts&#x60; finder.  Each returned series carries a &#x60;metricType&#x60; (IMPRESSION, CLICK, SPENDING, MAX_POTENTIAL_BUDGET, COST_PER_MILLION_IMPRESSIONS, ...) and a &#x60;granularity&#x60; (DAILY, SEVEN_DAY, THIRTY_DAY, CUSTOM). LinkedIn caps the daily spending forecast at 1.2x the daily budget and returns 0 once the total budget is exhausted.  Non-LinkedIn accounts return &#x60;available: false&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        GetLinkedInSupplyForecastRequest getLinkedInSupplyForecastRequest = new GetLinkedInSupplyForecastRequest(); // GetLinkedInSupplyForecastRequest | 
        try {
            GetLinkedInSupplyForecast200Response result = apiInstance.getLinkedInSupplyForecast(getLinkedInSupplyForecastRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getLinkedInSupplyForecast");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **getLinkedInSupplyForecastRequest** | [**GetLinkedInSupplyForecastRequest**](GetLinkedInSupplyForecastRequest.md)|  | |

### Return type

[**GetLinkedInSupplyForecast200Response**](GetLinkedInSupplyForecast200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Forecast series |  -  |
| **400** | Invalid targeting, missing budget, or LinkedIn forecast validation error (e.g. END_DATE_MAX_HORIZON_FOR_FORECAST). |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. |  -  |
| **404** | Resource not found |  -  |

## getLinkedInSupplyForecastWithHttpInfo

> ApiResponse<GetLinkedInSupplyForecast200Response> getLinkedInSupplyForecast getLinkedInSupplyForecastWithHttpInfo(getLinkedInSupplyForecastRequest)

Impressions, clicks and spend forecast (LinkedIn)

LinkedIn-only. Forecasted impressions, clicks, spend and ~20 other metrics for a targeting spec over a time range. Wraps LinkedIn&#39;s &#x60;adSupplyForecasts&#x60; finder.  Each returned series carries a &#x60;metricType&#x60; (IMPRESSION, CLICK, SPENDING, MAX_POTENTIAL_BUDGET, COST_PER_MILLION_IMPRESSIONS, ...) and a &#x60;granularity&#x60; (DAILY, SEVEN_DAY, THIRTY_DAY, CUSTOM). LinkedIn caps the daily spending forecast at 1.2x the daily budget and returns 0 once the total budget is exhausted.  Non-LinkedIn accounts return &#x60;available: false&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        GetLinkedInSupplyForecastRequest getLinkedInSupplyForecastRequest = new GetLinkedInSupplyForecastRequest(); // GetLinkedInSupplyForecastRequest | 
        try {
            ApiResponse<GetLinkedInSupplyForecast200Response> response = apiInstance.getLinkedInSupplyForecastWithHttpInfo(getLinkedInSupplyForecastRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getLinkedInSupplyForecast");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **getLinkedInSupplyForecastRequest** | [**GetLinkedInSupplyForecastRequest**](GetLinkedInSupplyForecastRequest.md)|  | |

### Return type

ApiResponse<[**GetLinkedInSupplyForecast200Response**](GetLinkedInSupplyForecast200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Forecast series |  -  |
| **400** | Invalid targeting, missing budget, or LinkedIn forecast validation error (e.g. END_DATE_MAX_HORIZON_FOR_FORECAST). |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. |  -  |
| **404** | Resource not found |  -  |


## getRfPrediction

> CreateRfPrediction201Response getRfPrediction(predictionId, accountId, adAccountId)

Read a Reach &amp; Frequency prediction (Meta)

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String predictionId = "predictionId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | 
        try {
            CreateRfPrediction201Response result = apiInstance.getRfPrediction(predictionId, accountId, adAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getRfPrediction");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **predictionId** | **String**|  | |
| **accountId** | **String**|  | |
| **adAccountId** | **String**|  | |

### Return type

[**CreateRfPrediction201Response**](CreateRfPrediction201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Prediction status and estimates |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## getRfPredictionWithHttpInfo

> ApiResponse<CreateRfPrediction201Response> getRfPrediction getRfPredictionWithHttpInfo(predictionId, accountId, adAccountId)

Read a Reach &amp; Frequency prediction (Meta)

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String predictionId = "predictionId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | 
        try {
            ApiResponse<CreateRfPrediction201Response> response = apiInstance.getRfPredictionWithHttpInfo(predictionId, accountId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#getRfPrediction");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **predictionId** | **String**|  | |
| **accountId** | **String**|  | |
| **adAccountId** | **String**|  | |

### Return type

ApiResponse<[**CreateRfPrediction201Response**](CreateRfPrediction201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Prediction status and estimates |  -  |
| **400** | Invalid input |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## listAdAccounts

> ListAdAccounts200Response listAdAccounts(accountId, adAccountId, limit)

List ad accounts

Returns the platform ad accounts available for the given social account (e.g. Meta ad accounts, TikTok advertiser IDs, Google Ads customer IDs).  For TikTok agencies: enumerates every advertiser under every Business Center the token can read (paginated server-side), then chunks the lookup against TikTok&#39;s &#x60;/advertiser/info/&#x60; endpoint (which has a per-call cap of ≤100 IDs). Solo advertisers without a BC fall back to the OAuth-time &#x60;advertiser_ids&#x60; list. Cached for 1h on the SocialAccount; lazy-refreshed on first call after expiry. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | Social account ID
        String adAccountId = "adAccountId_example"; // String | Filter response to a single platform ad account ID (e.g. `act_123` for Meta, advertiser_id for TikTok). Returns at most one item.
        Integer limit = 56; // Integer | Clamp the returned `accounts[]` length. Useful for typeahead pickers on agency tokens with hundreds of advertisers.
        try {
            ListAdAccounts200Response result = apiInstance.listAdAccounts(accountId, adAccountId, limit);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listAdAccounts");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Social account ID | |
| **adAccountId** | **String**| Filter response to a single platform ad account ID (e.g. &#x60;act_123&#x60; for Meta, advertiser_id for TikTok). Returns at most one item. | [optional] |
| **limit** | **Integer**| Clamp the returned &#x60;accounts[]&#x60; length. Useful for typeahead pickers on agency tokens with hundreds of advertisers. | [optional] |

### Return type

[**ListAdAccounts200Response**](ListAdAccounts200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad accounts |  -  |
| **401** | Unauthorized |  -  |
| **422** | Platform ads connection required (TikTok Ads, X Ads) or Instagram missing linked Facebook account |  -  |

## listAdAccountsWithHttpInfo

> ApiResponse<ListAdAccounts200Response> listAdAccounts listAdAccountsWithHttpInfo(accountId, adAccountId, limit)

List ad accounts

Returns the platform ad accounts available for the given social account (e.g. Meta ad accounts, TikTok advertiser IDs, Google Ads customer IDs).  For TikTok agencies: enumerates every advertiser under every Business Center the token can read (paginated server-side), then chunks the lookup against TikTok&#39;s &#x60;/advertiser/info/&#x60; endpoint (which has a per-call cap of ≤100 IDs). Solo advertisers without a BC fall back to the OAuth-time &#x60;advertiser_ids&#x60; list. Cached for 1h on the SocialAccount; lazy-refreshed on first call after expiry. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | Social account ID
        String adAccountId = "adAccountId_example"; // String | Filter response to a single platform ad account ID (e.g. `act_123` for Meta, advertiser_id for TikTok). Returns at most one item.
        Integer limit = 56; // Integer | Clamp the returned `accounts[]` length. Useful for typeahead pickers on agency tokens with hundreds of advertisers.
        try {
            ApiResponse<ListAdAccounts200Response> response = apiInstance.listAdAccountsWithHttpInfo(accountId, adAccountId, limit);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listAdAccounts");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Social account ID | |
| **adAccountId** | **String**| Filter response to a single platform ad account ID (e.g. &#x60;act_123&#x60; for Meta, advertiser_id for TikTok). Returns at most one item. | [optional] |
| **limit** | **Integer**| Clamp the returned &#x60;accounts[]&#x60; length. Useful for typeahead pickers on agency tokens with hundreds of advertisers. | [optional] |

### Return type

ApiResponse<[**ListAdAccounts200Response**](ListAdAccounts200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad accounts |  -  |
| **401** | Unauthorized |  -  |
| **422** | Platform ads connection required (TikTok Ads, X Ads) or Instagram missing linked Facebook account |  -  |


## listAdCatalogProductSets

> ListAdCatalogProductSets200Response listAdCatalogProductSets(catalogId, accountId)

List a catalog&#39;s product sets

Lists a Meta product catalog&#39;s product sets — the unit a catalog ad promotes. Pass the chosen set as &#x60;promotedObject.productSetId&#x60; on POST /v1/ads/create with &#x60;goal: catalog_sales&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String accountId = "accountId_example"; // String | A facebook, instagram, or metaads social account ID
        try {
            ListAdCatalogProductSets200Response result = apiInstance.listAdCatalogProductSets(catalogId, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listAdCatalogProductSets");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **accountId** | **String**| A facebook, instagram, or metaads social account ID | |

### Return type

[**ListAdCatalogProductSets200Response**](ListAdCatalogProductSets200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product sets |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |

## listAdCatalogProductSetsWithHttpInfo

> ApiResponse<ListAdCatalogProductSets200Response> listAdCatalogProductSets listAdCatalogProductSetsWithHttpInfo(catalogId, accountId)

List a catalog&#39;s product sets

Lists a Meta product catalog&#39;s product sets — the unit a catalog ad promotes. Pass the chosen set as &#x60;promotedObject.productSetId&#x60; on POST /v1/ads/create with &#x60;goal: catalog_sales&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String catalogId = "catalogId_example"; // String | Meta product catalog ID (from GET /v1/ads/catalogs)
        String accountId = "accountId_example"; // String | A facebook, instagram, or metaads social account ID
        try {
            ApiResponse<ListAdCatalogProductSets200Response> response = apiInstance.listAdCatalogProductSetsWithHttpInfo(catalogId, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listAdCatalogProductSets");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **catalogId** | **String**| Meta product catalog ID (from GET /v1/ads/catalogs) | |
| **accountId** | **String**| A facebook, instagram, or metaads social account ID | |

### Return type

ApiResponse<[**ListAdCatalogProductSets200Response**](ListAdCatalogProductSets200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Product sets |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |


## listAdCatalogs

> ListAdCatalogs200Response listAdCatalogs(accountId, adAccountId)

List Meta product catalogs

Lists the Meta product catalogs reachable from an ad account (owned + agency-shared catalogs of the ad account&#39;s business), for Advantage+ catalog ads (&#x60;goal: catalog_sales&#x60; on POST /v1/ads/create — e.g. vehicle inventory catalogs). Read-only; uses scopes customers already granted (no reconnect needed). Catalog contents (items, feeds) are managed in Meta Commerce Manager, not through this API.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | A facebook, instagram, or metaads social account ID
        String adAccountId = "adAccountId_example"; // String | Meta ad account ID (act_...)
        try {
            ListAdCatalogs200Response result = apiInstance.listAdCatalogs(accountId, adAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listAdCatalogs");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| A facebook, instagram, or metaads social account ID | |
| **adAccountId** | **String**| Meta ad account ID (act_...) | |

### Return type

[**ListAdCatalogs200Response**](ListAdCatalogs200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Catalogs |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |

## listAdCatalogsWithHttpInfo

> ApiResponse<ListAdCatalogs200Response> listAdCatalogs listAdCatalogsWithHttpInfo(accountId, adAccountId)

List Meta product catalogs

Lists the Meta product catalogs reachable from an ad account (owned + agency-shared catalogs of the ad account&#39;s business), for Advantage+ catalog ads (&#x60;goal: catalog_sales&#x60; on POST /v1/ads/create — e.g. vehicle inventory catalogs). Read-only; uses scopes customers already granted (no reconnect needed). Catalog contents (items, feeds) are managed in Meta Commerce Manager, not through this API.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | A facebook, instagram, or metaads social account ID
        String adAccountId = "adAccountId_example"; // String | Meta ad account ID (act_...)
        try {
            ApiResponse<ListAdCatalogs200Response> response = apiInstance.listAdCatalogsWithHttpInfo(accountId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listAdCatalogs");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| A facebook, instagram, or metaads social account ID | |
| **adAccountId** | **String**| Meta ad account ID (act_...) | |

### Return type

ApiResponse<[**ListAdCatalogs200Response**](ListAdCatalogs200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Catalogs |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |


## listAdCreatives

> ListAdCreatives200Response listAdCreatives(accountId, adAccountId, fields, limit, after)

Creative library (Meta)

Lists the ad account&#39;s creative library (Meta&#39;s &#x60;/act_X/adcreatives&#x60;), rows returned verbatim. The default projection covers id, name, status, object type, thumbnail, object_story_spec / asset_feed_spec and url_tags; &#x60;fields&#x60; is a raw-passthrough override. Any creative id here is reusable on the create endpoints via &#x60;existingCreativeId&#x60;. Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>).
        String fields = "fields_example"; // String | Comma-separated Graph field override (supports nested {} projections).
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ListAdCreatives200Response result = apiInstance.listAdCreatives(accountId, adAccountId, fields, limit, after);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listAdCreatives");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **adAccountId** | **String**| Meta ad account id (act_&lt;n&gt;). | |
| **fields** | **String**| Comma-separated Graph field override (supports nested {} projections). | [optional] |
| **limit** | **Integer**| Rows per page | [optional] [default to 25] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

[**ListAdCreatives200Response**](ListAdCreatives200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Creatives (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## listAdCreativesWithHttpInfo

> ApiResponse<ListAdCreatives200Response> listAdCreatives listAdCreativesWithHttpInfo(accountId, adAccountId, fields, limit, after)

Creative library (Meta)

Lists the ad account&#39;s creative library (Meta&#39;s &#x60;/act_X/adcreatives&#x60;), rows returned verbatim. The default projection covers id, name, status, object type, thumbnail, object_story_spec / asset_feed_spec and url_tags; &#x60;fields&#x60; is a raw-passthrough override. Any creative id here is reusable on the create endpoints via &#x60;existingCreativeId&#x60;. Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>).
        String fields = "fields_example"; // String | Comma-separated Graph field override (supports nested {} projections).
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ApiResponse<ListAdCreatives200Response> response = apiInstance.listAdCreativesWithHttpInfo(accountId, adAccountId, fields, limit, after);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listAdCreatives");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **adAccountId** | **String**| Meta ad account id (act_&lt;n&gt;). | |
| **fields** | **String**| Comma-separated Graph field override (supports nested {} projections). | [optional] |
| **limit** | **Integer**| Rows per page | [optional] [default to 25] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

ApiResponse<[**ListAdCreatives200Response**](ListAdCreatives200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Creatives (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## listAdImages

> ListAdImages200Response listAdImages(accountId, adAccountId, fields, limit, after)

Ad image library (Meta)

Lists the ad account&#39;s image library (Meta&#39;s &#x60;/act_X/adimages&#x60;), rows returned verbatim. The default projection covers hash, url, name, dimensions and status; &#x60;fields&#x60; is a raw-passthrough override. Any &#x60;hash&#x60; here is reusable wherever Meta accepts &#x60;image_hash&#x60; (e.g. &#x60;imageHash&#x60; on POST /v1/ads/creatives). Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>).
        String fields = "fields_example"; // String | Comma-separated Graph field override (supports nested {} projections).
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ListAdImages200Response result = apiInstance.listAdImages(accountId, adAccountId, fields, limit, after);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listAdImages");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **adAccountId** | **String**| Meta ad account id (act_&lt;n&gt;). | |
| **fields** | **String**| Comma-separated Graph field override (supports nested {} projections). | [optional] |
| **limit** | **Integer**| Rows per page | [optional] [default to 25] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

[**ListAdImages200Response**](ListAdImages200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad images (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## listAdImagesWithHttpInfo

> ApiResponse<ListAdImages200Response> listAdImages listAdImagesWithHttpInfo(accountId, adAccountId, fields, limit, after)

Ad image library (Meta)

Lists the ad account&#39;s image library (Meta&#39;s &#x60;/act_X/adimages&#x60;), rows returned verbatim. The default projection covers hash, url, name, dimensions and status; &#x60;fields&#x60; is a raw-passthrough override. Any &#x60;hash&#x60; here is reusable wherever Meta accepts &#x60;image_hash&#x60; (e.g. &#x60;imageHash&#x60; on POST /v1/ads/creatives). Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>).
        String fields = "fields_example"; // String | Comma-separated Graph field override (supports nested {} projections).
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ApiResponse<ListAdImages200Response> response = apiInstance.listAdImagesWithHttpInfo(accountId, adAccountId, fields, limit, after);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listAdImages");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **adAccountId** | **String**| Meta ad account id (act_&lt;n&gt;). | |
| **fields** | **String**| Comma-separated Graph field override (supports nested {} projections). | [optional] |
| **limit** | **Integer**| Rows per page | [optional] [default to 25] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

ApiResponse<[**ListAdImages200Response**](ListAdImages200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad images (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## listAdLabels

> ListAdLabels200Response listAdLabels(accountId, adAccountId, limit, after)

Ad labels (Meta)

Lists the ad account&#39;s organizational labels (Meta&#39;s &#x60;/act_X/adlabels&#x60;), rows returned verbatim (id, name, created/updated time). Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>).
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ListAdLabels200Response result = apiInstance.listAdLabels(accountId, adAccountId, limit, after);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listAdLabels");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **adAccountId** | **String**| Meta ad account id (act_&lt;n&gt;). | |
| **limit** | **Integer**| Rows per page | [optional] [default to 25] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

[**ListAdLabels200Response**](ListAdLabels200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad labels (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## listAdLabelsWithHttpInfo

> ApiResponse<ListAdLabels200Response> listAdLabels listAdLabelsWithHttpInfo(accountId, adAccountId, limit, after)

Ad labels (Meta)

Lists the ad account&#39;s organizational labels (Meta&#39;s &#x60;/act_X/adlabels&#x60;), rows returned verbatim (id, name, created/updated time). Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>).
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ApiResponse<ListAdLabels200Response> response = apiInstance.listAdLabelsWithHttpInfo(accountId, adAccountId, limit, after);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listAdLabels");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **adAccountId** | **String**| Meta ad account id (act_&lt;n&gt;). | |
| **limit** | **Integer**| Rows per page | [optional] [default to 25] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

ApiResponse<[**ListAdLabels200Response**](ListAdLabels200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad labels (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## listAdStudies

> ListAdStudies200Response listAdStudies(accountId, adAccountId, fields, limit, after)

A/B tests and lift studies (Meta)

Lists the ad account&#39;s A/B tests and lift studies (Meta&#39;s &#x60;/act_X/ad_studies&#x60;), rows returned verbatim. The default projection covers id, name, type, timing and cells with split percentages; &#x60;fields&#x60; is a raw-passthrough override. Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>).
        String fields = "fields_example"; // String | Comma-separated Graph field override (supports nested {} projections).
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ListAdStudies200Response result = apiInstance.listAdStudies(accountId, adAccountId, fields, limit, after);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listAdStudies");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **adAccountId** | **String**| Meta ad account id (act_&lt;n&gt;). | |
| **fields** | **String**| Comma-separated Graph field override (supports nested {} projections). | [optional] |
| **limit** | **Integer**| Rows per page | [optional] [default to 25] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

[**ListAdStudies200Response**](ListAdStudies200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad studies (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## listAdStudiesWithHttpInfo

> ApiResponse<ListAdStudies200Response> listAdStudies listAdStudiesWithHttpInfo(accountId, adAccountId, fields, limit, after)

A/B tests and lift studies (Meta)

Lists the ad account&#39;s A/B tests and lift studies (Meta&#39;s &#x60;/act_X/ad_studies&#x60;), rows returned verbatim. The default projection covers id, name, type, timing and cells with split percentages; &#x60;fields&#x60; is a raw-passthrough override. Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String adAccountId = "adAccountId_example"; // String | Meta ad account id (act_<n>).
        String fields = "fields_example"; // String | Comma-separated Graph field override (supports nested {} projections).
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ApiResponse<ListAdStudies200Response> response = apiInstance.listAdStudiesWithHttpInfo(accountId, adAccountId, fields, limit, after);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listAdStudies");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **adAccountId** | **String**| Meta ad account id (act_&lt;n&gt;). | |
| **fields** | **String**| Comma-separated Graph field override (supports nested {} projections). | [optional] |
| **limit** | **Integer**| Rows per page | [optional] [default to 25] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

ApiResponse<[**ListAdStudies200Response**](ListAdStudies200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ad studies (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## listAds

> ListAds200Response listAds(page, limit, source, status, platform, accountId, adAccountId, profileId, campaignId, platformAdId, effectiveObjectStoryId, effectiveInstagramMediaId, fromDate, toDate)

List ads

Returns a paginated list of ads with metrics computed over an optional date range. Use source&#x3D;all to include externally-synced ads from platform ad managers. If no date range is provided, defaults to the last 90 days. Date range is capped at 730 days max.  To find the Zernio ad behind a comment you see in Meta Business Manager, filter by platformAdId (the Meta ad ID), effectiveObjectStoryId (Facebook), or effectiveInstagramMediaId (Instagram) — those are the post/media the ad&#39;s engagement lives on, and are also returned on each ad&#39;s &#x60;creative&#x60; object. Then call GET /v1/ads/{adId}/comments with the returned ad id. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        Integer page = 1; // Integer | Page number (1-based)
        Integer limit = 50; // Integer | 
        String source = "zernio"; // String | all (default) = Zernio-created + platform-discovered ads. zernio = restrict to Zernio-created only.
        AdStatus status = AdStatus.fromValue("active"); // AdStatus | 
        String platform = "facebook"; // String | 
        String accountId = "accountId_example"; // String | Social account ID
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID (e.g. act_123 for Meta). Mirrors the same filter on /v1/ads/campaigns and /v1/ads/tree.
        String profileId = "profileId_example"; // String | Profile ID
        String campaignId = "campaignId_example"; // String | Platform campaign ID (filter ads within a campaign)
        String platformAdId = "platformAdId_example"; // String | Meta ad ID. Returns the ad with this platform-side ad ID.
        String effectiveObjectStoryId = "effectiveObjectStoryId_example"; // String | Facebook `{pageId}_{postId}` of the post the ad's engagement lives on (Meta `effective_object_story_id`). Use to map a Business-Manager-visible post back to the Zernio ad.
        String effectiveInstagramMediaId = "effectiveInstagramMediaId_example"; // String | Instagram media ID of the boosted post (Meta `effective_instagram_media_id`). Use to map a Business-Manager-visible IG post back to the Zernio ad.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of metrics date range (YYYY-MM-DD). Defaults to 90 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of metrics date range (YYYY-MM-DD). Defaults to today. Max 730-day range.
        try {
            ListAds200Response result = apiInstance.listAds(page, limit, source, status, platform, accountId, adAccountId, profileId, campaignId, platformAdId, effectiveObjectStoryId, effectiveInstagramMediaId, fromDate, toDate);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listAds");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
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
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter] |
| **accountId** | **String**| Social account ID | [optional] |
| **adAccountId** | **String**| Platform ad account ID (e.g. act_123 for Meta). Mirrors the same filter on /v1/ads/campaigns and /v1/ads/tree. | [optional] |
| **profileId** | **String**| Profile ID | [optional] |
| **campaignId** | **String**| Platform campaign ID (filter ads within a campaign) | [optional] |
| **platformAdId** | **String**| Meta ad ID. Returns the ad with this platform-side ad ID. | [optional] |
| **effectiveObjectStoryId** | **String**| Facebook &#x60;{pageId}_{postId}&#x60; of the post the ad&#39;s engagement lives on (Meta &#x60;effective_object_story_id&#x60;). Use to map a Business-Manager-visible post back to the Zernio ad. | [optional] |
| **effectiveInstagramMediaId** | **String**| Instagram media ID of the boosted post (Meta &#x60;effective_instagram_media_id&#x60;). Use to map a Business-Manager-visible IG post back to the Zernio ad. | [optional] |
| **fromDate** | **LocalDate**| Start of metrics date range (YYYY-MM-DD). Defaults to 90 days ago. | [optional] |
| **toDate** | **LocalDate**| End of metrics date range (YYYY-MM-DD). Defaults to today. Max 730-day range. | [optional] |

### Return type

[**ListAds200Response**](ListAds200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated ads |  -  |
| **202** | Part of the requested date range predates the ingested history; a background backfill job has been queued. The body has the same shape as the 200 response, carries the currently-available data, and includes &#x60;backfillPending: true&#x60;. A &#x60;Retry-After&#x60; header carries the recommended poll interval in seconds. Allow the job a short time to run (typically 1-3 minutes) and submit the request again; once ingestion completes the same request returns 200 with the full range. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |

## listAdsWithHttpInfo

> ApiResponse<ListAds200Response> listAds listAdsWithHttpInfo(page, limit, source, status, platform, accountId, adAccountId, profileId, campaignId, platformAdId, effectiveObjectStoryId, effectiveInstagramMediaId, fromDate, toDate)

List ads

Returns a paginated list of ads with metrics computed over an optional date range. Use source&#x3D;all to include externally-synced ads from platform ad managers. If no date range is provided, defaults to the last 90 days. Date range is capped at 730 days max.  To find the Zernio ad behind a comment you see in Meta Business Manager, filter by platformAdId (the Meta ad ID), effectiveObjectStoryId (Facebook), or effectiveInstagramMediaId (Instagram) — those are the post/media the ad&#39;s engagement lives on, and are also returned on each ad&#39;s &#x60;creative&#x60; object. Then call GET /v1/ads/{adId}/comments with the returned ad id. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        Integer page = 1; // Integer | Page number (1-based)
        Integer limit = 50; // Integer | 
        String source = "zernio"; // String | all (default) = Zernio-created + platform-discovered ads. zernio = restrict to Zernio-created only.
        AdStatus status = AdStatus.fromValue("active"); // AdStatus | 
        String platform = "facebook"; // String | 
        String accountId = "accountId_example"; // String | Social account ID
        String adAccountId = "adAccountId_example"; // String | Platform ad account ID (e.g. act_123 for Meta). Mirrors the same filter on /v1/ads/campaigns and /v1/ads/tree.
        String profileId = "profileId_example"; // String | Profile ID
        String campaignId = "campaignId_example"; // String | Platform campaign ID (filter ads within a campaign)
        String platformAdId = "platformAdId_example"; // String | Meta ad ID. Returns the ad with this platform-side ad ID.
        String effectiveObjectStoryId = "effectiveObjectStoryId_example"; // String | Facebook `{pageId}_{postId}` of the post the ad's engagement lives on (Meta `effective_object_story_id`). Use to map a Business-Manager-visible post back to the Zernio ad.
        String effectiveInstagramMediaId = "effectiveInstagramMediaId_example"; // String | Instagram media ID of the boosted post (Meta `effective_instagram_media_id`). Use to map a Business-Manager-visible IG post back to the Zernio ad.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of metrics date range (YYYY-MM-DD). Defaults to 90 days ago.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of metrics date range (YYYY-MM-DD). Defaults to today. Max 730-day range.
        try {
            ApiResponse<ListAds200Response> response = apiInstance.listAdsWithHttpInfo(page, limit, source, status, platform, accountId, adAccountId, profileId, campaignId, platformAdId, effectiveObjectStoryId, effectiveInstagramMediaId, fromDate, toDate);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listAds");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
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
| **platform** | **String**|  | [optional] [enum: facebook, instagram, tiktok, linkedin, pinterest, google, twitter] |
| **accountId** | **String**| Social account ID | [optional] |
| **adAccountId** | **String**| Platform ad account ID (e.g. act_123 for Meta). Mirrors the same filter on /v1/ads/campaigns and /v1/ads/tree. | [optional] |
| **profileId** | **String**| Profile ID | [optional] |
| **campaignId** | **String**| Platform campaign ID (filter ads within a campaign) | [optional] |
| **platformAdId** | **String**| Meta ad ID. Returns the ad with this platform-side ad ID. | [optional] |
| **effectiveObjectStoryId** | **String**| Facebook &#x60;{pageId}_{postId}&#x60; of the post the ad&#39;s engagement lives on (Meta &#x60;effective_object_story_id&#x60;). Use to map a Business-Manager-visible post back to the Zernio ad. | [optional] |
| **effectiveInstagramMediaId** | **String**| Instagram media ID of the boosted post (Meta &#x60;effective_instagram_media_id&#x60;). Use to map a Business-Manager-visible IG post back to the Zernio ad. | [optional] |
| **fromDate** | **LocalDate**| Start of metrics date range (YYYY-MM-DD). Defaults to 90 days ago. | [optional] |
| **toDate** | **LocalDate**| End of metrics date range (YYYY-MM-DD). Defaults to today. Max 730-day range. | [optional] |

### Return type

ApiResponse<[**ListAds200Response**](ListAds200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated ads |  -  |
| **202** | Part of the requested date range predates the ingested history; a background backfill job has been queued. The body has the same shape as the 200 response, carries the currently-available data, and includes &#x60;backfillPending: true&#x60;. A &#x60;Retry-After&#x60; header carries the recommended poll interval in seconds. Allow the job a short time to run (typically 1-3 minutes) and submit the request again; once ingestion completes the same request returns 200 with the full range. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |


## listAdsBusinessCenters

> ListAdsBusinessCenters200Response listAdsBusinessCenters(accountId)

List TikTok Business Centers

Returns the TikTok Business Centers (BCs) the connected &#x60;tiktokads&#x60; account can read. Each BC reports its advertiser count so callers can build agency-style pickers without re-walking &#x60;/v1/ads/accounts&#x60; per BC.  TikTok-only. Solo advertisers (non-agency tokens) return an empty array. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | ID of the `tiktokads` (or parent `tiktok` posting) SocialAccount
        try {
            ListAdsBusinessCenters200Response result = apiInstance.listAdsBusinessCenters(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listAdsBusinessCenters");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| ID of the &#x60;tiktokads&#x60; (or parent &#x60;tiktok&#x60; posting) SocialAccount | |

### Return type

[**ListAdsBusinessCenters200Response**](ListAdsBusinessCenters200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Business centers |  -  |
| **401** | Unauthorized |  -  |
| **404** | TikTok account not found |  -  |
| **422** | TikTok Ads not connected |  -  |

## listAdsBusinessCentersWithHttpInfo

> ApiResponse<ListAdsBusinessCenters200Response> listAdsBusinessCenters listAdsBusinessCentersWithHttpInfo(accountId)

List TikTok Business Centers

Returns the TikTok Business Centers (BCs) the connected &#x60;tiktokads&#x60; account can read. Each BC reports its advertiser count so callers can build agency-style pickers without re-walking &#x60;/v1/ads/accounts&#x60; per BC.  TikTok-only. Solo advertisers (non-agency tokens) return an empty array. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | ID of the `tiktokads` (or parent `tiktok` posting) SocialAccount
        try {
            ApiResponse<ListAdsBusinessCenters200Response> response = apiInstance.listAdsBusinessCentersWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listAdsBusinessCenters");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| ID of the &#x60;tiktokads&#x60; (or parent &#x60;tiktok&#x60; posting) SocialAccount | |

### Return type

ApiResponse<[**ListAdsBusinessCenters200Response**](ListAdsBusinessCenters200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Business centers |  -  |
| **401** | Unauthorized |  -  |
| **404** | TikTok account not found |  -  |
| **422** | TikTok Ads not connected |  -  |


## listConversionAssociations

> ListConversionAssociations200Response listConversionAssociations(accountId, destinationId, adAccountId)

List associated campaigns

LinkedIn-only today. Returns the campaigns currently associated with this conversion rule. Note that auto-association on rule creation runs once at create time; campaigns created after the rule still need explicit association. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String destinationId = "destinationId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | 
        try {
            ListConversionAssociations200Response result = apiInstance.listConversionAssociations(accountId, destinationId, adAccountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listConversionAssociations");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**|  | |
| **destinationId** | **String**|  | |
| **adAccountId** | **String**|  | |

### Return type

[**ListConversionAssociations200Response**](ListConversionAssociations200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Associations listed |  -  |
| **400** | Validation error. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on or LinkedIn reconnect required. |  -  |
| **404** | Account or destination not found. |  -  |
| **405** | Platform does not support associations. |  -  |
| **429** | LinkedIn rate limit hit. Retry with backoff. |  -  |

## listConversionAssociationsWithHttpInfo

> ApiResponse<ListConversionAssociations200Response> listConversionAssociations listConversionAssociationsWithHttpInfo(accountId, destinationId, adAccountId)

List associated campaigns

LinkedIn-only today. Returns the campaigns currently associated with this conversion rule. Note that auto-association on rule creation runs once at create time; campaigns created after the rule still need explicit association. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String destinationId = "destinationId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | 
        try {
            ApiResponse<ListConversionAssociations200Response> response = apiInstance.listConversionAssociationsWithHttpInfo(accountId, destinationId, adAccountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listConversionAssociations");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**|  | |
| **destinationId** | **String**|  | |
| **adAccountId** | **String**|  | |

### Return type

ApiResponse<[**ListConversionAssociations200Response**](ListConversionAssociations200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Associations listed |  -  |
| **400** | Validation error. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on or LinkedIn reconnect required. |  -  |
| **404** | Account or destination not found. |  -  |
| **405** | Platform does not support associations. |  -  |
| **429** | LinkedIn rate limit hit. Retry with backoff. |  -  |


## listConversionDestinations

> ListConversionDestinations200Response listConversionDestinations(accountId)

List conversion destinations

Returns the list of pixels (Meta), conversion actions (Google), or conversion rules (LinkedIn) accessible to the connected ads account. Use the returned &#x60;id&#x60; as &#x60;destinationId&#x60; when posting to &#x60;POST /v1/ads/conversions&#x60;.  For Google and LinkedIn, each destination&#39;s &#x60;type&#x60; reflects the conversion type (PURCHASE, LEAD, SIGN_UP, etc.) — the event type is locked to the destination. For Meta, &#x60;type&#x60; is absent: pixels accept any event name per request.  For LinkedIn, destinations are returned across every sponsored ad account the connected token can access; the &#x60;adAccountId&#x60; field on each destination identifies the parent ad account and is required for subsequent CRUD calls (update, delete, associations, metrics). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | SocialAccount ID (metaads, googleads, linkedinads, or tiktokads).
        try {
            ListConversionDestinations200Response result = apiInstance.listConversionDestinations(accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listConversionDestinations");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| SocialAccount ID (metaads, googleads, linkedinads, or tiktokads). | |

### Return type

[**ListConversionDestinations200Response**](ListConversionDestinations200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Destinations listed |  -  |
| **400** | Account&#39;s platform is not supported by the Conversions API. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), OR (for LinkedIn) the connected account lacks the &#x60;rw_conversions&#x60; scope and must be reconnected.  |  -  |
| **404** | Account not found or not accessible. |  -  |
| **429** | LinkedIn rate limit hit. Retry with backoff. |  -  |

## listConversionDestinationsWithHttpInfo

> ApiResponse<ListConversionDestinations200Response> listConversionDestinations listConversionDestinationsWithHttpInfo(accountId)

List conversion destinations

Returns the list of pixels (Meta), conversion actions (Google), or conversion rules (LinkedIn) accessible to the connected ads account. Use the returned &#x60;id&#x60; as &#x60;destinationId&#x60; when posting to &#x60;POST /v1/ads/conversions&#x60;.  For Google and LinkedIn, each destination&#39;s &#x60;type&#x60; reflects the conversion type (PURCHASE, LEAD, SIGN_UP, etc.) — the event type is locked to the destination. For Meta, &#x60;type&#x60; is absent: pixels accept any event name per request.  For LinkedIn, destinations are returned across every sponsored ad account the connected token can access; the &#x60;adAccountId&#x60; field on each destination identifies the parent ad account and is required for subsequent CRUD calls (update, delete, associations, metrics). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | SocialAccount ID (metaads, googleads, linkedinads, or tiktokads).
        try {
            ApiResponse<ListConversionDestinations200Response> response = apiInstance.listConversionDestinationsWithHttpInfo(accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listConversionDestinations");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| SocialAccount ID (metaads, googleads, linkedinads, or tiktokads). | |

### Return type

ApiResponse<[**ListConversionDestinations200Response**](ListConversionDestinations200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Destinations listed |  -  |
| **400** | Account&#39;s platform is not supported by the Conversions API. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), OR (for LinkedIn) the connected account lacks the &#x60;rw_conversions&#x60; scope and must be reconnected.  |  -  |
| **404** | Account not found or not accessible. |  -  |
| **429** | LinkedIn rate limit hit. Retry with backoff. |  -  |


## listFormLeads

> ListFormLeads200Response listFormLeads(formId, accountId, limit, cursor, since)

List leads for a single form

Returns leads for one form. Serves persisted leads (ingested via the leadgen webhook) when available, falling back to a live Graph read. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String formId = "formId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        Integer limit = 25; // Integer | 
        String cursor = "cursor_example"; // String | 
        Integer since = 56; // Integer | Unix seconds.
        try {
            ListFormLeads200Response result = apiInstance.listFormLeads(formId, accountId, limit, cursor, since);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listFormLeads");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **formId** | **String**|  | |
| **accountId** | **String**|  | |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **cursor** | **String**|  | [optional] |
| **since** | **Integer**| Unix seconds. | [optional] |

### Return type

[**ListFormLeads200Response**](ListFormLeads200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Leads for the form. |  -  |
| **401** | Unauthorized |  -  |

## listFormLeadsWithHttpInfo

> ApiResponse<ListFormLeads200Response> listFormLeads listFormLeadsWithHttpInfo(formId, accountId, limit, cursor, since)

List leads for a single form

Returns leads for one form. Serves persisted leads (ingested via the leadgen webhook) when available, falling back to a live Graph read. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String formId = "formId_example"; // String | 
        String accountId = "accountId_example"; // String | 
        Integer limit = 25; // Integer | 
        String cursor = "cursor_example"; // String | 
        Integer since = 56; // Integer | Unix seconds.
        try {
            ApiResponse<ListFormLeads200Response> response = apiInstance.listFormLeadsWithHttpInfo(formId, accountId, limit, cursor, since);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listFormLeads");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **formId** | **String**|  | |
| **accountId** | **String**|  | |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **cursor** | **String**|  | [optional] |
| **since** | **Integer**| Unix seconds. | [optional] |

### Return type

ApiResponse<[**ListFormLeads200Response**](ListFormLeads200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Leads for the form. |  -  |
| **401** | Unauthorized |  -  |


## listHighDemandPeriods

> ListHighDemandPeriods200Response listHighDemandPeriods(accountId, campaignId, adSetId, limit, after)

High demand periods / budget schedules (Meta)

Scheduled budget increases (Meta&#39;s budget-scheduling API). The Graph edge lives on the campaign and ad-set nodes only, so exactly one of &#x60;campaignId&#x60; / &#x60;adSetId&#x60; (platform ids) is required. Rows returned verbatim (budget_value, budget_value_type, time window, recurrence). Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String campaignId = "campaignId_example"; // String | Platform campaign id. Exactly one of campaignId / adSetId.
        String adSetId = "adSetId_example"; // String | Platform ad set id. Exactly one of campaignId / adSetId.
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ListHighDemandPeriods200Response result = apiInstance.listHighDemandPeriods(accountId, campaignId, adSetId, limit, after);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listHighDemandPeriods");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **campaignId** | **String**| Platform campaign id. Exactly one of campaignId / adSetId. | [optional] |
| **adSetId** | **String**| Platform ad set id. Exactly one of campaignId / adSetId. | [optional] |
| **limit** | **Integer**| Rows per page | [optional] [default to 25] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

[**ListHighDemandPeriods200Response**](ListHighDemandPeriods200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Budget schedules (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## listHighDemandPeriodsWithHttpInfo

> ApiResponse<ListHighDemandPeriods200Response> listHighDemandPeriods listHighDemandPeriodsWithHttpInfo(accountId, campaignId, adSetId, limit, after)

High demand periods / budget schedules (Meta)

Scheduled budget increases (Meta&#39;s budget-scheduling API). The Graph edge lives on the campaign and ad-set nodes only, so exactly one of &#x60;campaignId&#x60; / &#x60;adSetId&#x60; (platform ids) is required. Rows returned verbatim (budget_value, budget_value_type, time window, recurrence). Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String campaignId = "campaignId_example"; // String | Platform campaign id. Exactly one of campaignId / adSetId.
        String adSetId = "adSetId_example"; // String | Platform ad set id. Exactly one of campaignId / adSetId.
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ApiResponse<ListHighDemandPeriods200Response> response = apiInstance.listHighDemandPeriodsWithHttpInfo(accountId, campaignId, adSetId, limit, after);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listHighDemandPeriods");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **campaignId** | **String**| Platform campaign id. Exactly one of campaignId / adSetId. | [optional] |
| **adSetId** | **String**| Platform ad set id. Exactly one of campaignId / adSetId. | [optional] |
| **limit** | **Integer**| Rows per page | [optional] [default to 25] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

ApiResponse<[**ListHighDemandPeriods200Response**](ListHighDemandPeriods200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Budget schedules (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## listLeadForms

> ListLeadForms200Response listLeadForms(accountId, limit, cursor)

List lead forms

Lists the Lead Gen forms owned by the connected Facebook Page. Requires the Ads add-on.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected facebook account id.
        Integer limit = 25; // Integer | 
        String cursor = "cursor_example"; // String | 
        try {
            ListLeadForms200Response result = apiInstance.listLeadForms(accountId, limit, cursor);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listLeadForms");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected facebook account id. | |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **cursor** | **String**|  | [optional] |

### Return type

[**ListLeadForms200Response**](ListLeadForms200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Forms list. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required. |  -  |

## listLeadFormsWithHttpInfo

> ApiResponse<ListLeadForms200Response> listLeadForms listLeadFormsWithHttpInfo(accountId, limit, cursor)

List lead forms

Lists the Lead Gen forms owned by the connected Facebook Page. Requires the Ads add-on.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | Connected facebook account id.
        Integer limit = 25; // Integer | 
        String cursor = "cursor_example"; // String | 
        try {
            ApiResponse<ListLeadForms200Response> response = apiInstance.listLeadFormsWithHttpInfo(accountId, limit, cursor);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listLeadForms");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Connected facebook account id. | |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **cursor** | **String**|  | [optional] |

### Return type

ApiResponse<[**ListLeadForms200Response**](ListLeadForms200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Forms list. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required. |  -  |


## listLeads

> ListLeads200Response listLeads(formId, accountId, limit, since, cursor)

List submitted leads

Returns persisted Meta Lead Gen leads for your team, newest-first, with keyset pagination on &#x60;cursor&#x60;. Leads are ingested in real time from the &#x60;leadgen&#x60; webhook. Requires the Ads add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String formId = "formId_example"; // String | Filter to a single lead form.
        String accountId = "accountId_example"; // String | Filter to a single connected account.
        Integer limit = 25; // Integer | 
        Integer since = 56; // Integer | Unix seconds; only leads created at/after this Meta timestamp.
        String cursor = "cursor_example"; // String | Keyset cursor from a previous response's pagination.cursor.
        try {
            ListLeads200Response result = apiInstance.listLeads(formId, accountId, limit, since, cursor);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listLeads");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **formId** | **String**| Filter to a single lead form. | [optional] |
| **accountId** | **String**| Filter to a single connected account. | [optional] |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **since** | **Integer**| Unix seconds; only leads created at/after this Meta timestamp. | [optional] |
| **cursor** | **String**| Keyset cursor from a previous response&#39;s pagination.cursor. | [optional] |

### Return type

[**ListLeads200Response**](ListLeads200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Lead list. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required. |  -  |

## listLeadsWithHttpInfo

> ApiResponse<ListLeads200Response> listLeads listLeadsWithHttpInfo(formId, accountId, limit, since, cursor)

List submitted leads

Returns persisted Meta Lead Gen leads for your team, newest-first, with keyset pagination on &#x60;cursor&#x60;. Leads are ingested in real time from the &#x60;leadgen&#x60; webhook. Requires the Ads add-on. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String formId = "formId_example"; // String | Filter to a single lead form.
        String accountId = "accountId_example"; // String | Filter to a single connected account.
        Integer limit = 25; // Integer | 
        Integer since = 56; // Integer | Unix seconds; only leads created at/after this Meta timestamp.
        String cursor = "cursor_example"; // String | Keyset cursor from a previous response's pagination.cursor.
        try {
            ApiResponse<ListLeads200Response> response = apiInstance.listLeadsWithHttpInfo(formId, accountId, limit, since, cursor);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listLeads");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **formId** | **String**| Filter to a single lead form. | [optional] |
| **accountId** | **String**| Filter to a single connected account. | [optional] |
| **limit** | **Integer**|  | [optional] [default to 25] |
| **since** | **Integer**| Unix seconds; only leads created at/after this Meta timestamp. | [optional] |
| **cursor** | **String**| Keyset cursor from a previous response&#39;s pagination.cursor. | [optional] |

### Return type

ApiResponse<[**ListLeads200Response**](ListLeads200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Lead list. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on required. |  -  |


## listMetaBusinesses

> ListMetaBusinesses200Response listMetaBusinesses(accountId, limit, after)

Businesses list (Meta)

Business Manager portfolios the connected Meta user belongs to (Meta&#39;s &#x60;/me/businesses&#x60;), rows returned verbatim (id, name, verification_status, created_time). Token-scoped, so no &#x60;adAccountId&#x60; is needed. Meta only; for TikTok Business Centers use &#x60;GET /v1/ads/business-centers&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ListMetaBusinesses200Response result = apiInstance.listMetaBusinesses(accountId, limit, after);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listMetaBusinesses");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **limit** | **Integer**| Rows per page | [optional] [default to 25] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

[**ListMetaBusinesses200Response**](ListMetaBusinesses200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Businesses (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## listMetaBusinessesWithHttpInfo

> ApiResponse<ListMetaBusinesses200Response> listMetaBusinesses listMetaBusinessesWithHttpInfo(accountId, limit, after)

Businesses list (Meta)

Business Manager portfolios the connected Meta user belongs to (Meta&#39;s &#x60;/me/businesses&#x60;), rows returned verbatim (id, name, verification_status, created_time). Token-scoped, so no &#x60;adAccountId&#x60; is needed. Meta only; for TikTok Business Centers use &#x60;GET /v1/ads/business-centers&#x60;.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ApiResponse<ListMetaBusinesses200Response> response = apiInstance.listMetaBusinessesWithHttpInfo(accountId, limit, after);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listMetaBusinesses");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **limit** | **Integer**| Rows per page | [optional] [default to 25] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

ApiResponse<[**ListMetaBusinesses200Response**](ListMetaBusinesses200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Businesses (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## listWhatsAppConversions

> ListWhatsAppConversions200Response listWhatsAppConversions(accountId, limit)

List conversion events

Returns the most recent conversion events sent through &#x60;POST /v1/whatsapp/conversions&#x60; for the given WhatsApp account. Sourced from delivery logs (Axiom &#x60;late&#x60; dataset), so the visible window is bounded by log retention (about 30 days). Useful for rendering a \&quot;recent activity\&quot; panel on the conversions setup tab without standing up a parallel persistence layer.  Per-event payload mirrors the structured log we write on every successful send: &#x60;eventName&#x60;, &#x60;conversationId&#x60;, &#x60;eventsReceived&#x60;, &#x60;eventsFailed&#x60;, &#x60;traceId&#x60;, &#x60;durationMs&#x60;, and the wall-clock &#x60;timestamp&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        Integer limit = 50; // Integer | Max events to return (1-200, default 50).
        try {
            ListWhatsAppConversions200Response result = apiInstance.listWhatsAppConversions(accountId, limit);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listWhatsAppConversions");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| WhatsApp social account ID | |
| **limit** | **Integer**| Max events to return (1-200, default 50). | [optional] [default to 50] |

### Return type

[**ListWhatsAppConversions200Response**](ListWhatsAppConversions200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Recent conversion events |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |

## listWhatsAppConversionsWithHttpInfo

> ApiResponse<ListWhatsAppConversions200Response> listWhatsAppConversions listWhatsAppConversionsWithHttpInfo(accountId, limit)

List conversion events

Returns the most recent conversion events sent through &#x60;POST /v1/whatsapp/conversions&#x60; for the given WhatsApp account. Sourced from delivery logs (Axiom &#x60;late&#x60; dataset), so the visible window is bounded by log retention (about 30 days). Useful for rendering a \&quot;recent activity\&quot; panel on the conversions setup tab without standing up a parallel persistence layer.  Per-event payload mirrors the structured log we write on every successful send: &#x60;eventName&#x60;, &#x60;conversationId&#x60;, &#x60;eventsReceived&#x60;, &#x60;eventsFailed&#x60;, &#x60;traceId&#x60;, &#x60;durationMs&#x60;, and the wall-clock &#x60;timestamp&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | WhatsApp social account ID
        Integer limit = 50; // Integer | Max events to return (1-200, default 50).
        try {
            ApiResponse<ListWhatsAppConversions200Response> response = apiInstance.listWhatsAppConversionsWithHttpInfo(accountId, limit);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#listWhatsAppConversions");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| WhatsApp social account ID | |
| **limit** | **Integer**| Max events to return (1-200, default 50). | [optional] [default to 50] |

### Return type

ApiResponse<[**ListWhatsAppConversions200Response**](ListWhatsAppConversions200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Recent conversion events |  -  |
| **401** | Unauthorized |  -  |
| **404** | WhatsApp account not found |  -  |


## queryAdInsights

> QueryAdInsights200Response queryAdInsights(accountId, objectId, level, fields, breakdowns, actionBreakdowns, actionAttributionWindows, actionReportTime, useUnifiedAttributionSetting, filtering, datePreset, fromDate, toDate, timeIncrement, limit, after)

Flexible live insights query (Meta)

Live, flexible insights query against Meta&#39;s Graph API. Unlike GET /v1/ads/{adId}/analytics (fixed metric set, cached), this forwards caller-chosen &#x60;fields&#x60;, &#x60;breakdowns&#x60; and &#x60;filtering&#x60; to any Meta insights node and returns Meta&#39;s rows verbatim.  &#x60;objectId&#x60; selects the node: an ad account, campaign, ad set or ad platform id. &#x60;level&#x60; sets row granularity independently of the node.  Semantic validation is Meta&#39;s: an unknown field or invalid breakdown combination returns a 400 carrying Meta&#39;s message. For long ranges or agency-scale accounts prefer the async variant (POST /v1/ads/insights/reports). Meta only. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String objectId = "objectId_example"; // String | Meta insights node: act_<n>, campaign id, ad set id or ad id.
        String level = "ad"; // String | Row granularity
        String fields = "fields_example"; // String | Comma-separated Graph insights fields (e.g. spend,impressions,frequency,website_purchase_roas). Omitted = Meta's default set.
        String breakdowns = "breakdowns_example"; // String | Comma-separated Graph breakdowns (e.g. age,gender or publisher_platform).
        String actionBreakdowns = "actionBreakdowns_example"; // String | Comma-separated Graph action breakdowns. Segments the actions[] arrays in each row.
        String actionAttributionWindows = "actionAttributionWindows_example"; // String | Comma-separated Meta attribution windows. Action values are returned keyed per window.
        String actionReportTime = "actionReportTime_example"; // String | When actions are counted: impression, conversion or mixed.
        Boolean useUnifiedAttributionSetting = true; // Boolean | Use the ad sets' own attribution settings for action counting.
        String filtering = "filtering_example"; // String | JSON array of Meta filter objects: [{\"field\", \"operator\", \"value\"}]. Applied server-side by Meta.
        String datePreset = "datePreset_example"; // String | Meta date_preset (e.g. last_7d, last_30d, this_month). Mutually exclusive with fromDate/toDate.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of range (YYYY-MM-DD); requires toDate.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of range (YYYY-MM-DD); requires fromDate.
        String timeIncrement = "timeIncrement_example"; // String | Days per row (1-90), monthly, or all_days.
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            QueryAdInsights200Response result = apiInstance.queryAdInsights(accountId, objectId, level, fields, breakdowns, actionBreakdowns, actionAttributionWindows, actionReportTime, useUnifiedAttributionSetting, filtering, datePreset, fromDate, toDate, timeIncrement, limit, after);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#queryAdInsights");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **objectId** | **String**| Meta insights node: act_&lt;n&gt;, campaign id, ad set id or ad id. | |
| **level** | **String**| Row granularity | [optional] [enum: ad, adset, campaign, account] |
| **fields** | **String**| Comma-separated Graph insights fields (e.g. spend,impressions,frequency,website_purchase_roas). Omitted &#x3D; Meta&#39;s default set. | [optional] |
| **breakdowns** | **String**| Comma-separated Graph breakdowns (e.g. age,gender or publisher_platform). | [optional] |
| **actionBreakdowns** | **String**| Comma-separated Graph action breakdowns. Segments the actions[] arrays in each row. | [optional] |
| **actionAttributionWindows** | **String**| Comma-separated Meta attribution windows. Action values are returned keyed per window. | [optional] |
| **actionReportTime** | **String**| When actions are counted: impression, conversion or mixed. | [optional] |
| **useUnifiedAttributionSetting** | **Boolean**| Use the ad sets&#39; own attribution settings for action counting. | [optional] |
| **filtering** | **String**| JSON array of Meta filter objects: [{\&quot;field\&quot;, \&quot;operator\&quot;, \&quot;value\&quot;}]. Applied server-side by Meta. | [optional] |
| **datePreset** | **String**| Meta date_preset (e.g. last_7d, last_30d, this_month). Mutually exclusive with fromDate/toDate. | [optional] |
| **fromDate** | **LocalDate**| Start of range (YYYY-MM-DD); requires toDate. | [optional] |
| **toDate** | **LocalDate**| End of range (YYYY-MM-DD); requires fromDate. | [optional] |
| **timeIncrement** | **String**| Days per row (1-90), monthly, or all_days. | [optional] |
| **limit** | **Integer**| Rows per page | [optional] [default to 25] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

[**QueryAdInsights200Response**](QueryAdInsights200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Insight rows (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query (unknown field, invalid breakdown combo) — message carries Meta&#39;s error |  -  |
| **401** | Unauthorized |  -  |
| **429** | Meta rate limit reached |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## queryAdInsightsWithHttpInfo

> ApiResponse<QueryAdInsights200Response> queryAdInsights queryAdInsightsWithHttpInfo(accountId, objectId, level, fields, breakdowns, actionBreakdowns, actionAttributionWindows, actionReportTime, useUnifiedAttributionSetting, filtering, datePreset, fromDate, toDate, timeIncrement, limit, after)

Flexible live insights query (Meta)

Live, flexible insights query against Meta&#39;s Graph API. Unlike GET /v1/ads/{adId}/analytics (fixed metric set, cached), this forwards caller-chosen &#x60;fields&#x60;, &#x60;breakdowns&#x60; and &#x60;filtering&#x60; to any Meta insights node and returns Meta&#39;s rows verbatim.  &#x60;objectId&#x60; selects the node: an ad account, campaign, ad set or ad platform id. &#x60;level&#x60; sets row granularity independently of the node.  Semantic validation is Meta&#39;s: an unknown field or invalid breakdown combination returns a 400 carrying Meta&#39;s message. For long ranges or agency-scale accounts prefer the async variant (POST /v1/ads/insights/reports). Meta only. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token.
        String objectId = "objectId_example"; // String | Meta insights node: act_<n>, campaign id, ad set id or ad id.
        String level = "ad"; // String | Row granularity
        String fields = "fields_example"; // String | Comma-separated Graph insights fields (e.g. spend,impressions,frequency,website_purchase_roas). Omitted = Meta's default set.
        String breakdowns = "breakdowns_example"; // String | Comma-separated Graph breakdowns (e.g. age,gender or publisher_platform).
        String actionBreakdowns = "actionBreakdowns_example"; // String | Comma-separated Graph action breakdowns. Segments the actions[] arrays in each row.
        String actionAttributionWindows = "actionAttributionWindows_example"; // String | Comma-separated Meta attribution windows. Action values are returned keyed per window.
        String actionReportTime = "actionReportTime_example"; // String | When actions are counted: impression, conversion or mixed.
        Boolean useUnifiedAttributionSetting = true; // Boolean | Use the ad sets' own attribution settings for action counting.
        String filtering = "filtering_example"; // String | JSON array of Meta filter objects: [{\"field\", \"operator\", \"value\"}]. Applied server-side by Meta.
        String datePreset = "datePreset_example"; // String | Meta date_preset (e.g. last_7d, last_30d, this_month). Mutually exclusive with fromDate/toDate.
        LocalDate fromDate = LocalDate.now(); // LocalDate | Start of range (YYYY-MM-DD); requires toDate.
        LocalDate toDate = LocalDate.now(); // LocalDate | End of range (YYYY-MM-DD); requires fromDate.
        String timeIncrement = "timeIncrement_example"; // String | Days per row (1-90), monthly, or all_days.
        Integer limit = 25; // Integer | Rows per page
        String after = "after_example"; // String | Cursor from paging.after of the previous page.
        try {
            ApiResponse<QueryAdInsights200Response> response = apiInstance.queryAdInsightsWithHttpInfo(accountId, objectId, level, fields, breakdowns, actionBreakdowns, actionAttributionWindows, actionReportTime, useUnifiedAttributionSetting, filtering, datePreset, fromDate, toDate, timeIncrement, limit, after);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#queryAdInsights");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Zernio SocialAccount id (posting or ads variant) used to resolve the Meta token. | |
| **objectId** | **String**| Meta insights node: act_&lt;n&gt;, campaign id, ad set id or ad id. | |
| **level** | **String**| Row granularity | [optional] [enum: ad, adset, campaign, account] |
| **fields** | **String**| Comma-separated Graph insights fields (e.g. spend,impressions,frequency,website_purchase_roas). Omitted &#x3D; Meta&#39;s default set. | [optional] |
| **breakdowns** | **String**| Comma-separated Graph breakdowns (e.g. age,gender or publisher_platform). | [optional] |
| **actionBreakdowns** | **String**| Comma-separated Graph action breakdowns. Segments the actions[] arrays in each row. | [optional] |
| **actionAttributionWindows** | **String**| Comma-separated Meta attribution windows. Action values are returned keyed per window. | [optional] |
| **actionReportTime** | **String**| When actions are counted: impression, conversion or mixed. | [optional] |
| **useUnifiedAttributionSetting** | **Boolean**| Use the ad sets&#39; own attribution settings for action counting. | [optional] |
| **filtering** | **String**| JSON array of Meta filter objects: [{\&quot;field\&quot;, \&quot;operator\&quot;, \&quot;value\&quot;}]. Applied server-side by Meta. | [optional] |
| **datePreset** | **String**| Meta date_preset (e.g. last_7d, last_30d, this_month). Mutually exclusive with fromDate/toDate. | [optional] |
| **fromDate** | **LocalDate**| Start of range (YYYY-MM-DD); requires toDate. | [optional] |
| **toDate** | **LocalDate**| End of range (YYYY-MM-DD); requires fromDate. | [optional] |
| **timeIncrement** | **String**| Days per row (1-90), monthly, or all_days. | [optional] |
| **limit** | **Integer**| Rows per page | [optional] [default to 25] |
| **after** | **String**| Cursor from paging.after of the previous page. | [optional] |

### Return type

ApiResponse<[**QueryAdInsights200Response**](QueryAdInsights200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Insight rows (raw Meta shape) |  -  |
| **400** | Invalid input, or Meta rejected the query (unknown field, invalid breakdown combo) — message carries Meta&#39;s error |  -  |
| **401** | Unauthorized |  -  |
| **429** | Meta rate limit reached |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## removeConversionAssociations

> RemoveConversionAssociations200Response removeConversionAssociations(accountId, destinationId, adAccountId, campaignIds)

Remove associated campaigns

Remove one or more campaign associations from this conversion rule. Pass &#x60;adAccountId&#x60; and &#x60;campaignIds&#x60; as query parameters (&#x60;campaignIds&#x60; is comma-separated). The route also accepts a JSON body with the same fields for clients that prefer DELETE-with-body, but the documented surface is query-only because some SDK code generators (e.g. Python) collapse query + body parameters with the same name into a single kwarg. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String destinationId = "destinationId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | 
        String campaignIds = "campaignIds_example"; // String | Comma-separated list of campaign IDs.
        try {
            RemoveConversionAssociations200Response result = apiInstance.removeConversionAssociations(accountId, destinationId, adAccountId, campaignIds);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#removeConversionAssociations");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**|  | |
| **destinationId** | **String**|  | |
| **adAccountId** | **String**|  | |
| **campaignIds** | **String**| Comma-separated list of campaign IDs. | |

### Return type

[**RemoveConversionAssociations200Response**](RemoveConversionAssociations200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-campaign batch result. Status is 200 even when some rows failed — inspect &#x60;failed[]&#x60; for details.  |  -  |
| **400** | Validation error: missing &#x60;adAccountId&#x60; or &#x60;campaignIds&#x60;, or campaignIds exceeds 100 entries per request.  |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on or LinkedIn reconnect required. |  -  |
| **404** | Account or destination not found. |  -  |
| **405** | Platform does not support associations. |  -  |
| **429** | LinkedIn rate limit hit. Retry with backoff. |  -  |

## removeConversionAssociationsWithHttpInfo

> ApiResponse<RemoveConversionAssociations200Response> removeConversionAssociations removeConversionAssociationsWithHttpInfo(accountId, destinationId, adAccountId, campaignIds)

Remove associated campaigns

Remove one or more campaign associations from this conversion rule. Pass &#x60;adAccountId&#x60; and &#x60;campaignIds&#x60; as query parameters (&#x60;campaignIds&#x60; is comma-separated). The route also accepts a JSON body with the same fields for clients that prefer DELETE-with-body, but the documented surface is query-only because some SDK code generators (e.g. Python) collapse query + body parameters with the same name into a single kwarg. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String destinationId = "destinationId_example"; // String | 
        String adAccountId = "adAccountId_example"; // String | 
        String campaignIds = "campaignIds_example"; // String | Comma-separated list of campaign IDs.
        try {
            ApiResponse<RemoveConversionAssociations200Response> response = apiInstance.removeConversionAssociationsWithHttpInfo(accountId, destinationId, adAccountId, campaignIds);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#removeConversionAssociations");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**|  | |
| **destinationId** | **String**|  | |
| **adAccountId** | **String**|  | |
| **campaignIds** | **String**| Comma-separated list of campaign IDs. | |

### Return type

ApiResponse<[**RemoveConversionAssociations200Response**](RemoveConversionAssociations200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Per-campaign batch result. Status is 200 even when some rows failed — inspect &#x60;failed[]&#x60; for details.  |  -  |
| **400** | Validation error: missing &#x60;adAccountId&#x60; or &#x60;campaignIds&#x60;, or campaignIds exceeds 100 entries per request.  |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on or LinkedIn reconnect required. |  -  |
| **404** | Account or destination not found. |  -  |
| **405** | Platform does not support associations. |  -  |
| **429** | LinkedIn rate limit hit. Retry with backoff. |  -  |


## reserveRfPrediction

> ReserveRfPrediction201Response reserveRfPrediction(predictionId, reserveRfPredictionRequest)

Reserve a Reach &amp; Frequency prediction (Meta)

Locks the quoted price + inventory until the returned &#x60;expiresAt&#x60; and mints a NEW prediction id — pass that RESERVED id (not the original) as &#x60;rfPredictionId&#x60; on POST /v1/ads/create. Release an unused reservation via DELETE. Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String predictionId = "predictionId_example"; // String | 
        ReserveRfPredictionRequest reserveRfPredictionRequest = new ReserveRfPredictionRequest(); // ReserveRfPredictionRequest | 
        try {
            ReserveRfPrediction201Response result = apiInstance.reserveRfPrediction(predictionId, reserveRfPredictionRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#reserveRfPrediction");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **predictionId** | **String**|  | |
| **reserveRfPredictionRequest** | [**ReserveRfPredictionRequest**](ReserveRfPredictionRequest.md)|  | |

### Return type

[**ReserveRfPrediction201Response**](ReserveRfPrediction201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Reserved; &#x60;prediction.predictionId&#x60; is the new RESERVED id |  -  |
| **400** | Invalid input, or Meta rejected the reserve |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## reserveRfPredictionWithHttpInfo

> ApiResponse<ReserveRfPrediction201Response> reserveRfPrediction reserveRfPredictionWithHttpInfo(predictionId, reserveRfPredictionRequest)

Reserve a Reach &amp; Frequency prediction (Meta)

Locks the quoted price + inventory until the returned &#x60;expiresAt&#x60; and mints a NEW prediction id — pass that RESERVED id (not the original) as &#x60;rfPredictionId&#x60; on POST /v1/ads/create. Release an unused reservation via DELETE. Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String predictionId = "predictionId_example"; // String | 
        ReserveRfPredictionRequest reserveRfPredictionRequest = new ReserveRfPredictionRequest(); // ReserveRfPredictionRequest | 
        try {
            ApiResponse<ReserveRfPrediction201Response> response = apiInstance.reserveRfPredictionWithHttpInfo(predictionId, reserveRfPredictionRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#reserveRfPrediction");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **predictionId** | **String**|  | |
| **reserveRfPredictionRequest** | [**ReserveRfPredictionRequest**](ReserveRfPredictionRequest.md)|  | |

### Return type

ApiResponse<[**ReserveRfPrediction201Response**](ReserveRfPrediction201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Reserved; &#x60;prediction.predictionId&#x60; is the new RESERVED id |  -  |
| **400** | Invalid input, or Meta rejected the reserve |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## searchAdInterests

> SearchAdInterests200Response searchAdInterests(q, accountId)

Search targeting interests

Deprecated alias for &#x60;GET /v1/ads/targeting/search?dimension&#x3D;interest&#x60;. Kept for backward compatibility, it returns the legacy &#x60;{ interests: [...] }&#x60; shape rather than the normalized &#x60;{ results: [...] }&#x60;. New integrations should use &#x60;GET /v1/ads/targeting/search&#x60; with &#x60;dimension&#x3D;interest&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String q = "q_example"; // String | Search query
        String accountId = "accountId_example"; // String | Social account ID
        try {
            SearchAdInterests200Response result = apiInstance.searchAdInterests(q, accountId);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#searchAdInterests");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **q** | **String**| Search query | |
| **accountId** | **String**| Social account ID | |

### Return type

[**SearchAdInterests200Response**](SearchAdInterests200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Matching interests |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |

## searchAdInterestsWithHttpInfo

> ApiResponse<SearchAdInterests200Response> searchAdInterests searchAdInterestsWithHttpInfo(q, accountId)

Search targeting interests

Deprecated alias for &#x60;GET /v1/ads/targeting/search?dimension&#x3D;interest&#x60;. Kept for backward compatibility, it returns the legacy &#x60;{ interests: [...] }&#x60; shape rather than the normalized &#x60;{ results: [...] }&#x60;. New integrations should use &#x60;GET /v1/ads/targeting/search&#x60; with &#x60;dimension&#x3D;interest&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String q = "q_example"; // String | Search query
        String accountId = "accountId_example"; // String | Social account ID
        try {
            ApiResponse<SearchAdInterests200Response> response = apiInstance.searchAdInterestsWithHttpInfo(q, accountId);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#searchAdInterests");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **q** | **String**| Search query | |
| **accountId** | **String**| Social account ID | |

### Return type

ApiResponse<[**SearchAdInterests200Response**](SearchAdInterests200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Matching interests |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |


## searchAdTargeting

> SearchAdTargeting200Response searchAdTargeting(accountId, q, dimension, geoType, countryCode, limit)

Search targeting options

Resolve a human-readable query into the platform&#39;s opaque targeting ids used in the &#x60;TargetingSpec&#x60; (&#x60;countries&#x60;/&#x60;regions&#x60;/&#x60;cities&#x60;/&#x60;zips&#x60;/&#x60;metros&#x60; geo keys, and &#x60;interests&#x60;/&#x60;behaviors&#x60; entity ids) on &#x60;POST /v1/ads/create&#x60;, &#x60;POST /v1/ads/targeting/reach-estimate&#x60;, and &#x60;saved_targeting&#x60; audiences.  The &#x60;dimension&#x60; param selects what is searched, &#x60;geo&#x60; (locations, further scoped by &#x60;geoType&#x60;), &#x60;interest&#x60;, &#x60;behavior&#x60;, or &#x60;income&#x60;. Availability of each dimension varies by platform (e.g. behaviours are Meta/TikTok only). Results are normalized across platforms into a single shape, so the same client code consumes Meta, TikTok, LinkedIn, X, Pinterest, and Google results.  TikTok geo searches return every matching level in one list (&#x60;type&#x60; is &#x60;country&#x60;, &#x60;region&#x60;, &#x60;city&#x60;, &#x60;district&#x60;, or &#x60;metro&#x60; for DMA areas) — &#x60;geoType&#x60; is not applied. Results are scoped to the advertiser&#39;s targetable markets, and every id is usable in &#x60;regions&#x60;/&#x60;cities&#x60;/&#x60;metros&#x60; keys on &#x60;POST /v1/ads/create&#x60;.  For geo queries, &#x60;q&#x60; should contain only the locality name (e.g. &#x60;\&quot;Amsterdam\&quot;&#x60;, not &#x60;\&quot;Amsterdam, NL\&quot;&#x60;). Use &#x60;countryCode&#x60; to disambiguate. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | Social account ID (a connected account on the target ad platform).
        String q = "q_example"; // String | Search query. For geo, the locality name only (no region/country suffix).
        String dimension = "geo"; // String | What to search. `geo` resolves locations (scope further with `geoType`), `interest`/`behavior` resolve audience entities, `income` resolves income-tier options. Defaults to `interest` for backward compatibility with the deprecated /v1/ads/interests alias.
        String geoType = "country"; // String | Only used when `dimension=geo`. The kind of location to resolve. Defaults to `city`.
        String countryCode = "countryCode_example"; // String | ISO 3166-1 alpha-2 country code (e.g. NL) to scope a geo search.
        Integer limit = 25; // Integer | Maximum results to return.
        try {
            SearchAdTargeting200Response result = apiInstance.searchAdTargeting(accountId, q, dimension, geoType, countryCode, limit);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#searchAdTargeting");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Social account ID (a connected account on the target ad platform). | |
| **q** | **String**| Search query. For geo, the locality name only (no region/country suffix). | |
| **dimension** | **String**| What to search. &#x60;geo&#x60; resolves locations (scope further with &#x60;geoType&#x60;), &#x60;interest&#x60;/&#x60;behavior&#x60; resolve audience entities, &#x60;income&#x60; resolves income-tier options. Defaults to &#x60;interest&#x60; for backward compatibility with the deprecated /v1/ads/interests alias. | [optional] [default to interest] [enum: geo, interest, behavior, income] |
| **geoType** | **String**| Only used when &#x60;dimension&#x3D;geo&#x60;. The kind of location to resolve. Defaults to &#x60;city&#x60;. | [optional] [default to city] [enum: country, region, city, zip, metro] |
| **countryCode** | **String**| ISO 3166-1 alpha-2 country code (e.g. NL) to scope a geo search. | [optional] |
| **limit** | **Integer**| Maximum results to return. | [optional] [default to 25] |

### Return type

[**SearchAdTargeting200Response**](SearchAdTargeting200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Matching targeting options (normalized) |  -  |
| **400** | Missing or invalid query parameters |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Account not found, or the platform does not support the requested dimension |  -  |

## searchAdTargetingWithHttpInfo

> ApiResponse<SearchAdTargeting200Response> searchAdTargeting searchAdTargetingWithHttpInfo(accountId, q, dimension, geoType, countryCode, limit)

Search targeting options

Resolve a human-readable query into the platform&#39;s opaque targeting ids used in the &#x60;TargetingSpec&#x60; (&#x60;countries&#x60;/&#x60;regions&#x60;/&#x60;cities&#x60;/&#x60;zips&#x60;/&#x60;metros&#x60; geo keys, and &#x60;interests&#x60;/&#x60;behaviors&#x60; entity ids) on &#x60;POST /v1/ads/create&#x60;, &#x60;POST /v1/ads/targeting/reach-estimate&#x60;, and &#x60;saved_targeting&#x60; audiences.  The &#x60;dimension&#x60; param selects what is searched, &#x60;geo&#x60; (locations, further scoped by &#x60;geoType&#x60;), &#x60;interest&#x60;, &#x60;behavior&#x60;, or &#x60;income&#x60;. Availability of each dimension varies by platform (e.g. behaviours are Meta/TikTok only). Results are normalized across platforms into a single shape, so the same client code consumes Meta, TikTok, LinkedIn, X, Pinterest, and Google results.  TikTok geo searches return every matching level in one list (&#x60;type&#x60; is &#x60;country&#x60;, &#x60;region&#x60;, &#x60;city&#x60;, &#x60;district&#x60;, or &#x60;metro&#x60; for DMA areas) — &#x60;geoType&#x60; is not applied. Results are scoped to the advertiser&#39;s targetable markets, and every id is usable in &#x60;regions&#x60;/&#x60;cities&#x60;/&#x60;metros&#x60; keys on &#x60;POST /v1/ads/create&#x60;.  For geo queries, &#x60;q&#x60; should contain only the locality name (e.g. &#x60;\&quot;Amsterdam\&quot;&#x60;, not &#x60;\&quot;Amsterdam, NL\&quot;&#x60;). Use &#x60;countryCode&#x60; to disambiguate. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | Social account ID (a connected account on the target ad platform).
        String q = "q_example"; // String | Search query. For geo, the locality name only (no region/country suffix).
        String dimension = "geo"; // String | What to search. `geo` resolves locations (scope further with `geoType`), `interest`/`behavior` resolve audience entities, `income` resolves income-tier options. Defaults to `interest` for backward compatibility with the deprecated /v1/ads/interests alias.
        String geoType = "country"; // String | Only used when `dimension=geo`. The kind of location to resolve. Defaults to `city`.
        String countryCode = "countryCode_example"; // String | ISO 3166-1 alpha-2 country code (e.g. NL) to scope a geo search.
        Integer limit = 25; // Integer | Maximum results to return.
        try {
            ApiResponse<SearchAdTargeting200Response> response = apiInstance.searchAdTargetingWithHttpInfo(accountId, q, dimension, geoType, countryCode, limit);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#searchAdTargeting");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| Social account ID (a connected account on the target ad platform). | |
| **q** | **String**| Search query. For geo, the locality name only (no region/country suffix). | |
| **dimension** | **String**| What to search. &#x60;geo&#x60; resolves locations (scope further with &#x60;geoType&#x60;), &#x60;interest&#x60;/&#x60;behavior&#x60; resolve audience entities, &#x60;income&#x60; resolves income-tier options. Defaults to &#x60;interest&#x60; for backward compatibility with the deprecated /v1/ads/interests alias. | [optional] [default to interest] [enum: geo, interest, behavior, income] |
| **geoType** | **String**| Only used when &#x60;dimension&#x3D;geo&#x60;. The kind of location to resolve. Defaults to &#x60;city&#x60;. | [optional] [default to city] [enum: country, region, city, zip, metro] |
| **countryCode** | **String**| ISO 3166-1 alpha-2 country code (e.g. NL) to scope a geo search. | [optional] |
| **limit** | **Integer**| Maximum results to return. | [optional] [default to 25] |

### Return type

ApiResponse<[**SearchAdTargeting200Response**](SearchAdTargeting200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Matching targeting options (normalized) |  -  |
| **400** | Missing or invalid query parameters |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required. Legacy plans need the Ads add-on; included by default on usage-based plans. |  -  |
| **404** | Account not found, or the platform does not support the requested dimension |  -  |


## sendConversions

> SendConversions200Response sendConversions(sendConversionsRequest)

Send conversion events

Relay one or more conversion events to the target ad platform&#39;s native Conversions API. Platform is inferred from the provided &#x60;accountId&#x60;. Requires the Ads add-on.  Supported platforms:  - Meta (&#x60;metaads&#x60;) via Graph API - Google Ads (&#x60;googleads&#x60;) via Data Manager API &#x60;ingestEvents&#x60; - LinkedIn (&#x60;linkedinads&#x60;) via &#x60;/rest/conversionEvents&#x60; - TikTok (&#x60;tiktokads&#x60;) via the Offline Events API &#x60;/offline/batch/&#x60; — OFFLINE conversions only  &#x60;destinationId&#x60; semantics differ per platform:  - Meta: pixel (dataset) ID, e.g. &#x60;123456789012345&#x60; - Google: conversion action resource name, e.g. &#x60;customers/1234567890/conversionActions/987654321&#x60; - LinkedIn: conversion rule ID or URN, e.g. &#x60;104012&#x60; or &#x60;urn:lla:llaPartnerConversion:104012&#x60; - TikTok: Offline Event Set ID, e.g. &#x60;7057103914977558530&#x60;  TikTok notes: this path sends OFFLINE conversions (in-store / CRM / call-center), not web-pixel events. Each event must carry an email or phone (TikTok requires at least one). The connected TikTok ads account must have granted the Offline Events permission; older grants must reconnect.  Callers can list valid destinations via &#x60;GET /v1/accounts/{accountId}/conversion-destinations&#x60;.  All PII (email, phone, names, external IDs) is hashed with SHA-256 server-side per each platform&#39;s normalization spec, including Google&#39;s Gmail-specific dot/plus-suffix stripping. Send plaintext. LinkedIn &#x60;externalIds&#x60; are passed through as plaintext per LinkedIn&#39;s spec; only emails and phones are hashed.  For LinkedIn, the connected account must have been authorized after the Conversions API rollout (i.e. the OAuth grant must include &#x60;rw_conversions&#x60;). Older accounts must reconnect.  Batching is handled automatically. Meta caps at 1000 events per request and rejects the entire batch if any event is malformed. Google caps at 2000. LinkedIn caps at 5000 and is also all-or-nothing per chunk.  Dedup: pass a stable &#x60;eventId&#x60; on every event. Meta and LinkedIn use it to dedupe against browser-side pixel/Insight Tag events; Google maps it to &#x60;transactionId&#x60;.  Per-platform &#x60;eventName&#x60; semantics:  - Meta: free-form. Standard names (Purchase, Lead, ...) match Meta&#39;s built-in events; custom strings are accepted. - Google: ignored. The conversion action&#39;s category determines the event type. Send the standard name closest to your action for documentation, but the platform will not branch on it. - LinkedIn: ignored. The conversion rule&#39;s &#x60;type&#x60; (LEAD, PURCHASE, etc.) is locked to the destination at rule-creation time. Send the standard name for documentation; LinkedIn does not branch on it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        SendConversionsRequest sendConversionsRequest = new SendConversionsRequest(); // SendConversionsRequest | 
        try {
            SendConversions200Response result = apiInstance.sendConversions(sendConversionsRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#sendConversions");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **sendConversionsRequest** | [**SendConversionsRequest**](SendConversionsRequest.md)|  | |

### Return type

[**SendConversions200Response**](SendConversions200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Events processed. Inspect &#x60;eventsFailed&#x60; and &#x60;failures[]&#x60; to detect partial failure. For Meta, a batch is all-or-nothing (either every event in a chunk succeeds, or every event in the chunk is listed in failures). For Google, the API returns success/failure at the request level only.  |  -  |
| **400** | Invalid body (missing accountId/destinationId/events, malformed event shape). |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), OR (for LinkedIn) the connected account lacks the &#x60;rw_conversions&#x60; scope and must be reconnected.  |  -  |
| **404** | Account not found or not accessible. |  -  |
| **429** | LinkedIn token-level rate limit hit (600 requests/min, 300k/day per token). Retry with backoff. Meta and Google have their own rate-limit semantics surfaced via platform-specific 4xx responses.  |  -  |

## sendConversionsWithHttpInfo

> ApiResponse<SendConversions200Response> sendConversions sendConversionsWithHttpInfo(sendConversionsRequest)

Send conversion events

Relay one or more conversion events to the target ad platform&#39;s native Conversions API. Platform is inferred from the provided &#x60;accountId&#x60;. Requires the Ads add-on.  Supported platforms:  - Meta (&#x60;metaads&#x60;) via Graph API - Google Ads (&#x60;googleads&#x60;) via Data Manager API &#x60;ingestEvents&#x60; - LinkedIn (&#x60;linkedinads&#x60;) via &#x60;/rest/conversionEvents&#x60; - TikTok (&#x60;tiktokads&#x60;) via the Offline Events API &#x60;/offline/batch/&#x60; — OFFLINE conversions only  &#x60;destinationId&#x60; semantics differ per platform:  - Meta: pixel (dataset) ID, e.g. &#x60;123456789012345&#x60; - Google: conversion action resource name, e.g. &#x60;customers/1234567890/conversionActions/987654321&#x60; - LinkedIn: conversion rule ID or URN, e.g. &#x60;104012&#x60; or &#x60;urn:lla:llaPartnerConversion:104012&#x60; - TikTok: Offline Event Set ID, e.g. &#x60;7057103914977558530&#x60;  TikTok notes: this path sends OFFLINE conversions (in-store / CRM / call-center), not web-pixel events. Each event must carry an email or phone (TikTok requires at least one). The connected TikTok ads account must have granted the Offline Events permission; older grants must reconnect.  Callers can list valid destinations via &#x60;GET /v1/accounts/{accountId}/conversion-destinations&#x60;.  All PII (email, phone, names, external IDs) is hashed with SHA-256 server-side per each platform&#39;s normalization spec, including Google&#39;s Gmail-specific dot/plus-suffix stripping. Send plaintext. LinkedIn &#x60;externalIds&#x60; are passed through as plaintext per LinkedIn&#39;s spec; only emails and phones are hashed.  For LinkedIn, the connected account must have been authorized after the Conversions API rollout (i.e. the OAuth grant must include &#x60;rw_conversions&#x60;). Older accounts must reconnect.  Batching is handled automatically. Meta caps at 1000 events per request and rejects the entire batch if any event is malformed. Google caps at 2000. LinkedIn caps at 5000 and is also all-or-nothing per chunk.  Dedup: pass a stable &#x60;eventId&#x60; on every event. Meta and LinkedIn use it to dedupe against browser-side pixel/Insight Tag events; Google maps it to &#x60;transactionId&#x60;.  Per-platform &#x60;eventName&#x60; semantics:  - Meta: free-form. Standard names (Purchase, Lead, ...) match Meta&#39;s built-in events; custom strings are accepted. - Google: ignored. The conversion action&#39;s category determines the event type. Send the standard name closest to your action for documentation, but the platform will not branch on it. - LinkedIn: ignored. The conversion rule&#39;s &#x60;type&#x60; (LEAD, PURCHASE, etc.) is locked to the destination at rule-creation time. Send the standard name for documentation; LinkedIn does not branch on it. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        SendConversionsRequest sendConversionsRequest = new SendConversionsRequest(); // SendConversionsRequest | 
        try {
            ApiResponse<SendConversions200Response> response = apiInstance.sendConversionsWithHttpInfo(sendConversionsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#sendConversions");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **sendConversionsRequest** | [**SendConversionsRequest**](SendConversionsRequest.md)|  | |

### Return type

ApiResponse<[**SendConversions200Response**](SendConversions200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Events processed. Inspect &#x60;eventsFailed&#x60; and &#x60;failures[]&#x60; to detect partial failure. For Meta, a batch is all-or-nothing (either every event in a chunk succeeds, or every event in the chunk is listed in failures). For Google, the API returns success/failure at the request level only.  |  -  |
| **400** | Invalid body (missing accountId/destinationId/events, malformed event shape). |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads access required (Ads add-on on legacy plans, included on usage-based plans), OR (for LinkedIn) the connected account lacks the &#x60;rw_conversions&#x60; scope and must be reconnected.  |  -  |
| **404** | Account not found or not accessible. |  -  |
| **429** | LinkedIn token-level rate limit hit (600 requests/min, 300k/day per token). Retry with backoff. Meta and Google have their own rate-limit semantics surfaced via platform-specific 4xx responses.  |  -  |


## sendWhatsAppConversion

> SendWhatsAppConversion200Response sendWhatsAppConversion(sendWhatsAppConversionRequest)

Send WhatsApp conversion event

Forward a WhatsApp Business Messaging conversion event (&#x60;LeadSubmitted&#x60;, &#x60;Purchase&#x60;, &#x60;AddToCart&#x60;, &#x60;InitiateCheckout&#x60;, &#x60;ViewContent&#x60;) to Meta&#39;s Conversions API with &#x60;action_source &#x3D; business_messaging&#x60; and &#x60;messaging_channel &#x3D; whatsapp&#x60;. The endpoint looks up the originating CTWA click ID (&#x60;ctwa_clid&#x60;) captured on the first inbound message of the conversation and replays it on every event so Meta can attribute the conversion back to the Click-to-WhatsApp ad that drove the chat.  Configuration prerequisite on the WhatsApp account metadata:   - &#x60;metaCapiDatasetId&#x60;: the Meta dataset ID linked to the WABA.     Provision one with &#x60;POST /v1/whatsapp/dataset&#x60;.  The WABA ID (already set automatically at connect time) is forwarded as &#x60;user_data.whatsapp_business_account_id&#x60;, which is the per-channel attribution identifier Meta requires for WhatsApp events. No Facebook Page ID is needed (that field is the Messenger-branch identifier).  Identify the conversation by either &#x60;conversationId&#x60; (preferred) or &#x60;phoneE164&#x60; (digits only, no &#x60;+&#x60;). At least one is required. If the conversation has no captured &#x60;ctwa_clid&#x60;, the request returns 422 because there is nothing to attribute.  Token and dataset coupling: the WhatsApp account&#39;s accessToken must have access to the configured &#x60;metaCapiDatasetId&#x60;. By default a WABA&#39;s system-user token is scoped to the WABA&#39;s own Business Manager and cannot post to a pixel owned by a different Business; Meta returns code 100 in that case. Either share the dataset with the WhatsApp app&#39;s Business in BM, or use a dataset already in the same Business as the WABA. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        SendWhatsAppConversionRequest sendWhatsAppConversionRequest = new SendWhatsAppConversionRequest(); // SendWhatsAppConversionRequest | 
        try {
            SendWhatsAppConversion200Response result = apiInstance.sendWhatsAppConversion(sendWhatsAppConversionRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#sendWhatsAppConversion");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **sendWhatsAppConversionRequest** | [**SendWhatsAppConversionRequest**](SendWhatsAppConversionRequest.md)|  | |

### Return type

[**SendWhatsAppConversion200Response**](SendWhatsAppConversion200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event submitted to Meta. Inspect &#x60;eventsFailed&#x60; and &#x60;failures[]&#x60; to detect partial failures. A 200 does not mean Meta accepted the event; the status reflects \&quot;request reached Meta\&quot; only.  |  -  |
| **400** | Invalid body. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Conversation not found. |  -  |
| **422** | Configuration missing (no &#x60;metaCapiDatasetId&#x60; on the account, set it via POST /v1/whatsapp/dataset) OR the resolved conversation has no captured &#x60;ctwa_clid&#x60;.  |  -  |

## sendWhatsAppConversionWithHttpInfo

> ApiResponse<SendWhatsAppConversion200Response> sendWhatsAppConversion sendWhatsAppConversionWithHttpInfo(sendWhatsAppConversionRequest)

Send WhatsApp conversion event

Forward a WhatsApp Business Messaging conversion event (&#x60;LeadSubmitted&#x60;, &#x60;Purchase&#x60;, &#x60;AddToCart&#x60;, &#x60;InitiateCheckout&#x60;, &#x60;ViewContent&#x60;) to Meta&#39;s Conversions API with &#x60;action_source &#x3D; business_messaging&#x60; and &#x60;messaging_channel &#x3D; whatsapp&#x60;. The endpoint looks up the originating CTWA click ID (&#x60;ctwa_clid&#x60;) captured on the first inbound message of the conversation and replays it on every event so Meta can attribute the conversion back to the Click-to-WhatsApp ad that drove the chat.  Configuration prerequisite on the WhatsApp account metadata:   - &#x60;metaCapiDatasetId&#x60;: the Meta dataset ID linked to the WABA.     Provision one with &#x60;POST /v1/whatsapp/dataset&#x60;.  The WABA ID (already set automatically at connect time) is forwarded as &#x60;user_data.whatsapp_business_account_id&#x60;, which is the per-channel attribution identifier Meta requires for WhatsApp events. No Facebook Page ID is needed (that field is the Messenger-branch identifier).  Identify the conversation by either &#x60;conversationId&#x60; (preferred) or &#x60;phoneE164&#x60; (digits only, no &#x60;+&#x60;). At least one is required. If the conversation has no captured &#x60;ctwa_clid&#x60;, the request returns 422 because there is nothing to attribute.  Token and dataset coupling: the WhatsApp account&#39;s accessToken must have access to the configured &#x60;metaCapiDatasetId&#x60;. By default a WABA&#39;s system-user token is scoped to the WABA&#39;s own Business Manager and cannot post to a pixel owned by a different Business; Meta returns code 100 in that case. Either share the dataset with the WhatsApp app&#39;s Business in BM, or use a dataset already in the same Business as the WABA. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        SendWhatsAppConversionRequest sendWhatsAppConversionRequest = new SendWhatsAppConversionRequest(); // SendWhatsAppConversionRequest | 
        try {
            ApiResponse<SendWhatsAppConversion200Response> response = apiInstance.sendWhatsAppConversionWithHttpInfo(sendWhatsAppConversionRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#sendWhatsAppConversion");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **sendWhatsAppConversionRequest** | [**SendWhatsAppConversionRequest**](SendWhatsAppConversionRequest.md)|  | |

### Return type

ApiResponse<[**SendWhatsAppConversion200Response**](SendWhatsAppConversion200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Event submitted to Meta. Inspect &#x60;eventsFailed&#x60; and &#x60;failures[]&#x60; to detect partial failures. A 200 does not mean Meta accepted the event; the status reflects \&quot;request reached Meta\&quot; only.  |  -  |
| **400** | Invalid body. |  -  |
| **401** | Unauthorized |  -  |
| **404** | Conversation not found. |  -  |
| **422** | Configuration missing (no &#x60;metaCapiDatasetId&#x60; on the account, set it via POST /v1/whatsapp/dataset) OR the resolved conversation has no captured &#x60;ctwa_clid&#x60;.  |  -  |


## updateAd

> UpdateAd200Response updateAd(adId, updateAdRequest)

Update ad

Patch one or more fields on an ad. Status, budget, targeting, and creative changes are propagated to the platform.  Per-platform support: - **Meta** (Facebook + Instagram): all fields supported. - **TikTok**: status, budget, targeting (via &#x60;/v2/adgroup/update/&#x60;), and creative   (via &#x60;/v2/ad/update/&#x60; patch-style — &#x60;headline&#x60; is ignored, &#x60;body&#x60; becomes &#x60;ad_text&#x60;). - **Pinterest / X / LinkedIn / Google**: status + budget only. Sending &#x60;targeting&#x60;   or &#x60;creative&#x60; returns 501 with code &#x60;unsupported_platform_operation&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String adId = "adId_example"; // String | 
        UpdateAdRequest updateAdRequest = new UpdateAdRequest(); // UpdateAdRequest | 
        try {
            UpdateAd200Response result = apiInstance.updateAd(adId, updateAdRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#updateAd");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
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
| **400** | Invalid status transition or budget below minimum |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |
| **501** | targeting or creative not supported on the platform (Meta + TikTok only) |  -  |

## updateAdWithHttpInfo

> ApiResponse<UpdateAd200Response> updateAd updateAdWithHttpInfo(adId, updateAdRequest)

Update ad

Patch one or more fields on an ad. Status, budget, targeting, and creative changes are propagated to the platform.  Per-platform support: - **Meta** (Facebook + Instagram): all fields supported. - **TikTok**: status, budget, targeting (via &#x60;/v2/adgroup/update/&#x60;), and creative   (via &#x60;/v2/ad/update/&#x60; patch-style — &#x60;headline&#x60; is ignored, &#x60;body&#x60; becomes &#x60;ad_text&#x60;). - **Pinterest / X / LinkedIn / Google**: status + budget only. Sending &#x60;targeting&#x60;   or &#x60;creative&#x60; returns 501 with code &#x60;unsupported_platform_operation&#x60;. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String adId = "adId_example"; // String | 
        UpdateAdRequest updateAdRequest = new UpdateAdRequest(); // UpdateAdRequest | 
        try {
            ApiResponse<UpdateAd200Response> response = apiInstance.updateAdWithHttpInfo(adId, updateAdRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#updateAd");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
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
| **400** | Invalid status transition or budget below minimum |  -  |
| **401** | Unauthorized |  -  |
| **404** | Resource not found |  -  |
| **501** | targeting or creative not supported on the platform (Meta + TikTok only) |  -  |


## updateAdAccount

> UpdateAdAccount200Response updateAdAccount(updateAdAccountRequest)

Update ad account settings

Sets the default DSA beneficiary and payor on a Meta ad account (EU DSA, Article 26). Set them once and every EU-targeted call to &#x60;/v1/ads/create&#x60;, &#x60;/v1/ads/boost&#x60; and &#x60;/v1/ads/ctwa&#x60; on that ad account can omit &#x60;dsaBeneficiary&#x60;/&#x60;dsaPayor&#x60;: Meta applies the defaults automatically.  The values are written to the ad account on Meta, the same setting Ads Manager edits. Nothing is stored in Zernio, and defaults already set in Ads Manager work identically. Zernio never guesses these values for you. Beneficiary and payor are legal disclosures shown to EU users, so you must provide the entity names explicitly. Use &#x60;GET /v1/ads/dsa-recommendations&#x60; to offer suggestions in your UI.  If &#x60;defaultDsaPayor&#x60; is omitted, the beneficiary is also set as the payor, which covers the common case where the same entity benefits from and pays for the ads. Read the current values back with &#x60;GET /v1/ads/dsa-defaults&#x60;.  Currently supported for Meta accounts only; other platforms return 400. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        UpdateAdAccountRequest updateAdAccountRequest = new UpdateAdAccountRequest(); // UpdateAdAccountRequest | 
        try {
            UpdateAdAccount200Response result = apiInstance.updateAdAccount(updateAdAccountRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#updateAdAccount");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **updateAdAccountRequest** | [**UpdateAdAccountRequest**](UpdateAdAccountRequest.md)|  | |

### Return type

[**UpdateAdAccount200Response**](UpdateAdAccount200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | DSA defaults updated (re-read from Meta after the write) |  -  |
| **400** | Unsupported platform (non-Meta account) or invalid adAccountId |  -  |
| **401** | Unauthorized |  -  |
| **404** | Social account not found |  -  |

## updateAdAccountWithHttpInfo

> ApiResponse<UpdateAdAccount200Response> updateAdAccount updateAdAccountWithHttpInfo(updateAdAccountRequest)

Update ad account settings

Sets the default DSA beneficiary and payor on a Meta ad account (EU DSA, Article 26). Set them once and every EU-targeted call to &#x60;/v1/ads/create&#x60;, &#x60;/v1/ads/boost&#x60; and &#x60;/v1/ads/ctwa&#x60; on that ad account can omit &#x60;dsaBeneficiary&#x60;/&#x60;dsaPayor&#x60;: Meta applies the defaults automatically.  The values are written to the ad account on Meta, the same setting Ads Manager edits. Nothing is stored in Zernio, and defaults already set in Ads Manager work identically. Zernio never guesses these values for you. Beneficiary and payor are legal disclosures shown to EU users, so you must provide the entity names explicitly. Use &#x60;GET /v1/ads/dsa-recommendations&#x60; to offer suggestions in your UI.  If &#x60;defaultDsaPayor&#x60; is omitted, the beneficiary is also set as the payor, which covers the common case where the same entity benefits from and pays for the ads. Read the current values back with &#x60;GET /v1/ads/dsa-defaults&#x60;.  Currently supported for Meta accounts only; other platforms return 400. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        UpdateAdAccountRequest updateAdAccountRequest = new UpdateAdAccountRequest(); // UpdateAdAccountRequest | 
        try {
            ApiResponse<UpdateAdAccount200Response> response = apiInstance.updateAdAccountWithHttpInfo(updateAdAccountRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#updateAdAccount");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **updateAdAccountRequest** | [**UpdateAdAccountRequest**](UpdateAdAccountRequest.md)|  | |

### Return type

ApiResponse<[**UpdateAdAccount200Response**](UpdateAdAccount200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | DSA defaults updated (re-read from Meta after the write) |  -  |
| **400** | Unsupported platform (non-Meta account) or invalid adAccountId |  -  |
| **401** | Unauthorized |  -  |
| **404** | Social account not found |  -  |


## updateAdCreative

> UpdateAdCreative200Response updateAdCreative(creativeId, updateAdCreativeRequest)

Rename a creative (Meta)

Renames a creative. Creatives are immutable on Meta beyond &#x60;name&#x60; — for content changes create a new creative (POST /v1/ads/creatives) and swap it onto the ad (PUT /v1/ads/{adId} with &#x60;creative&#x60;). Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String creativeId = "creativeId_example"; // String | Platform creative id
        UpdateAdCreativeRequest updateAdCreativeRequest = new UpdateAdCreativeRequest(); // UpdateAdCreativeRequest | 
        try {
            UpdateAdCreative200Response result = apiInstance.updateAdCreative(creativeId, updateAdCreativeRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#updateAdCreative");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **creativeId** | **String**| Platform creative id | |
| **updateAdCreativeRequest** | [**UpdateAdCreativeRequest**](UpdateAdCreativeRequest.md)|  | |

### Return type

[**UpdateAdCreative200Response**](UpdateAdCreative200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Creative renamed |  -  |
| **400** | Invalid input, or Meta rejected the update |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## updateAdCreativeWithHttpInfo

> ApiResponse<UpdateAdCreative200Response> updateAdCreative updateAdCreativeWithHttpInfo(creativeId, updateAdCreativeRequest)

Rename a creative (Meta)

Renames a creative. Creatives are immutable on Meta beyond &#x60;name&#x60; — for content changes create a new creative (POST /v1/ads/creatives) and swap it onto the ad (PUT /v1/ads/{adId} with &#x60;creative&#x60;). Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String creativeId = "creativeId_example"; // String | Platform creative id
        UpdateAdCreativeRequest updateAdCreativeRequest = new UpdateAdCreativeRequest(); // UpdateAdCreativeRequest | 
        try {
            ApiResponse<UpdateAdCreative200Response> response = apiInstance.updateAdCreativeWithHttpInfo(creativeId, updateAdCreativeRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#updateAdCreative");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **creativeId** | **String**| Platform creative id | |
| **updateAdCreativeRequest** | [**UpdateAdCreativeRequest**](UpdateAdCreativeRequest.md)|  | |

### Return type

ApiResponse<[**UpdateAdCreative200Response**](UpdateAdCreative200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Creative renamed |  -  |
| **400** | Invalid input, or Meta rejected the update |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |


## updateAdStatus

> UpdateAdStatus200Response updateAdStatus(adId, updateAdStatusRequest)

Pause or resume a single ad

Ad-scoped pause/resume — touches ONLY this ad, never its parent ad set or campaign (so sibling ads keep running). Thin wrapper over the &#x60;status&#x60; field of PUT /v1/ads/{adId}, for callers that want a URL symmetric to /v1/ads/campaigns/{campaignId}/status and /v1/ads/ad-sets/{adSetId}/status.  &#x60;{adId}&#x60; accepts the same identifier dialects as GET/PUT /v1/ads/{adId} (Zernio hex &#x60;_id&#x60;, Meta numeric &#x60;platformAdId&#x60;, or the creative&#39;s effective story/media IDs). &#x60;platform&#x60; is inferred from the ad, so it&#39;s not required in the body. Ads in terminal statuses (rejected, completed, cancelled) and no-op flips (already in the target state) are skipped. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String adId = "adId_example"; // String | Zernio `_id` (hex), Meta `platformAdId` (numeric), or one of the creative's effective story/media IDs.
        UpdateAdStatusRequest updateAdStatusRequest = new UpdateAdStatusRequest(); // UpdateAdStatusRequest | 
        try {
            UpdateAdStatus200Response result = apiInstance.updateAdStatus(adId, updateAdStatusRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#updateAdStatus");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
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
| **updateAdStatusRequest** | [**UpdateAdStatusRequest**](UpdateAdStatusRequest.md)|  | |

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
| **401** | Unauthorized |  -  |
| **404** | Ad not found |  -  |

## updateAdStatusWithHttpInfo

> ApiResponse<UpdateAdStatus200Response> updateAdStatus updateAdStatusWithHttpInfo(adId, updateAdStatusRequest)

Pause or resume a single ad

Ad-scoped pause/resume — touches ONLY this ad, never its parent ad set or campaign (so sibling ads keep running). Thin wrapper over the &#x60;status&#x60; field of PUT /v1/ads/{adId}, for callers that want a URL symmetric to /v1/ads/campaigns/{campaignId}/status and /v1/ads/ad-sets/{adSetId}/status.  &#x60;{adId}&#x60; accepts the same identifier dialects as GET/PUT /v1/ads/{adId} (Zernio hex &#x60;_id&#x60;, Meta numeric &#x60;platformAdId&#x60;, or the creative&#39;s effective story/media IDs). &#x60;platform&#x60; is inferred from the ad, so it&#39;s not required in the body. Ads in terminal statuses (rejected, completed, cancelled) and no-op flips (already in the target state) are skipped. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String adId = "adId_example"; // String | Zernio `_id` (hex), Meta `platformAdId` (numeric), or one of the creative's effective story/media IDs.
        UpdateAdStatusRequest updateAdStatusRequest = new UpdateAdStatusRequest(); // UpdateAdStatusRequest | 
        try {
            ApiResponse<UpdateAdStatus200Response> response = apiInstance.updateAdStatusWithHttpInfo(adId, updateAdStatusRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#updateAdStatus");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
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
| **updateAdStatusRequest** | [**UpdateAdStatusRequest**](UpdateAdStatusRequest.md)|  | |

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
| **401** | Unauthorized |  -  |
| **404** | Ad not found |  -  |


## updateAdTrackingTags

> void updateAdTrackingTags(adId, updateAdTrackingTagsRequest)

Set ad tracking tags

Unified update. Send only the fields for the ad&#39;s platform: - Meta: &#x60;urlTags&#x60; (array of {key,value}). Meta creatives are immutable, so this rebuilds the   creative and repoints the ad. By DEFAULT we PRESERVE the existing creative verbatim   (re-post its object_story_spec + the new url_tags, reusing the image), so you send &#x60;urlTags&#x60;   ALONE — no need to read back headline/body/CTA. &#x60;creative&#x60; (headline, body, callToAction,   linkUrl, imageUrl) is OPTIONAL and only needed to rebuild explicitly, or for SHARE / page-post   / dark / asset_feed creatives whose object_story_spec Meta strips (those return 422 asking for   &#x60;creative&#x60;). - Google: &#x60;trackingUrlTemplate&#x60; and/or &#x60;finalUrlSuffix&#x60; (full template strings; account quota applies). - LinkedIn: &#x60;dynamicValueParameters&#x60; and/or &#x60;customValueParameters&#x60; (campaign-level Dynamic UTM). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String adId = "adId_example"; // String | 
        UpdateAdTrackingTagsRequest updateAdTrackingTagsRequest = new UpdateAdTrackingTagsRequest(); // UpdateAdTrackingTagsRequest | 
        try {
            apiInstance.updateAdTrackingTags(adId, updateAdTrackingTagsRequest);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#updateAdTrackingTags");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
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
| **updateAdTrackingTagsRequest** | [**UpdateAdTrackingTagsRequest**](UpdateAdTrackingTagsRequest.md)|  | |

### Return type


null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated |  -  |
| **401** | Unauthorized |  -  |
| **404** | Ad not found |  -  |
| **405** | Platform has no click-URL tracking surface |  -  |
| **422** | Meta creative cannot be rebuilt (e.g. placement-customized/asset-feed/dark creative) |  -  |

## updateAdTrackingTagsWithHttpInfo

> ApiResponse<Void> updateAdTrackingTags updateAdTrackingTagsWithHttpInfo(adId, updateAdTrackingTagsRequest)

Set ad tracking tags

Unified update. Send only the fields for the ad&#39;s platform: - Meta: &#x60;urlTags&#x60; (array of {key,value}). Meta creatives are immutable, so this rebuilds the   creative and repoints the ad. By DEFAULT we PRESERVE the existing creative verbatim   (re-post its object_story_spec + the new url_tags, reusing the image), so you send &#x60;urlTags&#x60;   ALONE — no need to read back headline/body/CTA. &#x60;creative&#x60; (headline, body, callToAction,   linkUrl, imageUrl) is OPTIONAL and only needed to rebuild explicitly, or for SHARE / page-post   / dark / asset_feed creatives whose object_story_spec Meta strips (those return 422 asking for   &#x60;creative&#x60;). - Google: &#x60;trackingUrlTemplate&#x60; and/or &#x60;finalUrlSuffix&#x60; (full template strings; account quota applies). - LinkedIn: &#x60;dynamicValueParameters&#x60; and/or &#x60;customValueParameters&#x60; (campaign-level Dynamic UTM). 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String adId = "adId_example"; // String | 
        UpdateAdTrackingTagsRequest updateAdTrackingTagsRequest = new UpdateAdTrackingTagsRequest(); // UpdateAdTrackingTagsRequest | 
        try {
            ApiResponse<Void> response = apiInstance.updateAdTrackingTagsWithHttpInfo(adId, updateAdTrackingTagsRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#updateAdTrackingTags");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
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
| **updateAdTrackingTagsRequest** | [**UpdateAdTrackingTagsRequest**](UpdateAdTrackingTagsRequest.md)|  | |

### Return type


ApiResponse<Void>

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated |  -  |
| **401** | Unauthorized |  -  |
| **404** | Ad not found |  -  |
| **405** | Platform has no click-URL tracking surface |  -  |
| **422** | Meta creative cannot be rebuilt (e.g. placement-customized/asset-feed/dark creative) |  -  |


## updateConversionDestination

> GetConversionDestination200Response updateConversionDestination(accountId, destinationId, updateConversionDestinationRequest)

Update a conversion destination

Partial-update a conversion rule. LinkedIn-only today. Whitelisted fields: &#x60;name&#x60;, &#x60;enabled&#x60;, attribution windows, &#x60;valueType&#x60;, &#x60;value&#x60;, &#x60;attributionType&#x60;. The rule&#39;s &#x60;type&#x60; and parent ad account are intentionally not exposed for update — recreate the rule if those need to change. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String destinationId = "destinationId_example"; // String | 
        UpdateConversionDestinationRequest updateConversionDestinationRequest = new UpdateConversionDestinationRequest(); // UpdateConversionDestinationRequest | 
        try {
            GetConversionDestination200Response result = apiInstance.updateConversionDestination(accountId, destinationId, updateConversionDestinationRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#updateConversionDestination");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**|  | |
| **destinationId** | **String**|  | |
| **updateConversionDestinationRequest** | [**UpdateConversionDestinationRequest**](UpdateConversionDestinationRequest.md)|  | |

### Return type

[**GetConversionDestination200Response**](GetConversionDestination200Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Destination updated (re-fetched canonical state) |  -  |
| **400** | Invalid body or LinkedIn validation failure. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on or LinkedIn reconnect required. |  -  |
| **404** | Account or destination not found. |  -  |
| **405** | Platform does not support updating destinations. |  -  |
| **429** | LinkedIn rate limit hit. Retry with backoff. |  -  |

## updateConversionDestinationWithHttpInfo

> ApiResponse<GetConversionDestination200Response> updateConversionDestination updateConversionDestinationWithHttpInfo(accountId, destinationId, updateConversionDestinationRequest)

Update a conversion destination

Partial-update a conversion rule. LinkedIn-only today. Whitelisted fields: &#x60;name&#x60;, &#x60;enabled&#x60;, attribution windows, &#x60;valueType&#x60;, &#x60;value&#x60;, &#x60;attributionType&#x60;. The rule&#39;s &#x60;type&#x60; and parent ad account are intentionally not exposed for update — recreate the rule if those need to change. 

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        String accountId = "accountId_example"; // String | 
        String destinationId = "destinationId_example"; // String | 
        UpdateConversionDestinationRequest updateConversionDestinationRequest = new UpdateConversionDestinationRequest(); // UpdateConversionDestinationRequest | 
        try {
            ApiResponse<GetConversionDestination200Response> response = apiInstance.updateConversionDestinationWithHttpInfo(accountId, destinationId, updateConversionDestinationRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#updateConversionDestination");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**|  | |
| **destinationId** | **String**|  | |
| **updateConversionDestinationRequest** | [**UpdateConversionDestinationRequest**](UpdateConversionDestinationRequest.md)|  | |

### Return type

ApiResponse<[**GetConversionDestination200Response**](GetConversionDestination200Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Destination updated (re-fetched canonical state) |  -  |
| **400** | Invalid body or LinkedIn validation failure. |  -  |
| **401** | Unauthorized |  -  |
| **403** | Ads add-on or LinkedIn reconnect required. |  -  |
| **404** | Account or destination not found. |  -  |
| **405** | Platform does not support updating destinations. |  -  |
| **429** | LinkedIn rate limit hit. Retry with backoff. |  -  |


## uploadAdImage

> UploadAdImage201Response uploadAdImage(uploadAdImageRequest)

Upload an ad image from base64 (Meta)

Uploads raw image bytes to the Meta ad account&#39;s image library — for callers whose creatives aren&#39;t hosted at a public URL. Returns the image &#x60;hash&#x60; (Meta&#39;s identifier for the asset) and the Meta-hosted &#x60;url&#x60;, which can be used directly as &#x60;imageUrl&#x60; on the create endpoints. Max 30 MB decoded. Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        UploadAdImageRequest uploadAdImageRequest = new UploadAdImageRequest(); // UploadAdImageRequest | 
        try {
            UploadAdImage201Response result = apiInstance.uploadAdImage(uploadAdImageRequest);
            System.out.println(result);
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#uploadAdImage");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Reason: " + e.getResponseBody());
            System.err.println("Response headers: " + e.getResponseHeaders());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **uploadAdImageRequest** | [**UploadAdImageRequest**](UploadAdImageRequest.md)|  | |

### Return type

[**UploadAdImage201Response**](UploadAdImage201Response.md)


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Image uploaded |  -  |
| **400** | Invalid input, or Meta rejected the image |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

## uploadAdImageWithHttpInfo

> ApiResponse<UploadAdImage201Response> uploadAdImage uploadAdImageWithHttpInfo(uploadAdImageRequest)

Upload an ad image from base64 (Meta)

Uploads raw image bytes to the Meta ad account&#39;s image library — for callers whose creatives aren&#39;t hosted at a public URL. Returns the image &#x60;hash&#x60; (Meta&#39;s identifier for the asset) and the Meta-hosted &#x60;url&#x60;, which can be used directly as &#x60;imageUrl&#x60; on the create endpoints. Max 30 MB decoded. Meta only.

### Example

```java
// Import classes:
import dev.zernio.ApiClient;
import dev.zernio.ApiException;
import dev.zernio.ApiResponse;
import dev.zernio.Configuration;
import dev.zernio.auth.*;
import dev.zernio.models.*;
import dev.zernio.api.AdsApi;

public class Example {
    public static void main(String[] args) {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath("https://zernio.com/api");
        
        // Configure HTTP bearer authorization: bearerAuth
        HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
        bearerAuth.setBearerToken("BEARER TOKEN");

        AdsApi apiInstance = new AdsApi(defaultClient);
        UploadAdImageRequest uploadAdImageRequest = new UploadAdImageRequest(); // UploadAdImageRequest | 
        try {
            ApiResponse<UploadAdImage201Response> response = apiInstance.uploadAdImageWithHttpInfo(uploadAdImageRequest);
            System.out.println("Status code: " + response.getStatusCode());
            System.out.println("Response headers: " + response.getHeaders());
            System.out.println("Response body: " + response.getData());
        } catch (ApiException e) {
            System.err.println("Exception when calling AdsApi#uploadAdImage");
            System.err.println("Status code: " + e.getCode());
            System.err.println("Response headers: " + e.getResponseHeaders());
            System.err.println("Reason: " + e.getResponseBody());
            e.printStackTrace();
        }
    }
}
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **uploadAdImageRequest** | [**UploadAdImageRequest**](UploadAdImageRequest.md)|  | |

### Return type

ApiResponse<[**UploadAdImage201Response**](UploadAdImage201Response.md)>


### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Image uploaded |  -  |
| **400** | Invalid input, or Meta rejected the image |  -  |
| **401** | Unauthorized |  -  |
| **501** | Only supported on Meta (facebook/instagram) |  -  |

