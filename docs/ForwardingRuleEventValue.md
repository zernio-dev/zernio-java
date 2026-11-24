

# ForwardingRuleEventValue

How one event is valued. `original` sends its own value. `fixed` sends `amount` in `currency`, even when the event came without a value. `percent` sends `amount` percent of its own value (10 sends 10%, rounded to cents) in its own currency, and leaves an event without a value without one.

## oneOf schemas
* [Fixed](Fixed.md)
* [Original](Original.md)
* [Percent](Percent.md)

## Example
```java
// Import classes:
import dev.zernio.model.ForwardingRuleEventValue;
import dev.zernio.model.Fixed;
import dev.zernio.model.Original;
import dev.zernio.model.Percent;

public class Example {
    public static void main(String[] args) {
        ForwardingRuleEventValue exampleForwardingRuleEventValue = new ForwardingRuleEventValue();

        // create a new Fixed
        Fixed exampleFixed = new Fixed();
        // set ForwardingRuleEventValue to Fixed
        exampleForwardingRuleEventValue.setActualInstance(exampleFixed);
        // to get back the Fixed set earlier
        Fixed testFixed = (Fixed) exampleForwardingRuleEventValue.getActualInstance();

        // create a new Original
        Original exampleOriginal = new Original();
        // set ForwardingRuleEventValue to Original
        exampleForwardingRuleEventValue.setActualInstance(exampleOriginal);
        // to get back the Original set earlier
        Original testOriginal = (Original) exampleForwardingRuleEventValue.getActualInstance();

        // create a new Percent
        Percent examplePercent = new Percent();
        // set ForwardingRuleEventValue to Percent
        exampleForwardingRuleEventValue.setActualInstance(examplePercent);
        // to get back the Percent set earlier
        Percent testPercent = (Percent) exampleForwardingRuleEventValue.getActualInstance();
    }
}
```


