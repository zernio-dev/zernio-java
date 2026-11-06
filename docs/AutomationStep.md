

# AutomationStep

One thing an ad rule does for each matching object, in order. An ad rule takes at most one `ads.*` change, can ask for approval before it and notify after it.  `id` is fixed by the step type; leave it out when writing. `GET /v1/automations/catalog` lists the platforms and subjects each step works on. 

## oneOf schemas
* [AutomationApprovalStep](AutomationApprovalStep.md)
* [AutomationNotifyStep](AutomationNotifyStep.md)
* [AutomationStepOneOf](AutomationStepOneOf.md)
* [AutomationStepOneOf1](AutomationStepOneOf1.md)
* [AutomationStepOneOf10](AutomationStepOneOf10.md)
* [AutomationStepOneOf2](AutomationStepOneOf2.md)
* [AutomationStepOneOf3](AutomationStepOneOf3.md)
* [AutomationStepOneOf4](AutomationStepOneOf4.md)
* [AutomationStepOneOf5](AutomationStepOneOf5.md)
* [AutomationStepOneOf6](AutomationStepOneOf6.md)
* [AutomationStepOneOf7](AutomationStepOneOf7.md)
* [AutomationStepOneOf8](AutomationStepOneOf8.md)
* [AutomationStepOneOf9](AutomationStepOneOf9.md)

