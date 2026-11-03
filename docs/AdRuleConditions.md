

# AdRuleConditions

A group: `all` (every item must hold) or `any` (one is enough). An item is a condition or another group, nested up to 3 levels, with at most 10 conditions in total. A rate with no denominator (a CPA with no conversions) never matches. 

## oneOf schemas
* [AdRuleConditionsOneOf](AdRuleConditionsOneOf.md)
* [AdRuleConditionsOneOf1](AdRuleConditionsOneOf1.md)

## Example
```java
// Import classes:
import dev.zernio.model.AdRuleConditions;
import dev.zernio.model.AdRuleConditionsOneOf;
import dev.zernio.model.AdRuleConditionsOneOf1;

public class Example {
    public static void main(String[] args) {
        AdRuleConditions exampleAdRuleConditions = new AdRuleConditions();

        // create a new AdRuleConditionsOneOf
        AdRuleConditionsOneOf exampleAdRuleConditionsOneOf = new AdRuleConditionsOneOf();
        // set AdRuleConditions to AdRuleConditionsOneOf
        exampleAdRuleConditions.setActualInstance(exampleAdRuleConditionsOneOf);
        // to get back the AdRuleConditionsOneOf set earlier
        AdRuleConditionsOneOf testAdRuleConditionsOneOf = (AdRuleConditionsOneOf) exampleAdRuleConditions.getActualInstance();

        // create a new AdRuleConditionsOneOf1
        AdRuleConditionsOneOf1 exampleAdRuleConditionsOneOf1 = new AdRuleConditionsOneOf1();
        // set AdRuleConditions to AdRuleConditionsOneOf1
        exampleAdRuleConditions.setActualInstance(exampleAdRuleConditionsOneOf1);
        // to get back the AdRuleConditionsOneOf1 set earlier
        AdRuleConditionsOneOf1 testAdRuleConditionsOneOf1 = (AdRuleConditionsOneOf1) exampleAdRuleConditions.getActualInstance();
    }
}
```


