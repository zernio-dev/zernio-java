

# CommerceDiscountValue

Null for free shipping, buy-X-get-Y and app discounts.

## oneOf schemas
* [CommerceDiscountValueOneOf](CommerceDiscountValueOneOf.md)
* [CommerceDiscountValueOneOf1](CommerceDiscountValueOneOf1.md)

NOTE: this class is nullable.

## Example
```java
// Import classes:
import dev.zernio.model.CommerceDiscountValue;
import dev.zernio.model.CommerceDiscountValueOneOf;
import dev.zernio.model.CommerceDiscountValueOneOf1;

public class Example {
    public static void main(String[] args) {
        CommerceDiscountValue exampleCommerceDiscountValue = new CommerceDiscountValue();

        // create a new CommerceDiscountValueOneOf
        CommerceDiscountValueOneOf exampleCommerceDiscountValueOneOf = new CommerceDiscountValueOneOf();
        // set CommerceDiscountValue to CommerceDiscountValueOneOf
        exampleCommerceDiscountValue.setActualInstance(exampleCommerceDiscountValueOneOf);
        // to get back the CommerceDiscountValueOneOf set earlier
        CommerceDiscountValueOneOf testCommerceDiscountValueOneOf = (CommerceDiscountValueOneOf) exampleCommerceDiscountValue.getActualInstance();

        // create a new CommerceDiscountValueOneOf1
        CommerceDiscountValueOneOf1 exampleCommerceDiscountValueOneOf1 = new CommerceDiscountValueOneOf1();
        // set CommerceDiscountValue to CommerceDiscountValueOneOf1
        exampleCommerceDiscountValue.setActualInstance(exampleCommerceDiscountValueOneOf1);
        // to get back the CommerceDiscountValueOneOf1 set earlier
        CommerceDiscountValueOneOf1 testCommerceDiscountValueOneOf1 = (CommerceDiscountValueOneOf1) exampleCommerceDiscountValue.getActualInstance();
    }
}
```


