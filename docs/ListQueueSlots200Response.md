

# ListQueueSlots200Response

## oneOf schemas
* [ListQueueSlots200ResponseOneOf](ListQueueSlots200ResponseOneOf.md)
* [QueueSlotsResponse](QueueSlotsResponse.md)

## Example
```java
// Import classes:
import dev.zernio.model.ListQueueSlots200Response;
import dev.zernio.model.ListQueueSlots200ResponseOneOf;
import dev.zernio.model.QueueSlotsResponse;

public class Example {
    public static void main(String[] args) {
        ListQueueSlots200Response exampleListQueueSlots200Response = new ListQueueSlots200Response();

        // create a new ListQueueSlots200ResponseOneOf
        ListQueueSlots200ResponseOneOf exampleListQueueSlots200ResponseOneOf = new ListQueueSlots200ResponseOneOf();
        // set ListQueueSlots200Response to ListQueueSlots200ResponseOneOf
        exampleListQueueSlots200Response.setActualInstance(exampleListQueueSlots200ResponseOneOf);
        // to get back the ListQueueSlots200ResponseOneOf set earlier
        ListQueueSlots200ResponseOneOf testListQueueSlots200ResponseOneOf = (ListQueueSlots200ResponseOneOf) exampleListQueueSlots200Response.getActualInstance();

        // create a new QueueSlotsResponse
        QueueSlotsResponse exampleQueueSlotsResponse = new QueueSlotsResponse();
        // set ListQueueSlots200Response to QueueSlotsResponse
        exampleListQueueSlots200Response.setActualInstance(exampleQueueSlotsResponse);
        // to get back the QueueSlotsResponse set earlier
        QueueSlotsResponse testQueueSlotsResponse = (QueueSlotsResponse) exampleListQueueSlots200Response.getActualInstance();
    }
}
```


