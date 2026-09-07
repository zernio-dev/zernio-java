

# UpdateAdRequestTargetingDevicesInner

## oneOf schemas
* [String](String.md)
* [UpdateAdRequestTargetingDevicesInnerOneOf](UpdateAdRequestTargetingDevicesInnerOneOf.md)

## Example
```java
// Import classes:
import dev.zernio.model.UpdateAdRequestTargetingDevicesInner;
import dev.zernio.model.String;
import dev.zernio.model.UpdateAdRequestTargetingDevicesInnerOneOf;

public class Example {
    public static void main(String[] args) {
        UpdateAdRequestTargetingDevicesInner exampleUpdateAdRequestTargetingDevicesInner = new UpdateAdRequestTargetingDevicesInner();

        // create a new String
        String exampleString = new String();
        // set UpdateAdRequestTargetingDevicesInner to String
        exampleUpdateAdRequestTargetingDevicesInner.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleUpdateAdRequestTargetingDevicesInner.getActualInstance();

        // create a new UpdateAdRequestTargetingDevicesInnerOneOf
        UpdateAdRequestTargetingDevicesInnerOneOf exampleUpdateAdRequestTargetingDevicesInnerOneOf = new UpdateAdRequestTargetingDevicesInnerOneOf();
        // set UpdateAdRequestTargetingDevicesInner to UpdateAdRequestTargetingDevicesInnerOneOf
        exampleUpdateAdRequestTargetingDevicesInner.setActualInstance(exampleUpdateAdRequestTargetingDevicesInnerOneOf);
        // to get back the UpdateAdRequestTargetingDevicesInnerOneOf set earlier
        UpdateAdRequestTargetingDevicesInnerOneOf testUpdateAdRequestTargetingDevicesInnerOneOf = (UpdateAdRequestTargetingDevicesInnerOneOf) exampleUpdateAdRequestTargetingDevicesInner.getActualInstance();
    }
}
```


