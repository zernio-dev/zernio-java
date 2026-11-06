

# UpdateAutomationRequestSubjects

## oneOf schemas
* [AutomationPostSubjects](AutomationPostSubjects.md)
* [AutomationSubjects](AutomationSubjects.md)

## Example
```java
// Import classes:
import dev.zernio.model.UpdateAutomationRequestSubjects;
import dev.zernio.model.AutomationPostSubjects;
import dev.zernio.model.AutomationSubjects;

public class Example {
    public static void main(String[] args) {
        UpdateAutomationRequestSubjects exampleUpdateAutomationRequestSubjects = new UpdateAutomationRequestSubjects();

        // create a new AutomationPostSubjects
        AutomationPostSubjects exampleAutomationPostSubjects = new AutomationPostSubjects();
        // set UpdateAutomationRequestSubjects to AutomationPostSubjects
        exampleUpdateAutomationRequestSubjects.setActualInstance(exampleAutomationPostSubjects);
        // to get back the AutomationPostSubjects set earlier
        AutomationPostSubjects testAutomationPostSubjects = (AutomationPostSubjects) exampleUpdateAutomationRequestSubjects.getActualInstance();

        // create a new AutomationSubjects
        AutomationSubjects exampleAutomationSubjects = new AutomationSubjects();
        // set UpdateAutomationRequestSubjects to AutomationSubjects
        exampleUpdateAutomationRequestSubjects.setActualInstance(exampleAutomationSubjects);
        // to get back the AutomationSubjects set earlier
        AutomationSubjects testAutomationSubjects = (AutomationSubjects) exampleUpdateAutomationRequestSubjects.getActualInstance();
    }
}
```


