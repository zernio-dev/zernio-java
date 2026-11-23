

# AutomationEventActionStep

A step of an event automation that acts on its own. `messages.send`, `contacts.tag` and `sequences.enroll` need an event about a conversation or a call: they act on that person.  `workflows.start` also takes an order event, reaching its customer by the phone the store holds. A step that does not fit its event is refused at its `type`.  Only `webhook.call` and `notify.send` run on `message.sent` and `message.failed`, which an automation's own messages fire. 

## oneOf schemas
* [AutomationEventActionStepOneOf](AutomationEventActionStepOneOf.md)
* [AutomationEventActionStepOneOf1](AutomationEventActionStepOneOf1.md)
* [AutomationEventActionStepOneOf2](AutomationEventActionStepOneOf2.md)
* [AutomationEventActionStepOneOf3](AutomationEventActionStepOneOf3.md)
* [AutomationEventActionStepOneOf4](AutomationEventActionStepOneOf4.md)

## Example
```java
// Import classes:
import dev.zernio.model.AutomationEventActionStep;
import dev.zernio.model.AutomationEventActionStepOneOf;
import dev.zernio.model.AutomationEventActionStepOneOf1;
import dev.zernio.model.AutomationEventActionStepOneOf2;
import dev.zernio.model.AutomationEventActionStepOneOf3;
import dev.zernio.model.AutomationEventActionStepOneOf4;

public class Example {
    public static void main(String[] args) {
        AutomationEventActionStep exampleAutomationEventActionStep = new AutomationEventActionStep();

        // create a new AutomationEventActionStepOneOf
        AutomationEventActionStepOneOf exampleAutomationEventActionStepOneOf = new AutomationEventActionStepOneOf();
        // set AutomationEventActionStep to AutomationEventActionStepOneOf
        exampleAutomationEventActionStep.setActualInstance(exampleAutomationEventActionStepOneOf);
        // to get back the AutomationEventActionStepOneOf set earlier
        AutomationEventActionStepOneOf testAutomationEventActionStepOneOf = (AutomationEventActionStepOneOf) exampleAutomationEventActionStep.getActualInstance();

        // create a new AutomationEventActionStepOneOf1
        AutomationEventActionStepOneOf1 exampleAutomationEventActionStepOneOf1 = new AutomationEventActionStepOneOf1();
        // set AutomationEventActionStep to AutomationEventActionStepOneOf1
        exampleAutomationEventActionStep.setActualInstance(exampleAutomationEventActionStepOneOf1);
        // to get back the AutomationEventActionStepOneOf1 set earlier
        AutomationEventActionStepOneOf1 testAutomationEventActionStepOneOf1 = (AutomationEventActionStepOneOf1) exampleAutomationEventActionStep.getActualInstance();

        // create a new AutomationEventActionStepOneOf2
        AutomationEventActionStepOneOf2 exampleAutomationEventActionStepOneOf2 = new AutomationEventActionStepOneOf2();
        // set AutomationEventActionStep to AutomationEventActionStepOneOf2
        exampleAutomationEventActionStep.setActualInstance(exampleAutomationEventActionStepOneOf2);
        // to get back the AutomationEventActionStepOneOf2 set earlier
        AutomationEventActionStepOneOf2 testAutomationEventActionStepOneOf2 = (AutomationEventActionStepOneOf2) exampleAutomationEventActionStep.getActualInstance();

        // create a new AutomationEventActionStepOneOf3
        AutomationEventActionStepOneOf3 exampleAutomationEventActionStepOneOf3 = new AutomationEventActionStepOneOf3();
        // set AutomationEventActionStep to AutomationEventActionStepOneOf3
        exampleAutomationEventActionStep.setActualInstance(exampleAutomationEventActionStepOneOf3);
        // to get back the AutomationEventActionStepOneOf3 set earlier
        AutomationEventActionStepOneOf3 testAutomationEventActionStepOneOf3 = (AutomationEventActionStepOneOf3) exampleAutomationEventActionStep.getActualInstance();

        // create a new AutomationEventActionStepOneOf4
        AutomationEventActionStepOneOf4 exampleAutomationEventActionStepOneOf4 = new AutomationEventActionStepOneOf4();
        // set AutomationEventActionStep to AutomationEventActionStepOneOf4
        exampleAutomationEventActionStep.setActualInstance(exampleAutomationEventActionStepOneOf4);
        // to get back the AutomationEventActionStepOneOf4 set earlier
        AutomationEventActionStepOneOf4 testAutomationEventActionStepOneOf4 = (AutomationEventActionStepOneOf4) exampleAutomationEventActionStep.getActualInstance();
    }
}
```


