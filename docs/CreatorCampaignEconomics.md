

# CreatorCampaignEconomics

How the campaign pays, picked by `type`. Amounts are USD cents.  Every type carries `budgetCents`, the most the campaign can pay out in total. Once earnings reach it, the campaign stops accruing and `creator_campaign.budget_exhausted` fires.  - `cpm`: `ratePer1kCents` per 1,000 of the counted `metric` (views by default), earned once a post reaches `minViewsToEarn` of it, capped per post by `maxPayoutPerClipCents`. - `per_post`: `perApprovedPostCents` for each approved post, at most `maxPostsPerParticipant` per participant. - `pool`: `budgetCents` is split at close among approved posts by eligible views; a post needs `minViewsToQualify` views to share. - `ad_performance`: pays on the results of the ads that run each post (see `GET /v1/creator-campaigns/{campaignId}/ad-results`), counted once a day through the previous UTC day. Only Instagram, Facebook and TikTok posts. - `retainer`: `amountCents` per `period` once the creator has `requiredApprovedPosts` approved posts in it. `mode: smart` tops the period's commission up to `amountCents`. - `commission`: a share of the sales of the linked store (`storeAccountId`) credited to each creator by their discount code or tracking link. 

## oneOf schemas
* [CreatorCampaignEconomicsAdPerformance](CreatorCampaignEconomicsAdPerformance.md)
* [CreatorCampaignEconomicsCommission](CreatorCampaignEconomicsCommission.md)
* [CreatorCampaignEconomicsCpm](CreatorCampaignEconomicsCpm.md)
* [CreatorCampaignEconomicsPerPost](CreatorCampaignEconomicsPerPost.md)
* [CreatorCampaignEconomicsPool](CreatorCampaignEconomicsPool.md)
* [CreatorCampaignEconomicsRetainer](CreatorCampaignEconomicsRetainer.md)

## Example
```java
// Import classes:
import dev.zernio.model.CreatorCampaignEconomics;
import dev.zernio.model.CreatorCampaignEconomicsAdPerformance;
import dev.zernio.model.CreatorCampaignEconomicsCommission;
import dev.zernio.model.CreatorCampaignEconomicsCpm;
import dev.zernio.model.CreatorCampaignEconomicsPerPost;
import dev.zernio.model.CreatorCampaignEconomicsPool;
import dev.zernio.model.CreatorCampaignEconomicsRetainer;

public class Example {
    public static void main(String[] args) {
        CreatorCampaignEconomics exampleCreatorCampaignEconomics = new CreatorCampaignEconomics();

        // create a new CreatorCampaignEconomicsAdPerformance
        CreatorCampaignEconomicsAdPerformance exampleCreatorCampaignEconomicsAdPerformance = new CreatorCampaignEconomicsAdPerformance();
        // set CreatorCampaignEconomics to CreatorCampaignEconomicsAdPerformance
        exampleCreatorCampaignEconomics.setActualInstance(exampleCreatorCampaignEconomicsAdPerformance);
        // to get back the CreatorCampaignEconomicsAdPerformance set earlier
        CreatorCampaignEconomicsAdPerformance testCreatorCampaignEconomicsAdPerformance = (CreatorCampaignEconomicsAdPerformance) exampleCreatorCampaignEconomics.getActualInstance();

        // create a new CreatorCampaignEconomicsCommission
        CreatorCampaignEconomicsCommission exampleCreatorCampaignEconomicsCommission = new CreatorCampaignEconomicsCommission();
        // set CreatorCampaignEconomics to CreatorCampaignEconomicsCommission
        exampleCreatorCampaignEconomics.setActualInstance(exampleCreatorCampaignEconomicsCommission);
        // to get back the CreatorCampaignEconomicsCommission set earlier
        CreatorCampaignEconomicsCommission testCreatorCampaignEconomicsCommission = (CreatorCampaignEconomicsCommission) exampleCreatorCampaignEconomics.getActualInstance();

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

        // create a new CreatorCampaignEconomicsRetainer
        CreatorCampaignEconomicsRetainer exampleCreatorCampaignEconomicsRetainer = new CreatorCampaignEconomicsRetainer();
        // set CreatorCampaignEconomics to CreatorCampaignEconomicsRetainer
        exampleCreatorCampaignEconomics.setActualInstance(exampleCreatorCampaignEconomicsRetainer);
        // to get back the CreatorCampaignEconomicsRetainer set earlier
        CreatorCampaignEconomicsRetainer testCreatorCampaignEconomicsRetainer = (CreatorCampaignEconomicsRetainer) exampleCreatorCampaignEconomics.getActualInstance();
    }
}
```


