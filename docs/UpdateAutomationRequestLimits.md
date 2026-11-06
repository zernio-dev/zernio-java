

# UpdateAutomationRequestLimits

## oneOf schemas
* [AutomationEventLimits](AutomationEventLimits.md)
* [AutomationLimits](AutomationLimits.md)

## Example
```java
// Import classes:
import dev.zernio.model.UpdateAutomationRequestLimits;
import dev.zernio.model.AutomationEventLimits;
import dev.zernio.model.AutomationLimits;

public class Example {
    public static void main(String[] args) {
        UpdateAutomationRequestLimits exampleUpdateAutomationRequestLimits = new UpdateAutomationRequestLimits();

        // create a new AutomationEventLimits
        AutomationEventLimits exampleAutomationEventLimits = new AutomationEventLimits();
        // set UpdateAutomationRequestLimits to AutomationEventLimits
        exampleUpdateAutomationRequestLimits.setActualInstance(exampleAutomationEventLimits);
        // to get back the AutomationEventLimits set earlier
        AutomationEventLimits testAutomationEventLimits = (AutomationEventLimits) exampleUpdateAutomationRequestLimits.getActualInstance();

        // create a new AutomationLimits
        AutomationLimits exampleAutomationLimits = new AutomationLimits();
        // set UpdateAutomationRequestLimits to AutomationLimits
        exampleUpdateAutomationRequestLimits.setActualInstance(exampleAutomationLimits);
        // to get back the AutomationLimits set earlier
        AutomationLimits testAutomationLimits = (AutomationLimits) exampleUpdateAutomationRequestLimits.getActualInstance();
    }
}
```


