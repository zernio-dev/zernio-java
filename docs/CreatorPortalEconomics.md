

# CreatorPortalEconomics

How the campaign pays, without its budget. Amounts in cents. A pool campaign shows the pool size as `poolCents`.

## oneOf schemas
* [CPM](CPM.md)
* [PerPost](PerPost.md)
* [Pool](Pool.md)

## Example
```java
// Import classes:
import dev.zernio.model.CreatorPortalEconomics;
import dev.zernio.model.CPM;
import dev.zernio.model.PerPost;
import dev.zernio.model.Pool;

public class Example {
    public static void main(String[] args) {
        CreatorPortalEconomics exampleCreatorPortalEconomics = new CreatorPortalEconomics();

        // create a new CPM
        CPM exampleCPM = new CPM();
        // set CreatorPortalEconomics to CPM
        exampleCreatorPortalEconomics.setActualInstance(exampleCPM);
        // to get back the CPM set earlier
        CPM testCPM = (CPM) exampleCreatorPortalEconomics.getActualInstance();

        // create a new PerPost
        PerPost examplePerPost = new PerPost();
        // set CreatorPortalEconomics to PerPost
        exampleCreatorPortalEconomics.setActualInstance(examplePerPost);
        // to get back the PerPost set earlier
        PerPost testPerPost = (PerPost) exampleCreatorPortalEconomics.getActualInstance();

        // create a new Pool
        Pool examplePool = new Pool();
        // set CreatorPortalEconomics to Pool
        exampleCreatorPortalEconomics.setActualInstance(examplePool);
        // to get back the Pool set earlier
        Pool testPool = (Pool) exampleCreatorPortalEconomics.getActualInstance();
    }
}
```


