

# CreateInboxConversation404Response

## anyOf schemas
* [CreateInboxConversation404ResponseAnyOf](CreateInboxConversation404ResponseAnyOf.md)
* [WhatsAppTemplateLookupError](WhatsAppTemplateLookupError.md)

## Example
```java
// Import classes:
import dev.zernio.model.CreateInboxConversation404Response;
import dev.zernio.model.CreateInboxConversation404ResponseAnyOf;
import dev.zernio.model.WhatsAppTemplateLookupError;

public class Example {
    public static void main(String[] args) {
        CreateInboxConversation404Response exampleCreateInboxConversation404Response = new CreateInboxConversation404Response();

        // create a new CreateInboxConversation404ResponseAnyOf
        CreateInboxConversation404ResponseAnyOf exampleCreateInboxConversation404ResponseAnyOf = new CreateInboxConversation404ResponseAnyOf();
        // set CreateInboxConversation404Response to CreateInboxConversation404ResponseAnyOf
        exampleCreateInboxConversation404Response.setActualInstance(exampleCreateInboxConversation404ResponseAnyOf);
        // to get back the CreateInboxConversation404ResponseAnyOf set earlier
        CreateInboxConversation404ResponseAnyOf testCreateInboxConversation404ResponseAnyOf = (CreateInboxConversation404ResponseAnyOf) exampleCreateInboxConversation404Response.getActualInstance();

        // create a new WhatsAppTemplateLookupError
        WhatsAppTemplateLookupError exampleWhatsAppTemplateLookupError = new WhatsAppTemplateLookupError();
        // set CreateInboxConversation404Response to WhatsAppTemplateLookupError
        exampleCreateInboxConversation404Response.setActualInstance(exampleWhatsAppTemplateLookupError);
        // to get back the WhatsAppTemplateLookupError set earlier
        WhatsAppTemplateLookupError testWhatsAppTemplateLookupError = (WhatsAppTemplateLookupError) exampleCreateInboxConversation404Response.getActualInstance();
    }
}
```


