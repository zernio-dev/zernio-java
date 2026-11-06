

# AutomationFactConditionOneOfValue

## anyOf schemas
* [BigDecimal](BigDecimal.md)
* [String](String.md)

## Example
```java
// Import classes:
import dev.zernio.model.AutomationFactConditionOneOfValue;
import dev.zernio.model.BigDecimal;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        AutomationFactConditionOneOfValue exampleAutomationFactConditionOneOfValue = new AutomationFactConditionOneOfValue();

        // create a new BigDecimal
        BigDecimal exampleBigDecimal = new BigDecimal();
        // set AutomationFactConditionOneOfValue to BigDecimal
        exampleAutomationFactConditionOneOfValue.setActualInstance(exampleBigDecimal);
        // to get back the BigDecimal set earlier
        BigDecimal testBigDecimal = (BigDecimal) exampleAutomationFactConditionOneOfValue.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set AutomationFactConditionOneOfValue to String
        exampleAutomationFactConditionOneOfValue.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleAutomationFactConditionOneOfValue.getActualInstance();
    }
}
```


