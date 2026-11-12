

# CommerceRefundRequestShipping

Refund the shipping: `{ \"full\": true }` for what is left of it, or `{ \"amount\": \"5.00\" }` for part of it.

## oneOf schemas
* [CommerceRefundRequestShippingOneOf](CommerceRefundRequestShippingOneOf.md)
* [CommerceRefundRequestShippingOneOf1](CommerceRefundRequestShippingOneOf1.md)

## Example
```java
// Import classes:
import dev.zernio.model.CommerceRefundRequestShipping;
import dev.zernio.model.CommerceRefundRequestShippingOneOf;
import dev.zernio.model.CommerceRefundRequestShippingOneOf1;

public class Example {
    public static void main(String[] args) {
        CommerceRefundRequestShipping exampleCommerceRefundRequestShipping = new CommerceRefundRequestShipping();

        // create a new CommerceRefundRequestShippingOneOf
        CommerceRefundRequestShippingOneOf exampleCommerceRefundRequestShippingOneOf = new CommerceRefundRequestShippingOneOf();
        // set CommerceRefundRequestShipping to CommerceRefundRequestShippingOneOf
        exampleCommerceRefundRequestShipping.setActualInstance(exampleCommerceRefundRequestShippingOneOf);
        // to get back the CommerceRefundRequestShippingOneOf set earlier
        CommerceRefundRequestShippingOneOf testCommerceRefundRequestShippingOneOf = (CommerceRefundRequestShippingOneOf) exampleCommerceRefundRequestShipping.getActualInstance();

        // create a new CommerceRefundRequestShippingOneOf1
        CommerceRefundRequestShippingOneOf1 exampleCommerceRefundRequestShippingOneOf1 = new CommerceRefundRequestShippingOneOf1();
        // set CommerceRefundRequestShipping to CommerceRefundRequestShippingOneOf1
        exampleCommerceRefundRequestShipping.setActualInstance(exampleCommerceRefundRequestShippingOneOf1);
        // to get back the CommerceRefundRequestShippingOneOf1 set earlier
        CommerceRefundRequestShippingOneOf1 testCommerceRefundRequestShippingOneOf1 = (CommerceRefundRequestShippingOneOf1) exampleCommerceRefundRequestShipping.getActualInstance();
    }
}
```


