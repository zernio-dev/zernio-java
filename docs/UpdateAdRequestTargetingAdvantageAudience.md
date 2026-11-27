

# UpdateAdRequestTargetingAdvantageAudience

Meta only. Omit to preserve the existing setting on update. 0 or false = disabled, 1 or true = enabled (booleans are sent to Meta as 1/0). Also accepted as `advantageAudience`.

## oneOf schemas
* [Boolean](Boolean.md)
* [Integer](Integer.md)

## Example
```java
// Import classes:
import dev.zernio.model.UpdateAdRequestTargetingAdvantageAudience;
import dev.zernio.model.Boolean;
import dev.zernio.model.Integer;

public class Example {
    public static void main(String[] args) {
        UpdateAdRequestTargetingAdvantageAudience exampleUpdateAdRequestTargetingAdvantageAudience = new UpdateAdRequestTargetingAdvantageAudience();

        // create a new Boolean
        Boolean exampleBoolean = new Boolean();
        // set UpdateAdRequestTargetingAdvantageAudience to Boolean
        exampleUpdateAdRequestTargetingAdvantageAudience.setActualInstance(exampleBoolean);
        // to get back the Boolean set earlier
        Boolean testBoolean = (Boolean) exampleUpdateAdRequestTargetingAdvantageAudience.getActualInstance();

        // create a new Integer
        Integer exampleInteger = new Integer();
        // set UpdateAdRequestTargetingAdvantageAudience to Integer
        exampleUpdateAdRequestTargetingAdvantageAudience.setActualInstance(exampleInteger);
        // to get back the Integer set earlier
        Integer testInteger = (Integer) exampleUpdateAdRequestTargetingAdvantageAudience.getActualInstance();
    }
}
```


