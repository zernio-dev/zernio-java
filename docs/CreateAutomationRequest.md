

# CreateAutomationRequest

## oneOf schemas
* [AutomationDefinition](AutomationDefinition.md)
* [GraphAutomationDefinition](GraphAutomationDefinition.md)

## Example
```java
// Import classes:
import dev.zernio.model.CreateAutomationRequest;
import dev.zernio.model.AutomationDefinition;
import dev.zernio.model.GraphAutomationDefinition;

public class Example {
    public static void main(String[] args) {
        CreateAutomationRequest exampleCreateAutomationRequest = new CreateAutomationRequest();

        // create a new AutomationDefinition
        AutomationDefinition exampleAutomationDefinition = new AutomationDefinition();
        // set CreateAutomationRequest to AutomationDefinition
        exampleCreateAutomationRequest.setActualInstance(exampleAutomationDefinition);
        // to get back the AutomationDefinition set earlier
        AutomationDefinition testAutomationDefinition = (AutomationDefinition) exampleCreateAutomationRequest.getActualInstance();

        // create a new GraphAutomationDefinition
        GraphAutomationDefinition exampleGraphAutomationDefinition = new GraphAutomationDefinition();
        // set CreateAutomationRequest to GraphAutomationDefinition
        exampleCreateAutomationRequest.setActualInstance(exampleGraphAutomationDefinition);
        // to get back the GraphAutomationDefinition set earlier
        GraphAutomationDefinition testGraphAutomationDefinition = (GraphAutomationDefinition) exampleCreateAutomationRequest.getActualInstance();
    }
}
```


