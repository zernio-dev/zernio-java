

# AdCreativeDescriptionsInner

## oneOf schemas
* [GoogleRsaDescription](GoogleRsaDescription.md)
* [String](String.md)

## Example
```java
// Import classes:
import dev.zernio.model.AdCreativeDescriptionsInner;
import dev.zernio.model.GoogleRsaDescription;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        AdCreativeDescriptionsInner exampleAdCreativeDescriptionsInner = new AdCreativeDescriptionsInner();

        // create a new GoogleRsaDescription
        GoogleRsaDescription exampleGoogleRsaDescription = new GoogleRsaDescription();
        // set AdCreativeDescriptionsInner to GoogleRsaDescription
        exampleAdCreativeDescriptionsInner.setActualInstance(exampleGoogleRsaDescription);
        // to get back the GoogleRsaDescription set earlier
        GoogleRsaDescription testGoogleRsaDescription = (GoogleRsaDescription) exampleAdCreativeDescriptionsInner.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set AdCreativeDescriptionsInner to String
        exampleAdCreativeDescriptionsInner.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleAdCreativeDescriptionsInner.getActualInstance();
    }
}
```


