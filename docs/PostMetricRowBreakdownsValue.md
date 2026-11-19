

# PostMetricRowBreakdownsValue

## anyOf schemas
* [Map](Map.md)

NOTE: this class is nullable.

## Example
```java
// Import classes:
import dev.zernio.model.PostMetricRowBreakdownsValue;
import dev.zernio.model.Map;

public class Example {
    public static void main(String[] args) {
        PostMetricRowBreakdownsValue examplePostMetricRowBreakdownsValue = new PostMetricRowBreakdownsValue();

        // create a new Map
        Map exampleMap = new Map();
        // set PostMetricRowBreakdownsValue to Map
        examplePostMetricRowBreakdownsValue.setActualInstance(exampleMap);
        // to get back the Map set earlier
        Map testMap = (Map) examplePostMetricRowBreakdownsValue.getActualInstance();
    }
}
```


