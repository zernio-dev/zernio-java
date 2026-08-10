

# CreateStandaloneAdRequestPlatformSpecificData

Platform-specific options. The platform is derived from `accountId`; sending options for a different platform returns a 400. LinkedIn (campaign bidding and delivery controls) and Meta (the bid trio) have options today.  **Meta**: `bidStrategy`, `bidAmount` and `roasAverageFloor` may be sent here instead of at the root — the preferred home going forward. Sending the bid fields in BOTH places returns a 400 (`mutually_exclusive_fields`), and sending any of them in `adSetId` attach mode is a 400 too (the ad set already has its bid). 

## oneOf schemas
* [LinkedInAdsPlatformData](LinkedInAdsPlatformData.md)
* [MetaAdsPlatformData](MetaAdsPlatformData.md)

## Example
```java
// Import classes:
import dev.zernio.model.CreateStandaloneAdRequestPlatformSpecificData;
import dev.zernio.model.LinkedInAdsPlatformData;
import dev.zernio.model.MetaAdsPlatformData;

public class Example {
    public static void main(String[] args) {
        CreateStandaloneAdRequestPlatformSpecificData exampleCreateStandaloneAdRequestPlatformSpecificData = new CreateStandaloneAdRequestPlatformSpecificData();

        // create a new LinkedInAdsPlatformData
        LinkedInAdsPlatformData exampleLinkedInAdsPlatformData = new LinkedInAdsPlatformData();
        // set CreateStandaloneAdRequestPlatformSpecificData to LinkedInAdsPlatformData
        exampleCreateStandaloneAdRequestPlatformSpecificData.setActualInstance(exampleLinkedInAdsPlatformData);
        // to get back the LinkedInAdsPlatformData set earlier
        LinkedInAdsPlatformData testLinkedInAdsPlatformData = (LinkedInAdsPlatformData) exampleCreateStandaloneAdRequestPlatformSpecificData.getActualInstance();

        // create a new MetaAdsPlatformData
        MetaAdsPlatformData exampleMetaAdsPlatformData = new MetaAdsPlatformData();
        // set CreateStandaloneAdRequestPlatformSpecificData to MetaAdsPlatformData
        exampleCreateStandaloneAdRequestPlatformSpecificData.setActualInstance(exampleMetaAdsPlatformData);
        // to get back the MetaAdsPlatformData set earlier
        MetaAdsPlatformData testMetaAdsPlatformData = (MetaAdsPlatformData) exampleCreateStandaloneAdRequestPlatformSpecificData.getActualInstance();
    }
}
```


