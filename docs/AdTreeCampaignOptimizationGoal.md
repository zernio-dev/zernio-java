

# AdTreeCampaignOptimizationGoal

A single string when every ad set shares one optimization goal; a JSON array of the distinct goals when ad sets differ (never a comma-joined string); array element order is not guaranteed, treat it as an unordered set; the key is absent when no ad set carries a goal. Meta: e.g. OFFSITE_CONVERSIONS, VALUE, LEAD_GENERATION. LinkedIn: the campaign optimizationTargetType (e.g. MAX_CLICK, MAX_IMPRESSION, NONE); `NONE` with a manual costType is a campaign LinkedIn will not deliver.

## anyOf schemas
* [String](String.md)

## Example
```java
// Import classes:
import dev.zernio.model.AdTreeCampaignOptimizationGoal;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        AdTreeCampaignOptimizationGoal exampleAdTreeCampaignOptimizationGoal = new AdTreeCampaignOptimizationGoal();

        // create a new String
        String exampleString = new String();
        // set AdTreeCampaignOptimizationGoal to String
        exampleAdTreeCampaignOptimizationGoal.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleAdTreeCampaignOptimizationGoal.getActualInstance();
    }
}
```


