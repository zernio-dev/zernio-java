

# WebhookPayloadCommentCommentAd

Ad context. Present only when the comment was made on paid content; absent for comments on organic posts that are not promoted.  **Instagram**: populated from the webhook payload's value.media.ad_id, value.media.ad_title and value.media.original_media_id, each only when Meta includes it.  **Facebook**: populated from a Graph API lookup of the parent post. Present when the post is an ad dark post (isDarkPost true, whatever its promotionStatus) or an organic post that is or was boosted (promotionStatus \"active\", \"extendable\" or \"finished\").  Meta does not link a dark post back to its ad, so on Facebook id is set only when exactly one ad on the Page, created before the dark post, carries the same copy as the post. title is never set on Facebook. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Meta ad ID. Instagram: from the webhook. Facebook: only on a dark post matched to a single ad by its copy. |  [optional] |
|**title** | **String** | Ad creative title (Instagram only). |  [optional] |
|**originalMediaId** | **String** | Original media ID that Meta reports for the ad (Instagram only). |  [optional] |
|**promotionStatus** | **String** | Facebook only. The parent post&#39;s promotion_status as the Graph API returns it, for example \&quot;active\&quot; (organic post currently boosted). Ad dark posts usually report \&quot;inactive\&quot; and sometimes \&quot;ineligible\&quot;, so use isDarkPost, not this value, to tell an ad comment apart.  |  [optional] |
|**isDarkPost** | **Boolean** | Facebook only: true when the post is an unpublished ad creative (dark post), false for a boosted organic post. |  [optional] |



