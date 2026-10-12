

# GetAdReview200ResponseReviewReviewFeedback

Meta only. The Ad's `ad_review_feedback`, verbatim. Both maps are empty when Meta returned no feedback (approved or in-review ad).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**global** | **Map&lt;String, String&gt;** | Meta &#x60;global&#x60;: policy or reason -&gt; Meta&#39;s explanation. |  [optional] |
|**placementSpecific** | **Map&lt;String, Map&lt;String, String&gt;&gt;** | Meta &#x60;placement_specific&#x60;: placement (facebook, instagram, ...) -&gt; reason -&gt; Meta&#39;s explanation. |  [optional] |



