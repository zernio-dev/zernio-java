

# ConnectAds200Response

## oneOf schemas
* [ConnectAds200ResponseOneOf](ConnectAds200ResponseOneOf.md)
* [ConnectAds200ResponseOneOf1](ConnectAds200ResponseOneOf1.md)

## Example
```java
// Import classes:
import dev.zernio.model.ConnectAds200Response;
import dev.zernio.model.ConnectAds200ResponseOneOf;
import dev.zernio.model.ConnectAds200ResponseOneOf1;

public class Example {
    public static void main(String[] args) {
        ConnectAds200Response exampleConnectAds200Response = new ConnectAds200Response();

        // create a new ConnectAds200ResponseOneOf
        ConnectAds200ResponseOneOf exampleConnectAds200ResponseOneOf = new ConnectAds200ResponseOneOf();
        // set ConnectAds200Response to ConnectAds200ResponseOneOf
        exampleConnectAds200Response.setActualInstance(exampleConnectAds200ResponseOneOf);
        // to get back the ConnectAds200ResponseOneOf set earlier
        ConnectAds200ResponseOneOf testConnectAds200ResponseOneOf = (ConnectAds200ResponseOneOf) exampleConnectAds200Response.getActualInstance();

        // create a new ConnectAds200ResponseOneOf1
        ConnectAds200ResponseOneOf1 exampleConnectAds200ResponseOneOf1 = new ConnectAds200ResponseOneOf1();
        // set ConnectAds200Response to ConnectAds200ResponseOneOf1
        exampleConnectAds200Response.setActualInstance(exampleConnectAds200ResponseOneOf1);
        // to get back the ConnectAds200ResponseOneOf1 set earlier
        ConnectAds200ResponseOneOf1 testConnectAds200ResponseOneOf1 = (ConnectAds200ResponseOneOf1) exampleConnectAds200Response.getActualInstance();
    }
}
```


