

# PostLogPostId

## oneOf schemas
* [PostLogPostIdOneOf](PostLogPostIdOneOf.md)
* [String](String.md)

## Example
```java
// Import classes:
import dev.zernio.model.PostLogPostId;
import dev.zernio.model.PostLogPostIdOneOf;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        PostLogPostId examplePostLogPostId = new PostLogPostId();

        // create a new PostLogPostIdOneOf
        PostLogPostIdOneOf examplePostLogPostIdOneOf = new PostLogPostIdOneOf();
        // set PostLogPostId to PostLogPostIdOneOf
        examplePostLogPostId.setActualInstance(examplePostLogPostIdOneOf);
        // to get back the PostLogPostIdOneOf set earlier
        PostLogPostIdOneOf testPostLogPostIdOneOf = (PostLogPostIdOneOf) examplePostLogPostId.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set PostLogPostId to String
        examplePostLogPostId.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) examplePostLogPostId.getActualInstance();
    }
}
```


