

# AutomationTemplateInputDefault

Used when an install leaves the input out. An input with a default is never missing.

## anyOf schemas
* [BigDecimal](BigDecimal.md)
* [String](String.md)

## Example
```java
// Import classes:
import dev.zernio.model.AutomationTemplateInputDefault;
import dev.zernio.model.BigDecimal;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        AutomationTemplateInputDefault exampleAutomationTemplateInputDefault = new AutomationTemplateInputDefault();

        // create a new BigDecimal
        BigDecimal exampleBigDecimal = new BigDecimal();
        // set AutomationTemplateInputDefault to BigDecimal
        exampleAutomationTemplateInputDefault.setActualInstance(exampleBigDecimal);
        // to get back the BigDecimal set earlier
        BigDecimal testBigDecimal = (BigDecimal) exampleAutomationTemplateInputDefault.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set AutomationTemplateInputDefault to String
        exampleAutomationTemplateInputDefault.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleAutomationTemplateInputDefault.getActualInstance();
    }
}
```


