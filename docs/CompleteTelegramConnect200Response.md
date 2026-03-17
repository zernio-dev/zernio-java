

# CompleteTelegramConnect200Response

## oneOf schemas
* [Connected](Connected.md)
* [Expired](Expired.md)
* [Pending](Pending.md)

## Example
```java
// Import classes:
import dev.zernio.model.CompleteTelegramConnect200Response;
import dev.zernio.model.Connected;
import dev.zernio.model.Expired;
import dev.zernio.model.Pending;

public class Example {
    public static void main(String[] args) {
        CompleteTelegramConnect200Response exampleCompleteTelegramConnect200Response = new CompleteTelegramConnect200Response();

        // create a new Connected
        Connected exampleConnected = new Connected();
        // set CompleteTelegramConnect200Response to Connected
        exampleCompleteTelegramConnect200Response.setActualInstance(exampleConnected);
        // to get back the Connected set earlier
        Connected testConnected = (Connected) exampleCompleteTelegramConnect200Response.getActualInstance();

        // create a new Expired
        Expired exampleExpired = new Expired();
        // set CompleteTelegramConnect200Response to Expired
        exampleCompleteTelegramConnect200Response.setActualInstance(exampleExpired);
        // to get back the Expired set earlier
        Expired testExpired = (Expired) exampleCompleteTelegramConnect200Response.getActualInstance();

        // create a new Pending
        Pending examplePending = new Pending();
        // set CompleteTelegramConnect200Response to Pending
        exampleCompleteTelegramConnect200Response.setActualInstance(examplePending);
        // to get back the Pending set earlier
        Pending testPending = (Pending) exampleCompleteTelegramConnect200Response.getActualInstance();
    }
}
```


