

# UpdateAdSetRequestRegionalRegulationIdentitiesValue

## anyOf schemas
* [Integer](Integer.md)
* [String](String.md)

## Example
```java
// Import classes:
import dev.zernio.model.UpdateAdSetRequestRegionalRegulationIdentitiesValue;
import dev.zernio.model.Integer;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        UpdateAdSetRequestRegionalRegulationIdentitiesValue exampleUpdateAdSetRequestRegionalRegulationIdentitiesValue = new UpdateAdSetRequestRegionalRegulationIdentitiesValue();

        // create a new Integer
        Integer exampleInteger = new Integer();
        // set UpdateAdSetRequestRegionalRegulationIdentitiesValue to Integer
        exampleUpdateAdSetRequestRegionalRegulationIdentitiesValue.setActualInstance(exampleInteger);
        // to get back the Integer set earlier
        Integer testInteger = (Integer) exampleUpdateAdSetRequestRegionalRegulationIdentitiesValue.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set UpdateAdSetRequestRegionalRegulationIdentitiesValue to String
        exampleUpdateAdSetRequestRegionalRegulationIdentitiesValue.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleUpdateAdSetRequestRegionalRegulationIdentitiesValue.getActualInstance();
    }
}
```


