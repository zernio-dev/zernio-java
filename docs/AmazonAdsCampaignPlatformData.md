

# AmazonAdsCampaignPlatformData

Amazon Ads: the ad product of the campaign and its settings. Unknown keys return a 400.  The unified `goal` maps onto the product: Sponsored Products takes `conversions`; Sponsored Brands takes `traffic` (PAGE_VISIT), `awareness` (BRAND_IMPRESSION_SHARE), `video_views` (AD_VIEWS) and `conversions` (ACQUIRE_NEW_CUSTOMERS); Sponsored Display takes `traffic` (optimizes for clicks), `conversions` and `awareness` (optimizes for reach and bills by viewable impressions). 

## oneOf schemas
* [AmazonSponsoredBrandsCampaignData](AmazonSponsoredBrandsCampaignData.md)
* [AmazonSponsoredDisplayCampaignData](AmazonSponsoredDisplayCampaignData.md)
* [AmazonSponsoredProductsCampaignData](AmazonSponsoredProductsCampaignData.md)

## Example
```java
// Import classes:
import dev.zernio.model.AmazonAdsCampaignPlatformData;
import dev.zernio.model.AmazonSponsoredBrandsCampaignData;
import dev.zernio.model.AmazonSponsoredDisplayCampaignData;
import dev.zernio.model.AmazonSponsoredProductsCampaignData;

public class Example {
    public static void main(String[] args) {
        AmazonAdsCampaignPlatformData exampleAmazonAdsCampaignPlatformData = new AmazonAdsCampaignPlatformData();

        // create a new AmazonSponsoredBrandsCampaignData
        AmazonSponsoredBrandsCampaignData exampleAmazonSponsoredBrandsCampaignData = new AmazonSponsoredBrandsCampaignData();
        // set AmazonAdsCampaignPlatformData to AmazonSponsoredBrandsCampaignData
        exampleAmazonAdsCampaignPlatformData.setActualInstance(exampleAmazonSponsoredBrandsCampaignData);
        // to get back the AmazonSponsoredBrandsCampaignData set earlier
        AmazonSponsoredBrandsCampaignData testAmazonSponsoredBrandsCampaignData = (AmazonSponsoredBrandsCampaignData) exampleAmazonAdsCampaignPlatformData.getActualInstance();

        // create a new AmazonSponsoredDisplayCampaignData
        AmazonSponsoredDisplayCampaignData exampleAmazonSponsoredDisplayCampaignData = new AmazonSponsoredDisplayCampaignData();
        // set AmazonAdsCampaignPlatformData to AmazonSponsoredDisplayCampaignData
        exampleAmazonAdsCampaignPlatformData.setActualInstance(exampleAmazonSponsoredDisplayCampaignData);
        // to get back the AmazonSponsoredDisplayCampaignData set earlier
        AmazonSponsoredDisplayCampaignData testAmazonSponsoredDisplayCampaignData = (AmazonSponsoredDisplayCampaignData) exampleAmazonAdsCampaignPlatformData.getActualInstance();

        // create a new AmazonSponsoredProductsCampaignData
        AmazonSponsoredProductsCampaignData exampleAmazonSponsoredProductsCampaignData = new AmazonSponsoredProductsCampaignData();
        // set AmazonAdsCampaignPlatformData to AmazonSponsoredProductsCampaignData
        exampleAmazonAdsCampaignPlatformData.setActualInstance(exampleAmazonSponsoredProductsCampaignData);
        // to get back the AmazonSponsoredProductsCampaignData set earlier
        AmazonSponsoredProductsCampaignData testAmazonSponsoredProductsCampaignData = (AmazonSponsoredProductsCampaignData) exampleAmazonAdsCampaignPlatformData.getActualInstance();
    }
}
```


