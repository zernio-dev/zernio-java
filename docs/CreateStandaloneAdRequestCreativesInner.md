

# CreateStandaloneAdRequestCreativesInner

Each creative must supply EXACTLY ONE of `imageUrl` (image creative) or `video` (video creative).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Exact name for this ad. Falls back to &#x60;&lt;name&gt; #N&#x60; (N &#x3D; 1-based position). |  [optional] |
|**headline** | **String** |  |  |
|**body** | **String** |  |  |
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



