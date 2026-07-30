

# LinkedInAdsPlatformDataThoughtLeader

POST /v1/ads/create only. Sponsors an existing LinkedIn post (a share or ugcPost authored by your organization's Company Page) as the creative, keeping its commentary, author and engagement. Unlike boostPost, which provisions its own CampaignGroup + Campaign around the post, this variant attaches the reference under the campaign /v1/ads/create builds — same shape as every other format, so the caller can pick bidding / targeting / schedule freely. No headline, body, imageUrl or organization are needed; the referenced post carries its own commentary and author. Mutually exclusive with the other creative sources. Posts from personal profiles (Thought Leader Ads) are NOT supported (see postUrn). 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**postUrn** | **String** | LinkedIn share or ugcPost URN, urn:li:share:N or urn:li:ugcPost:N. Get it via \&quot;Copy link to post\&quot; on the target LinkedIn post (the URL contains -share- for a share or -ugcPost- for a ugcPost, then the numeric id). The post must be authored by an organization (Company Page). Member (personal profile) posts, i.e. Thought Leader Ads proper, are rejected by LinkedIn&#39;s public Marketing API regardless of sponsorship approval and of post type (a LinkedIn limitation; their Campaign Manager creates those through a private API). Referencing a member post returns a 422 with a clear error.  |  |



