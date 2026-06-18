

# CreateStandaloneAdRequestPlacements

Meta only. Manual ad placements. Omit for automatic placements (Meta's default, recommended for most cases — Meta optimises delivery across all eligible surfaces). When set, restricts delivery to the chosen surfaces, mapped onto the ad set's `targeting.{publisher_platforms, facebook_positions, instagram_positions, messenger_positions, audience_network_positions, threads_positions, whatsapp_positions, device_platforms}`. Enum membership is validated here; Meta additionally enforces co-selection rules (e.g. some positions require their parent publisher platform) and returns an actionable error which we surface. Non-Meta platforms reject this field. Can be combined with `rawTargeting` — when both are set, the placement spec is converted to Meta's snake_case and merged into the raw targeting object before it is sent to Meta. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**publisherPlatforms** | [**List&lt;PublisherPlatformsEnum&gt;**](#List&lt;PublisherPlatformsEnum&gt;) | Top-level platforms to deliver on. A position field below is only honoured when its parent platform is included here. |  [optional] |
|**facebookPositions** | [**List&lt;FacebookPositionsEnum&gt;**](#List&lt;FacebookPositionsEnum&gt;) |  |  [optional] |
|**instagramPositions** | [**List&lt;InstagramPositionsEnum&gt;**](#List&lt;InstagramPositionsEnum&gt;) |  |  [optional] |
|**messengerPositions** | [**List&lt;MessengerPositionsEnum&gt;**](#List&lt;MessengerPositionsEnum&gt;) |  |  [optional] |
|**audienceNetworkPositions** | [**List&lt;AudienceNetworkPositionsEnum&gt;**](#List&lt;AudienceNetworkPositionsEnum&gt;) |  |  [optional] |
|**threadsPositions** | [**List&lt;ThreadsPositionsEnum&gt;**](#List&lt;ThreadsPositionsEnum&gt;) |  |  [optional] |
|**whatsappPositions** | [**List&lt;WhatsappPositionsEnum&gt;**](#List&lt;WhatsappPositionsEnum&gt;) |  |  [optional] |
|**devicePlatforms** | [**List&lt;DevicePlatformsEnum&gt;**](#List&lt;DevicePlatformsEnum&gt;) | Restrict by device. Omit to deliver on both mobile and desktop. |  [optional] |



## Enum: List&lt;PublisherPlatformsEnum&gt;

| Name | Value |
|---- | -----|
| FACEBOOK | &quot;facebook&quot; |
| INSTAGRAM | &quot;instagram&quot; |
| THREADS | &quot;threads&quot; |
| MESSENGER | &quot;messenger&quot; |
| AUDIENCE_NETWORK | &quot;audience_network&quot; |



## Enum: List&lt;FacebookPositionsEnum&gt;

| Name | Value |
|---- | -----|
| FEED | &quot;feed&quot; |
| RIGHT_HAND_COLUMN | &quot;right_hand_column&quot; |
| MARKETPLACE | &quot;marketplace&quot; |
| VIDEO_FEEDS | &quot;video_feeds&quot; |
| STORY | &quot;story&quot; |
| SEARCH | &quot;search&quot; |
| INSTREAM_VIDEO | &quot;instream_video&quot; |
| FACEBOOK_REELS | &quot;facebook_reels&quot; |
| FACEBOOK_REELS_OVERLAY | &quot;facebook_reels_overlay&quot; |
| PROFILE_FEED | &quot;profile_feed&quot; |
| NOTIFICATION | &quot;notification&quot; |



## Enum: List&lt;InstagramPositionsEnum&gt;

| Name | Value |
|---- | -----|
| STREAM | &quot;stream&quot; |
| STORY | &quot;story&quot; |
| EXPLORE | &quot;explore&quot; |
| EXPLORE_HOME | &quot;explore_home&quot; |
| REELS | &quot;reels&quot; |
| PROFILE_FEED | &quot;profile_feed&quot; |
| IG_SEARCH | &quot;ig_search&quot; |
| PROFILE_REELS | &quot;profile_reels&quot; |



## Enum: List&lt;MessengerPositionsEnum&gt;

| Name | Value |
|---- | -----|
| MESSENGER_HOME | &quot;messenger_home&quot; |
| SPONSORED_MESSAGES | &quot;sponsored_messages&quot; |
| STORY | &quot;story&quot; |



## Enum: List&lt;AudienceNetworkPositionsEnum&gt;

| Name | Value |
|---- | -----|
| CLASSIC | &quot;classic&quot; |
| REWARDED_VIDEO | &quot;rewarded_video&quot; |



## Enum: List&lt;ThreadsPositionsEnum&gt;

| Name | Value |
|---- | -----|
| THREADS_STREAM | &quot;threads_stream&quot; |



## Enum: List&lt;WhatsappPositionsEnum&gt;

| Name | Value |
|---- | -----|
| STATUS | &quot;status&quot; |



## Enum: List&lt;DevicePlatformsEnum&gt;

| Name | Value |
|---- | -----|
| MOBILE | &quot;mobile&quot; |
| DESKTOP | &quot;desktop&quot; |



