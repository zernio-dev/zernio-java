

# SearchAdTargetingLocations200ResponseResultsInnerRegionId

Parent region ID (cities only).

## oneOf schemas
* [Integer](Integer.md)
* [String](String.md)

## Example
```java
// Import classes:
import dev.zernio.model.SearchAdTargetingLocations200ResponseResultsInnerRegionId;
import dev.zernio.model.Integer;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        SearchAdTargetingLocations200ResponseResultsInnerRegionId exampleSearchAdTargetingLocations200ResponseResultsInnerRegionId = new SearchAdTargetingLocations200ResponseResultsInnerRegionId();

        // create a new Integer
        Integer exampleInteger = new Integer();
        // set SearchAdTargetingLocations200ResponseResultsInnerRegionId to Integer
        exampleSearchAdTargetingLocations200ResponseResultsInnerRegionId.setActualInstance(exampleInteger);
        // to get back the Integer set earlier
        Integer testInteger = (Integer) exampleSearchAdTargetingLocations200ResponseResultsInnerRegionId.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set SearchAdTargetingLocations200ResponseResultsInnerRegionId to String
        exampleSearchAdTargetingLocations200ResponseResultsInnerRegionId.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleSearchAdTargetingLocations200ResponseResultsInnerRegionId.getActualInstance();
    }
}
```


