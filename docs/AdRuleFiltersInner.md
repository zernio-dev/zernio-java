

# AdRuleFiltersInner

## oneOf schemas
* [BudgetLevel](BudgetLevel.md)
* [DaysLive](DaysLive.md)
* [DaysSinceChange](DaysSinceChange.md)
* [Ids](Ids.md)
* [NameOrGoal](NameOrGoal.md)

## Example
```java
// Import classes:
import dev.zernio.model.AdRuleFiltersInner;
import dev.zernio.model.BudgetLevel;
import dev.zernio.model.DaysLive;
import dev.zernio.model.DaysSinceChange;
import dev.zernio.model.Ids;
import dev.zernio.model.NameOrGoal;

public class Example {
    public static void main(String[] args) {
        AdRuleFiltersInner exampleAdRuleFiltersInner = new AdRuleFiltersInner();

        // create a new BudgetLevel
        BudgetLevel exampleBudgetLevel = new BudgetLevel();
        // set AdRuleFiltersInner to BudgetLevel
        exampleAdRuleFiltersInner.setActualInstance(exampleBudgetLevel);
        // to get back the BudgetLevel set earlier
        BudgetLevel testBudgetLevel = (BudgetLevel) exampleAdRuleFiltersInner.getActualInstance();

        // create a new DaysLive
        DaysLive exampleDaysLive = new DaysLive();
        // set AdRuleFiltersInner to DaysLive
        exampleAdRuleFiltersInner.setActualInstance(exampleDaysLive);
        // to get back the DaysLive set earlier
        DaysLive testDaysLive = (DaysLive) exampleAdRuleFiltersInner.getActualInstance();

        // create a new DaysSinceChange
        DaysSinceChange exampleDaysSinceChange = new DaysSinceChange();
        // set AdRuleFiltersInner to DaysSinceChange
        exampleAdRuleFiltersInner.setActualInstance(exampleDaysSinceChange);
        // to get back the DaysSinceChange set earlier
        DaysSinceChange testDaysSinceChange = (DaysSinceChange) exampleAdRuleFiltersInner.getActualInstance();

        // create a new Ids
        Ids exampleIds = new Ids();
        // set AdRuleFiltersInner to Ids
        exampleAdRuleFiltersInner.setActualInstance(exampleIds);
        // to get back the Ids set earlier
        Ids testIds = (Ids) exampleAdRuleFiltersInner.getActualInstance();

        // create a new NameOrGoal
        NameOrGoal exampleNameOrGoal = new NameOrGoal();
        // set AdRuleFiltersInner to NameOrGoal
        exampleAdRuleFiltersInner.setActualInstance(exampleNameOrGoal);
        // to get back the NameOrGoal set earlier
        NameOrGoal testNameOrGoal = (NameOrGoal) exampleAdRuleFiltersInner.getActualInstance();
    }
}
```


