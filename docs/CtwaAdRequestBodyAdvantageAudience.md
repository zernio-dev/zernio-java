

# CtwaAdRequestBodyAdvantageAudience

Meta's Advantage+ audience expansion. `0` or `false` (default) keeps targeting strict; `1` or `true` lets Meta expand beyond the supplied targeting when its delivery system finds better matches. Booleans are sent to Meta as 1/0. Always sent on CREATE (Meta requires it). 

## oneOf schemas
* [Boolean](Boolean.md)
* [Integer](Integer.md)

## Example
```java
// Import classes:
import dev.zernio.model.CtwaAdRequestBodyAdvantageAudience;
import dev.zernio.model.Boolean;
import dev.zernio.model.Integer;

public class Example {
    public static void main(String[] args) {
        CtwaAdRequestBodyAdvantageAudience exampleCtwaAdRequestBodyAdvantageAudience = new CtwaAdRequestBodyAdvantageAudience();

        // create a new Boolean
        Boolean exampleBoolean = new Boolean();
        // set CtwaAdRequestBodyAdvantageAudience to Boolean
        exampleCtwaAdRequestBodyAdvantageAudience.setActualInstance(exampleBoolean);
        // to get back the Boolean set earlier
        Boolean testBoolean = (Boolean) exampleCtwaAdRequestBodyAdvantageAudience.getActualInstance();

        // create a new Integer
        Integer exampleInteger = new Integer();
        // set CtwaAdRequestBodyAdvantageAudience to Integer
        exampleCtwaAdRequestBodyAdvantageAudience.setActualInstance(exampleInteger);
        // to get back the Integer set earlier
        Integer testInteger = (Integer) exampleCtwaAdRequestBodyAdvantageAudience.getActualInstance();
    }
}
```


