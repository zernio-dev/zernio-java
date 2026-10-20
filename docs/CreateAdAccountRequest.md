

# CreateAdAccountRequest

## oneOf schemas
* [CreateGoogleAdAccountRequest](CreateGoogleAdAccountRequest.md)
* [CreateMetaAdAccountRequest](CreateMetaAdAccountRequest.md)

## Example
```java
// Import classes:
import dev.zernio.model.CreateAdAccountRequest;
import dev.zernio.model.CreateGoogleAdAccountRequest;
import dev.zernio.model.CreateMetaAdAccountRequest;

public class Example {
    public static void main(String[] args) {
        CreateAdAccountRequest exampleCreateAdAccountRequest = new CreateAdAccountRequest();

        // create a new CreateGoogleAdAccountRequest
        CreateGoogleAdAccountRequest exampleCreateGoogleAdAccountRequest = new CreateGoogleAdAccountRequest();
        // set CreateAdAccountRequest to CreateGoogleAdAccountRequest
        exampleCreateAdAccountRequest.setActualInstance(exampleCreateGoogleAdAccountRequest);
        // to get back the CreateGoogleAdAccountRequest set earlier
        CreateGoogleAdAccountRequest testCreateGoogleAdAccountRequest = (CreateGoogleAdAccountRequest) exampleCreateAdAccountRequest.getActualInstance();

        // create a new CreateMetaAdAccountRequest
        CreateMetaAdAccountRequest exampleCreateMetaAdAccountRequest = new CreateMetaAdAccountRequest();
        // set CreateAdAccountRequest to CreateMetaAdAccountRequest
        exampleCreateAdAccountRequest.setActualInstance(exampleCreateMetaAdAccountRequest);
        // to get back the CreateMetaAdAccountRequest set earlier
        CreateMetaAdAccountRequest testCreateMetaAdAccountRequest = (CreateMetaAdAccountRequest) exampleCreateAdAccountRequest.getActualInstance();
    }
}
```


