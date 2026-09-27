

# GoogleDemandGenInput

Creative, channel and audience settings for a Google Demand Gen campaign (campaignType demand_gen). Creates one ad group with one ad: a multi-asset image ad, a video responsive ad when youtubeVideoIds is sent, or a carousel ad when carouselCards is sent.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adGroupName** | **String** | Defaults to the ad name. |  [optional] |
|**finalUrl** | **URI** |  |  |
|**businessName** | **String** |  |  |
|**headlines** | **List&lt;String&gt;** | Distinct texts. A carousel ad takes exactly one. |  |
|**longHeadlines** | **List&lt;String&gt;** | Video ads only, and required there. |  [optional] |
|**descriptions** | **List&lt;String&gt;** | A carousel ad takes exactly one. |  |
|**callToAction** | **String** | Image and carousel ads only. Call to action text such as &#39;Learn more&#39;; Google picks one when omitted. |  [optional] |
|**images** | [**GoogleDemandGenInputImages**](GoogleDemandGenInputImages.md) |  |  |
|**youtubeVideoIds** | **List&lt;String&gt;** | Makes the ad a video responsive ad. |  [optional] |
|**carouselCards** | [**List&lt;GoogleDemandGenInputCarouselCardsInner&gt;**](GoogleDemandGenInputCarouselCardsInner.md) | Makes the ad a carousel ad. Each card needs its own image (no two cards may share one); use the same image shape on every card. Card images are uploaded to the account&#39;s asset library before the campaign is created, validateOnly included (Google checks cards against existing images; identical images are reused, not duplicated). |  [optional] |
|**channels** | [**List&lt;ChannelsEnum&gt;**](#List&lt;ChannelsEnum&gt;) | Channel controls on the ad group. Only the listed channels serve; omit to serve on all of them. |  [optional] |
|**audience** | [**GoogleDemandGenInputAudience**](GoogleDemandGenInputAudience.md) |  |  [optional] |
|**audienceId** | **String** | Attach an existing Google Audience by numeric id instead of audience. |  [optional] |



## Enum: List&lt;ChannelsEnum&gt;

| Name | Value |
|---- | -----|
| YOUTUBE_IN_STREAM | &quot;youtube_in_stream&quot; |
| YOUTUBE_IN_FEED | &quot;youtube_in_feed&quot; |
| YOUTUBE_SHORTS | &quot;youtube_shorts&quot; |
| DISCOVER | &quot;discover&quot; |
| GMAIL | &quot;gmail&quot; |
| DISPLAY | &quot;display&quot; |



