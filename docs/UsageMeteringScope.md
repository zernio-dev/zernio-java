

# UsageMeteringScope

Present with `profileId` / `externalId` / `accountId`: echoes the group the payload was projected onto. A profile scope carries both ids.

## oneOf schemas
* [DeleteInboxReviewReplyRequest](DeleteInboxReviewReplyRequest.md)
* [UsageProfileRef](UsageProfileRef.md)

## Example
```java
// Import classes:
import dev.zernio.model.UsageMeteringScope;
import dev.zernio.model.DeleteInboxReviewReplyRequest;
import dev.zernio.model.UsageProfileRef;

public class Example {
    public static void main(String[] args) {
        UsageMeteringScope exampleUsageMeteringScope = new UsageMeteringScope();

        // create a new DeleteInboxReviewReplyRequest
        DeleteInboxReviewReplyRequest exampleDeleteInboxReviewReplyRequest = new DeleteInboxReviewReplyRequest();
        // set UsageMeteringScope to DeleteInboxReviewReplyRequest
        exampleUsageMeteringScope.setActualInstance(exampleDeleteInboxReviewReplyRequest);
        // to get back the DeleteInboxReviewReplyRequest set earlier
        DeleteInboxReviewReplyRequest testDeleteInboxReviewReplyRequest = (DeleteInboxReviewReplyRequest) exampleUsageMeteringScope.getActualInstance();

        // create a new UsageProfileRef
        UsageProfileRef exampleUsageProfileRef = new UsageProfileRef();
        // set UsageMeteringScope to UsageProfileRef
        exampleUsageMeteringScope.setActualInstance(exampleUsageProfileRef);
        // to get back the UsageProfileRef set earlier
        UsageProfileRef testUsageProfileRef = (UsageProfileRef) exampleUsageMeteringScope.getActualInstance();
    }
}
```


