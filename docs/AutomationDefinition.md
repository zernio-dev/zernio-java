

# AutomationDefinition

An automation of one of six kinds. The kind follows from `trigger.type`, each type belonging to one kind; a `schedule` is an ad rule unless `subjects.each` is `post`, and a flow may leave `trigger.type` out:  - **Ad rule**: a `schedule` trigger over campaigns, ad sets, ads, Google keywords or Google search terms, with metric `conditions` and ad `steps`. - **Event**: a Zernio event in `trigger.type`, narrowed by `trigger.filter`, with notify steps, or none to only record each matching event as a check. - **Scheduled**: a `schedule` trigger over `subjects.each: post`, narrowed by `filter`, with notify and boost steps. - **Sequence**: an `enrollment` trigger on one account, with message steps sent over time. - **Comment to DM**: a comment door in `trigger.type` (`comment.keyword`, `comment.live`, `story.reply`, `story.mention`) with a `graph`. - **Flow**: a workflow trigger (`inbound_message`, `api_call`, `comment` and the others) with the builder's `graph`; `trigger.type` may be left out, read from the graph's trigger node. 

## oneOf schemas
* [AdRuleAutomationDefinition](AdRuleAutomationDefinition.md)
* [CommentAutomationDefinition](CommentAutomationDefinition.md)
* [EventAutomationDefinition](EventAutomationDefinition.md)
* [FlowAutomationDefinition](FlowAutomationDefinition.md)
* [ScheduledAutomationDefinition](ScheduledAutomationDefinition.md)
* [SequenceAutomationDefinition](SequenceAutomationDefinition.md)

## Example
```java
// Import classes:
import dev.zernio.model.AutomationDefinition;
import dev.zernio.model.AdRuleAutomationDefinition;
import dev.zernio.model.CommentAutomationDefinition;
import dev.zernio.model.EventAutomationDefinition;
import dev.zernio.model.FlowAutomationDefinition;
import dev.zernio.model.ScheduledAutomationDefinition;
import dev.zernio.model.SequenceAutomationDefinition;

public class Example {
    public static void main(String[] args) {
        AutomationDefinition exampleAutomationDefinition = new AutomationDefinition();

        // create a new AdRuleAutomationDefinition
        AdRuleAutomationDefinition exampleAdRuleAutomationDefinition = new AdRuleAutomationDefinition();
        // set AutomationDefinition to AdRuleAutomationDefinition
        exampleAutomationDefinition.setActualInstance(exampleAdRuleAutomationDefinition);
        // to get back the AdRuleAutomationDefinition set earlier
        AdRuleAutomationDefinition testAdRuleAutomationDefinition = (AdRuleAutomationDefinition) exampleAutomationDefinition.getActualInstance();

        // create a new CommentAutomationDefinition
        CommentAutomationDefinition exampleCommentAutomationDefinition = new CommentAutomationDefinition();
        // set AutomationDefinition to CommentAutomationDefinition
        exampleAutomationDefinition.setActualInstance(exampleCommentAutomationDefinition);
        // to get back the CommentAutomationDefinition set earlier
        CommentAutomationDefinition testCommentAutomationDefinition = (CommentAutomationDefinition) exampleAutomationDefinition.getActualInstance();

        // create a new EventAutomationDefinition
        EventAutomationDefinition exampleEventAutomationDefinition = new EventAutomationDefinition();
        // set AutomationDefinition to EventAutomationDefinition
        exampleAutomationDefinition.setActualInstance(exampleEventAutomationDefinition);
        // to get back the EventAutomationDefinition set earlier
        EventAutomationDefinition testEventAutomationDefinition = (EventAutomationDefinition) exampleAutomationDefinition.getActualInstance();

        // create a new FlowAutomationDefinition
        FlowAutomationDefinition exampleFlowAutomationDefinition = new FlowAutomationDefinition();
        // set AutomationDefinition to FlowAutomationDefinition
        exampleAutomationDefinition.setActualInstance(exampleFlowAutomationDefinition);
        // to get back the FlowAutomationDefinition set earlier
        FlowAutomationDefinition testFlowAutomationDefinition = (FlowAutomationDefinition) exampleAutomationDefinition.getActualInstance();

        // create a new ScheduledAutomationDefinition
        ScheduledAutomationDefinition exampleScheduledAutomationDefinition = new ScheduledAutomationDefinition();
        // set AutomationDefinition to ScheduledAutomationDefinition
        exampleAutomationDefinition.setActualInstance(exampleScheduledAutomationDefinition);
        // to get back the ScheduledAutomationDefinition set earlier
        ScheduledAutomationDefinition testScheduledAutomationDefinition = (ScheduledAutomationDefinition) exampleAutomationDefinition.getActualInstance();

        // create a new SequenceAutomationDefinition
        SequenceAutomationDefinition exampleSequenceAutomationDefinition = new SequenceAutomationDefinition();
        // set AutomationDefinition to SequenceAutomationDefinition
        exampleAutomationDefinition.setActualInstance(exampleSequenceAutomationDefinition);
        // to get back the SequenceAutomationDefinition set earlier
        SequenceAutomationDefinition testSequenceAutomationDefinition = (SequenceAutomationDefinition) exampleAutomationDefinition.getActualInstance();
    }
}
```


