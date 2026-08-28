

# UsageMeteringScope

Present with `profileId` / `accountId`: echoes the group the payload was projected onto.

## oneOf schemas
* [DeleteInboxReviewReplyRequest](DeleteInboxReviewReplyRequest.md)
* [UsageMeteringScopeOneOf](UsageMeteringScopeOneOf.md)

## Example
```java
// Import classes:
import dev.zernio.model.UsageMeteringScope;
import dev.zernio.model.DeleteInboxReviewReplyRequest;
import dev.zernio.model.UsageMeteringScopeOneOf;

public class Example {
    public static void main(String[] args) {
        UsageMeteringScope exampleUsageMeteringScope = new UsageMeteringScope();

        // create a new DeleteInboxReviewReplyRequest
        DeleteInboxReviewReplyRequest exampleDeleteInboxReviewReplyRequest = new DeleteInboxReviewReplyRequest();
        // set UsageMeteringScope to DeleteInboxReviewReplyRequest
        exampleUsageMeteringScope.setActualInstance(exampleDeleteInboxReviewReplyRequest);
        // to get back the DeleteInboxReviewReplyRequest set earlier
        DeleteInboxReviewReplyRequest testDeleteInboxReviewReplyRequest = (DeleteInboxReviewReplyRequest) exampleUsageMeteringScope.getActualInstance();

        // create a new UsageMeteringScopeOneOf
        UsageMeteringScopeOneOf exampleUsageMeteringScopeOneOf = new UsageMeteringScopeOneOf();
        // set UsageMeteringScope to UsageMeteringScopeOneOf
        exampleUsageMeteringScope.setActualInstance(exampleUsageMeteringScopeOneOf);
        // to get back the UsageMeteringScopeOneOf set earlier
        UsageMeteringScopeOneOf testUsageMeteringScopeOneOf = (UsageMeteringScopeOneOf) exampleUsageMeteringScope.getActualInstance();
    }
}
```


