

# AppLovinAdsPlatformDataAssetsInner

## oneOf schemas
* [AppLovinAdsPlatformDataAssetsInnerOneOf](AppLovinAdsPlatformDataAssetsInnerOneOf.md)
* [WebhookPayloadCampaignSubmissionParticipant](WebhookPayloadCampaignSubmissionParticipant.md)

## Example
```java
// Import classes:
import dev.zernio.model.AppLovinAdsPlatformDataAssetsInner;
import dev.zernio.model.AppLovinAdsPlatformDataAssetsInnerOneOf;
import dev.zernio.model.WebhookPayloadCampaignSubmissionParticipant;

public class Example {
    public static void main(String[] args) {
        AppLovinAdsPlatformDataAssetsInner exampleAppLovinAdsPlatformDataAssetsInner = new AppLovinAdsPlatformDataAssetsInner();

        // create a new AppLovinAdsPlatformDataAssetsInnerOneOf
        AppLovinAdsPlatformDataAssetsInnerOneOf exampleAppLovinAdsPlatformDataAssetsInnerOneOf = new AppLovinAdsPlatformDataAssetsInnerOneOf();
        // set AppLovinAdsPlatformDataAssetsInner to AppLovinAdsPlatformDataAssetsInnerOneOf
        exampleAppLovinAdsPlatformDataAssetsInner.setActualInstance(exampleAppLovinAdsPlatformDataAssetsInnerOneOf);
        // to get back the AppLovinAdsPlatformDataAssetsInnerOneOf set earlier
        AppLovinAdsPlatformDataAssetsInnerOneOf testAppLovinAdsPlatformDataAssetsInnerOneOf = (AppLovinAdsPlatformDataAssetsInnerOneOf) exampleAppLovinAdsPlatformDataAssetsInner.getActualInstance();

        // create a new WebhookPayloadCampaignSubmissionParticipant
        WebhookPayloadCampaignSubmissionParticipant exampleWebhookPayloadCampaignSubmissionParticipant = new WebhookPayloadCampaignSubmissionParticipant();
        // set AppLovinAdsPlatformDataAssetsInner to WebhookPayloadCampaignSubmissionParticipant
        exampleAppLovinAdsPlatformDataAssetsInner.setActualInstance(exampleWebhookPayloadCampaignSubmissionParticipant);
        // to get back the WebhookPayloadCampaignSubmissionParticipant set earlier
        WebhookPayloadCampaignSubmissionParticipant testWebhookPayloadCampaignSubmissionParticipant = (WebhookPayloadCampaignSubmissionParticipant) exampleAppLovinAdsPlatformDataAssetsInner.getActualInstance();
    }
}
```


