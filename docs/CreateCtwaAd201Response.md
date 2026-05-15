

# CreateCtwaAd201Response

## oneOf schemas
* [CtwaMultiResponse](CtwaMultiResponse.md)
* [CtwaSingleResponse](CtwaSingleResponse.md)

## Example
```java
// Import classes:
import dev.zernio.model.CreateCtwaAd201Response;
import dev.zernio.model.CtwaMultiResponse;
import dev.zernio.model.CtwaSingleResponse;

public class Example {
    public static void main(String[] args) {
        CreateCtwaAd201Response exampleCreateCtwaAd201Response = new CreateCtwaAd201Response();

        // create a new CtwaMultiResponse
        CtwaMultiResponse exampleCtwaMultiResponse = new CtwaMultiResponse();
        // set CreateCtwaAd201Response to CtwaMultiResponse
        exampleCreateCtwaAd201Response.setActualInstance(exampleCtwaMultiResponse);
        // to get back the CtwaMultiResponse set earlier
        CtwaMultiResponse testCtwaMultiResponse = (CtwaMultiResponse) exampleCreateCtwaAd201Response.getActualInstance();

        // create a new CtwaSingleResponse
        CtwaSingleResponse exampleCtwaSingleResponse = new CtwaSingleResponse();
        // set CreateCtwaAd201Response to CtwaSingleResponse
        exampleCreateCtwaAd201Response.setActualInstance(exampleCtwaSingleResponse);
        // to get back the CtwaSingleResponse set earlier
        CtwaSingleResponse testCtwaSingleResponse = (CtwaSingleResponse) exampleCreateCtwaAd201Response.getActualInstance();
    }
}
```


