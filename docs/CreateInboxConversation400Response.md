

# CreateInboxConversation400Response

## anyOf schemas
* [CreateInboxConversation400ResponseAnyOf](CreateInboxConversation400ResponseAnyOf.md)
* [WhatsAppTemplateLookupError](WhatsAppTemplateLookupError.md)

## Example
```java
// Import classes:
import dev.zernio.model.CreateInboxConversation400Response;
import dev.zernio.model.CreateInboxConversation400ResponseAnyOf;
import dev.zernio.model.WhatsAppTemplateLookupError;

public class Example {
    public static void main(String[] args) {
        CreateInboxConversation400Response exampleCreateInboxConversation400Response = new CreateInboxConversation400Response();

        // create a new CreateInboxConversation400ResponseAnyOf
        CreateInboxConversation400ResponseAnyOf exampleCreateInboxConversation400ResponseAnyOf = new CreateInboxConversation400ResponseAnyOf();
        // set CreateInboxConversation400Response to CreateInboxConversation400ResponseAnyOf
        exampleCreateInboxConversation400Response.setActualInstance(exampleCreateInboxConversation400ResponseAnyOf);
        // to get back the CreateInboxConversation400ResponseAnyOf set earlier
        CreateInboxConversation400ResponseAnyOf testCreateInboxConversation400ResponseAnyOf = (CreateInboxConversation400ResponseAnyOf) exampleCreateInboxConversation400Response.getActualInstance();

        // create a new WhatsAppTemplateLookupError
        WhatsAppTemplateLookupError exampleWhatsAppTemplateLookupError = new WhatsAppTemplateLookupError();
        // set CreateInboxConversation400Response to WhatsAppTemplateLookupError
        exampleCreateInboxConversation400Response.setActualInstance(exampleWhatsAppTemplateLookupError);
        // to get back the WhatsAppTemplateLookupError set earlier
        WhatsAppTemplateLookupError testWhatsAppTemplateLookupError = (WhatsAppTemplateLookupError) exampleCreateInboxConversation400Response.getActualInstance();
    }
}
```


