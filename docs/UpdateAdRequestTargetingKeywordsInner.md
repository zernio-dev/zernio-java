

# UpdateAdRequestTargetingKeywordsInner

## oneOf schemas
* [String](String.md)
* [UpdateAdRequestTargetingKeywordsInnerOneOf](UpdateAdRequestTargetingKeywordsInnerOneOf.md)

## Example
```java
// Import classes:
import dev.zernio.model.UpdateAdRequestTargetingKeywordsInner;
import dev.zernio.model.String;
import dev.zernio.model.UpdateAdRequestTargetingKeywordsInnerOneOf;

public class Example {
    public static void main(String[] args) {
        UpdateAdRequestTargetingKeywordsInner exampleUpdateAdRequestTargetingKeywordsInner = new UpdateAdRequestTargetingKeywordsInner();

        // create a new String
        String exampleString = new String();
        // set UpdateAdRequestTargetingKeywordsInner to String
        exampleUpdateAdRequestTargetingKeywordsInner.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleUpdateAdRequestTargetingKeywordsInner.getActualInstance();

        // create a new UpdateAdRequestTargetingKeywordsInnerOneOf
        UpdateAdRequestTargetingKeywordsInnerOneOf exampleUpdateAdRequestTargetingKeywordsInnerOneOf = new UpdateAdRequestTargetingKeywordsInnerOneOf();
        // set UpdateAdRequestTargetingKeywordsInner to UpdateAdRequestTargetingKeywordsInnerOneOf
        exampleUpdateAdRequestTargetingKeywordsInner.setActualInstance(exampleUpdateAdRequestTargetingKeywordsInnerOneOf);
        // to get back the UpdateAdRequestTargetingKeywordsInnerOneOf set earlier
        UpdateAdRequestTargetingKeywordsInnerOneOf testUpdateAdRequestTargetingKeywordsInnerOneOf = (UpdateAdRequestTargetingKeywordsInnerOneOf) exampleUpdateAdRequestTargetingKeywordsInner.getActualInstance();
    }
}
```


