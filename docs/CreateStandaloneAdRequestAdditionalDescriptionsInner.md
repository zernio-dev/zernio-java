

# CreateStandaloneAdRequestAdditionalDescriptionsInner

## oneOf schemas
* [GoogleRsaDescription](GoogleRsaDescription.md)
* [String](String.md)

## Example
```java
// Import classes:
import dev.zernio.model.CreateStandaloneAdRequestAdditionalDescriptionsInner;
import dev.zernio.model.GoogleRsaDescription;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        CreateStandaloneAdRequestAdditionalDescriptionsInner exampleCreateStandaloneAdRequestAdditionalDescriptionsInner = new CreateStandaloneAdRequestAdditionalDescriptionsInner();

        // create a new GoogleRsaDescription
        GoogleRsaDescription exampleGoogleRsaDescription = new GoogleRsaDescription();
        // set CreateStandaloneAdRequestAdditionalDescriptionsInner to GoogleRsaDescription
        exampleCreateStandaloneAdRequestAdditionalDescriptionsInner.setActualInstance(exampleGoogleRsaDescription);
        // to get back the GoogleRsaDescription set earlier
        GoogleRsaDescription testGoogleRsaDescription = (GoogleRsaDescription) exampleCreateStandaloneAdRequestAdditionalDescriptionsInner.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set CreateStandaloneAdRequestAdditionalDescriptionsInner to String
        exampleCreateStandaloneAdRequestAdditionalDescriptionsInner.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleCreateStandaloneAdRequestAdditionalDescriptionsInner.getActualInstance();
    }
}
```


