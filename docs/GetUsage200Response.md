

# GetUsage200Response

## oneOf schemas
* [UsageMetering](UsageMetering.md)
* [UsageStats](UsageStats.md)

## Example
```java
// Import classes:
import dev.zernio.model.GetUsage200Response;
import dev.zernio.model.UsageMetering;
import dev.zernio.model.UsageStats;

public class Example {
    public static void main(String[] args) {
        GetUsage200Response exampleGetUsage200Response = new GetUsage200Response();

        // create a new UsageMetering
        UsageMetering exampleUsageMetering = new UsageMetering();
        // set GetUsage200Response to UsageMetering
        exampleGetUsage200Response.setActualInstance(exampleUsageMetering);
        // to get back the UsageMetering set earlier
        UsageMetering testUsageMetering = (UsageMetering) exampleGetUsage200Response.getActualInstance();

        // create a new UsageStats
        UsageStats exampleUsageStats = new UsageStats();
        // set GetUsage200Response to UsageStats
        exampleGetUsage200Response.setActualInstance(exampleUsageStats);
        // to get back the UsageStats set earlier
        UsageStats testUsageStats = (UsageStats) exampleGetUsage200Response.getActualInstance();
    }
}
```


