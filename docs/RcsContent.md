

# RcsContent

Message content. `suggestions` (max 11) render as chips under the message.

## oneOf schemas
* [RcsContentOneOf](RcsContentOneOf.md)
* [RcsContentOneOf1](RcsContentOneOf1.md)
* [RcsContentOneOf2](RcsContentOneOf2.md)
* [RcsContentOneOf3](RcsContentOneOf3.md)

## Example
```java
// Import classes:
import dev.zernio.model.RcsContent;
import dev.zernio.model.RcsContentOneOf;
import dev.zernio.model.RcsContentOneOf1;
import dev.zernio.model.RcsContentOneOf2;
import dev.zernio.model.RcsContentOneOf3;

public class Example {
    public static void main(String[] args) {
        RcsContent exampleRcsContent = new RcsContent();

        // create a new RcsContentOneOf
        RcsContentOneOf exampleRcsContentOneOf = new RcsContentOneOf();
        // set RcsContent to RcsContentOneOf
        exampleRcsContent.setActualInstance(exampleRcsContentOneOf);
        // to get back the RcsContentOneOf set earlier
        RcsContentOneOf testRcsContentOneOf = (RcsContentOneOf) exampleRcsContent.getActualInstance();

        // create a new RcsContentOneOf1
        RcsContentOneOf1 exampleRcsContentOneOf1 = new RcsContentOneOf1();
        // set RcsContent to RcsContentOneOf1
        exampleRcsContent.setActualInstance(exampleRcsContentOneOf1);
        // to get back the RcsContentOneOf1 set earlier
        RcsContentOneOf1 testRcsContentOneOf1 = (RcsContentOneOf1) exampleRcsContent.getActualInstance();

        // create a new RcsContentOneOf2
        RcsContentOneOf2 exampleRcsContentOneOf2 = new RcsContentOneOf2();
        // set RcsContent to RcsContentOneOf2
        exampleRcsContent.setActualInstance(exampleRcsContentOneOf2);
        // to get back the RcsContentOneOf2 set earlier
        RcsContentOneOf2 testRcsContentOneOf2 = (RcsContentOneOf2) exampleRcsContent.getActualInstance();

        // create a new RcsContentOneOf3
        RcsContentOneOf3 exampleRcsContentOneOf3 = new RcsContentOneOf3();
        // set RcsContent to RcsContentOneOf3
        exampleRcsContent.setActualInstance(exampleRcsContentOneOf3);
        // to get back the RcsContentOneOf3 set earlier
        RcsContentOneOf3 testRcsContentOneOf3 = (RcsContentOneOf3) exampleRcsContent.getActualInstance();
    }
}
```


