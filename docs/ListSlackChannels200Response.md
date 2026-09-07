

# ListSlackChannels200Response

## oneOf schemas
* [ChannelPicker](ChannelPicker.md)
* [StartOAuth](StartOAuth.md)

## Example
```java
// Import classes:
import dev.zernio.model.ListSlackChannels200Response;
import dev.zernio.model.ChannelPicker;
import dev.zernio.model.StartOAuth;

public class Example {
    public static void main(String[] args) {
        ListSlackChannels200Response exampleListSlackChannels200Response = new ListSlackChannels200Response();

        // create a new ChannelPicker
        ChannelPicker exampleChannelPicker = new ChannelPicker();
        // set ListSlackChannels200Response to ChannelPicker
        exampleListSlackChannels200Response.setActualInstance(exampleChannelPicker);
        // to get back the ChannelPicker set earlier
        ChannelPicker testChannelPicker = (ChannelPicker) exampleListSlackChannels200Response.getActualInstance();

        // create a new StartOAuth
        StartOAuth exampleStartOAuth = new StartOAuth();
        // set ListSlackChannels200Response to StartOAuth
        exampleListSlackChannels200Response.setActualInstance(exampleStartOAuth);
        // to get back the StartOAuth set earlier
        StartOAuth testStartOAuth = (StartOAuth) exampleListSlackChannels200Response.getActualInstance();
    }
}
```


