

# GetConversionMetrics200ResponseRowsInnerMetricsValue

## oneOf schemas
* [BigDecimal](BigDecimal.md)
* [String](String.md)

## Example
```java
// Import classes:
import dev.zernio.model.GetConversionMetrics200ResponseRowsInnerMetricsValue;
import dev.zernio.model.BigDecimal;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        GetConversionMetrics200ResponseRowsInnerMetricsValue exampleGetConversionMetrics200ResponseRowsInnerMetricsValue = new GetConversionMetrics200ResponseRowsInnerMetricsValue();

        // create a new BigDecimal
        BigDecimal exampleBigDecimal = new BigDecimal();
        // set GetConversionMetrics200ResponseRowsInnerMetricsValue to BigDecimal
        exampleGetConversionMetrics200ResponseRowsInnerMetricsValue.setActualInstance(exampleBigDecimal);
        // to get back the BigDecimal set earlier
        BigDecimal testBigDecimal = (BigDecimal) exampleGetConversionMetrics200ResponseRowsInnerMetricsValue.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set GetConversionMetrics200ResponseRowsInnerMetricsValue to String
        exampleGetConversionMetrics200ResponseRowsInnerMetricsValue.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleGetConversionMetrics200ResponseRowsInnerMetricsValue.getActualInstance();
    }
}
```


