

# CreateStandaloneAdRequestCreativesInner

Each creative must supply EXACTLY ONE of `imageUrl` (image creative) or `video` (video creative).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Exact name for this ad. Falls back to &#x60;&lt;name&gt; #N&#x60; (N &#x3D; 1-based position). |  [optional] |
|**headline** | **String** |  |  |
|**body** | **String** |  |  |
|**description** | **String** | Link description for this ad (link_data.description; video creatives: video_data.link_description). Falls back to the top-level &#x60;description&#x60;; when both are omitted Meta scrapes the destination URL&#39;s OG description. |  [optional] |
|**imageUrl** | **URI** | Image creative. Mutually exclusive with &#x60;video&#x60;. |  [optional] |
|**video** | [**CreateStandaloneAdRequestCreativesInnerVideo**](CreateStandaloneAdRequestCreativesInnerVideo.md) |  |  [optional] |
|**linkUrl** | **URI** |  |  |
|**callToAction** | [**CallToActionEnum**](#CallToActionEnum) |  |  |



## Enum: CallToActionEnum

| Name | Value |
|---- | -----|
| LEARN_MORE | &quot;LEARN_MORE&quot; |
| SHOP_NOW | &quot;SHOP_NOW&quot; |
| SIGN_UP | &quot;SIGN_UP&quot; |
| BOOK_TRAVEL | &quot;BOOK_TRAVEL&quot; |
| CONTACT_US | &quot;CONTACT_US&quot; |
| DOWNLOAD | &quot;DOWNLOAD&quot; |
| GET_OFFER | &quot;GET_OFFER&quot; |
| GET_QUOTE | &quot;GET_QUOTE&quot; |
| SUBSCRIBE | &quot;SUBSCRIBE&quot; |
| WATCH_MORE | &quot;WATCH_MORE&quot; |
| ADD_TO_CART | &quot;ADD_TO_CART&quot; |
| APPLY_NOW | &quot;APPLY_NOW&quot; |
| BOOK_NOW | &quot;BOOK_NOW&quot; |
| BUY_TICKETS | &quot;BUY_TICKETS&quot; |
| DONATE | &quot;DONATE&quot; |
| DONATE_NOW | &quot;DONATE_NOW&quot; |
| GET_DIRECTIONS | &quot;GET_DIRECTIONS&quot; |
| GET_SHOWTIMES | &quot;GET_SHOWTIMES&quot; |
| LISTEN_NOW | &quot;LISTEN_NOW&quot; |
| ORDER_NOW | &quot;ORDER_NOW&quot; |
| PLAY_GAME | &quot;PLAY_GAME&quot; |
| REQUEST_TIME | &quot;REQUEST_TIME&quot; |
| SEE_MENU | &quot;SEE_MENU&quot; |
| START_ORDER | &quot;START_ORDER&quot; |
| INSTALL_MOBILE_APP | &quot;INSTALL_MOBILE_APP&quot; |
| USE_APP | &quot;USE_APP&quot; |



