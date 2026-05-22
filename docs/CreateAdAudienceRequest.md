

# CreateAdAudienceRequest

## oneOf schemas
* [SavedTargetingAudience](SavedTargetingAudience.md)
* [UploadedOrDerivedAudience](UploadedOrDerivedAudience.md)

## Example
```java
// Import classes:
import dev.zernio.model.CreateAdAudienceRequest;
import dev.zernio.model.SavedTargetingAudience;
import dev.zernio.model.UploadedOrDerivedAudience;

public class Example {
    public static void main(String[] args) {
        CreateAdAudienceRequest exampleCreateAdAudienceRequest = new CreateAdAudienceRequest();

        // create a new SavedTargetingAudience
        SavedTargetingAudience exampleSavedTargetingAudience = new SavedTargetingAudience();
        // set CreateAdAudienceRequest to SavedTargetingAudience
        exampleCreateAdAudienceRequest.setActualInstance(exampleSavedTargetingAudience);
        // to get back the SavedTargetingAudience set earlier
        SavedTargetingAudience testSavedTargetingAudience = (SavedTargetingAudience) exampleCreateAdAudienceRequest.getActualInstance();

        // create a new UploadedOrDerivedAudience
        UploadedOrDerivedAudience exampleUploadedOrDerivedAudience = new UploadedOrDerivedAudience();
        // set CreateAdAudienceRequest to UploadedOrDerivedAudience
        exampleCreateAdAudienceRequest.setActualInstance(exampleUploadedOrDerivedAudience);
        // to get back the UploadedOrDerivedAudience set earlier
        UploadedOrDerivedAudience testUploadedOrDerivedAudience = (UploadedOrDerivedAudience) exampleCreateAdAudienceRequest.getActualInstance();
    }
}
```


