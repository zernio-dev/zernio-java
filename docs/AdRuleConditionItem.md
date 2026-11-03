

# AdRuleConditionItem

## oneOf schemas
* [AdRuleCondition](AdRuleCondition.md)
* [AdRuleConditions](AdRuleConditions.md)

## Example
```java
// Import classes:
import dev.zernio.model.AdRuleConditionItem;
import dev.zernio.model.AdRuleCondition;
import dev.zernio.model.AdRuleConditions;

public class Example {
    public static void main(String[] args) {
        AdRuleConditionItem exampleAdRuleConditionItem = new AdRuleConditionItem();

        // create a new AdRuleCondition
        AdRuleCondition exampleAdRuleCondition = new AdRuleCondition();
        // set AdRuleConditionItem to AdRuleCondition
        exampleAdRuleConditionItem.setActualInstance(exampleAdRuleCondition);
        // to get back the AdRuleCondition set earlier
        AdRuleCondition testAdRuleCondition = (AdRuleCondition) exampleAdRuleConditionItem.getActualInstance();

        // create a new AdRuleConditions
        AdRuleConditions exampleAdRuleConditions = new AdRuleConditions();
        // set AdRuleConditionItem to AdRuleConditions
        exampleAdRuleConditionItem.setActualInstance(exampleAdRuleConditions);
        // to get back the AdRuleConditions set earlier
        AdRuleConditions testAdRuleConditions = (AdRuleConditions) exampleAdRuleConditionItem.getActualInstance();
    }
}
```


