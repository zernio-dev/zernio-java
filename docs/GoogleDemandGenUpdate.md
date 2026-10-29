

# GoogleDemandGenUpdate

Partial edit of a Google Demand Gen ad, sent in one atomic Google request. Every field you send replaces that whole field; fields you omit are kept.  Which creative fields apply depends on the ad (read from Google). A field the ad does not take returns 422.  - Image ads: headlines, descriptions, businessName, callToAction and images (landscape, square, portrait, logo). - Video ads: headlines, longHeadlines, descriptions, businessName, youtubeVideoIds and exactly one images.logo. - Carousel ads: exactly one headline, one description, one logo, businessName and callToAction. Their cards cannot be edited: create a new carousel ad.  New images are uploaded as new Google assets; the previous ones stay in the account's asset library.  **Ad group fields.** `channels`, `audience` and `audienceId` change the ad's ad group, so they apply to every ad in it. `audience` builds a new Google Audience and attaches it in place of the current one (the previous one is detached, not deleted); `audienceId` attaches an existing one.  Ad groups of campaigns migrated from Discovery use ungrouped audience segments, and Google refuses an Audience on them. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**finalUrl** | **URI** |  |  [optional] |
|**businessName** | **String** |  |  [optional] |
|**headlines** | **List&lt;String&gt;** |  |  [optional] |
|**longHeadlines** | **List&lt;String&gt;** | Video ads only. |  [optional] |
|**descriptions** | **List&lt;String&gt;** |  |  [optional] |
|**callToAction** | **String** | Image and carousel ads only. |  [optional] |
|**images** | [**GoogleDemandGenUpdateImages**](GoogleDemandGenUpdateImages.md) |  |  [optional] |
|**youtubeVideoIds** | **List&lt;String&gt;** | Video ads only. |  [optional] |
|**channels** | [**List&lt;ChannelsEnum&gt;**](#List&lt;ChannelsEnum&gt;) | Replaces the ad group&#39;s channel controls. Only the listed channels serve; Google Maps, which this list cannot select, is turned off. Omit to leave the ad group&#39;s channel controls unchanged. |  [optional] |
|**audience** | [**GoogleDemandGenAudience**](GoogleDemandGenAudience.md) |  |  [optional] |
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



