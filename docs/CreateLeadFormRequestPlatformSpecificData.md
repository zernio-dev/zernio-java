

# CreateLeadFormRequestPlatformSpecificData

Form content; the shape is selected by the accountId's platform. Unknown fields are a 400 (strict-parsed).

## oneOf schemas
* [LinkedInLeadFormPlatformData](LinkedInLeadFormPlatformData.md)
* [MetaLeadFormPlatformData](MetaLeadFormPlatformData.md)

## Example
```java
// Import classes:
import dev.zernio.model.CreateLeadFormRequestPlatformSpecificData;
import dev.zernio.model.LinkedInLeadFormPlatformData;
import dev.zernio.model.MetaLeadFormPlatformData;

public class Example {
    public static void main(String[] args) {
        CreateLeadFormRequestPlatformSpecificData exampleCreateLeadFormRequestPlatformSpecificData = new CreateLeadFormRequestPlatformSpecificData();

        // create a new LinkedInLeadFormPlatformData
        LinkedInLeadFormPlatformData exampleLinkedInLeadFormPlatformData = new LinkedInLeadFormPlatformData();
        // set CreateLeadFormRequestPlatformSpecificData to LinkedInLeadFormPlatformData
        exampleCreateLeadFormRequestPlatformSpecificData.setActualInstance(exampleLinkedInLeadFormPlatformData);
        // to get back the LinkedInLeadFormPlatformData set earlier
        LinkedInLeadFormPlatformData testLinkedInLeadFormPlatformData = (LinkedInLeadFormPlatformData) exampleCreateLeadFormRequestPlatformSpecificData.getActualInstance();

        // create a new MetaLeadFormPlatformData
        MetaLeadFormPlatformData exampleMetaLeadFormPlatformData = new MetaLeadFormPlatformData();
        // set CreateLeadFormRequestPlatformSpecificData to MetaLeadFormPlatformData
        exampleCreateLeadFormRequestPlatformSpecificData.setActualInstance(exampleMetaLeadFormPlatformData);
        // to get back the MetaLeadFormPlatformData set earlier
        MetaLeadFormPlatformData testMetaLeadFormPlatformData = (MetaLeadFormPlatformData) exampleCreateLeadFormRequestPlatformSpecificData.getActualInstance();
    }
}
```


