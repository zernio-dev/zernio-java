

# UpdateCampaignTargetingRequestTargetingDevicesInner

## oneOf schemas
* [String](String.md)
* [UpdateCampaignTargetingRequestTargetingDevicesInnerOneOf](UpdateCampaignTargetingRequestTargetingDevicesInnerOneOf.md)

## Example
```java
// Import classes:
import dev.zernio.model.UpdateCampaignTargetingRequestTargetingDevicesInner;
import dev.zernio.model.String;
import dev.zernio.model.UpdateCampaignTargetingRequestTargetingDevicesInnerOneOf;

public class Example {
    public static void main(String[] args) {
        UpdateCampaignTargetingRequestTargetingDevicesInner exampleUpdateCampaignTargetingRequestTargetingDevicesInner = new UpdateCampaignTargetingRequestTargetingDevicesInner();

        // create a new String
        String exampleString = new String();
        // set UpdateCampaignTargetingRequestTargetingDevicesInner to String
        exampleUpdateCampaignTargetingRequestTargetingDevicesInner.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleUpdateCampaignTargetingRequestTargetingDevicesInner.getActualInstance();

        // create a new UpdateCampaignTargetingRequestTargetingDevicesInnerOneOf
        UpdateCampaignTargetingRequestTargetingDevicesInnerOneOf exampleUpdateCampaignTargetingRequestTargetingDevicesInnerOneOf = new UpdateCampaignTargetingRequestTargetingDevicesInnerOneOf();
        // set UpdateCampaignTargetingRequestTargetingDevicesInner to UpdateCampaignTargetingRequestTargetingDevicesInnerOneOf
        exampleUpdateCampaignTargetingRequestTargetingDevicesInner.setActualInstance(exampleUpdateCampaignTargetingRequestTargetingDevicesInnerOneOf);
        // to get back the UpdateCampaignTargetingRequestTargetingDevicesInnerOneOf set earlier
        UpdateCampaignTargetingRequestTargetingDevicesInnerOneOf testUpdateCampaignTargetingRequestTargetingDevicesInnerOneOf = (UpdateCampaignTargetingRequestTargetingDevicesInnerOneOf) exampleUpdateCampaignTargetingRequestTargetingDevicesInner.getActualInstance();
    }
}
```


