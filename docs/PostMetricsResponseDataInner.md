

# PostMetricsResponseDataInner

## anyOf schemas
* [PostMetricAge](PostMetricAge.md)
* [PostMetricChange](PostMetricChange.md)
* [PostMetricFormat](PostMetricFormat.md)
* [PostMetricGroup](PostMetricGroup.md)
* [PostMetricRow](PostMetricRow.md)
* [PostMetricSlot](PostMetricSlot.md)

## Example
```java
// Import classes:
import dev.zernio.model.PostMetricsResponseDataInner;
import dev.zernio.model.PostMetricAge;
import dev.zernio.model.PostMetricChange;
import dev.zernio.model.PostMetricFormat;
import dev.zernio.model.PostMetricGroup;
import dev.zernio.model.PostMetricRow;
import dev.zernio.model.PostMetricSlot;

public class Example {
    public static void main(String[] args) {
        PostMetricsResponseDataInner examplePostMetricsResponseDataInner = new PostMetricsResponseDataInner();

        // create a new PostMetricAge
        PostMetricAge examplePostMetricAge = new PostMetricAge();
        // set PostMetricsResponseDataInner to PostMetricAge
        examplePostMetricsResponseDataInner.setActualInstance(examplePostMetricAge);
        // to get back the PostMetricAge set earlier
        PostMetricAge testPostMetricAge = (PostMetricAge) examplePostMetricsResponseDataInner.getActualInstance();

        // create a new PostMetricChange
        PostMetricChange examplePostMetricChange = new PostMetricChange();
        // set PostMetricsResponseDataInner to PostMetricChange
        examplePostMetricsResponseDataInner.setActualInstance(examplePostMetricChange);
        // to get back the PostMetricChange set earlier
        PostMetricChange testPostMetricChange = (PostMetricChange) examplePostMetricsResponseDataInner.getActualInstance();

        // create a new PostMetricFormat
        PostMetricFormat examplePostMetricFormat = new PostMetricFormat();
        // set PostMetricsResponseDataInner to PostMetricFormat
        examplePostMetricsResponseDataInner.setActualInstance(examplePostMetricFormat);
        // to get back the PostMetricFormat set earlier
        PostMetricFormat testPostMetricFormat = (PostMetricFormat) examplePostMetricsResponseDataInner.getActualInstance();

        // create a new PostMetricGroup
        PostMetricGroup examplePostMetricGroup = new PostMetricGroup();
        // set PostMetricsResponseDataInner to PostMetricGroup
        examplePostMetricsResponseDataInner.setActualInstance(examplePostMetricGroup);
        // to get back the PostMetricGroup set earlier
        PostMetricGroup testPostMetricGroup = (PostMetricGroup) examplePostMetricsResponseDataInner.getActualInstance();

        // create a new PostMetricRow
        PostMetricRow examplePostMetricRow = new PostMetricRow();
        // set PostMetricsResponseDataInner to PostMetricRow
        examplePostMetricsResponseDataInner.setActualInstance(examplePostMetricRow);
        // to get back the PostMetricRow set earlier
        PostMetricRow testPostMetricRow = (PostMetricRow) examplePostMetricsResponseDataInner.getActualInstance();

        // create a new PostMetricSlot
        PostMetricSlot examplePostMetricSlot = new PostMetricSlot();
        // set PostMetricsResponseDataInner to PostMetricSlot
        examplePostMetricsResponseDataInner.setActualInstance(examplePostMetricSlot);
        // to get back the PostMetricSlot set earlier
        PostMetricSlot testPostMetricSlot = (PostMetricSlot) examplePostMetricsResponseDataInner.getActualInstance();
    }
}
```


