

# UpdateCommerceProductPricesRequestVariantsInnerPrice

## oneOf schemas
* [BigDecimal](BigDecimal.md)
* [String](String.md)

## Example
```java
// Import classes:
import dev.zernio.model.UpdateCommerceProductPricesRequestVariantsInnerPrice;
import dev.zernio.model.BigDecimal;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        UpdateCommerceProductPricesRequestVariantsInnerPrice exampleUpdateCommerceProductPricesRequestVariantsInnerPrice = new UpdateCommerceProductPricesRequestVariantsInnerPrice();

        // create a new BigDecimal
        BigDecimal exampleBigDecimal = new BigDecimal();
        // set UpdateCommerceProductPricesRequestVariantsInnerPrice to BigDecimal
        exampleUpdateCommerceProductPricesRequestVariantsInnerPrice.setActualInstance(exampleBigDecimal);
        // to get back the BigDecimal set earlier
        BigDecimal testBigDecimal = (BigDecimal) exampleUpdateCommerceProductPricesRequestVariantsInnerPrice.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set UpdateCommerceProductPricesRequestVariantsInnerPrice to String
        exampleUpdateCommerceProductPricesRequestVariantsInnerPrice.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleUpdateCommerceProductPricesRequestVariantsInnerPrice.getActualInstance();
    }
}
```


