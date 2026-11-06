

# AutomationTemplateInstallResponse

## oneOf schemas
* [OneInstall](OneInstall.md)
* [SeveralTargets](SeveralTargets.md)

## Example
```java
// Import classes:
import dev.zernio.model.AutomationTemplateInstallResponse;
import dev.zernio.model.OneInstall;
import dev.zernio.model.SeveralTargets;

public class Example {
    public static void main(String[] args) {
        AutomationTemplateInstallResponse exampleAutomationTemplateInstallResponse = new AutomationTemplateInstallResponse();

        // create a new OneInstall
        OneInstall exampleOneInstall = new OneInstall();
        // set AutomationTemplateInstallResponse to OneInstall
        exampleAutomationTemplateInstallResponse.setActualInstance(exampleOneInstall);
        // to get back the OneInstall set earlier
        OneInstall testOneInstall = (OneInstall) exampleAutomationTemplateInstallResponse.getActualInstance();

        // create a new SeveralTargets
        SeveralTargets exampleSeveralTargets = new SeveralTargets();
        // set AutomationTemplateInstallResponse to SeveralTargets
        exampleAutomationTemplateInstallResponse.setActualInstance(exampleSeveralTargets);
        // to get back the SeveralTargets set earlier
        SeveralTargets testSeveralTargets = (SeveralTargets) exampleAutomationTemplateInstallResponse.getActualInstance();
    }
}
```


