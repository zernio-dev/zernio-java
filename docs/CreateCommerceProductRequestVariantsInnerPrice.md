

# CreateCommerceProductRequestVariantsInnerPrice

Decimal amount in the store currency.

## oneOf schemas
* [BigDecimal](BigDecimal.md)
* [String](String.md)

## Example
```java
// Import classes:
import dev.zernio.model.CreateCommerceProductRequestVariantsInnerPrice;
import dev.zernio.model.BigDecimal;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        CreateCommerceProductRequestVariantsInnerPrice exampleCreateCommerceProductRequestVariantsInnerPrice = new CreateCommerceProductRequestVariantsInnerPrice();

        // create a new BigDecimal
        BigDecimal exampleBigDecimal = new BigDecimal();
        // set CreateCommerceProductRequestVariantsInnerPrice to BigDecimal
        exampleCreateCommerceProductRequestVariantsInnerPrice.setActualInstance(exampleBigDecimal);
        // to get back the BigDecimal set earlier
        BigDecimal testBigDecimal = (BigDecimal) exampleCreateCommerceProductRequestVariantsInnerPrice.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set CreateCommerceProductRequestVariantsInnerPrice to String
        exampleCreateCommerceProductRequestVariantsInnerPrice.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleCreateCommerceProductRequestVariantsInnerPrice.getActualInstance();
    }
}
```


