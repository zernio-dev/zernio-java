

# RemediateWhatsAppNumberRequestDocumentsInner

## oneOf schemas
* [RemediateWhatsAppNumberRequestDocumentsInnerOneOf](RemediateWhatsAppNumberRequestDocumentsInnerOneOf.md)
* [SubmitWhatsAppNumberKycRequestDocumentsInnerOneOf](SubmitWhatsAppNumberKycRequestDocumentsInnerOneOf.md)

## Example
```java
// Import classes:
import dev.zernio.model.RemediateWhatsAppNumberRequestDocumentsInner;
import dev.zernio.model.RemediateWhatsAppNumberRequestDocumentsInnerOneOf;
import dev.zernio.model.SubmitWhatsAppNumberKycRequestDocumentsInnerOneOf;

public class Example {
    public static void main(String[] args) {
        RemediateWhatsAppNumberRequestDocumentsInner exampleRemediateWhatsAppNumberRequestDocumentsInner = new RemediateWhatsAppNumberRequestDocumentsInner();

        // create a new RemediateWhatsAppNumberRequestDocumentsInnerOneOf
        RemediateWhatsAppNumberRequestDocumentsInnerOneOf exampleRemediateWhatsAppNumberRequestDocumentsInnerOneOf = new RemediateWhatsAppNumberRequestDocumentsInnerOneOf();
        // set RemediateWhatsAppNumberRequestDocumentsInner to RemediateWhatsAppNumberRequestDocumentsInnerOneOf
        exampleRemediateWhatsAppNumberRequestDocumentsInner.setActualInstance(exampleRemediateWhatsAppNumberRequestDocumentsInnerOneOf);
        // to get back the RemediateWhatsAppNumberRequestDocumentsInnerOneOf set earlier
        RemediateWhatsAppNumberRequestDocumentsInnerOneOf testRemediateWhatsAppNumberRequestDocumentsInnerOneOf = (RemediateWhatsAppNumberRequestDocumentsInnerOneOf) exampleRemediateWhatsAppNumberRequestDocumentsInner.getActualInstance();

        // create a new SubmitWhatsAppNumberKycRequestDocumentsInnerOneOf
        SubmitWhatsAppNumberKycRequestDocumentsInnerOneOf exampleSubmitWhatsAppNumberKycRequestDocumentsInnerOneOf = new SubmitWhatsAppNumberKycRequestDocumentsInnerOneOf();
        // set RemediateWhatsAppNumberRequestDocumentsInner to SubmitWhatsAppNumberKycRequestDocumentsInnerOneOf
        exampleRemediateWhatsAppNumberRequestDocumentsInner.setActualInstance(exampleSubmitWhatsAppNumberKycRequestDocumentsInnerOneOf);
        // to get back the SubmitWhatsAppNumberKycRequestDocumentsInnerOneOf set earlier
        SubmitWhatsAppNumberKycRequestDocumentsInnerOneOf testSubmitWhatsAppNumberKycRequestDocumentsInnerOneOf = (SubmitWhatsAppNumberKycRequestDocumentsInnerOneOf) exampleRemediateWhatsAppNumberRequestDocumentsInner.getActualInstance();
    }
}
```


