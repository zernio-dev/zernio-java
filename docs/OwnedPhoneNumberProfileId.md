

# OwnedPhoneNumberProfileId

The profile the number belongs to: `{ _id, name }` when the profile exists, otherwise its id.

## oneOf schemas
* [OwnedPhoneNumberProfileIdOneOf](OwnedPhoneNumberProfileIdOneOf.md)
* [String](String.md)

## Example
```java
// Import classes:
import dev.zernio.model.OwnedPhoneNumberProfileId;
import dev.zernio.model.OwnedPhoneNumberProfileIdOneOf;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        OwnedPhoneNumberProfileId exampleOwnedPhoneNumberProfileId = new OwnedPhoneNumberProfileId();

        // create a new OwnedPhoneNumberProfileIdOneOf
        OwnedPhoneNumberProfileIdOneOf exampleOwnedPhoneNumberProfileIdOneOf = new OwnedPhoneNumberProfileIdOneOf();
        // set OwnedPhoneNumberProfileId to OwnedPhoneNumberProfileIdOneOf
        exampleOwnedPhoneNumberProfileId.setActualInstance(exampleOwnedPhoneNumberProfileIdOneOf);
        // to get back the OwnedPhoneNumberProfileIdOneOf set earlier
        OwnedPhoneNumberProfileIdOneOf testOwnedPhoneNumberProfileIdOneOf = (OwnedPhoneNumberProfileIdOneOf) exampleOwnedPhoneNumberProfileId.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set OwnedPhoneNumberProfileId to String
        exampleOwnedPhoneNumberProfileId.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) exampleOwnedPhoneNumberProfileId.getActualInstance();
    }
}
```


