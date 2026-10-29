

# CreatorCampaignEconomics

How the campaign pays, picked by `type`. Amounts are USD cents.  Every type carries `budgetCents`, the most the campaign can pay out in total. Once earnings reach it, the campaign stops accruing and `creator_campaign.budget_exhausted` fires.  - `cpm`: `ratePer1kCents` per 1,000 eligible views, earned from `minViewsToEarn` views on, capped per post by `maxPayoutPerClipCents`. - `per_post`: `perApprovedPostCents` for each approved post, at most `maxPostsPerParticipant` per participant. - `pool`: `budgetCents` is split at close among approved posts by eligible views; a post needs `minViewsToQualify` views to share. 

## oneOf schemas
* [CreatorCampaignEconomicsCpm](CreatorCampaignEconomicsCpm.md)
* [CreatorCampaignEconomicsPerPost](CreatorCampaignEconomicsPerPost.md)
* [CreatorCampaignEconomicsPool](CreatorCampaignEconomicsPool.md)

## Example
```java
// Import classes:
import dev.zernio.model.CreatorCampaignEconomics;
import dev.zernio.model.CreatorCampaignEconomicsCpm;
import dev.zernio.model.CreatorCampaignEconomicsPerPost;
import dev.zernio.model.CreatorCampaignEconomicsPool;

public class Example {
    public static void main(String[] args) {
        CreatorCampaignEconomics exampleCreatorCampaignEconomics = new CreatorCampaignEconomics();

        // create a new CreatorCampaignEconomicsCpm
        CreatorCampaignEconomicsCpm exampleCreatorCampaignEconomicsCpm = new CreatorCampaignEconomicsCpm();
        // set CreatorCampaignEconomics to CreatorCampaignEconomicsCpm
        exampleCreatorCampaignEconomics.setActualInstance(exampleCreatorCampaignEconomicsCpm);
        // to get back the CreatorCampaignEconomicsCpm set earlier
        CreatorCampaignEconomicsCpm testCreatorCampaignEconomicsCpm = (CreatorCampaignEconomicsCpm) exampleCreatorCampaignEconomics.getActualInstance();

        // create a new CreatorCampaignEconomicsPerPost
        CreatorCampaignEconomicsPerPost exampleCreatorCampaignEconomicsPerPost = new CreatorCampaignEconomicsPerPost();
        // set CreatorCampaignEconomics to CreatorCampaignEconomicsPerPost
        exampleCreatorCampaignEconomics.setActualInstance(exampleCreatorCampaignEconomicsPerPost);
        // to get back the CreatorCampaignEconomicsPerPost set earlier
        CreatorCampaignEconomicsPerPost testCreatorCampaignEconomicsPerPost = (CreatorCampaignEconomicsPerPost) exampleCreatorCampaignEconomics.getActualInstance();

        // create a new CreatorCampaignEconomicsPool
        CreatorCampaignEconomicsPool exampleCreatorCampaignEconomicsPool = new CreatorCampaignEconomicsPool();
        // set CreatorCampaignEconomics to CreatorCampaignEconomicsPool
        exampleCreatorCampaignEconomics.setActualInstance(exampleCreatorCampaignEconomicsPool);
        // to get back the CreatorCampaignEconomicsPool set earlier
        CreatorCampaignEconomicsPool testCreatorCampaignEconomicsPool = (CreatorCampaignEconomicsPool) exampleCreatorCampaignEconomics.getActualInstance();
    }
}
```


