

# CreateMessagingAd201Response

## oneOf schemas
* [CtwaMultiResponse](CtwaMultiResponse.md)
* [CtwaSingleResponse](CtwaSingleResponse.md)

## Example
```java
// Import classes:
import dev.zernio.model.CreateMessagingAd201Response;
import dev.zernio.model.CtwaMultiResponse;
import dev.zernio.model.CtwaSingleResponse;

public class Example {
    public static void main(String[] args) {
        CreateMessagingAd201Response exampleCreateMessagingAd201Response = new CreateMessagingAd201Response();

        // create a new CtwaMultiResponse
        CtwaMultiResponse exampleCtwaMultiResponse = new CtwaMultiResponse();
        // set CreateMessagingAd201Response to CtwaMultiResponse
        exampleCreateMessagingAd201Response.setActualInstance(exampleCtwaMultiResponse);
        // to get back the CtwaMultiResponse set earlier
        CtwaMultiResponse testCtwaMultiResponse = (CtwaMultiResponse) exampleCreateMessagingAd201Response.getActualInstance();

        // create a new CtwaSingleResponse
        CtwaSingleResponse exampleCtwaSingleResponse = new CtwaSingleResponse();
        // set CreateMessagingAd201Response to CtwaSingleResponse
        exampleCreateMessagingAd201Response.setActualInstance(exampleCtwaSingleResponse);
        // to get back the CtwaSingleResponse set earlier
        CtwaSingleResponse testCtwaSingleResponse = (CtwaSingleResponse) exampleCreateMessagingAd201Response.getActualInstance();
    }
}
```


