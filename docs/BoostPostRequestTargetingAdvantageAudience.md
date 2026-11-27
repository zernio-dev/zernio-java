

# BoostPostRequestTargetingAdvantageAudience

Meta only. 0 or false = disabled (default), 1 or true = enabled (booleans are sent to Meta as 1/0).

## oneOf schemas
* [Boolean](Boolean.md)
* [Integer](Integer.md)

## Example
```java
// Import classes:
import dev.zernio.model.BoostPostRequestTargetingAdvantageAudience;
import dev.zernio.model.Boolean;
import dev.zernio.model.Integer;

public class Example {
    public static void main(String[] args) {
        BoostPostRequestTargetingAdvantageAudience exampleBoostPostRequestTargetingAdvantageAudience = new BoostPostRequestTargetingAdvantageAudience();

        // create a new Boolean
        Boolean exampleBoolean = new Boolean();
        // set BoostPostRequestTargetingAdvantageAudience to Boolean
        exampleBoostPostRequestTargetingAdvantageAudience.setActualInstance(exampleBoolean);
        // to get back the Boolean set earlier
        Boolean testBoolean = (Boolean) exampleBoostPostRequestTargetingAdvantageAudience.getActualInstance();

        // create a new Integer
        Integer exampleInteger = new Integer();
        // set BoostPostRequestTargetingAdvantageAudience to Integer
        exampleBoostPostRequestTargetingAdvantageAudience.setActualInstance(exampleInteger);
        // to get back the Integer set earlier
        Integer testInteger = (Integer) exampleBoostPostRequestTargetingAdvantageAudience.getActualInstance();
    }
}
```


