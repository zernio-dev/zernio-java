

# SendInboxMessage502Response

## anyOf schemas
* [ErrorResponse](ErrorResponse.md)
* [WhatsAppTemplateLookupError](WhatsAppTemplateLookupError.md)

## Example
```java
// Import classes:
import dev.zernio.model.SendInboxMessage502Response;
import dev.zernio.model.ErrorResponse;
import dev.zernio.model.WhatsAppTemplateLookupError;

public class Example {
    public static void main(String[] args) {
        SendInboxMessage502Response exampleSendInboxMessage502Response = new SendInboxMessage502Response();

        // create a new ErrorResponse
        ErrorResponse exampleErrorResponse = new ErrorResponse();
        // set SendInboxMessage502Response to ErrorResponse
        exampleSendInboxMessage502Response.setActualInstance(exampleErrorResponse);
        // to get back the ErrorResponse set earlier
        ErrorResponse testErrorResponse = (ErrorResponse) exampleSendInboxMessage502Response.getActualInstance();

        // create a new WhatsAppTemplateLookupError
        WhatsAppTemplateLookupError exampleWhatsAppTemplateLookupError = new WhatsAppTemplateLookupError();
        // set SendInboxMessage502Response to WhatsAppTemplateLookupError
        exampleSendInboxMessage502Response.setActualInstance(exampleWhatsAppTemplateLookupError);
        // to get back the WhatsAppTemplateLookupError set earlier
        WhatsAppTemplateLookupError testWhatsAppTemplateLookupError = (WhatsAppTemplateLookupError) exampleSendInboxMessage502Response.getActualInstance();
    }
}
```


