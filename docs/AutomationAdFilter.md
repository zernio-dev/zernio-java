

# AutomationAdFilter

Narrows the ad objects checked, before any metric is read. `GET /v1/automations/catalog` lists the fields each subject accepts. 

## oneOf schemas
* [AutomationAdFilterOneOf](AutomationAdFilterOneOf.md)
* [AutomationAdFilterOneOf1](AutomationAdFilterOneOf1.md)
* [AutomationAdFilterOneOf2](AutomationAdFilterOneOf2.md)
* [AutomationAdFilterOneOf3](AutomationAdFilterOneOf3.md)

## Example
```java
// Import classes:
import dev.zernio.model.AutomationAdFilter;
import dev.zernio.model.AutomationAdFilterOneOf;
import dev.zernio.model.AutomationAdFilterOneOf1;
import dev.zernio.model.AutomationAdFilterOneOf2;
import dev.zernio.model.AutomationAdFilterOneOf3;

public class Example {
    public static void main(String[] args) {
        AutomationAdFilter exampleAutomationAdFilter = new AutomationAdFilter();

        // create a new AutomationAdFilterOneOf
        AutomationAdFilterOneOf exampleAutomationAdFilterOneOf = new AutomationAdFilterOneOf();
        // set AutomationAdFilter to AutomationAdFilterOneOf
        exampleAutomationAdFilter.setActualInstance(exampleAutomationAdFilterOneOf);
        // to get back the AutomationAdFilterOneOf set earlier
        AutomationAdFilterOneOf testAutomationAdFilterOneOf = (AutomationAdFilterOneOf) exampleAutomationAdFilter.getActualInstance();

        // create a new AutomationAdFilterOneOf1
        AutomationAdFilterOneOf1 exampleAutomationAdFilterOneOf1 = new AutomationAdFilterOneOf1();
        // set AutomationAdFilter to AutomationAdFilterOneOf1
        exampleAutomationAdFilter.setActualInstance(exampleAutomationAdFilterOneOf1);
        // to get back the AutomationAdFilterOneOf1 set earlier
        AutomationAdFilterOneOf1 testAutomationAdFilterOneOf1 = (AutomationAdFilterOneOf1) exampleAutomationAdFilter.getActualInstance();

        // create a new AutomationAdFilterOneOf2
        AutomationAdFilterOneOf2 exampleAutomationAdFilterOneOf2 = new AutomationAdFilterOneOf2();
        // set AutomationAdFilter to AutomationAdFilterOneOf2
        exampleAutomationAdFilter.setActualInstance(exampleAutomationAdFilterOneOf2);
        // to get back the AutomationAdFilterOneOf2 set earlier
        AutomationAdFilterOneOf2 testAutomationAdFilterOneOf2 = (AutomationAdFilterOneOf2) exampleAutomationAdFilter.getActualInstance();

        // create a new AutomationAdFilterOneOf3
        AutomationAdFilterOneOf3 exampleAutomationAdFilterOneOf3 = new AutomationAdFilterOneOf3();
        // set AutomationAdFilter to AutomationAdFilterOneOf3
        exampleAutomationAdFilter.setActualInstance(exampleAutomationAdFilterOneOf3);
        // to get back the AutomationAdFilterOneOf3 set earlier
        AutomationAdFilterOneOf3 testAutomationAdFilterOneOf3 = (AutomationAdFilterOneOf3) exampleAutomationAdFilter.getActualInstance();
    }
}
```