## Example
```java
// Import classes:
import dev.zernio.model.AutomationStep;
import dev.zernio.model.AutomationApprovalStep;
import dev.zernio.model.AutomationNotifyStep;
import dev.zernio.model.AutomationStepOneOf;
import dev.zernio.model.AutomationStepOneOf1;
import dev.zernio.model.AutomationStepOneOf10;
import dev.zernio.model.AutomationStepOneOf2;
import dev.zernio.model.AutomationStepOneOf3;
import dev.zernio.model.AutomationStepOneOf4;
import dev.zernio.model.AutomationStepOneOf5;
import dev.zernio.model.AutomationStepOneOf6;
import dev.zernio.model.AutomationStepOneOf7;
import dev.zernio.model.AutomationStepOneOf8;
import dev.zernio.model.AutomationStepOneOf9;

public class Example {
    public static void main(String[] args) {
        AutomationStep exampleAutomationStep = new AutomationStep();

        // create a new AutomationApprovalStep
        AutomationApprovalStep exampleAutomationApprovalStep = new AutomationApprovalStep();
        // set AutomationStep to AutomationApprovalStep
        exampleAutomationStep.setActualInstance(exampleAutomationApprovalStep);
        // to get back the AutomationApprovalStep set earlier
        AutomationApprovalStep testAutomationApprovalStep = (AutomationApprovalStep) exampleAutomationStep.getActualInstance();

        // create a new AutomationNotifyStep
        AutomationNotifyStep exampleAutomationNotifyStep = new AutomationNotifyStep();
        // set AutomationStep to AutomationNotifyStep
        exampleAutomationStep.setActualInstance(exampleAutomationNotifyStep);
        // to get back the AutomationNotifyStep set earlier
        AutomationNotifyStep testAutomationNotifyStep = (AutomationNotifyStep) exampleAutomationStep.getActualInstance();

        // create a new AutomationStepOneOf
        AutomationStepOneOf exampleAutomationStepOneOf = new AutomationStepOneOf();
        // set AutomationStep to AutomationStepOneOf
        exampleAutomationStep.setActualInstance(exampleAutomationStepOneOf);
        // to get back the AutomationStepOneOf set earlier
        AutomationStepOneOf testAutomationStepOneOf = (AutomationStepOneOf) exampleAutomationStep.getActualInstance();

        // create a new AutomationStepOneOf1
        AutomationStepOneOf1 exampleAutomationStepOneOf1 = new AutomationStepOneOf1();
        // set AutomationStep to AutomationStepOneOf1
        exampleAutomationStep.setActualInstance(exampleAutomationStepOneOf1);
        // to get back the AutomationStepOneOf1 set earlier
        AutomationStepOneOf1 testAutomationStepOneOf1 = (AutomationStepOneOf1) exampleAutomationStep.getActualInstance();

        // create a new AutomationStepOneOf10
        AutomationStepOneOf10 exampleAutomationStepOneOf10 = new AutomationStepOneOf10();
        // set AutomationStep to AutomationStepOneOf10
        exampleAutomationStep.setActualInstance(exampleAutomationStepOneOf10);
        // to get back the AutomationStepOneOf10 set earlier
        AutomationStepOneOf10 testAutomationStepOneOf10 = (AutomationStepOneOf10) exampleAutomationStep.getActualInstance();

        // create a new AutomationStepOneOf2
        AutomationStepOneOf2 exampleAutomationStepOneOf2 = new AutomationStepOneOf2();
        // set AutomationStep to AutomationStepOneOf2
        exampleAutomationStep.setActualInstance(exampleAutomationStepOneOf2);
        // to get back the AutomationStepOneOf2 set earlier
        AutomationStepOneOf2 testAutomationStepOneOf2 = (AutomationStepOneOf2) exampleAutomationStep.getActualInstance();

        // create a new AutomationStepOneOf3
        AutomationStepOneOf3 exampleAutomationStepOneOf3 = new AutomationStepOneOf3();
        // set AutomationStep to AutomationStepOneOf3
        exampleAutomationStep.setActualInstance(exampleAutomationStepOneOf3);
        // to get back the AutomationStepOneOf3 set earlier
        AutomationStepOneOf3 testAutomationStepOneOf3 = (AutomationStepOneOf3) exampleAutomationStep.getActualInstance();

        // create a new AutomationStepOneOf4
        AutomationStepOneOf4 exampleAutomationStepOneOf4 = new AutomationStepOneOf4();
        // set AutomationStep to AutomationStepOneOf4
        exampleAutomationStep.setActualInstance(exampleAutomationStepOneOf4);
        // to get back the AutomationStepOneOf4 set earlier
        AutomationStepOneOf4 testAutomationStepOneOf4 = (AutomationStepOneOf4) exampleAutomationStep.getActualInstance();

        // create a new AutomationStepOneOf5
        AutomationStepOneOf5 exampleAutomationStepOneOf5 = new AutomationStepOneOf5();
        // set AutomationStep to AutomationStepOneOf5
        exampleAutomationStep.setActualInstance(exampleAutomationStepOneOf5);
        // to get back the AutomationStepOneOf5 set earlier
        AutomationStepOneOf5 testAutomationStepOneOf5 = (AutomationStepOneOf5) exampleAutomationStep.getActualInstance();

        // create a new AutomationStepOneOf6
        AutomationStepOneOf6 exampleAutomationStepOneOf6 = new AutomationStepOneOf6();
        // set AutomationStep to AutomationStepOneOf6
        exampleAutomationStep.setActualInstance(exampleAutomationStepOneOf6);
        // to get back the AutomationStepOneOf6 set earlier
        AutomationStepOneOf6 testAutomationStepOneOf6 = (AutomationStepOneOf6) exampleAutomationStep.getActualInstance();

        // create a new AutomationStepOneOf7
        AutomationStepOneOf7 exampleAutomationStepOneOf7 = new AutomationStepOneOf7();
        // set AutomationStep to AutomationStepOneOf7
        exampleAutomationStep.setActualInstance(exampleAutomationStepOneOf7);
        // to get back the AutomationStepOneOf7 set earlier
        AutomationStepOneOf7 testAutomationStepOneOf7 = (AutomationStepOneOf7) exampleAutomationStep.getActualInstance();

        // create a new AutomationStepOneOf8
        AutomationStepOneOf8 exampleAutomationStepOneOf8 = new AutomationStepOneOf8();
        // set AutomationStep to AutomationStepOneOf8
        exampleAutomationStep.setActualInstance(exampleAutomationStepOneOf8);
        // to get back the AutomationStepOneOf8 set earlier
        AutomationStepOneOf8 testAutomationStepOneOf8 = (AutomationStepOneOf8) exampleAutomationStep.getActualInstance();

        // create a new AutomationStepOneOf9
        AutomationStepOneOf9 exampleAutomationStepOneOf9 = new AutomationStepOneOf9();
        // set AutomationStep to AutomationStepOneOf9
        exampleAutomationStep.setActualInstance(exampleAutomationStepOneOf9);
        // to get back the AutomationStepOneOf9 set earlier
        AutomationStepOneOf9 testAutomationStepOneOf9 = (AutomationStepOneOf9) exampleAutomationStep.getActualInstance();
    }
}
```


