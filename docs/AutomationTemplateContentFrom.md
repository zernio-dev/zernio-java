

# AutomationTemplateContentFrom

Copy existing automations: your own (`automationIds`), one of Zernio's templates (`templateId`, for example `stop_losers`), or a template shared by link (`shareToken`).

## oneOf schemas
* [FromASharedTemplate](FromASharedTemplate.md)
* [FromAZernioTemplate](FromAZernioTemplate.md)
* [FromYourAutomations](FromYourAutomations.md)

## Example
```java
// Import classes:
import dev.zernio.model.AutomationTemplateContentFrom;
import dev.zernio.model.FromASharedTemplate;
import dev.zernio.model.FromAZernioTemplate;
import dev.zernio.model.FromYourAutomations;

public class Example {
    public static void main(String[] args) {
        AutomationTemplateContentFrom exampleAutomationTemplateContentFrom = new AutomationTemplateContentFrom();

        // create a new FromASharedTemplate
        FromASharedTemplate exampleFromASharedTemplate = new FromASharedTemplate();
        // set AutomationTemplateContentFrom to FromASharedTemplate
        exampleAutomationTemplateContentFrom.setActualInstance(exampleFromASharedTemplate);
        // to get back the FromASharedTemplate set earlier
        FromASharedTemplate testFromASharedTemplate = (FromASharedTemplate) exampleAutomationTemplateContentFrom.getActualInstance();

        // create a new FromAZernioTemplate
        FromAZernioTemplate exampleFromAZernioTemplate = new FromAZernioTemplate();
        // set AutomationTemplateContentFrom to FromAZernioTemplate
        exampleAutomationTemplateContentFrom.setActualInstance(exampleFromAZernioTemplate);
        // to get back the FromAZernioTemplate set earlier
        FromAZernioTemplate testFromAZernioTemplate = (FromAZernioTemplate) exampleAutomationTemplateContentFrom.getActualInstance();

        // create a new FromYourAutomations
        FromYourAutomations exampleFromYourAutomations = new FromYourAutomations();
        // set AutomationTemplateContentFrom to FromYourAutomations
        exampleAutomationTemplateContentFrom.setActualInstance(exampleFromYourAutomations);
        // to get back the FromYourAutomations set earlier
        FromYourAutomations testFromYourAutomations = (FromYourAutomations) exampleAutomationTemplateContentFrom.getActualInstance();
    }
}
```


