

# Automation

## oneOf schemas
* [AutomationOneOf](AutomationOneOf.md)
* [AutomationOneOf1](AutomationOneOf1.md)
* [AutomationOneOf2](AutomationOneOf2.md)

## Example
```java
// Import classes:
import dev.zernio.model.Automation;
import dev.zernio.model.AutomationOneOf;
import dev.zernio.model.AutomationOneOf1;
import dev.zernio.model.AutomationOneOf2;

public class Example {
    public static void main(String[] args) {
        Automation exampleAutomation = new Automation();

        // create a new AutomationOneOf
        AutomationOneOf exampleAutomationOneOf = new AutomationOneOf();
        // set Automation to AutomationOneOf
        exampleAutomation.setActualInstance(exampleAutomationOneOf);
        // to get back the AutomationOneOf set earlier
        AutomationOneOf testAutomationOneOf = (AutomationOneOf) exampleAutomation.getActualInstance();

        // create a new AutomationOneOf1
        AutomationOneOf1 exampleAutomationOneOf1 = new AutomationOneOf1();
        // set Automation to AutomationOneOf1
        exampleAutomation.setActualInstance(exampleAutomationOneOf1);
        // to get back the AutomationOneOf1 set earlier
        AutomationOneOf1 testAutomationOneOf1 = (AutomationOneOf1) exampleAutomation.getActualInstance();

        // create a new AutomationOneOf2
        AutomationOneOf2 exampleAutomationOneOf2 = new AutomationOneOf2();
        // set Automation to AutomationOneOf2
        exampleAutomation.setActualInstance(exampleAutomationOneOf2);
        // to get back the AutomationOneOf2 set earlier
        AutomationOneOf2 testAutomationOneOf2 = (AutomationOneOf2) exampleAutomation.getActualInstance();
    }
}
```


