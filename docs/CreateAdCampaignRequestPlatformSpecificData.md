

# CreateAdCampaignRequestPlatformSpecificData

Amazon Ads (required there: the ad product and its campaign settings) and AppLovin (the campaign type, app or website, goal, bidding and tracking; its creative set fields do not apply here) only, 400 elsewhere.

## oneOf schemas
* [AmazonAdsCampaignPlatformData](AmazonAdsCampaignPlatformData.md)
* [AppLovinAdsPlatformData](AppLovinAdsPlatformData.md)

## Example
```java
// Import classes:
import dev.zernio.model.CreateAdCampaignRequestPlatformSpecificData;
import dev.zernio.model.AmazonAdsCampaignPlatformData;
import dev.zernio.model.AppLovinAdsPlatformData;

public class Example {
    public static void main(String[] args) {
        CreateAdCampaignRequestPlatformSpecificData exampleCreateAdCampaignRequestPlatformSpecificData = new CreateAdCampaignRequestPlatformSpecificData();

        // create a new AmazonAdsCampaignPlatformData
        AmazonAdsCampaignPlatformData exampleAmazonAdsCampaignPlatformData = new AmazonAdsCampaignPlatformData();
        // set CreateAdCampaignRequestPlatformSpecificData to AmazonAdsCampaignPlatformData
        exampleCreateAdCampaignRequestPlatformSpecificData.setActualInstance(exampleAmazonAdsCampaignPlatformData);
        // to get back the AmazonAdsCampaignPlatformData set earlier
        AmazonAdsCampaignPlatformData testAmazonAdsCampaignPlatformData = (AmazonAdsCampaignPlatformData) exampleCreateAdCampaignRequestPlatformSpecificData.getActualInstance();

        // create a new AppLovinAdsPlatformData
        AppLovinAdsPlatformData exampleAppLovinAdsPlatformData = new AppLovinAdsPlatformData();
        // set CreateAdCampaignRequestPlatformSpecificData to AppLovinAdsPlatformData
        exampleCreateAdCampaignRequestPlatformSpecificData.setActualInstance(exampleAppLovinAdsPlatformData);
        // to get back the AppLovinAdsPlatformData set earlier
        AppLovinAdsPlatformData testAppLovinAdsPlatformData = (AppLovinAdsPlatformData) exampleCreateAdCampaignRequestPlatformSpecificData.getActualInstance();
    }
}
```


