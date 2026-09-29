

# CreateCommerceProductRequestVariantsInnerCompareAtPrice

## oneOf schemas
* [BigDecimal](BigDecimal.md)
* [String](String.md)

NOTE: this class is nullable.

## Example
```java
// Import classes:
import dev.zernio.model.CreateCommerceProductRequestVariantsInnerCompareAtPrice;
import dev.zernio.model.BigDecimal;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        CreateCommerceProductRequestVariantsInnerCompareAtPrice exampleCreateCommerceProductRequestVariantsInnerCompareAtPrice = new CreateCommerceProductRequestVariantsInnerCompareAtPrice();

        // create a new BigDecimal
        BigDecimal exampleBigDecimal = new BigDecimal();
        // set CreateCommerceProductRequestVariantsInnerCompareAtPrice to BigDecimal
        exampleCreateCommerceProductRequestVariantsInnerCompareAtPrice.setActualInstance(exampleBigDecimal);
        // to get back the BigDecimal set earlier
        BigDecimal testBigDecimal = (BigDecimal) exampleCreateCommerceProductRequestVariantsInnerCompareAtPrice.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set CreateCommerceProductRequestVariantsInnerCompareAtPrice to String
        exampleCreateCommerceProductRequestVariantsInnerCompareAtPrice.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleCreateCommerceProductRequestVariantsInnerCompareAtPrice.getActualInstance();
    }
}
```


