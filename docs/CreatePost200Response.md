

# CreatePost200Response

## oneOf schemas
* [PostCreateResponse](PostCreateResponse.md)
* [TikTokDryRunVerdict](TikTokDryRunVerdict.md)

## Example
```java
// Import classes:
import dev.zernio.model.CreatePost200Response;
import dev.zernio.model.PostCreateResponse;
import dev.zernio.model.TikTokDryRunVerdict;

public class Example {
    public static void main(String[] args) {
        CreatePost200Response exampleCreatePost200Response = new CreatePost200Response();

        // create a new PostCreateResponse
        PostCreateResponse examplePostCreateResponse = new PostCreateResponse();
        // set CreatePost200Response to PostCreateResponse
        exampleCreatePost200Response.setActualInstance(examplePostCreateResponse);
        // to get back the PostCreateResponse set earlier
        PostCreateResponse testPostCreateResponse = (PostCreateResponse) exampleCreatePost200Response.getActualInstance();

        // create a new TikTokDryRunVerdict
        TikTokDryRunVerdict exampleTikTokDryRunVerdict = new TikTokDryRunVerdict();
        // set CreatePost200Response to TikTokDryRunVerdict
        exampleCreatePost200Response.setActualInstance(exampleTikTokDryRunVerdict);
        // to get back the TikTokDryRunVerdict set earlier
        TikTokDryRunVerdict testTikTokDryRunVerdict = (TikTokDryRunVerdict) exampleCreatePost200Response.getActualInstance();
    }
}
```


