

# CreateStandaloneAdRequestAdvantageAudience

Meta only. Controls the Advantage audience feature (targeting_automation). 0 or false = disabled (default), 1 or true = enabled (booleans are sent to Meta as 1/0). Meta Marketing API requires this field on all ad set creation requests.

## oneOf schemas
* [Boolean](Boolean.md)
* [Integer](Integer.md)

## Example
```java
// Import classes:
import dev.zernio.model.CreateStandaloneAdRequestAdvantageAudience;
import dev.zernio.model.Boolean;
import dev.zernio.model.Integer;

public class Example {
    public static void main(String[] args) {
        CreateStandaloneAdRequestAdvantageAudience exampleCreateStandaloneAdRequestAdvantageAudience = new CreateStandaloneAdRequestAdvantageAudience();

        // create a new Boolean
        Boolean exampleBoolean = new Boolean();
        // set CreateStandaloneAdRequestAdvantageAudience to Boolean
        exampleCreateStandaloneAdRequestAdvantageAudience.setActualInstance(exampleBoolean);
        // to get back the Boolean set earlier
        Boolean testBoolean = (Boolean) exampleCreateStandaloneAdRequestAdvantageAudience.getActualInstance();

        // create a new Integer
        Integer exampleInteger = new Integer();
        // set CreateStandaloneAdRequestAdvantageAudience to Integer
        exampleCreateStandaloneAdRequestAdvantageAudience.setActualInstance(exampleInteger);
        // to get back the Integer set earlier
        Integer testInteger = (Integer) exampleCreateStandaloneAdRequestAdvantageAudience.getActualInstance();
    }
}
```


