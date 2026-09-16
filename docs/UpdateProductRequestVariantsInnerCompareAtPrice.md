

# UpdateProductRequestVariantsInnerCompareAtPrice

Strike-through price. Send null to remove it.

## oneOf schemas
* [BigDecimal](BigDecimal.md)
* [String](String.md)

NOTE: this class is nullable.

## Example
```java
// Import classes:
import dev.zernio.model.UpdateProductRequestVariantsInnerCompareAtPrice;
import dev.zernio.model.BigDecimal;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        UpdateProductRequestVariantsInnerCompareAtPrice exampleUpdateProductRequestVariantsInnerCompareAtPrice = new UpdateProductRequestVariantsInnerCompareAtPrice();

        // create a new BigDecimal
        BigDecimal exampleBigDecimal = new BigDecimal();
        // set UpdateProductRequestVariantsInnerCompareAtPrice to BigDecimal
        exampleUpdateProductRequestVariantsInnerCompareAtPrice.setActualInstance(exampleBigDecimal);
        // to get back the BigDecimal set earlier
        BigDecimal testBigDecimal = (BigDecimal) exampleUpdateProductRequestVariantsInnerCompareAtPrice.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set UpdateProductRequestVariantsInnerCompareAtPrice to String
        exampleUpdateProductRequestVariantsInnerCompareAtPrice.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleUpdateProductRequestVariantsInnerCompareAtPrice.getActualInstance();
    }
}
```


