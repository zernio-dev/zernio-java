

# LinkedInAdsPlatformDataThoughtLeader

POST /v1/ads/create only. Thought-leader ad: references someone else's existing LinkedIn share or ugcPost as the creative. Unlike boostPost, which provisions its own CampaignGroup + Campaign around the post, this variant attaches the reference under the campaign /v1/ads/create builds — same shape as every other format, so the caller can pick bidding / targeting / schedule freely. No headline, body, imageUrl or organization are needed; the referenced post carries its own commentary and author. Mutually exclusive with the other creative sources. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**postUrn** | **String** | LinkedIn share or ugcPost URN, urn:li:share:N or urn:li:ugcPost:N. Get it via \&quot;Copy link to post\&quot; on the target LinkedIn post (the URL contains -share- for a share or -ugcPost- for a ugcPost, then the numeric id). For member (personal profile) posts, LinkedIn&#39;s API only accepts video and document posts (ugcPost URNs); text and image member posts (share URNs) are rejected by LinkedIn regardless of sponsorship approval (a LinkedIn API limitation; those can only be sponsored from Campaign Manager). The member must have authorised sponsorship for the ad account&#39;s organization.  |  |



