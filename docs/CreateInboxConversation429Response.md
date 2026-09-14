

# CreateInboxConversation429Response

## anyOf schemas
* [CreateInboxConversation429ResponseAnyOf](CreateInboxConversation429ResponseAnyOf.md)
* [WhatsAppTemplateLookupError](WhatsAppTemplateLookupError.md)

## Example
```java
// Import classes:
import dev.zernio.model.CreateInboxConversation429Response;
import dev.zernio.model.CreateInboxConversation429ResponseAnyOf;
import dev.zernio.model.WhatsAppTemplateLookupError;

public class Example {
    public static void main(String[] args) {
        CreateInboxConversation429Response exampleCreateInboxConversation429Response = new CreateInboxConversation429Response();

        // create a new CreateInboxConversation429ResponseAnyOf
        CreateInboxConversation429ResponseAnyOf exampleCreateInboxConversation429ResponseAnyOf = new CreateInboxConversation429ResponseAnyOf();
        // set CreateInboxConversation429Response to CreateInboxConversation429ResponseAnyOf
        exampleCreateInboxConversation429Response.setActualInstance(exampleCreateInboxConversation429ResponseAnyOf);
        // to get back the CreateInboxConversation429ResponseAnyOf set earlier
        CreateInboxConversation429ResponseAnyOf testCreateInboxConversation429ResponseAnyOf = (CreateInboxConversation429ResponseAnyOf) exampleCreateInboxConversation429Response.getActualInstance();

        // create a new WhatsAppTemplateLookupError
        WhatsAppTemplateLookupError exampleWhatsAppTemplateLookupError = new WhatsAppTemplateLookupError();
        // set CreateInboxConversation429Response to WhatsAppTemplateLookupError
        exampleCreateInboxConversation429Response.setActualInstance(exampleWhatsAppTemplateLookupError);
        // to get back the WhatsAppTemplateLookupError set earlier
        WhatsAppTemplateLookupError testWhatsAppTemplateLookupError = (WhatsAppTemplateLookupError) exampleCreateInboxConversation429Response.getActualInstance();
    }
}
```


