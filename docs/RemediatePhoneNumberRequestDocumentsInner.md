

# RemediatePhoneNumberRequestDocumentsInner

## oneOf schemas
* [RemediatePhoneNumberRequestDocumentsInnerOneOf](RemediatePhoneNumberRequestDocumentsInnerOneOf.md)
* [SubmitPhoneNumberKycRequestDocumentsInnerOneOf](SubmitPhoneNumberKycRequestDocumentsInnerOneOf.md)

## Example
```java
// Import classes:
import dev.zernio.model.RemediatePhoneNumberRequestDocumentsInner;
import dev.zernio.model.RemediatePhoneNumberRequestDocumentsInnerOneOf;
import dev.zernio.model.SubmitPhoneNumberKycRequestDocumentsInnerOneOf;

public class Example {
    public static void main(String[] args) {
        RemediatePhoneNumberRequestDocumentsInner exampleRemediatePhoneNumberRequestDocumentsInner = new RemediatePhoneNumberRequestDocumentsInner();

        // create a new RemediatePhoneNumberRequestDocumentsInnerOneOf
        RemediatePhoneNumberRequestDocumentsInnerOneOf exampleRemediatePhoneNumberRequestDocumentsInnerOneOf = new RemediatePhoneNumberRequestDocumentsInnerOneOf();
        // set RemediatePhoneNumberRequestDocumentsInner to RemediatePhoneNumberRequestDocumentsInnerOneOf
        exampleRemediatePhoneNumberRequestDocumentsInner.setActualInstance(exampleRemediatePhoneNumberRequestDocumentsInnerOneOf);
        // to get back the RemediatePhoneNumberRequestDocumentsInnerOneOf set earlier
        RemediatePhoneNumberRequestDocumentsInnerOneOf testRemediatePhoneNumberRequestDocumentsInnerOneOf = (RemediatePhoneNumberRequestDocumentsInnerOneOf) exampleRemediatePhoneNumberRequestDocumentsInner.getActualInstance();

        // create a new SubmitPhoneNumberKycRequestDocumentsInnerOneOf
        SubmitPhoneNumberKycRequestDocumentsInnerOneOf exampleSubmitPhoneNumberKycRequestDocumentsInnerOneOf = new SubmitPhoneNumberKycRequestDocumentsInnerOneOf();
        // set RemediatePhoneNumberRequestDocumentsInner to SubmitPhoneNumberKycRequestDocumentsInnerOneOf
        exampleRemediatePhoneNumberRequestDocumentsInner.setActualInstance(exampleSubmitPhoneNumberKycRequestDocumentsInnerOneOf);
        // to get back the SubmitPhoneNumberKycRequestDocumentsInnerOneOf set earlier
        SubmitPhoneNumberKycRequestDocumentsInnerOneOf testSubmitPhoneNumberKycRequestDocumentsInnerOneOf = (SubmitPhoneNumberKycRequestDocumentsInnerOneOf) exampleRemediatePhoneNumberRequestDocumentsInner.getActualInstance();
    }
}
```


