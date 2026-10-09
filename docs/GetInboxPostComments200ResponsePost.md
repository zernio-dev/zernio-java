

# GetInboxPostComments200ResponsePost

(Reddit, Facebook and Instagram) Metadata for the target post, returned alongside the comments so integrators can render a preview of the post being commented on without an additional request.  Facebook and Instagram return the Meta shape: the post thumbnail, text and permalink, for any post the account can read, including the hidden dark posts Meta publishes for each variant of an ad (dynamic creative, placement asset customization, Advantage+). Facebook posts need the Facebook Page connection and Instagram media the Instagram connection. `thumbnailUrl` and `mediaUrl` are Meta CDN URLs that expire: store a copy if you render them later. On Instagram, `productType` tells an ad (`AD`) from organic media (`FEED`, `REELS`, `STORY`).  Absent on other platforms, when the post cannot be read with the connection's token, and on Reddit when the upstream response is missing the post listing (deleted post, malformed response). 

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


