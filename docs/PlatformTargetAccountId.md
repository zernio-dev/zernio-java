

# PlatformTargetAccountId

## oneOf schemas
* [SocialAccount](SocialAccount.md)
* [String](String.md)

## Example
```java
// Import classes:
import dev.zernio.model.PlatformTargetAccountId;
import dev.zernio.model.SocialAccount;
import dev.zernio.model.String;

public class Example {
    public static void main(String[] args) {
        PlatformTargetAccountId examplePlatformTargetAccountId = new PlatformTargetAccountId();

        // create a new SocialAccount
        SocialAccount exampleSocialAccount = new SocialAccount();
        // set PlatformTargetAccountId to SocialAccount
        examplePlatformTargetAccountId.setActualInstance(exampleSocialAccount);
        // to get back the SocialAccount set earlier
        SocialAccount testSocialAccount = (SocialAccount) examplePlatformTargetAccountId.getActualInstance();

        // create a new String
        String exampleString = new String();
        // set PlatformTargetAccountId to String
        examplePlatformTargetAccountId.setActualInstance(exampleString);
        // to get back the String set earlier
        String testString = (String) examplePlatformTargetAccountId.getActualInstance();
    }
}
```


