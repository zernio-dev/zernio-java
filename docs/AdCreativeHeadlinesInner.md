

# AdCreativeHeadlinesInner

## oneOf schemas
* [GoogleRsaHeadline](GoogleRsaHeadline.md)
* [String](String.md)

## Example
```java
// Import classes:
import dev.zernio.model.AdCreativeHeadlinesInner;
import dev.zernio.model.GoogleRsaHeadline;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        AdCreativeHeadlinesInner exampleAdCreativeHeadlinesInner = new AdCreativeHeadlinesInner();

        // create a new GoogleRsaHeadline
        GoogleRsaHeadline exampleGoogleRsaHeadline = new GoogleRsaHeadline();
        // set AdCreativeHeadlinesInner to GoogleRsaHeadline
        exampleAdCreativeHeadlinesInner.setActualInstance(exampleGoogleRsaHeadline);
        // to get back the GoogleRsaHeadline set earlier
        GoogleRsaHeadline testGoogleRsaHeadline = (GoogleRsaHeadline) exampleAdCreativeHeadlinesInner.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set AdCreativeHeadlinesInner to String
        exampleAdCreativeHeadlinesInner.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleAdCreativeHeadlinesInner.getActualInstance();
    }
}
```


