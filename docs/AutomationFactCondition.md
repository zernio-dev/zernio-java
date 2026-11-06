

# AutomationFactCondition

Narrows by the facts of the event or post, such as `platform` or `likes`: one comparison, or a group where `all` must hold or `any` is enough. Groups nest.  A leaf whose `field` is not a fact of the event or post is refused. Text compares ignoring case. A number or date that does not parse never matches. 

## oneOf schemas
* [AutomationFactConditionOneOf](AutomationFactConditionOneOf.md)
* [AutomationFactConditionOneOf1](AutomationFactConditionOneOf1.md)
* [AutomationFactConditionOneOf2](AutomationFactConditionOneOf2.md)

## Example
```java
// Import classes:
import dev.zernio.model.AutomationFactCondition;
import dev.zernio.model.AutomationFactConditionOneOf;
import dev.zernio.model.AutomationFactConditionOneOf1;
import dev.zernio.model.AutomationFactConditionOneOf2;

public class Example {
    public static void main(String[] args) {
        AutomationFactCondition exampleAutomationFactCondition = new AutomationFactCondition();

        // create a new AutomationFactConditionOneOf
        AutomationFactConditionOneOf exampleAutomationFactConditionOneOf = new AutomationFactConditionOneOf();
        // set AutomationFactCondition to AutomationFactConditionOneOf
        exampleAutomationFactCondition.setActualInstance(exampleAutomationFactConditionOneOf);
        // to get back the AutomationFactConditionOneOf set earlier
        AutomationFactConditionOneOf testAutomationFactConditionOneOf = (AutomationFactConditionOneOf) exampleAutomationFactCondition.getActualInstance();

        // create a new AutomationFactConditionOneOf1
        AutomationFactConditionOneOf1 exampleAutomationFactConditionOneOf1 = new AutomationFactConditionOneOf1();
        // set AutomationFactCondition to AutomationFactConditionOneOf1
        exampleAutomationFactCondition.setActualInstance(exampleAutomationFactConditionOneOf1);
        // to get back the AutomationFactConditionOneOf1 set earlier
        AutomationFactConditionOneOf1 testAutomationFactConditionOneOf1 = (AutomationFactConditionOneOf1) exampleAutomationFactCondition.getActualInstance();

        // create a new AutomationFactConditionOneOf2
        AutomationFactConditionOneOf2 exampleAutomationFactConditionOneOf2 = new AutomationFactConditionOneOf2();
        // set AutomationFactCondition to AutomationFactConditionOneOf2
        exampleAutomationFactCondition.setActualInstance(exampleAutomationFactConditionOneOf2);
        // to get back the AutomationFactConditionOneOf2 set earlier
        AutomationFactConditionOneOf2 testAutomationFactConditionOneOf2 = (AutomationFactConditionOneOf2) exampleAutomationFactCondition.getActualInstance();
    }
}
```


