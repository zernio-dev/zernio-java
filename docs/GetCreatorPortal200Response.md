

# GetCreatorPortal200Response

## oneOf schemas
* [CreatorPortalInvite](CreatorPortalInvite.md)
* [CreatorPortalParticipant](CreatorPortalParticipant.md)

## Example
```java
// Import classes:
import dev.zernio.model.GetCreatorPortal200Response;
import dev.zernio.model.CreatorPortalInvite;
import dev.zernio.model.CreatorPortalParticipant;

public class Example {
    public static void main(String[] args) {
        GetCreatorPortal200Response exampleGetCreatorPortal200Response = new GetCreatorPortal200Response();

        // create a new CreatorPortalInvite
        CreatorPortalInvite exampleCreatorPortalInvite = new CreatorPortalInvite();
        // set GetCreatorPortal200Response to CreatorPortalInvite
        exampleGetCreatorPortal200Response.setActualInstance(exampleCreatorPortalInvite);
        // to get back the CreatorPortalInvite set earlier
        CreatorPortalInvite testCreatorPortalInvite = (CreatorPortalInvite) exampleGetCreatorPortal200Response.getActualInstance();

        // create a new CreatorPortalParticipant
        CreatorPortalParticipant exampleCreatorPortalParticipant = new CreatorPortalParticipant();
        // set GetCreatorPortal200Response to CreatorPortalParticipant
        exampleGetCreatorPortal200Response.setActualInstance(exampleCreatorPortalParticipant);
        // to get back the CreatorPortalParticipant set earlier
        CreatorPortalParticipant testCreatorPortalParticipant = (CreatorPortalParticipant) exampleGetCreatorPortal200Response.getActualInstance();
    }
}
```


