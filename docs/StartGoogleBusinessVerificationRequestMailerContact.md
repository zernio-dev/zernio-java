

# StartGoogleBusinessVerificationRequestMailerContact

For ADDRESS (postcard) verification. The contact name Google prints on the postcard; an object is also accepted.

## anyOf schemas
* [Object](Object.md)
* [String](String.md)

## Example
```java
// Import classes:
import dev.zernio.model.StartGoogleBusinessVerificationRequestMailerContact;
import dev.zernio.model.Object;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        StartGoogleBusinessVerificationRequestMailerContact exampleStartGoogleBusinessVerificationRequestMailerContact = new StartGoogleBusinessVerificationRequestMailerContact();

        // create a new Object
        Object exampleObject = new Object();
        // set StartGoogleBusinessVerificationRequestMailerContact to Object
        exampleStartGoogleBusinessVerificationRequestMailerContact.setActualInstance(exampleObject);
        // to get back the Object set earlier
        Object testObject = (Object) exampleStartGoogleBusinessVerificationRequestMailerContact.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set StartGoogleBusinessVerificationRequestMailerContact to String
        exampleStartGoogleBusinessVerificationRequestMailerContact.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleStartGoogleBusinessVerificationRequestMailerContact.getActualInstance();
    }
}
```


