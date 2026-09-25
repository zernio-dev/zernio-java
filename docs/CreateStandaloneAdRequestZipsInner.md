

# CreateStandaloneAdRequestZipsInner

## oneOf schemas
* [BoostPostRequestTargetingRegionsInner](BoostPostRequestTargetingRegionsInner.md)
* [String](String.md)

## Example
```java
// Import classes:
import dev.zernio.model.CreateStandaloneAdRequestZipsInner;
import dev.zernio.model.BoostPostRequestTargetingRegionsInner;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        CreateStandaloneAdRequestZipsInner exampleCreateStandaloneAdRequestZipsInner = new CreateStandaloneAdRequestZipsInner();

        // create a new BoostPostRequestTargetingRegionsInner
        BoostPostRequestTargetingRegionsInner exampleBoostPostRequestTargetingRegionsInner = new BoostPostRequestTargetingRegionsInner();
        // set CreateStandaloneAdRequestZipsInner to BoostPostRequestTargetingRegionsInner
        exampleCreateStandaloneAdRequestZipsInner.setActualInstance(exampleBoostPostRequestTargetingRegionsInner);
        // to get back the BoostPostRequestTargetingRegionsInner set earlier
        BoostPostRequestTargetingRegionsInner testBoostPostRequestTargetingRegionsInner = (BoostPostRequestTargetingRegionsInner) exampleCreateStandaloneAdRequestZipsInner.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set CreateStandaloneAdRequestZipsInner to String
        exampleCreateStandaloneAdRequestZipsInner.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleCreateStandaloneAdRequestZipsInner.getActualInstance();
    }
}
```


