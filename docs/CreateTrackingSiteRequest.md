

# CreateTrackingSiteRequest

## oneOf schemas
* [AnyWebsite](AnyWebsite.md)
* [ConnectedStore](ConnectedStore.md)

## Example
```java
// Import classes:
import dev.zernio.model.CreateTrackingSiteRequest;
import dev.zernio.model.AnyWebsite;
import dev.zernio.model.ConnectedStore;

public class Example {
    public static void main(String[] args) {
        CreateTrackingSiteRequest exampleCreateTrackingSiteRequest = new CreateTrackingSiteRequest();

        // create a new AnyWebsite
        AnyWebsite exampleAnyWebsite = new AnyWebsite();
        // set CreateTrackingSiteRequest to AnyWebsite
        exampleCreateTrackingSiteRequest.setActualInstance(exampleAnyWebsite);
        // to get back the AnyWebsite set earlier
        AnyWebsite testAnyWebsite = (AnyWebsite) exampleCreateTrackingSiteRequest.getActualInstance();

        // create a new ConnectedStore
        ConnectedStore exampleConnectedStore = new ConnectedStore();
        // set CreateTrackingSiteRequest to ConnectedStore
        exampleCreateTrackingSiteRequest.setActualInstance(exampleConnectedStore);
        // to get back the ConnectedStore set earlier
        ConnectedStore testConnectedStore = (ConnectedStore) exampleCreateTrackingSiteRequest.getActualInstance();
    }
}
```


