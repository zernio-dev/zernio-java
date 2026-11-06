

# ScheduledAutomationDefinitionStepsInner

## oneOf schemas
* [AutomationBoostStep](AutomationBoostStep.md)
* [AutomationNotifyStep](AutomationNotifyStep.md)

## Example
```java
// Import classes:
import dev.zernio.model.ScheduledAutomationDefinitionStepsInner;
import dev.zernio.model.AutomationBoostStep;
import dev.zernio.model.AutomationNotifyStep;

public class Example {
    public static void main(String[] args) {
        ScheduledAutomationDefinitionStepsInner exampleScheduledAutomationDefinitionStepsInner = new ScheduledAutomationDefinitionStepsInner();

        // create a new AutomationBoostStep
        AutomationBoostStep exampleAutomationBoostStep = new AutomationBoostStep();
        // set ScheduledAutomationDefinitionStepsInner to AutomationBoostStep
        exampleScheduledAutomationDefinitionStepsInner.setActualInstance(exampleAutomationBoostStep);
        // to get back the AutomationBoostStep set earlier
        AutomationBoostStep testAutomationBoostStep = (AutomationBoostStep) exampleScheduledAutomationDefinitionStepsInner.getActualInstance();

        // create a new AutomationNotifyStep
        AutomationNotifyStep exampleAutomationNotifyStep = new AutomationNotifyStep();
        // set ScheduledAutomationDefinitionStepsInner to AutomationNotifyStep
        exampleScheduledAutomationDefinitionStepsInner.setActualInstance(exampleAutomationNotifyStep);
        // to get back the AutomationNotifyStep set earlier
        AutomationNotifyStep testAutomationNotifyStep = (AutomationNotifyStep) exampleScheduledAutomationDefinitionStepsInner.getActualInstance();
    }
}
```


