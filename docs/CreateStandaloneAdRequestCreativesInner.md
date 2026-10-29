

# CreateStandaloneAdRequestCreativesInner

Each creative must supply EXACTLY ONE of `imageUrl` (image creative) or `video` (video creative).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creativeFeatures** | [**Map&lt;String, InnerEnum&gt;**](#Map&lt;String, InnerEnum&gt;) | Replaces the entire top-level creativeFeatures map for this item. Omit to inherit; an empty map clears these defaults. |  [optional] |
|**name** | **String** | Exact name for this ad. Falls back to &#x60;&lt;name&gt; #N&#x60; (N &#x3D; 1-based position). |  [optional] |
|**headline** | **String** |  |  |
|**body** | **String** |  |  |
|**description** | **String** | Link description for this ad (link_data.description; video creatives: video_data.link_description). Falls back to the top-level &#x60;description&#x60;; when both are omitted Meta scrapes the destination URL&#39;s OG description. |  [optional] |
|**imageUrl** | **URI** | Image creative. Mutually exclusive with &#x60;video&#x60;. |  [optional] |
|**video** | [**CreateStandaloneAdRequestCreativesInnerVideo**](CreateStandaloneAdRequestCreativesInnerVideo.md) |  |  [optional] |
|**linkUrl** | **URI** |  |  |
|**callToAction** | [**CallToActionEnum**](#CallToActionEnum) |  |  |



## Enum: Map&lt;String, InnerEnum&gt;

| Name | Value |
|---- | -----|
| OPT_IN | &quot;OPT_IN&quot; |
| OPT_OUT | &quot;OPT_OUT&quot; |



## Enum: CallToActionEnum

| Name | Value |
|---- | -----|
| BOOK_TRAVEL | &quot;BOOK_TRAVEL&quot; |
| CONTACT_US | &quot;CONTACT_US&quot; |
| DONATE | &quot;DONATE&quot; |
| DONATE_NOW | &quot;DONATE_NOW&quot; |
| DOWNLOAD | &quot;DOWNLOAD&quot; |
| GET_DIRECTIONS | &quot;GET_DIRECTIONS&quot; |
| GO_LIVE | &quot;GO_LIVE&quot; |
| INTERESTED | &quot;INTERESTED&quot; |
| LEARN_MORE | &quot;LEARN_MORE&quot; |
| SEE_DETAILS | &quot;SEE_DETAILS&quot; |
| LIKE_PAGE | &quot;LIKE_PAGE&quot; |
| MESSAGE_PAGE | &quot;MESSAGE_PAGE&quot; |
| RAISE_MONEY | &quot;RAISE_MONEY&quot; |
| SAVE | &quot;SAVE&quot; |
| SEND_TIP | &quot;SEND_TIP&quot; |
| SHOP_NOW | &quot;SHOP_NOW&quot; |
| SIGN_UP | &quot;SIGN_UP&quot; |
| VIEW_INSTAGRAM_PROFILE | &quot;VIEW_INSTAGRAM_PROFILE&quot; |
| INSTAGRAM_MESSAGE | &quot;INSTAGRAM_MESSAGE&quot; |
| LOYALTY_LEARN_MORE | &quot;LOYALTY_LEARN_MORE&quot; |
| PURCHASE_GIFT_CARDS | &quot;PURCHASE_GIFT_CARDS&quot; |
| PAY_TO_ACCESS | &quot;PAY_TO_ACCESS&quot; |
| SEE_MORE | &quot;SEE_MORE&quot; |
| TRY_IN_CAMERA | &quot;TRY_IN_CAMERA&quot; |
| WHATSAPP_LINK | &quot;WHATSAPP_LINK&quot; |
| GET_IN_TOUCH | &quot;GET_IN_TOUCH&quot; |
| TRY_NOW | &quot;TRY_NOW&quot; |
| ASK_A_QUESTION | &quot;ASK_A_QUESTION&quot; |
| START_A_CHAT | &quot;START_A_CHAT&quot; |
| CHAT_NOW | &quot;CHAT_NOW&quot; |
| ASK_US | &quot;ASK_US&quot; |
| CHAT_WITH_US | &quot;CHAT_WITH_US&quot; |
| SHOP_ON_RETAILER | &quot;SHOP_ON_RETAILER&quot; |
| BOOK_NOW | &quot;BOOK_NOW&quot; |
| CHECK_AVAILABILITY | &quot;CHECK_AVAILABILITY&quot; |
| ORDER_NOW | &quot;ORDER_NOW&quot; |
| WHATSAPP_MESSAGE | &quot;WHATSAPP_MESSAGE&quot; |
| GET_MOBILE_APP | &quot;GET_MOBILE_APP&quot; |
| INSTALL_MOBILE_APP | &quot;INSTALL_MOBILE_APP&quot; |
| USE_MOBILE_APP | &quot;USE_MOBILE_APP&quot; |
| INSTALL_APP | &quot;INSTALL_APP&quot; |
| USE_APP | &quot;USE_APP&quot; |
| PLAY_GAME | &quot;PLAY_GAME&quot; |
| TRY_DEMO | &quot;TRY_DEMO&quot; |
| WATCH_VIDEO | &quot;WATCH_VIDEO&quot; |
| WATCH_MORE | &quot;WATCH_MORE&quot; |
| OPEN_LINK | &quot;OPEN_LINK&quot; |
| NO_BUTTON | &quot;NO_BUTTON&quot; |
| LISTEN_MUSIC | &quot;LISTEN_MUSIC&quot; |
| MOBILE_DOWNLOAD | &quot;MOBILE_DOWNLOAD&quot; |
| GET_OFFER | &quot;GET_OFFER&quot; |
| GET_OFFER_VIEW | &quot;GET_OFFER_VIEW&quot; |
| BUY_NOW | &quot;BUY_NOW&quot; |
| BUY_TICKETS | &quot;BUY_TICKETS&quot; |
| UPDATE_APP | &quot;UPDATE_APP&quot; |
| BET_NOW | &quot;BET_NOW&quot; |
| ADD_TO_CART | &quot;ADD_TO_CART&quot; |
| SELL_NOW | &quot;SELL_NOW&quot; |
| GET_SHOWTIMES | &quot;GET_SHOWTIMES&quot; |
| LISTEN_NOW | &quot;LISTEN_NOW&quot; |
| GET_EVENT_TICKETS | &quot;GET_EVENT_TICKETS&quot; |
| REMIND_ME | &quot;REMIND_ME&quot; |
| SEARCH_MORE | &quot;SEARCH_MORE&quot; |
| PRE_REGISTER | &quot;PRE_REGISTER&quot; |
| SWIPE_UP_PRODUCT | &quot;SWIPE_UP_PRODUCT&quot; |
| SWIPE_UP_SHOP | &quot;SWIPE_UP_SHOP&quot; |
| PLAY_GAME_ON_FACEBOOK | &quot;PLAY_GAME_ON_FACEBOOK&quot; |
| VISIT_WORLD | &quot;VISIT_WORLD&quot; |
| OPEN_INSTANT_APP | &quot;OPEN_INSTANT_APP&quot; |
| JOIN_GROUP | &quot;JOIN_GROUP&quot; |
| GET_PROMOTIONS | &quot;GET_PROMOTIONS&quot; |
| SEND_UPDATES | &quot;SEND_UPDATES&quot; |
| INQUIRE_NOW | &quot;INQUIRE_NOW&quot; |
| VISIT_PROFILE | &quot;VISIT_PROFILE&quot; |
| CHAT_ON_WHATSAPP | &quot;CHAT_ON_WHATSAPP&quot; |
| EXPLORE_MORE | &quot;EXPLORE_MORE&quot; |
| CONFIRM | &quot;CONFIRM&quot; |
| JOIN_CHANNEL | &quot;JOIN_CHANNEL&quot; |
| MAKE_AN_APPOINTMENT | &quot;MAKE_AN_APPOINTMENT&quot; |
| ASK_ABOUT_SERVICES | &quot;ASK_ABOUT_SERVICES&quot; |
| BOOK_A_CONSULTATION | &quot;BOOK_A_CONSULTATION&quot; |
| GET_A_QUOTE | &quot;GET_A_QUOTE&quot; |
| BUY_VIA_MESSAGE | &quot;BUY_VIA_MESSAGE&quot; |
| ASK_FOR_MORE_INFO | &quot;ASK_FOR_MORE_INFO&quot; |
| VIEW_PRODUCT | &quot;VIEW_PRODUCT&quot; |
| VIEW_CHANNEL | &quot;VIEW_CHANNEL&quot; |
| WATCH_LIVE_VIDEO | &quot;WATCH_LIVE_VIDEO&quot; |
| JOIN_LIVE_VIDEO | &quot;JOIN_LIVE_VIDEO&quot; |
| IMAGINE | &quot;IMAGINE&quot; |
| WATCH_NOW | &quot;WATCH_NOW&quot; |
| STREAM_NOW | &quot;STREAM_NOW&quot; |
| BUY_ACTIVITY_TICKETS | &quot;BUY_ACTIVITY_TICKETS&quot; |
| CALL | &quot;CALL&quot; |
| MISSED_CALL | &quot;MISSED_CALL&quot; |
| CALL_NOW | &quot;CALL_NOW&quot; |
| CALL_ME | &quot;CALL_ME&quot; |
| APPLY_NOW | &quot;APPLY_NOW&quot; |
| BUY | &quot;BUY&quot; |
| GET_QUOTE | &quot;GET_QUOTE&quot; |
| SUBSCRIBE | &quot;SUBSCRIBE&quot; |
| RECORD_NOW | &quot;RECORD_NOW&quot; |
| VOTE_NOW | &quot;VOTE_NOW&quot; |
| GIVE_FREE_RIDES | &quot;GIVE_FREE_RIDES&quot; |
| REGISTER_NOW | &quot;REGISTER_NOW&quot; |
| OPEN_MESSENGER_EXT | &quot;OPEN_MESSENGER_EXT&quot; |
| EVENT_RSVP | &quot;EVENT_RSVP&quot; |
| CIVIC_ACTION | &quot;CIVIC_ACTION&quot; |
| SEND_INVITES | &quot;SEND_INVITES&quot; |
| REFER_FRIENDS | &quot;REFER_FRIENDS&quot; |
| REQUEST_TIME | &quot;REQUEST_TIME&quot; |
| SEE_MENU | &quot;SEE_MENU&quot; |
| SEARCH | &quot;SEARCH&quot; |
| TRY_IT | &quot;TRY_IT&quot; |
| TRY_ON | &quot;TRY_ON&quot; |
| LINK_CARD | &quot;LINK_CARD&quot; |
| DIAL_CODE | &quot;DIAL_CODE&quot; |
| FIND_YOUR_GROUPS | &quot;FIND_YOUR_GROUPS&quot; |
| START_ORDER | &quot;START_ORDER&quot; |



