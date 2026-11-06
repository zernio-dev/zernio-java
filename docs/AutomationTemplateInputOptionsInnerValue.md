

# AutomationTemplateInputOptionsInnerValue

## anyOf schemas
* [BigDecimal](BigDecimal.md)
* [String](String.md)

## Example
```java
// Import classes:
import dev.zernio.model.AutomationTemplateInputOptionsInnerValue;
import dev.zernio.model.BigDecimal;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        AutomationTemplateInputOptionsInnerValue exampleAutomationTemplateInputOptionsInnerValue = new AutomationTemplateInputOptionsInnerValue();

        // create a new BigDecimal
        BigDecimal exampleBigDecimal = new BigDecimal();
        // set AutomationTemplateInputOptionsInnerValue to BigDecimal
        exampleAutomationTemplateInputOptionsInnerValue.setActualInstance(exampleBigDecimal);
        // to get back the BigDecimal set earlier
        BigDecimal testBigDecimal = (BigDecimal) exampleAutomationTemplateInputOptionsInnerValue.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set AutomationTemplateInputOptionsInnerValue to String
        exampleAutomationTemplateInputOptionsInnerValue.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleAutomationTemplateInputOptionsInnerValue.getActualInstance();
    }
}
```


