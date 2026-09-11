

# SelectFacebookPageRequest

## oneOf schemas
* [SelectFacebookPageRequestOneOf](SelectFacebookPageRequestOneOf.md)
* [SelectFacebookPageRequestOneOf1](SelectFacebookPageRequestOneOf1.md)

## Example
```java
// Import classes:
import dev.zernio.model.SelectFacebookPageRequest;
import dev.zernio.model.SelectFacebookPageRequestOneOf;
import dev.zernio.model.SelectFacebookPageRequestOneOf1;

public class Example {
    public static void main(String[] args) {
        SelectFacebookPageRequest exampleSelectFacebookPageRequest = new SelectFacebookPageRequest();

        // create a new SelectFacebookPageRequestOneOf
        SelectFacebookPageRequestOneOf exampleSelectFacebookPageRequestOneOf = new SelectFacebookPageRequestOneOf();
        // set SelectFacebookPageRequest to SelectFacebookPageRequestOneOf
        exampleSelectFacebookPageRequest.setActualInstance(exampleSelectFacebookPageRequestOneOf);
        // to get back the SelectFacebookPageRequestOneOf set earlier
        SelectFacebookPageRequestOneOf testSelectFacebookPageRequestOneOf = (SelectFacebookPageRequestOneOf) exampleSelectFacebookPageRequest.getActualInstance();

        // create a new SelectFacebookPageRequestOneOf1
        SelectFacebookPageRequestOneOf1 exampleSelectFacebookPageRequestOneOf1 = new SelectFacebookPageRequestOneOf1();
        // set SelectFacebookPageRequest to SelectFacebookPageRequestOneOf1
        exampleSelectFacebookPageRequest.setActualInstance(exampleSelectFacebookPageRequestOneOf1);
        // to get back the SelectFacebookPageRequestOneOf1 set earlier
        SelectFacebookPageRequestOneOf1 testSelectFacebookPageRequestOneOf1 = (SelectFacebookPageRequestOneOf1) exampleSelectFacebookPageRequest.getActualInstance();
    }
}
```


