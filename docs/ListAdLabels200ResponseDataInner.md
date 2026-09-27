

# ListAdLabels200ResponseDataInner

## oneOf schemas
* [GoogleAdLabel](GoogleAdLabel.md)
* [Object](Object.md)

## Example
```java
// Import classes:
import dev.zernio.model.ListAdLabels200ResponseDataInner;
import dev.zernio.model.GoogleAdLabel;
import dev.zernio.model.Object;

public class Example {
    public static void main(String[] args) {
        ListAdLabels200ResponseDataInner exampleListAdLabels200ResponseDataInner = new ListAdLabels200ResponseDataInner();

        // create a new GoogleAdLabel
        GoogleAdLabel exampleGoogleAdLabel = new GoogleAdLabel();
        // set ListAdLabels200ResponseDataInner to GoogleAdLabel
        exampleListAdLabels200ResponseDataInner.setActualInstance(exampleGoogleAdLabel);
        // to get back the GoogleAdLabel set earlier
        GoogleAdLabel testGoogleAdLabel = (GoogleAdLabel) exampleListAdLabels200ResponseDataInner.getActualInstance();

        // create a new Object
        Object exampleObject = new Object();
        // set ListAdLabels200ResponseDataInner to Object
        exampleListAdLabels200ResponseDataInner.setActualInstance(exampleObject);
        // to get back the Object set earlier
        Object testObject = (Object) exampleListAdLabels200ResponseDataInner.getActualInstance();
    }
}
```


