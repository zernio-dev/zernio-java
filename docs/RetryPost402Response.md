

# RetryPost402Response

## anyOf schemas
* [BalanceRequiredError](BalanceRequiredError.md)
* [GetYouTubeDailyViews400Response](GetYouTubeDailyViews400Response.md)

## Example
```java
// Import classes:
import dev.zernio.model.RetryPost402Response;
import dev.zernio.model.BalanceRequiredError;
import dev.zernio.model.GetYouTubeDailyViews400Response;

public class Example {
    public static void main(String[] args) {
        RetryPost402Response exampleRetryPost402Response = new RetryPost402Response();

        // create a new BalanceRequiredError
        BalanceRequiredError exampleBalanceRequiredError = new BalanceRequiredError();
        // set RetryPost402Response to BalanceRequiredError
        exampleRetryPost402Response.setActualInstance(exampleBalanceRequiredError);
        // to get back the BalanceRequiredError set earlier
        BalanceRequiredError testBalanceRequiredError = (BalanceRequiredError) exampleRetryPost402Response.getActualInstance();

        // create a new GetYouTubeDailyViews400Response
        GetYouTubeDailyViews400Response exampleGetYouTubeDailyViews400Response = new GetYouTubeDailyViews400Response();
        // set RetryPost402Response to GetYouTubeDailyViews400Response
        exampleRetryPost402Response.setActualInstance(exampleGetYouTubeDailyViews400Response);
        // to get back the GetYouTubeDailyViews400Response set earlier
        GetYouTubeDailyViews400Response testGetYouTubeDailyViews400Response = (GetYouTubeDailyViews400Response) exampleRetryPost402Response.getActualInstance();
    }
}
```


