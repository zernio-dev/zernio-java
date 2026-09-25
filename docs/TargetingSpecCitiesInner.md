

# TargetingSpecCitiesInner

## oneOf schemas
* [String](String.md)
* [TargetingSpecCitiesInnerOneOf](TargetingSpecCitiesInnerOneOf.md)

## Example
```java
// Import classes:
import dev.zernio.model.TargetingSpecCitiesInner;
import dev.zernio.model.String;
import dev.zernio.model.TargetingSpecCitiesInnerOneOf;

public class Example {
    public static void main(String[] args) {
        TargetingSpecCitiesInner exampleTargetingSpecCitiesInner = new TargetingSpecCitiesInner();

        // create a new String
        String exampleString = new String();
        // set TargetingSpecCitiesInner to String
        exampleTargetingSpecCitiesInner.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleTargetingSpecCitiesInner.getActualInstance();

        // create a new TargetingSpecCitiesInnerOneOf
        TargetingSpecCitiesInnerOneOf exampleTargetingSpecCitiesInnerOneOf = new TargetingSpecCitiesInnerOneOf();
        // set TargetingSpecCitiesInner to TargetingSpecCitiesInnerOneOf
        exampleTargetingSpecCitiesInner.setActualInstance(exampleTargetingSpecCitiesInnerOneOf);
        // to get back the TargetingSpecCitiesInnerOneOf set earlier
        TargetingSpecCitiesInnerOneOf testTargetingSpecCitiesInnerOneOf = (TargetingSpecCitiesInnerOneOf) exampleTargetingSpecCitiesInner.getActualInstance();
    }
}
```


