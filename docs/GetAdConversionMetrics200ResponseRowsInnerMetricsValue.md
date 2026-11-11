

# GetAdConversionMetrics200ResponseRowsInnerMetricsValue

## oneOf schemas
* [BigDecimal](BigDecimal.md)
* [String](String.md)

## Example
```java
// Import classes:
import dev.zernio.model.GetAdConversionMetrics200ResponseRowsInnerMetricsValue;
import dev.zernio.model.BigDecimal;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        GetAdConversionMetrics200ResponseRowsInnerMetricsValue exampleGetAdConversionMetrics200ResponseRowsInnerMetricsValue = new GetAdConversionMetrics200ResponseRowsInnerMetricsValue();

        // create a new BigDecimal
        BigDecimal exampleBigDecimal = new BigDecimal();
        // set GetAdConversionMetrics200ResponseRowsInnerMetricsValue to BigDecimal
        exampleGetAdConversionMetrics200ResponseRowsInnerMetricsValue.setActualInstance(exampleBigDecimal);
        // to get back the BigDecimal set earlier
        BigDecimal testBigDecimal = (BigDecimal) exampleGetAdConversionMetrics200ResponseRowsInnerMetricsValue.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set GetAdConversionMetrics200ResponseRowsInnerMetricsValue to String
        exampleGetAdConversionMetrics200ResponseRowsInnerMetricsValue.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleGetAdConversionMetrics200ResponseRowsInnerMetricsValue.getActualInstance();
    }
}
```


