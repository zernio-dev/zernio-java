

# CreateStandaloneAdRequestRegionsInner

## oneOf schemas
* [CreateStandaloneAdRequestRegionsInnerOneOf](CreateStandaloneAdRequestRegionsInnerOneOf.md)
* [String](String.md)

## Example
```java
// Import classes:
import dev.zernio.model.CreateStandaloneAdRequestRegionsInner;
import dev.zernio.model.CreateStandaloneAdRequestRegionsInnerOneOf;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        CreateStandaloneAdRequestRegionsInner exampleCreateStandaloneAdRequestRegionsInner = new CreateStandaloneAdRequestRegionsInner();

        // create a new CreateStandaloneAdRequestRegionsInnerOneOf
        CreateStandaloneAdRequestRegionsInnerOneOf exampleCreateStandaloneAdRequestRegionsInnerOneOf = new CreateStandaloneAdRequestRegionsInnerOneOf();
        // set CreateStandaloneAdRequestRegionsInner to CreateStandaloneAdRequestRegionsInnerOneOf
        exampleCreateStandaloneAdRequestRegionsInner.setActualInstance(exampleCreateStandaloneAdRequestRegionsInnerOneOf);
        // to get back the CreateStandaloneAdRequestRegionsInnerOneOf set earlier
        CreateStandaloneAdRequestRegionsInnerOneOf testCreateStandaloneAdRequestRegionsInnerOneOf = (CreateStandaloneAdRequestRegionsInnerOneOf) exampleCreateStandaloneAdRequestRegionsInner.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set CreateStandaloneAdRequestRegionsInner to String
        exampleCreateStandaloneAdRequestRegionsInner.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleCreateStandaloneAdRequestRegionsInner.getActualInstance();
    }
}
```


