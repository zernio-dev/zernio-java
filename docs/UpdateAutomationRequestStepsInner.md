

# UpdateAutomationRequestStepsInner

## oneOf schemas
* [AutomationBoostStep](AutomationBoostStep.md)
* [AutomationStep](AutomationStep.md)

## Example
```java
// Import classes:
import dev.zernio.model.UpdateAutomationRequestStepsInner;
import dev.zernio.model.AutomationBoostStep;
import dev.zernio.model.AutomationStep;

public class Example {
    public static void main(String[] args) {
        UpdateAutomationRequestStepsInner exampleUpdateAutomationRequestStepsInner = new UpdateAutomationRequestStepsInner();

        // create a new AutomationBoostStep
        AutomationBoostStep exampleAutomationBoostStep = new AutomationBoostStep();
        // set UpdateAutomationRequestStepsInner to AutomationBoostStep
        exampleUpdateAutomationRequestStepsInner.setActualInstance(exampleAutomationBoostStep);
        // to get back the AutomationBoostStep set earlier
        AutomationBoostStep testAutomationBoostStep = (AutomationBoostStep) exampleUpdateAutomationRequestStepsInner.getActualInstance();

        // create a new AutomationStep
        AutomationStep exampleAutomationStep = new AutomationStep();
        // set UpdateAutomationRequestStepsInner to AutomationStep
        exampleUpdateAutomationRequestStepsInner.setActualInstance(exampleAutomationStep);
        // to get back the AutomationStep set earlier
        AutomationStep testAutomationStep = (AutomationStep) exampleUpdateAutomationRequestStepsInner.getActualInstance();
    }
}
```


