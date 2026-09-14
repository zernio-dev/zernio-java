

# CreateInboxConversation422Response

## anyOf schemas
* [CreateInboxConversation422ResponseAnyOf](CreateInboxConversation422ResponseAnyOf.md)
* [WhatsAppTemplateLookupError](WhatsAppTemplateLookupError.md)

## Example
```java
// Import classes:
import dev.zernio.model.CreateInboxConversation422Response;
import dev.zernio.model.CreateInboxConversation422ResponseAnyOf;
import dev.zernio.model.WhatsAppTemplateLookupError;

public class Example {
    public static void main(String[] args) {
        CreateInboxConversation422Response exampleCreateInboxConversation422Response = new CreateInboxConversation422Response();

        // create a new CreateInboxConversation422ResponseAnyOf
        CreateInboxConversation422ResponseAnyOf exampleCreateInboxConversation422ResponseAnyOf = new CreateInboxConversation422ResponseAnyOf();
        // set CreateInboxConversation422Response to CreateInboxConversation422ResponseAnyOf
        exampleCreateInboxConversation422Response.setActualInstance(exampleCreateInboxConversation422ResponseAnyOf);
        // to get back the CreateInboxConversation422ResponseAnyOf set earlier
        CreateInboxConversation422ResponseAnyOf testCreateInboxConversation422ResponseAnyOf = (CreateInboxConversation422ResponseAnyOf) exampleCreateInboxConversation422Response.getActualInstance();

        // create a new WhatsAppTemplateLookupError
        WhatsAppTemplateLookupError exampleWhatsAppTemplateLookupError = new WhatsAppTemplateLookupError();
        // set CreateInboxConversation422Response to WhatsAppTemplateLookupError
        exampleCreateInboxConversation422Response.setActualInstance(exampleWhatsAppTemplateLookupError);
        // to get back the WhatsAppTemplateLookupError set earlier
        WhatsAppTemplateLookupError testWhatsAppTemplateLookupError = (WhatsAppTemplateLookupError) exampleCreateInboxConversation422Response.getActualInstance();
    }
}
```


