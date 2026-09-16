

# UpdateProductRequestVariantsInnerPrice

Decimal amount in the store currency. Numbers are formatted to two decimals.

## oneOf schemas
* [BigDecimal](BigDecimal.md)
* [String](String.md)

## Example
```java
// Import classes:
import dev.zernio.model.UpdateProductRequestVariantsInnerPrice;
import dev.zernio.model.BigDecimal;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        UpdateProductRequestVariantsInnerPrice exampleUpdateProductRequestVariantsInnerPrice = new UpdateProductRequestVariantsInnerPrice();

        // create a new BigDecimal
        BigDecimal exampleBigDecimal = new BigDecimal();
        // set UpdateProductRequestVariantsInnerPrice to BigDecimal
        exampleUpdateProductRequestVariantsInnerPrice.setActualInstance(exampleBigDecimal);
        // to get back the BigDecimal set earlier
        BigDecimal testBigDecimal = (BigDecimal) exampleUpdateProductRequestVariantsInnerPrice.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set UpdateProductRequestVariantsInnerPrice to String
        exampleUpdateProductRequestVariantsInnerPrice.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleUpdateProductRequestVariantsInnerPrice.getActualInstance();
    }
}
```


