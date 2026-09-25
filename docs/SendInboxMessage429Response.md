

# SendInboxMessage429Response

## anyOf schemas
* [ErrorResponse](ErrorResponse.md)
* [WhatsAppTemplateLookupError](WhatsAppTemplateLookupError.md)

## Example
```java
// Import classes:
import dev.zernio.model.SendInboxMessage429Response;
import dev.zernio.model.ErrorResponse;
import dev.zernio.model.WhatsAppTemplateLookupError;

public class Example {
    public static void main(String[] args) {
        SendInboxMessage429Response exampleSendInboxMessage429Response = new SendInboxMessage429Response();

        // create a new ErrorResponse
        ErrorResponse exampleErrorResponse = new ErrorResponse();
        // set SendInboxMessage429Response to ErrorResponse
        exampleSendInboxMessage429Response.setActualInstance(exampleErrorResponse);
        // to get back the ErrorResponse set earlier
        ErrorResponse testErrorResponse = (ErrorResponse) exampleSendInboxMessage429Response.getActualInstance();

        // create a new WhatsAppTemplateLookupError
        WhatsAppTemplateLookupError exampleWhatsAppTemplateLookupError = new WhatsAppTemplateLookupError();
        // set SendInboxMessage429Response to WhatsAppTemplateLookupError
        exampleSendInboxMessage429Response.setActualInstance(exampleWhatsAppTemplateLookupError);
        // to get back the WhatsAppTemplateLookupError set earlier
        WhatsAppTemplateLookupError testWhatsAppTemplateLookupError = (WhatsAppTemplateLookupError) exampleSendInboxMessage429Response.getActualInstance();
    }
}
```


