

# GetLeadForm200ResponseForm

## oneOf schemas
* [MetaLeadForm](MetaLeadForm.md)
* [Object](Object.md)

## Example
```java
// Import classes:
import dev.zernio.model.GetLeadForm200ResponseForm;
import dev.zernio.model.MetaLeadForm;
import dev.zernio.model.Object;

public class Example {
    public static void main(String[] args) {
        GetLeadForm200ResponseForm exampleGetLeadForm200ResponseForm = new GetLeadForm200ResponseForm();

        // create a new MetaLeadForm
        MetaLeadForm exampleMetaLeadForm = new MetaLeadForm();
        // set GetLeadForm200ResponseForm to MetaLeadForm
        exampleGetLeadForm200ResponseForm.setActualInstance(exampleMetaLeadForm);
        // to get back the MetaLeadForm set earlier
        MetaLeadForm testMetaLeadForm = (MetaLeadForm) exampleGetLeadForm200ResponseForm.getActualInstance();

        // create a new Object
        Object exampleObject = new Object();
        // set GetLeadForm200ResponseForm to Object
        exampleGetLeadForm200ResponseForm.setActualInstance(exampleObject);
        // to get back the Object set earlier
        Object testObject = (Object) exampleGetLeadForm200ResponseForm.getActualInstance();
    }
}
```


