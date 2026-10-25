

# AdRuleAction

## oneOf schemas
* [AdRuleActionOneOf](AdRuleActionOneOf.md)
* [AdRuleActionOneOf1](AdRuleActionOneOf1.md)
* [AdRuleActionOneOf2](AdRuleActionOneOf2.md)
* [AdRuleActionOneOf3](AdRuleActionOneOf3.md)

## Example
```java
// Import classes:
import dev.zernio.model.AdRuleAction;
import dev.zernio.model.AdRuleActionOneOf;
import dev.zernio.model.AdRuleActionOneOf1;
import dev.zernio.model.AdRuleActionOneOf2;
import dev.zernio.model.AdRuleActionOneOf3;

public class Example {
    public static void main(String[] args) {
        AdRuleAction exampleAdRuleAction = new AdRuleAction();

        // create a new AdRuleActionOneOf
        AdRuleActionOneOf exampleAdRuleActionOneOf = new AdRuleActionOneOf();
        // set AdRuleAction to AdRuleActionOneOf
        exampleAdRuleAction.setActualInstance(exampleAdRuleActionOneOf);
        // to get back the AdRuleActionOneOf set earlier
        AdRuleActionOneOf testAdRuleActionOneOf = (AdRuleActionOneOf) exampleAdRuleAction.getActualInstance();

        // create a new AdRuleActionOneOf1
        AdRuleActionOneOf1 exampleAdRuleActionOneOf1 = new AdRuleActionOneOf1();
        // set AdRuleAction to AdRuleActionOneOf1
        exampleAdRuleAction.setActualInstance(exampleAdRuleActionOneOf1);
        // to get back the AdRuleActionOneOf1 set earlier
        AdRuleActionOneOf1 testAdRuleActionOneOf1 = (AdRuleActionOneOf1) exampleAdRuleAction.getActualInstance();

        // create a new AdRuleActionOneOf2
        AdRuleActionOneOf2 exampleAdRuleActionOneOf2 = new AdRuleActionOneOf2();
        // set AdRuleAction to AdRuleActionOneOf2
        exampleAdRuleAction.setActualInstance(exampleAdRuleActionOneOf2);
        // to get back the AdRuleActionOneOf2 set earlier
        AdRuleActionOneOf2 testAdRuleActionOneOf2 = (AdRuleActionOneOf2) exampleAdRuleAction.getActualInstance();

        // create a new AdRuleActionOneOf3
        AdRuleActionOneOf3 exampleAdRuleActionOneOf3 = new AdRuleActionOneOf3();
        // set AdRuleAction to AdRuleActionOneOf3
        exampleAdRuleAction.setActualInstance(exampleAdRuleActionOneOf3);
        // to get back the AdRuleActionOneOf3 set earlier
        AdRuleActionOneOf3 testAdRuleActionOneOf3 = (AdRuleActionOneOf3) exampleAdRuleAction.getActualInstance();
    }
}
```


