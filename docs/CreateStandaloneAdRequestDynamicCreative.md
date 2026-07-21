

# CreateStandaloneAdRequestDynamicCreative

Meta only. Dynamic Creative: supply a POOL of assets and Meta auto-combines and optimises them into the best-performing variations within a single ad (mapped to the creative's `asset_feed_spec`). When set, the top-level single-creative fields (`imageUrl`, `headline`, `body`, `linkUrl`, `callToAction`) are ignored. Mutually exclusive with the `creatives[]` multi-creative shape. Meta limits: ≤10 images, ≤5 bodies / titles / descriptions. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**imageUrls** | **List&lt;URI&gt;** | Pool of image URLs (1-10). Uploaded to the ad account and referenced by hash in the asset feed. |  |
|**bodies** | **List&lt;String&gt;** | Primary-text variations (the body copy). |  [optional] |
|**titles** | **List&lt;String&gt;** | Headline variations. |  [optional] |
|**descriptions** | **List&lt;String&gt;** | Description (link caption) variations. |  [optional] |
|**linkUrls** | **List&lt;URI&gt;** | Destination URL variations. At least one is required unless &#x60;goal&#x60; is &#x60;lead_generation&#x60;. |  [optional] |
|**callToActionTypes** | [**List&lt;CallToActionTypesEnum&gt;**](#List&lt;CallToActionTypesEnum&gt;) | CTA-button variations. Required. |  [optional] |
|**adFormat** | [**AdFormatEnum**](#AdFormatEnum) | Asset-feed ad format. Defaults to SINGLE_IMAGE. |  [optional] |



## Enum: List&lt;CallToActionTypesEnum&gt;

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
| REGISTER | &quot;REGISTER&quot; |
| JOIN | &quot;JOIN&quot; |
| ATTEND | &quot;ATTEND&quot; |
| REQUEST_DEMO | &quot;REQUEST_DEMO&quot; |
| VIEW_QUOTE | &quot;VIEW_QUOTE&quot; |
| APPLY | &quot;APPLY&quot; |
| SEE_MORE | &quot;SEE_MORE&quot; |
| BUY_NOW | &quot;BUY_NOW&quot; |



## Enum: AdFormatEnum

| Name | Value |
|---- | -----|
| SINGLE_IMAGE | &quot;SINGLE_IMAGE&quot; |
| CAROUSEL_IMAGE | &quot;CAROUSEL_IMAGE&quot; |



