

# AmazonAdsPlatformData

Amazon Ads (required): the ad product and everything the unified fields do not cover. Unknown keys return a 400.  Unified fields that apply:  - `name`, `campaignName`, `adSetName`, `adName`, `goal` and the status fields. - `budgetAmount` / `budgetType`: the campaign budget in whole currency units; lifetime on Sponsored Brands only. - `startDate` / `endDate`: calendar days in the profile time zone. - `keywords` and `negativeKeywords` (Sponsored Products and Brands), `campaignNegativeKeywords` (Sponsored Products). - `existingCampaignId`: a new ad group under an existing campaign of the same product, which keeps its goal when `goal` is omitted. - `adSetId`: new ads in an existing ad group.  Creative and audience fields (headline, body, linkUrl, imageUrl, countries, interests...) return a 400.  Goals per product are listed on `AmazonAdsCampaignPlatformData`. If anything after the campaign fails, the campaign is archived (Amazon's delete) and the error names the refused item, e.g. `keywords[2]`. 

## oneOf schemas
* [AmazonSponsoredBrandsAdData](AmazonSponsoredBrandsAdData.md)
* [AmazonSponsoredDisplayAdData](AmazonSponsoredDisplayAdData.md)
* [AmazonSponsoredProductsAdData](AmazonSponsoredProductsAdData.md)

## Example
```java
// Import classes:
import dev.zernio.model.AmazonAdsPlatformData;
import dev.zernio.model.AmazonSponsoredBrandsAdData;
import dev.zernio.model.AmazonSponsoredDisplayAdData;
import dev.zernio.model.AmazonSponsoredProductsAdData;

public class Example {
    public static void main(String[] args) {
        AmazonAdsPlatformData exampleAmazonAdsPlatformData = new AmazonAdsPlatformData();

        // create a new AmazonSponsoredBrandsAdData
        AmazonSponsoredBrandsAdData exampleAmazonSponsoredBrandsAdData = new AmazonSponsoredBrandsAdData();
        // set AmazonAdsPlatformData to AmazonSponsoredBrandsAdData
        exampleAmazonAdsPlatformData.setActualInstance(exampleAmazonSponsoredBrandsAdData);
        // to get back the AmazonSponsoredBrandsAdData set earlier
        AmazonSponsoredBrandsAdData testAmazonSponsoredBrandsAdData = (AmazonSponsoredBrandsAdData) exampleAmazonAdsPlatformData.getActualInstance();

        // create a new AmazonSponsoredDisplayAdData
        AmazonSponsoredDisplayAdData exampleAmazonSponsoredDisplayAdData = new AmazonSponsoredDisplayAdData();
        // set AmazonAdsPlatformData to AmazonSponsoredDisplayAdData
        exampleAmazonAdsPlatformData.setActualInstance(exampleAmazonSponsoredDisplayAdData);
        // to get back the AmazonSponsoredDisplayAdData set earlier
        AmazonSponsoredDisplayAdData testAmazonSponsoredDisplayAdData = (AmazonSponsoredDisplayAdData) exampleAmazonAdsPlatformData.getActualInstance();

        // create a new AmazonSponsoredProductsAdData
        AmazonSponsoredProductsAdData exampleAmazonSponsoredProductsAdData = new AmazonSponsoredProductsAdData();
        // set AmazonAdsPlatformData to AmazonSponsoredProductsAdData
        exampleAmazonAdsPlatformData.setActualInstance(exampleAmazonSponsoredProductsAdData);
        // to get back the AmazonSponsoredProductsAdData set earlier
        AmazonSponsoredProductsAdData testAmazonSponsoredProductsAdData = (AmazonSponsoredProductsAdData) exampleAmazonAdsPlatformData.getActualInstance();
    }
}
```


