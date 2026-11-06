

# AutomationTrigger

When the automation runs. Its shape decides the kind:  - A Zernio event name in `type` makes an event automation. - A `schedule` over `subjects.each: post` makes a scheduled automation. - Any other `schedule` makes an ad rule. 

## oneOf schemas
* [AutomationEventTrigger](AutomationEventTrigger.md)
* [AutomationPostSchedule](AutomationPostSchedule.md)
* [AutomationScheduleTrigger](AutomationScheduleTrigger.md)

## Example
```java
// Import classes:
import dev.zernio.model.AutomationTrigger;
import dev.zernio.model.AutomationEventTrigger;
import dev.zernio.model.AutomationPostSchedule;
import dev.zernio.model.AutomationScheduleTrigger;

public class Example {
    public static void main(String[] args) {
        AutomationTrigger exampleAutomationTrigger = new AutomationTrigger();

        // create a new AutomationEventTrigger
        AutomationEventTrigger exampleAutomationEventTrigger = new AutomationEventTrigger();
        // set AutomationTrigger to AutomationEventTrigger
        exampleAutomationTrigger.setActualInstance(exampleAutomationEventTrigger);
        // to get back the AutomationEventTrigger set earlier
        AutomationEventTrigger testAutomationEventTrigger = (AutomationEventTrigger) exampleAutomationTrigger.getActualInstance();

        // create a new AutomationPostSchedule
        AutomationPostSchedule exampleAutomationPostSchedule = new AutomationPostSchedule();
        // set AutomationTrigger to AutomationPostSchedule
        exampleAutomationTrigger.setActualInstance(exampleAutomationPostSchedule);
        // to get back the AutomationPostSchedule set earlier
        AutomationPostSchedule testAutomationPostSchedule = (AutomationPostSchedule) exampleAutomationTrigger.getActualInstance();

        // create a new AutomationScheduleTrigger
        AutomationScheduleTrigger exampleAutomationScheduleTrigger = new AutomationScheduleTrigger();
        // set AutomationTrigger to AutomationScheduleTrigger
        exampleAutomationTrigger.setActualInstance(exampleAutomationScheduleTrigger);
        // to get back the AutomationScheduleTrigger set earlier
        AutomationScheduleTrigger testAutomationScheduleTrigger = (AutomationScheduleTrigger) exampleAutomationTrigger.getActualInstance();
    }
}
```


