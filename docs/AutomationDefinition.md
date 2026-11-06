

# AutomationDefinition

An automation of one of three kinds, told apart by its shape:  - **Ad rule**: a `schedule` trigger over campaigns, ad sets or ads, with metric `conditions` and ad `steps`. - **Event**: a Zernio event in `trigger.type`, narrowed by `trigger.filter`, with notify steps. - **Scheduled**: a `schedule` trigger over `subjects.each: post`, narrowed by `filter`, with notify and boost steps. 

## oneOf schemas
* [AdRuleAutomationDefinition](AdRuleAutomationDefinition.md)
* [EventAutomationDefinition](EventAutomationDefinition.md)
* [ScheduledAutomationDefinition](ScheduledAutomationDefinition.md)

## Example
```java
// Import classes:
import dev.zernio.model.AutomationDefinition;
import dev.zernio.model.AdRuleAutomationDefinition;
import dev.zernio.model.EventAutomationDefinition;
import dev.zernio.model.ScheduledAutomationDefinition;

public class Example {
    public static void main(String[] args) {
        AutomationDefinition exampleAutomationDefinition = new AutomationDefinition();

        // create a new AdRuleAutomationDefinition
        AdRuleAutomationDefinition exampleAdRuleAutomationDefinition = new AdRuleAutomationDefinition();
        // set AutomationDefinition to AdRuleAutomationDefinition
        exampleAutomationDefinition.setActualInstance(exampleAdRuleAutomationDefinition);
        // to get back the AdRuleAutomationDefinition set earlier
        AdRuleAutomationDefinition testAdRuleAutomationDefinition = (AdRuleAutomationDefinition) exampleAutomationDefinition.getActualInstance();

        // create a new EventAutomationDefinition
        EventAutomationDefinition exampleEventAutomationDefinition = new EventAutomationDefinition();
        // set AutomationDefinition to EventAutomationDefinition
        exampleAutomationDefinition.setActualInstance(exampleEventAutomationDefinition);
        // to get back the EventAutomationDefinition set earlier
        EventAutomationDefinition testEventAutomationDefinition = (EventAutomationDefinition) exampleAutomationDefinition.getActualInstance();

        // create a new ScheduledAutomationDefinition
        ScheduledAutomationDefinition exampleScheduledAutomationDefinition = new ScheduledAutomationDefinition();
        // set AutomationDefinition to ScheduledAutomationDefinition
        exampleAutomationDefinition.setActualInstance(exampleScheduledAutomationDefinition);
        // to get back the ScheduledAutomationDefinition set earlier
        ScheduledAutomationDefinition testScheduledAutomationDefinition = (ScheduledAutomationDefinition) exampleAutomationDefinition.getActualInstance();
    }
}
```


