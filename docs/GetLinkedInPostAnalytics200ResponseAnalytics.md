

# GetLinkedInPostAnalytics200ResponseAnalytics


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**impressions** | **Integer** | Times the post was shown |  [optional] |
|**reach** | **Integer** | Unique members who saw the post |  [optional] |
|**likes** | **Integer** | Reactions on the post |  [optional] |
|**comments** | **Integer** | Comments on the post |  [optional] |
|**shares** | **Integer** | Reshares of the post |  [optional] |
|**saves** | **Integer** | Times the post was saved (personal accounts only; 0 for organization accounts) |  [optional] |
|**sends** | **Integer** | Times the post was sent via LinkedIn messaging (personal accounts only; 0 for organization accounts) |  [optional] |
|**clicks** | **Integer** | Clicks on the post (organization accounts only) |  [optional] |
|**views** | **Integer** | Video views (video posts only) |  [optional] |
|**engagementRate** | **BigDecimal** | Engagement rate, as a percentage rounded to 2 decimals: (likes + comments + shares + clicks + saves + sends) / impressions * 100. Unlike PostAnalytics.engagementRate on GET /v1/analytics, this one DOES count clicks and has no fallback denominator, so it is 0 whenever impressions is 0. For organization accounts the value is the rate LinkedIn returns, not one computed here. |  [optional] |



