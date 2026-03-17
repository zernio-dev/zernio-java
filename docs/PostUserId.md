

# PostUserId

## oneOf schemas
* [String](String.md)
* [User](User.md)

## Example
```java
// Import classes:
import dev.zernio.model.PostUserId;
import dev.zernio.model.String;
import dev.zernio.model.User;

public class Example {
    public static void main(String[] args) {
        PostUserId examplePostUserId = new PostUserId();

        // create a new String
        String exampleString = new String();
        // set PostUserId to String
        examplePostUserId.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) examplePostUserId.getActualInstance();

        // create a new User
        User exampleUser = new User();
        // set PostUserId to User
        examplePostUserId.setActualInstance(exampleUser);
        // to get back the User set earlier
        User testUser = (User) examplePostUserId.getActualInstance();
    }
}
```


