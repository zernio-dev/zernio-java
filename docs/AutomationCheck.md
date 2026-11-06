

# AutomationCheck

One check, shaped by the automation's kind.

## oneOf schemas
* [AdRuleAutomationCheck](AdRuleAutomationCheck.md)
* [EventAutomationCheck](EventAutomationCheck.md)
* [ScheduledAutomationCheck](ScheduledAutomationCheck.md)

## Example
```java
// Import classes:
import dev.zernio.model.AutomationCheck;
import dev.zernio.model.AdRuleAutomationCheck;
import dev.zernio.model.EventAutomationCheck;
import dev.zernio.model.ScheduledAutomationCheck;

public class Example {
    public static void main(String[] args) {
        AutomationCheck exampleAutomationCheck = new AutomationCheck();

        // create a new AdRuleAutomationCheck
        AdRuleAutomationCheck exampleAdRuleAutomationCheck = new AdRuleAutomationCheck();
        // set AutomationCheck to AdRuleAutomationCheck
        exampleAutomationCheck.setActualInstance(exampleAdRuleAutomationCheck);
        // to get back the AdRuleAutomationCheck set earlier
        AdRuleAutomationCheck testAdRuleAutomationCheck = (AdRuleAutomationCheck) exampleAutomationCheck.getActualInstance();

        // create a new EventAutomationCheck
        EventAutomationCheck exampleEventAutomationCheck = new EventAutomationCheck();
        // set AutomationCheck to EventAutomationCheck
        exampleAutomationCheck.setActualInstance(exampleEventAutomationCheck);
        // to get back the EventAutomationCheck set earlier
        EventAutomationCheck testEventAutomationCheck = (EventAutomationCheck) exampleAutomationCheck.getActualInstance();

        // create a new ScheduledAutomationCheck
        ScheduledAutomationCheck exampleScheduledAutomationCheck = new ScheduledAutomationCheck();
        // set AutomationCheck to ScheduledAutomationCheck
        exampleAutomationCheck.setActualInstance(exampleScheduledAutomationCheck);
        // to get back the ScheduledAutomationCheck set earlier
        ScheduledAutomationCheck testScheduledAutomationCheck = (ScheduledAutomationCheck) exampleAutomationCheck.getActualInstance();
    }
}
```


