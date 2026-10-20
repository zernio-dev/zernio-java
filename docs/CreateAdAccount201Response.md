

# CreateAdAccount201Response

## oneOf schemas
* [CreatedGoogleAdAccount](CreatedGoogleAdAccount.md)
* [CreatedMetaAdAccount](CreatedMetaAdAccount.md)

## Example
```java
// Import classes:
import dev.zernio.model.CreateAdAccount201Response;
import dev.zernio.model.CreatedGoogleAdAccount;
import dev.zernio.model.CreatedMetaAdAccount;

public class Example {
    public static void main(String[] args) {
        CreateAdAccount201Response exampleCreateAdAccount201Response = new CreateAdAccount201Response();

        // create a new CreatedGoogleAdAccount
        CreatedGoogleAdAccount exampleCreatedGoogleAdAccount = new CreatedGoogleAdAccount();
        // set CreateAdAccount201Response to CreatedGoogleAdAccount
        exampleCreateAdAccount201Response.setActualInstance(exampleCreatedGoogleAdAccount);
        // to get back the CreatedGoogleAdAccount set earlier
        CreatedGoogleAdAccount testCreatedGoogleAdAccount = (CreatedGoogleAdAccount) exampleCreateAdAccount201Response.getActualInstance();

        // create a new CreatedMetaAdAccount
        CreatedMetaAdAccount exampleCreatedMetaAdAccount = new CreatedMetaAdAccount();
        // set CreateAdAccount201Response to CreatedMetaAdAccount
        exampleCreateAdAccount201Response.setActualInstance(exampleCreatedMetaAdAccount);
        // to get back the CreatedMetaAdAccount set earlier
        CreatedMetaAdAccount testCreatedMetaAdAccount = (CreatedMetaAdAccount) exampleCreateAdAccount201Response.getActualInstance();
    }
}
```


