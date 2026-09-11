

# CreateStandaloneAdRequestAdditionalHeadlinesInner

## oneOf schemas
* [GoogleRsaHeadline](GoogleRsaHeadline.md)
* [String](String.md)

## Example
```java
// Import classes:
import dev.zernio.model.CreateStandaloneAdRequestAdditionalHeadlinesInner;
import dev.zernio.model.GoogleRsaHeadline;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        CreateStandaloneAdRequestAdditionalHeadlinesInner exampleCreateStandaloneAdRequestAdditionalHeadlinesInner = new CreateStandaloneAdRequestAdditionalHeadlinesInner();

        // create a new GoogleRsaHeadline
        GoogleRsaHeadline exampleGoogleRsaHeadline = new GoogleRsaHeadline();
        // set CreateStandaloneAdRequestAdditionalHeadlinesInner to GoogleRsaHeadline
        exampleCreateStandaloneAdRequestAdditionalHeadlinesInner.setActualInstance(exampleGoogleRsaHeadline);
        // to get back the GoogleRsaHeadline set earlier
        GoogleRsaHeadline testGoogleRsaHeadline = (GoogleRsaHeadline) exampleCreateStandaloneAdRequestAdditionalHeadlinesInner.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set CreateStandaloneAdRequestAdditionalHeadlinesInner to String
        exampleCreateStandaloneAdRequestAdditionalHeadlinesInner.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleCreateStandaloneAdRequestAdditionalHeadlinesInner.getActualInstance();
    }
}
```


