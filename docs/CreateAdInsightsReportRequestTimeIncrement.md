

# CreateAdInsightsReportRequestTimeIncrement

## oneOf schemas
* [Integer](Integer.md)
* [String](String.md)

## Example
```java
// Import classes:
import dev.zernio.model.CreateAdInsightsReportRequestTimeIncrement;
import dev.zernio.model.Integer;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        CreateAdInsightsReportRequestTimeIncrement exampleCreateAdInsightsReportRequestTimeIncrement = new CreateAdInsightsReportRequestTimeIncrement();

        // create a new Integer
        Integer exampleInteger = new Integer();
        // set CreateAdInsightsReportRequestTimeIncrement to Integer
        exampleCreateAdInsightsReportRequestTimeIncrement.setActualInstance(exampleInteger);
        // to get back the Integer set earlier
        Integer testInteger = (Integer) exampleCreateAdInsightsReportRequestTimeIncrement.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set CreateAdInsightsReportRequestTimeIncrement to String
        exampleCreateAdInsightsReportRequestTimeIncrement.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleCreateAdInsightsReportRequestTimeIncrement.getActualInstance();
    }
}
```


