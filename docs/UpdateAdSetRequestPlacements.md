

# UpdateAdSetRequestPlacements

Meta only (400 elsewhere). Manual placements, with the same object and enums as `placements` on POST /v1/ads/create.  - **Object:** REPLACES the ad set's current placement set (`publisher_platforms`, every `*_positions` list and `device_platforms`). A position list you leave out is removed. An object with no non-empty list is a 400 (send `null` instead). - **`null`:** removes every placement key, so Meta returns to automatic (Advantage+) placements. - **Omitted:** placements are left untouched.  Meta enforces co-selection rules (e.g. a position needs its publisher platform) and its error is returned as is. Meta may also reject `null` or a narrower set when an ad's creative uses per-placement asset customization (`placementAssets`).  Cannot be combined with `targeting.placements` (400). 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**publisherPlatforms** | [**List&lt;PublisherPlatformsEnum&gt;**](#List&lt;PublisherPlatformsEnum&gt;) |  |  [optional] |
|**facebookPositions** | [**List&lt;FacebookPositionsEnum&gt;**](#List&lt;FacebookPositionsEnum&gt;) |  |  [optional] |
|**instagramPositions** | [**List&lt;InstagramPositionsEnum&gt;**](#List&lt;InstagramPositionsEnum&gt;) |  |  [optional] |
|**messengerPositions** | [**List&lt;MessengerPositionsEnum&gt;**](#List&lt;MessengerPositionsEnum&gt;) |  |  [optional] |
|**audienceNetworkPositions** | [**List&lt;AudienceNetworkPositionsEnum&gt;**](#List&lt;AudienceNetworkPositionsEnum&gt;) |  |  [optional] |
|**threadsPositions** | [**List&lt;ThreadsPositionsEnum&gt;**](#List&lt;ThreadsPositionsEnum&gt;) |  |  [optional] |
|**whatsappPositions** | [**List&lt;WhatsappPositionsEnum&gt;**](#List&lt;WhatsappPositionsEnum&gt;) |  |  [optional] |
|**devicePlatforms** | [**List&lt;DevicePlatformsEnum&gt;**](#List&lt;DevicePlatformsEnum&gt;) |  |  [optional] |



## Enum: List&lt;PublisherPlatformsEnum&gt;

| Name | Value |
|---- | -----|
| FACEBOOK | &quot;facebook&quot; |
| INSTAGRAM | &quot;instagram&quot; |
| THREADS | &quot;threads&quot; |
| MESSENGER | &quot;messenger&quot; |
| AUDIENCE_NETWORK | &quot;audience_network&quot; |
| WHATSAPP | &quot;whatsapp&quot; |



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



