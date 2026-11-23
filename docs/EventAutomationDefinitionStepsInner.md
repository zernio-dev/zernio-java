

# EventAutomationDefinitionStepsInner

## oneOf schemas
* [AutomationEventActionStep](AutomationEventActionStep.md)
* [AutomationNotifyStep](AutomationNotifyStep.md)

## Example
```java
// Import classes:
import dev.zernio.model.EventAutomationDefinitionStepsInner;
import dev.zernio.model.AutomationEventActionStep;
import dev.zernio.model.AutomationNotifyStep;

public class Example {
    public static void main(String[] args) {
        EventAutomationDefinitionStepsInner exampleEventAutomationDefinitionStepsInner = new EventAutomationDefinitionStepsInner();

        // create a new AutomationEventActionStep
        AutomationEventActionStep exampleAutomationEventActionStep = new AutomationEventActionStep();
        // set EventAutomationDefinitionStepsInner to AutomationEventActionStep
        exampleEventAutomationDefinitionStepsInner.setActualInstance(exampleAutomationEventActionStep);
        // to get back the AutomationEventActionStep set earlier
        AutomationEventActionStep testAutomationEventActionStep = (AutomationEventActionStep) exampleEventAutomationDefinitionStepsInner.getActualInstance();

        // create a new AutomationNotifyStep
        AutomationNotifyStep exampleAutomationNotifyStep = new AutomationNotifyStep();
        // set EventAutomationDefinitionStepsInner to AutomationNotifyStep
        exampleEventAutomationDefinitionStepsInner.setActualInstance(exampleAutomationNotifyStep);
        // to get back the AutomationNotifyStep set earlier
        AutomationNotifyStep testAutomationNotifyStep = (AutomationNotifyStep) exampleEventAutomationDefinitionStepsInner.getActualInstance();
    }
}
```


