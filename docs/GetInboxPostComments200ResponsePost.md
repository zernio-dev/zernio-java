

# GetInboxPostComments200ResponsePost

(Reddit, Facebook and Instagram) Metadata for the target post, returned with the comments so you can render a preview without another request.  **Facebook and Instagram** return the Meta shape: post thumbnail, text and permalink, for any post the account can read, including hidden dark posts Meta publishes per ad variant (dynamic creative, placement asset customization, Advantage+).  - Facebook posts need the Facebook Page connection; Instagram media the Instagram connection. - `thumbnailUrl` and `mediaUrl` are expiring Meta CDN URLs: store a copy to render them later. - On Instagram, `productType` tells an ad (`AD`) from organic media (`FEED`, `REELS`, `STORY`).  **Absent** on other platforms, when the connection's token cannot read the post, and on Reddit when the upstream response lacks the post listing (deleted post, malformed response). 

## anyOf schemas
* [FacebookOrInstagramPost](FacebookOrInstagramPost.md)
* [RedditPost](RedditPost.md)

NOTE: this class is nullable.

## Example
```java
// Import classes:
import dev.zernio.model.GetInboxPostComments200ResponsePost;
import dev.zernio.model.FacebookOrInstagramPost;
import dev.zernio.model.RedditPost;

public class Example {
    public static void main(String[] args) {
        GetInboxPostComments200ResponsePost exampleGetInboxPostComments200ResponsePost = new GetInboxPostComments200ResponsePost();

        // create a new FacebookOrInstagramPost
        FacebookOrInstagramPost exampleFacebookOrInstagramPost = new FacebookOrInstagramPost();
        // set GetInboxPostComments200ResponsePost to FacebookOrInstagramPost
        exampleGetInboxPostComments200ResponsePost.setActualInstance(exampleFacebookOrInstagramPost);
        // to get back the FacebookOrInstagramPost set earlier
        FacebookOrInstagramPost testFacebookOrInstagramPost = (FacebookOrInstagramPost) exampleGetInboxPostComments200ResponsePost.getActualInstance();

        // create a new RedditPost
        RedditPost exampleRedditPost = new RedditPost();
        // set GetInboxPostComments200ResponsePost to RedditPost
        exampleGetInboxPostComments200ResponsePost.setActualInstance(exampleRedditPost);
        // to get back the RedditPost set earlier
        RedditPost testRedditPost = (RedditPost) exampleGetInboxPostComments200ResponsePost.getActualInstance();
    }
}
```


